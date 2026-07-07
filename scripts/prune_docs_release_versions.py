#!/usr/bin/env python3
"""Prune generated timestamp release versions from a built mike site."""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def contained_path(root: Path, child_name: str) -> Path:
    child = (root / child_name).resolve()
    try:
        child.relative_to(root)
    except ValueError:
        fail(f"refusing to remove path outside site root: {child_name}")
    return child


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: prune_docs_release_versions.py <site-dir> <version-regex>")

    site_dir = Path(sys.argv[1]).resolve()
    pattern = re.compile(sys.argv[2])
    versions_path = site_dir / "versions.json"

    if not site_dir.is_dir():
        fail(f"site directory not found: {site_dir}")
    if not versions_path.is_file():
        print("versions.json not found; nothing to prune")
        return

    versions = json.loads(versions_path.read_text(encoding="utf-8-sig"))
    if not isinstance(versions, list):
        fail("versions.json must contain a list")

    kept = []
    pruned = []
    for entry in versions:
        version = str(entry.get("version", "")) if isinstance(entry, dict) else ""
        if pattern.fullmatch(version):
            pruned.append(version)
            continue
        kept.append(entry)

    for version in pruned:
        version_dir = contained_path(site_dir, version)
        if version_dir.exists():
            if version_dir.is_dir():
                shutil.rmtree(version_dir)
            else:
                version_dir.unlink()
            print(f"pruned version directory: {version}")
        else:
            print(f"version directory already absent: {version}")

    if pruned:
        versions_path.write_text(
            json.dumps(kept, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"pruned versions.json entries: {', '.join(pruned)}")
    else:
        print("no timestamp release versions matched prune pattern")


if __name__ == "__main__":
    main()
