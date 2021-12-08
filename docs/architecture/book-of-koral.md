Koral은 Mold를 통해 Kubernetes 클러스터를 자동으로 배포하고 구성하는 Orchestration 기능을 제공하는 플러그인 확장으로, 이러한 기능을 적절하게 표현하기 위해 Kubernetes의 K와 합창이라는 의미를 가진 Choral을 합성한 단어로, 실제 발음은 Choral과 동일하게 발음합니다. 

Koral은 ABLESTACK 설치 시 기본적으로 설치되는 플러그인입니다. 이 기능을 사용의 사용은 플러그인 사용을 위한 설정을 적용하고, Kubernetes 클러스터를 배포하기 위한 실행 바이너리 ISO를 등록함으로써 가능합니다. Koral을 이용하면 쉽고 빠르게 컨테이너 환경을 ABLESTACK에 배포할 수 있으며, 안정적으로 운영할 수 있을 뿐 아니라, 필요 시 신속하게 확장이 가능합니다. 

## Koral의 설계 목표

Koral은 ABLESTACK 사용자에게 가상머신 기반의 애플리케이션이 아닌 컨테이너 기반의 애플리케이션 배포를 지원하기 위한 플러그인 입니다. Koral은 Mold와 연동하여 Kubernetes 클러스터를 위한 네트워크를 생성하고, 가상머신을 컨트롤러 노드 및 워커 노드로 하는 Kubernetes 클러스터를 배포합니다. 이를 통해 사용자는 컨테이너 기반 애플리케이션을 배포하고 사용할 수 있습니다. Koral은 사용자의 편리성, 원클릭 배포, 업그레이드, 스케일링, 최신의 Kubernetes 지원 등을 제공하기 위해 다음과 같은 목표로 지속적으로 플러그인을 개발하여 사용자에게 제공합니다. 

- Mold를 통한 간결하고 직관적인 웹 기반 원클릭 Kubernetes 클러스터 배포
- 애플리케이션 서비스 제공을 위한 Load Balancing 서비스 기본 제공
- 자동 방화벽 설정을 통해 별도의 방화벽 설정 없이도 기본 환경 접속 가능
- Kubernetes 버전 업그레이드 및 사설 Docker Registry 지원
- Kubernetes Provider를 통한 Kubernetes 클러스터 오토스테일링
- 최신의 Kubernetes 지원을 위한 클러스터 빌더 ISO 생성 기능 지원

본 문서에서는 이러한 설계 목표를 달성하기 위한 Koral의 아키텍처 및 각종 기능, 사용법 등에 대한 간단한 소개를 제공합니다. 

## 플러그인 아키텍처

Koral은 Mold에 내장된 플러그인으로 다음의 그림은 Mold 입장에서의 플러그인 아키텍처를 묘사합니다. 

<center>
![koral-plugin-architecture](../assets/images/koral-plugin-architecture.png)
</center>

### 글로벌 설정

Koral 기능을 사용하기 위해서는 Mold의 글로벌 설정에서 Koral을 활성화 하기 위한 설정을 수정하여 적용해야 합니다. 기본적으로 설정해야 할 글로벌 설정값은 다음과 같습니다. 

| 설정 항목       | 설명             | 기본값                |
| -----------  | -------------      | -----------------       |
| cloud.kubernetes.service.enabled | Koral 기능을 사용할지의 여부를 설정합니다. | false |
| cloud.kubernetes.cluster.max.size | Kubernetes 클러스터를 생성할 때 클러스터의 노드 수 최대값입니다. | 10 |
| cloud.kubernetes.clusternetwork.offering | Kubernetes 클러스터를 생성할 때 기본적으로 사용할 네트워크 제공 정책입니다. | Default Network Offering for Kubernetes Service |

Koral 기능을 사용하기 위해서는 반드시 `cloud.kubernetes.service.enabled` 항목의 값을 'true'로 설정해야 하고, Mold 서비스를 재시작해야 합니다.
### Mold UI

Mold 서비스를 재시작한 후 Mold UI에 접속하면 두개의 Koral 관련 메뉴가 생성됩니다. 

먼저 Kubernetes 바이너리 ISO를 등록하고 버전 관리를 할 수 있는 "쿠버네테스 ISOs" 메뉴가 이미지 섹션에 생성되고, 실제 Kubernetes 클러스터를 생성하는 기능을 제공하는 "쿠버네테스" 메뉴가 컴퓨트 섹션에 생성됩니다. 

해당 메뉴를 통해 Koral 기능을 사용할 수 있으며 해당 기능을 사용하기 위해서는 쿠버네테스 ISO를 먼저 등록해야 합니다. 
### 시스템 VM 템플릿

### Kubernetes 바이너리 ISO

### Kubernetes를 위한 기본 네트워크 오퍼링

## 서비스 아키텍처

## Kubernetes 버전 지원 