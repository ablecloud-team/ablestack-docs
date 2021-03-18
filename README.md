# ABLESTACK 사용자 가이드

ABLESTACK은 일반적인 x86 기반 서버를 클러스터링하여 스토리지, 가상화, 클라우드 환경을 통합하여 제공할 수 있도록 오픈소스를 기반으로 만들어진 HCI 배포판입니다. 본 리파지터리는 이러한 ABLESTACK의 전반적인 아키텍처 및 사용법, 그리고 각 구성요소에 대한 사용자 설명서를 제공하기 위한 공간입니다. 

## 개발환경 준비

ABLESTACK 사용자 가이드는 [MkDocs](https://www.mkdocs.org/)를 사용하여 도큐먼트를 빌드합니다. 따라서 개발을 위해서는 해당 환경을 준비해야 합니다. MkDocs는 다양한 환경에 설치하여 개발환경을 만들 수 있습니다. 각각의 운영체제에서 지원하는 패키지 관리자를 사용할 수 있으며 지원되는 패키지 관리자는 다음과 같습니다. 

- apt-get : Debian, Ubuntu 계열
- dnf, yum : fedora, RHEL, CentOS 계열
- homebrew : MacOS 계열
- chocolatey : Windows OS 계열

각 운영체제의 패키지 관리자를 이용해 설치 명령을 이용하면 MkDocs 패키지를 빠르게 설치할 수 있습니다. 
### MacOS 개발 환경 준비

MacOS에서 개발환경을 준비하기 위해서는 먼저 Homebrew 설치가 필요합니다. 다음과 같은 명령을 실행합니다. 

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Homebrew가 설치되면 다음의 명령을 이용해 MkDocs 패키지를 설치합니다. 

```
$ brew install mkdocs
```
### 수동으로 개발 환경 준비

만약, 기본적인 운영체제의 패키지 관리자를 이용해 설치하는 MkDocs가 최신의 버전이 아니어서 최신의 MkDocs 패키지를 설치하고자 한다면 Python을 이용해 직접 최신의 패키지를 설치할 수 있습니다. MkDocs 패키지를 설치하기 위해서는 먼저 운영체제에 Python이 설치되어 있어야 합니다. 운영체제별 Python 설치 방법은 별도의 가이드를 참고합니다. 

MkDocs는 Python 3.5 이상을 지원합니다. 또한 패키지 설치를 위해 PIP가 필요합니다. PIP를 최신으로 업그레이드 하기 위해 다음의 명령을 실행합니다. 

```
$ pip install --upgrade pip
```

MkDocs를 다음의 명령을 이용해 설치합니다. 

```
$ pip install mkdocs
```
