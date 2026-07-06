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

자동 배포는 다음 흐름을 기준으로 구성합니다.

1. `master` 브랜치 변경 또는 수동 실행으로 workflow 시작
2. Python, MkDocs, Material, `mike`, PDF export 의존성 설치
3. `.github/docs-deploy.yml`과 수동 입력값을 병합해 배포 설정 해석
4. `MKDOCS_EXPORTER_PDF=true`로 PDF 포함 빌드
5. `mike deploy`로 `gh-pages` 브랜치에 버전 산출물 반영
6. `mike set-default`로 기본 alias 설정
7. `gh-pages` 산출물을 운영 nginx 서버의 문서 루트로 동기화
8. HTTP 응답과 PDF 링크 검증

운영 서버 접속 정보와 SSH 개인키는 GitHub Secrets로만 관리합니다. 비밀번호, API key, SSH key 등 민감한 값은 저장소 파일에 기록하지 않습니다.

필요한 Secrets 예시는 다음과 같습니다.

- `DOCS_DEPLOY_SSH_KEY`: 운영 서버 배포용 SSH private key
- `DOCS_DEPLOY_KNOWN_HOSTS`: 운영 서버 host key

배포 대상 host, port, user, path와 `mike` 버전/alias 기본값은 `.github/docs-deploy.yml`에서 관리합니다.

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
