# ABLESTACK Online Docs

ABLESTACK Online Docs는 ABLESTACK의 아키텍처, 설치, 운영, 사용자 가이드를 제공하는 문서 저장소입니다. 문서는 [MkDocs](https://www.mkdocs.org/)와 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)로 빌드하며, 운영 배포본은 `mike`를 사용해 버전별 정적 사이트 구조로 관리합니다.

현재 운영 배포 구조는 단일 `site/` 디렉터리를 웹 서버 루트에 복사하는 방식이 아니라, `versions.json`, `latest` alias, 버전별 디렉터리를 포함하는 `mike` 산출물 구조입니다. 따라서 운영 배포 시에는 `mkdocs build` 결과물만 복사하지 않고 `mike` 기반 배포 절차를 사용해야 합니다.

## 문서 구조

- `docs/`: Markdown 문서와 정적 자산
- `docs/assets/`: 이미지, CSS, drawio 등 문서 자산
- `resources/`: PDF export용 스타일시트와 cover 템플릿
- `mkdocs.yml`: MkDocs 사이트, 테마, 플러그인, 목차 설정
- `pdf-title-hook.py`: H1 제목이 없는 페이지에 제목을 자동 추가하는 MkDocs hook
- `markdown-format.md`: 문서 작성 형식 예시

## 로컬 개발 환경

Python 가상환경을 만들고 저장소에서 관리하는 의존성 파일을 기준으로 패키지를 설치합니다. OS 패키지 매니저로 MkDocs를 직접 설치하면 운영 빌드와 버전이 달라질 수 있으므로 권장하지 않습니다.

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

Windows PowerShell에서는 가상환경 활성화 명령만 다음과 같이 실행합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

PDF export까지 로컬에서 확인해야 하는 경우 Playwright 브라우저가 필요합니다. GitHub Actions에서는 `playwright install --with-deps chromium` 방식으로 필요한 런타임을 함께 설치합니다.

## 로컬 미리보기

문서를 작성하는 동안에는 MkDocs 개발 서버로 결과를 확인합니다.

```bash
mkdocs serve
```

브라우저에서 다음 주소로 접속합니다.

```text
http://127.0.0.1:8000
```

다른 장비에서 접속해 확인해야 하는 경우 다음과 같이 실행합니다.

```bash
mkdocs serve -a 0.0.0.0:8000
```

## 로컬 빌드 검증

HTML 정적 사이트만 검증할 때는 다음 명령을 사용합니다.

```bash
mkdocs build
```

운영 배포와 동일하게 PDF export까지 포함해 검증하려면 `MKDOCS_EXPORTER_PDF` 환경변수를 활성화합니다.

```bash
MKDOCS_EXPORTER_PDF=true mkdocs build
```

Windows PowerShell에서는 다음과 같이 실행합니다.

```powershell
$env:MKDOCS_EXPORTER_PDF = "true"
mkdocs build
```

문서 링크 품질까지 엄격하게 확인할 때는 `mkdocs build --strict`를 별도로 실행합니다. `--strict`는 경고도 실패로 처리하므로, 운영 배포 전 품질 게이트로 사용하는 것을 권장합니다.

## 버전 배포 방식

운영 사이트는 `mike`를 사용해 문서 버전과 alias를 관리합니다. 루트 `index.html`은 기본 alias로 redirect하고, `versions.json`과 버전별 디렉터리는 `mike`가 생성합니다.

예를 들어 `4.0 Diplo` 버전을 `latest` alias로 배포하려면 다음과 같은 형태를 사용합니다.

```bash
MKDOCS_EXPORTER_PDF=true mike deploy --update-aliases "4.0 Diplo" latest
mike set-default latest
```

자동 배포에서는 버전명과 alias를 workflow에 직접 하드코딩하지 않고 설정 파일 또는 GitHub Actions 수동 실행 입력값으로 처리합니다. 기본값은 `.github/docs-deploy.yml`에서 관리하고, 수동 실행 시 입력값이 있으면 해당 값을 우선 적용합니다.

## GitHub Actions 자동 배포

자동 배포는 `.github/workflows/deploy-docs.yml`에서 수행합니다. 이 workflow는 문서 빌드, `mike` 버전 산출물 생성, nginx 운영 서버 동기화, air-gapped 환경용 nginx 컨테이너 이미지 생성을 한 흐름으로 검증합니다.

실행 모드는 다음과 같습니다.

- `codex/**` 브랜치 push: 빌드 검증, `mike` 산출물 생성, nginx 컨테이너 이미지 빌드/검증, 이미지 artifact 업로드
- `master` 브랜치 push: 날짜/시간 기반 release id 생성, `gh-pages` 반영, 운영 서버 동기화, GitHub Release 생성
- `workflow_dispatch`: 수동 입력값을 사용해 버전, alias, 기본 alias, `dry_run` 값을 override

1. `master` 브랜치 변경 또는 수동 실행으로 workflow 시작
2. Python, MkDocs, Material, `mike`, PDF export 의존성 설치
3. `.github/docs-deploy.yml`과 수동 입력값을 병합해 배포 설정 해석
4. `MKDOCS_EXPORTER_PDF=true`로 PDF 포함 빌드
5. `mike deploy`로 `gh-pages` 브랜치에 버전 산출물 반영
6. `mike set-default`로 기본 alias 설정
7. `gh-pages` 산출물을 운영 nginx 서버의 문서 루트로 동기화
8. SSH 파일 검증과, 설정된 경우 HTTP 응답 및 PDF 링크 검증

`codex/**` 브랜치에서는 운영 반영을 수행하지 않습니다. 이 모드에서는 `mike` 산출물을 로컬 브랜치로 생성해 Docker 이미지까지 검증하고, 운영 서버 SSH/rsync 단계는 건너뜁니다. 기능 브랜치에서 workflow 자체를 먼저 안전하게 확인하기 위한 모드입니다.

PR이 병합되어 `master` 브랜치에 push되면 자동 release mode가 적용됩니다. 이때 `mike.version`은 `.github/docs-deploy.yml`의 `mike.version` 값(`4.0 Diplo`)을 그대로 사용합니다. 따라서 상단 버전 선택기와 운영 서버 버전 디렉터리는 날짜/시간이 붙지 않은 `4.0 Diplo` 기준으로 유지되고, 같은 version이 이미 있으면 새 빌드 결과로 덮어씁니다.

날짜/시간이 필요한 릴리즈 식별자는 `mike.version`과 분리해 `release.id`로 생성합니다. 예를 들어 2026년 7월 7일 14시 30분 15초에 병합된 경우 다음 release id가 생성됩니다.

```text
4.0-Diplo-20260707-143015
```

자동 release mode에서는 `4.0 Diplo` version을 `latest` alias로 배포하고 `latest`를 기본 alias로 설정합니다. 기존 날짜형 release version 디렉터리는 배포 payload에서 제거하므로 운영 서버에 `4.0-Diplo-YYYYMMDD-HHmmss` 디렉터리가 계속 누적되지 않습니다. 또한 `release.dry_run: false` 설정을 사용하므로 `DOCS_DEPLOY_PASSWORD` Secret이 준비되어 있으면 운영 nginx 서버까지 자동 동기화합니다.

release version, release id, 빌드 일시, commit 정보는 workflow에서 `DOCS_RELEASE_VERSION`, `DOCS_RELEASE_ID`, `DOCS_RELEASE_BUILT_AT`, `DOCS_RELEASE_COMMIT` 환경변수로 MkDocs에 전달됩니다. `mkdocs.yml`은 이 값을 `extra.release`로 주입합니다. 시작 페이지(`docs/index.md`)에는 날짜형 release id 대신 version, 빌드 일시, commit만 표시하고, release id는 이미지/artifact 식별에 사용합니다.

운영 서버 접속 비밀번호는 GitHub Secrets로만 관리합니다. 비밀번호, API key, SSH key 등 민감한 값은 저장소 파일에 기록하지 않습니다.

필요한 Secrets 예시는 다음과 같습니다.

- `DOCS_DEPLOY_PASSWORD`: 운영 서버 SSH 접속 비밀번호

배포 대상 host, port, user, path와 `mike` 버전/alias 기본값은 `.github/docs-deploy.yml`에서 관리합니다. 기본 설정은 실제 반영 전 검증을 위해 `dry_run: true`이며, GitHub Actions 수동 실행 입력값으로 `dry_run=false`를 지정하면 운영 서버에 동기화합니다. 운영 서비스 검증은 `https://docs.ablecloud.io`를 기준으로 수행합니다.

주요 설정 항목은 다음과 같습니다.

```yaml
mike:
  version: "4.0 Diplo"
  aliases:
    - latest
  default: latest
  branch: gh-pages

build:
  strict: true
  pdf: true

release:
  enabled_on_master: true
  timezone: Asia/Seoul
  version_prefix: 4.0-Diplo
  timestamp_format: "%Y%m%d-%H%M%S"
  prune_version_pattern: "^4\\.0-Diplo-[0-9]{8}-[0-9]{6}$"
  github_release: true
  aliases:
    - latest
  default: latest
  dry_run: false

deploy:
  host: 211.115.222.251
  port: 10022
  user: root
  path: /usr/share/nginx/html
  dry_run: true

image:
  enabled: true
  name: ablestack-docs-nginx
  tag_aliases:
    - latest
  archive: true

verify:
  base_url: https://docs.ablecloud.io
```

## Air-gapped 이미지

GitHub Actions는 `mike`로 생성한 `gh-pages` 산출물을 그대로 포함하는 nginx Docker 이미지를 함께 생성합니다. 이 이미지는 Python, MkDocs, `mike` 없이 컨테이너 실행만으로 문서 사이트를 제공합니다.

이미지 산출물 기본값은 `.github/docs-deploy.yml`의 `image` 섹션에서 관리합니다. 기본 이미지 이름은 `ablestack-docs-nginx`이며, release mode에서는 `release.id` 값을 Docker tag로 변환한 태그와 `latest` 태그를 함께 생성합니다. 예를 들어 자동 release id `4.0-Diplo-20260707-143015`는 같은 이름의 Docker tag로 사용됩니다. GitHub Actions 환경에서는 commit 추적을 위해 `sha-<short-sha>` tag도 함께 생성합니다.

컨테이너 이미지는 `docker/nginx/Dockerfile`과 `docker/nginx/default.conf`를 사용합니다. 이미지에는 `mike` 산출물 전체가 `/usr/share/nginx/html/`로 복사되며, `latest` alias는 컨테이너 안에서 바로 서비스되도록 실제 디렉터리로 풀어 복사합니다.

workflow는 이미지를 만든 뒤 컨테이너를 직접 실행해서 다음 경로를 검증합니다. 컨테이너 내부 nginx는 80 포트를 사용하고, 기본 호스트 노출 포트는 8090입니다.

- `http://127.0.0.1:8090/`
- `http://127.0.0.1:8090/latest/`
- `http://127.0.0.1:8090/latest/index.pdf`

검증이 끝나면 `docker save | gzip`으로 air-gapped 전달용 tar.gz를 만들고 GitHub Actions artifact로 업로드합니다. artifact 이름은 기본적으로 다음 형태입니다.

```text
ablestack-docs-nginx-4.0-Diplo-20260707-143015.tar.gz
```

`master` 브랜치 자동 release mode에서는 운영 서버 배포와 HTTP 검증이 성공한 뒤 같은 release id로 GitHub Release도 생성합니다. Release에는 nginx 이미지 tar.gz가 asset으로 첨부되므로, GitHub Actions artifact 보존 기간과 별개로 Releases 화면에서 air-gapped 전달용 이미지를 받을 수 있습니다. 같은 release id로 workflow를 재실행하는 경우에는 release notes를 갱신하고 asset을 덮어씁니다.

GitHub Actions 화면에서 artifact를 다운로드하면 zip 파일로 내려받아질 수 있습니다. 이 경우 먼저 압축을 풀어 내부의 tar.gz 파일을 꺼냅니다.

```bash
unzip ablestack-docs-nginx-4.0-Diplo-20260707-143015.tar.gz.zip
```

폐쇄망 환경에서는 tar.gz 파일을 옮긴 뒤 다음과 같이 이미지를 로드하고 실행합니다.

```bash
docker load -i ablestack-docs-nginx-4.0-Diplo-20260707-143015.tar.gz

docker run -d \
  --name ablestack-docs \
  --restart unless-stopped \
  -p 8090:80 \
  ablestack-docs-nginx:4.0-Diplo-20260707-143015
```

컨테이너 실행 후에는 다음 명령으로 기본 페이지와 최신 버전 PDF를 확인합니다.

```bash
curl -fI http://127.0.0.1:8090/
curl -fI http://127.0.0.1:8090/latest/
curl -fI http://127.0.0.1:8090/latest/index.pdf
```

## 운영 배포 구조

운영 nginx 서버의 문서 루트는 `/usr/share/nginx/html/`입니다. 이 디렉터리는 `mike` 산출물 전용으로 관리합니다.

대표 구조는 다음과 같습니다.

```text
/usr/share/nginx/html/
├── index.html
├── versions.json
├── latest -> 4.0 Diplo
├── 1.0 Allo/
├── 2.0 Bronto/
├── 3.0 Cerato/
└── 4.0 Diplo/
```

`site/` 디렉터리만 직접 복사하면 버전 목록, 기본 alias, PDF 링크, 과거 버전 유지 구조가 깨질 수 있습니다. 운영 반영은 GitHub Actions에서 생성한 `mike` 산출물을 기준으로 수행합니다.

## 문서 작성 형식

이미지 정렬, 이미지 테두리, 코드블록, admonition 등 문서 작성 형식은 `markdown-format.md`를 참고합니다.

```markdown
![이미지 이름](이미지 상대경로){:class="imgCenter"}
```

문서 작성 시 기본 Markdown과 MkDocs Material 확장 문법을 함께 사용할 수 있습니다.

## 참고

- [MkDocs 가이드](https://www.mkdocs.org/)
- [Material for MkDocs 가이드](https://squidfunk.github.io/mkdocs-material/)
- [mike](https://github.com/jimporter/mike)
