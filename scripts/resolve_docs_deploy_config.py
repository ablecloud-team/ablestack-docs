import json
import os
import re
import shlex
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml


CONFIG_PATH = Path(".github/docs-deploy.yml")


def env_override(name):
    value = os.environ.get(name)
    if value is None:
        return None
    value = value.strip()
    return value or None


def parse_bool(value, default=False):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized in {"1", "true", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "no", "n", "off"}:
        return False
    raise ValueError(f"Invalid boolean value: {value!r}")


def docker_tag(value):
    tag = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(value).strip())
    tag = tag.strip(".-")
    if not tag:
        raise ValueError(f"Cannot derive Docker tag from {value!r}")
    return tag[:128]


def unique_values(values):
    seen = set()
    result = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def is_master_push():
    return (
        os.environ.get("GITHUB_EVENT_NAME") == "push"
        and os.environ.get("GITHUB_REF") == "refs/heads/master"
    )


def release_datetime(release):
    timezone = str(release.get("timezone", "UTC")).strip()
    return datetime.now(ZoneInfo(timezone))


def release_version(release, built_at):
    version_prefix = str(release.get("version_prefix", "release")).strip()
    timestamp_format = str(release.get("timestamp_format", "%Y%m%d-%H%M%S")).strip()
    if not version_prefix:
        raise ValueError("release.version_prefix is required")
    if not timestamp_format:
        raise ValueError("release.timestamp_format is required")

    timestamp = built_at.strftime(timestamp_format)
    return f"{version_prefix}-{timestamp}"


def display_datetime(value):
    timezone_name = value.tzname() or "UTC"
    return f"{value:%Y-%m-%d %H:%M:%S} {timezone_name}"


def emit_outputs(outputs):
    output_path = os.environ.get("GITHUB_OUTPUT")
    lines = [f"{key}={value}" for key, value in outputs.items()]
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines))
            handle.write("\n")
    else:
        print("\n".join(lines))


def main():
    config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))

    mike = config.get("mike", {})
    build = config.get("build", {})
    release = config.get("release", {})
    deploy = config.get("deploy", {})
    image = config.get("image", {})
    verify = config.get("verify", {})

    version_input = env_override("INPUT_MIKE_VERSION")
    use_release = (
        not version_input
        and is_master_push()
        and parse_bool(release.get("enabled_on_master"), False)
    )

    version = version_input or mike.get("version")
    aliases_input = env_override("INPUT_MIKE_ALIASES")
    aliases = shlex.split(aliases_input) if aliases_input else mike.get("aliases", [])
    default = env_override("INPUT_MIKE_DEFAULT") or mike.get("default")
    built_at = release_datetime(release)
    release_id = release_version(release, built_at) if use_release else version

    if use_release:
        aliases = release.get("aliases", aliases)
        default = release.get("default", default)

    dry_run_input = env_override("INPUT_DRY_RUN")
    dry_run_default = release.get("dry_run") if use_release else deploy.get("dry_run")
    dry_run = parse_bool(dry_run_input, parse_bool(dry_run_default, False))
    image_enabled = parse_bool(image.get("enabled"), False)
    image_name = str(image.get("name", "ablestack-docs-nginx")).strip()
    image_tag_aliases = image.get("tag_aliases", [])
    image_archive = parse_bool(image.get("archive"), True)

    if not version:
        raise ValueError("mike.version is required")
    if not isinstance(aliases, list):
        raise ValueError("mike.aliases must be a list")
    if not isinstance(image_tag_aliases, list):
        raise ValueError("image.tag_aliases must be a list")
    if not default:
        raise ValueError("mike.default is required")
    if deploy.get("auth") != "password":
        raise ValueError("Only password deployment auth is currently supported")
    if image_enabled and not image_name:
        raise ValueError("image.name is required when image.enabled is true")

    primary_image_tag = release_id if use_release else version
    image_tags = [docker_tag(primary_image_tag)]
    image_tags.extend(docker_tag(alias) for alias in image_tag_aliases)
    github_sha = os.environ.get("GITHUB_SHA", "").strip()
    github_sha_short = github_sha[:7] if github_sha else ""
    if github_sha:
        image_tags.append(docker_tag(f"sha-{github_sha_short}"))

    outputs = {
        "version": version,
        "aliases_json": json.dumps(aliases, ensure_ascii=False),
        "default": default,
        "branch": mike.get("branch", "gh-pages"),
        "strict": str(parse_bool(build.get("strict"), True)).lower(),
        "pdf": str(parse_bool(build.get("pdf"), True)).lower(),
        "deploy_host": deploy["host"],
        "deploy_port": str(deploy.get("port", 22)),
        "deploy_user": deploy.get("user", "root"),
        "deploy_path": deploy["path"].rstrip("/"),
        "dry_run": str(dry_run).lower(),
        "release": str(use_release).lower(),
        "release_version": version,
        "release_id": release_id,
        "release_built_at": display_datetime(built_at),
        "release_commit": github_sha_short,
        "prune_version_pattern": str(release.get("prune_version_pattern") or ""),
        "image_enabled": str(image_enabled).lower(),
        "image_name": image_name,
        "image_tags_json": json.dumps(unique_values(image_tags), ensure_ascii=False),
        "image_archive": str(image_archive).lower(),
        "verify_base_url": str(verify.get("base_url") or "").rstrip("/"),
    }
    emit_outputs(outputs)


if __name__ == "__main__":
    main()
