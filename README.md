# Ablestack 사용자 가이드

Ablestack는 일반적인 x86 기반 서버를 클러스터링하여 스토리지, 가상화, 클라우드 환경을 통합하여 제공할 수 있도록 오픈소스를 기반으로 만들어진 HCI 배포판입니다. 본 리파지터리는 이러한 Ablestack의 전반적인 아키텍처 및 사용법, 그리고 각 구성요소에 대한 사용자 설명서를 제공하기 위한 공간입니다. 

## 개발환경 준비

Ablestack 사용자 가이드는 [MkDocs](https://www.mkdocs.org/)를 사용하여 도큐먼트를 빌드합니다. 따라서 개발을 위해서는 해당 환경을 준비해야 합니다. MkDocs는 다양한 환경에 설치하여 개발환경을 만들 수 있습니다. 각각의 운영체제에서 지원하는 패키지 관리자를 사용할 수 있으며 지원되는 패키지 관리자는 다음과 같습니다. 

- apt-get : Debian, Ubuntu 계열
- dnf, yum : fedora, RHEL, CentOS 계열
- homebrew : MacOS 계열
- chocolatey : Windows OS 계열

각 운영체제의 패키지 관리자를 이용해 설치 명령을 이용하면 MkDocs 패키지를 빠르게 설치할 수 있습니다. 
### MacOS에 MkDocs 설치

MacOS에서 개발환경을 준비하기 위해서는 먼저 Homebrew 설치가 필요합니다. 다음과 같은 명령을 실행합니다. 

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Homebrew가 설치되면 다음의 명령을 이용해 MkDocs 패키지를 설치합니다. 

```
$ brew install mkdocs
```
### 수동으로 MkDocs 설치

만약, 기본적인 운영체제의 패키지 관리자를 이용해 설치하는 MkDocs가 최신의 버전이 아니어서 최신의 MkDocs 패키지를 설치하고자 한다면 Python을 이용해 직접 최신의 패키지를 설치할 수 있습니다. MkDocs 패키지를 설치하기 위해서는 먼저 운영체제에 Python이 설치되어 있어야 합니다. 운영체제별 Python 설치 방법은 별도의 가이드를 참고합니다. 

MkDocs는 Python 3.5 이상을 지원합니다. 또한 패키지 설치를 위해 PIP가 필요합니다. PIP를 최신으로 업그레이드 하기 위해 다음의 명령을 실행합니다. 

```
$ pip install --upgrade pip
```

MkDocs를 다음의 명령을 이용해 설치합니다. 

```
$ pip install mkdocs
```
### Docs Theme 설치

Ablestack Docs 사이트는 MkDocs의 Third Party 테마인 Material Theme을 사용합니다. 해당 테마를 개발환경에 설치하여 테마를 적용해야 합니다. 

다음의 명령을 개발환경에서 실행합니다. 

```
$ pip install mkdocs-material
```

## 플러그인 설치
### mike
여러 버전의 MkDocs 기반 문서를 쉽게 배포할 수 있게 해주는 플러그인 입니다.

다음의 명령을 개발환경에서 실행합니다.
```
$ pip install mike
```

### glightbox (Image Lightbox)
이미지 확대/축소 기능을 사용할 수 있는 플러그인 입니다.

다음의 명령을 개발환경에서 실행합니다.
```
$ pip install mkdocs-glightbox
```

## 개발 참여

개발환경을 설정했다면 Mold 사용자 가이드 소스를 GitHub 사용자 계정애 Fork하여 개발에 참여할 수 있습니다. GitHub 소스를 Fork 하고, 사용자 개발 환경에 Clone하여 개발에 참여하는 것은 GitHub의 사용자 가이드를 참고합니다. 

## 테스트

Ablestack Docs 소스를 Clone 한 디렉토리로 이동하면 mkdocs.yml 파일을 확인할 수 있습니다. 해당 파일이 있는 위치에서 다음의 명령을 실행합니다. 

```
$ mkdocs serve
```

jinja2.exceptions.TemplateNotFound 에러 처리

``` 
# Material의 language 템플릿 파일 ko.html를 kr.html로 이름을 변경합니다.
$ cd /opt/homebrew/lib/python3.10/site-packages/material/partials/languages/
$ mv ko.html kr.html
```
    

변경된 소스가 바로 반영되어 웹 브라우저에서 결과를 확인할 수 있으며 다음의 주소를 주소창에 입력하여 작성된 문서의 내용을 확인할 수 있습니다. 

```
http://127.0.0.1:8000
```

> mkdocs serve 명령은 개발환경의 로컬 IP를 이용해 테스트용으로 확인하기 위해 사용하는 명령입니다. 만약 외부에서 테스트를 하고자 하는 경우 -a 옵션 뒤에 0.0.0.0:8000 을 설정하여 테스트 서버를 실행할 수 있습니다. 예를 들어 다음과 같습니다. 
>
> $ mkdocs serve -a 0.0.0.0:8000

## 사용자 가이드 빌드

가이드를 작성한 후에는 일반 웹 서버에서 가이드 페이지를 서비스할 수 있도록 빌드해야 합니다. 빌드를 하기 위해서는 빌드 결과 파일이 만들어질 디렉토리를 먼저 만들어야 합니다. 예를 들어 다음과 같습니다. 

```
$ mkdir -p ~/Documents/mkdocs-sites/ablestack-docs
```

> 빌드 결과를 소스 디렉토리에 생성하지 않도록 주의해야 합니다.

빌드는 mkdocs.yml이 있는 디렉토리에서 다음과 같은 명령을 실행합니다. 

```
$ mkdocs build -t material -d ~/Documents/mkdocs-sites/ablestack-docs
```

정상적으로 실행되면 개발자가 작성한 문서에 따라 HTML, CSS 등의 파일이 자동으로 만들어진 것을 확인할 수 있습니다. 

## 배포

빌드가 완료된 소스는 일반 웹서버의 루트 디렉토리에 바로 업로드 하여 배포할 수 있습니다. 웹 서버의 루트디렉토리는 웹서버 제품에 따라 다르기 때문에 해당 웹 서버의 가이드를 참고해야 합니다. 

예를 들어 CentOS에서 기본적으로 사용하는 Apache Http Server(httpd)의 경우 /var/www/html이 기본적인 루트 디렉토리입니다. 해당 디렉토리에 빌드 완료된 결과를 배포하면 웹 서버를 통해 바로 결과를 확인할 수 있습니다. 

## 참고

문서 작성 시 스타일, 구성요소 등을 적용하기 위해 기본 Markdown 및 확장 Markdown의 문법 등을 참고하고자 하는 경우 다음의 도움말을 참고합니다. 

- [MkDocs 가이드](https://www.mkdocs.org/)
- [Material for MkDocs 가이드](https://squidfunk.github.io/mkdocs-material/)
