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
### Koral VM 이미지 템플릿

Koral은 가상머신에 Docker 와 Kubernetes 바이너리를 탑재하여 클러스터링하는 가상머신 기반의 컨테이너 서비스를 제공합니다. 따라서 Kubernetes 클러스터를 배포하기 위해서는 이러한 구성요소와 소프트웨어를 미리 탑재한 가상머신 이미지를 필요로 합니다. 

ABLESTACK은 백업 및 가상머신 콘솔, 가상 라우터 등의 기능을 제공하기 위해 관련 소프트웨어를 미리 탑재한 시스템 VM 템플릿을 기본적으로 제공합니다. 우리는 Koral를 위한 소프트웨어 역시 기존의 시스템 VM 템플릿에 탑재하여 관련 기능을 구현하는 것이 타당하다는 결론에 도달하였습니다. 

따라서 ABLESTACK의 시스템 VM 템플릿은 기존의 백업, 가상머신 콘솔, 가상 라우터 기능에 더해 Kubernetes 클러스터 배포를 위한 소프트웨어를 기본적으로 탑재하여 배포되며, 사용자가 플러그인을 활성화 하고 Mold UI를 통해 클러스터를 배포하면 해당 이미지를 사용하여 가상머신을 생성하게 됩니다. 

### Kubernetes 바이너리 ISO

Koral은 시스템 VM 템플릿을 이용해 Kubernetes 클러스터용 가상머신, 즉 컨트롤러 및 워커 노드를 배포한 후 가상머신 내부에 Kubernetes 클러스터를 위한 설정을 하게 됩니다. 이 때 해당 설정을 적용하기 위해 Kubernetes 바이너리 ISO를 가상머신에 마운트하여 관련된 바이너리를 가상머신에 탑재하고 프로그램을 실행하게 됩니다. 

따라서 ABLESTACK HCI를 관리하는 시스템 관리자는 반드시 ABLESTACK에서 공식적으로 제공하는 Kubernetes 바이너리 ISO를 다운로드하거나 해당 링크를 이용해 ISO를 Mold에 등록해야 합니다. 

현재 지원되는 Kubernetes 바이너리 ISO와 다운로드 링크는 다음과 같습니다.

| Kubernetes 바이너리 버전       | 다운로드 링크             | 
| -----------  | -------------      | 
| 1.20.9 | [다운로드](https://images.ablecloud.io/koral-setup-1.20.9.iso) |
| 1.21.3 | [다운로드](https://images.ablecloud.io/koral-setup-1.21.3.iso) |
| 1.22.4 | [다운로드](https://images.ablecloud.io/koral-setup-1.22.4.iso) |
| 1.23.0 | [다운로드](https://images.ablecloud.io/koral-setup-1.23.0.iso) |

### Kubernetes를 위한 기본 네트워크 오퍼링

Koral은 Kubernetes 클러스터를 배포할 때, 원활한 클러스터 배포 작업 모니터링 및 서비스 밸런싱을 위해 기본적인 네트워크 오퍼링을 이용해 클러스터를 배포합니다. 기본적으로 제공되는 네트워크 오퍼링은 다음과 같습니다. 

- DefaultNetworkOfferingforKubernetesService

해당 네트워크 오퍼링은 다음과 같은 네트워크 정책 및 서비스가 제공되도록 설정되어 있습니다. 

| 속성 | 설정값 |
| --- | ----- |
| 게스크 네트워크 종류 | Isolated |
| 트래픽 종류 | Guest |
| 네트워크 속도 | 200 Mb/s |
| 영구성 | false |
| 기본 Egress 정책 | true |
| 고가용성 | Required |
| 절약 모드 | true |
| VLAN 지정 | false |
| IP 범위 지정 | false |
| Public Access 지원 | false |
| 확장된 L2 Subnet 지원 | false |
| 지원되는 서비스 | DHCP : VirtualRouter |
|| StaticNat : VirtualRouter |
|| UserData : VirtualRouter |
|| SourceNat : VirtualRouter |
|| DNS : VirtualRouter |
|| LB : VirtualRouter |
|| Firewall : VirtualRouter |
|| VPN : VirtualRouter |
|| PortForwarding : VirtualRouter |

!!! info "Koral용 네트워크 제공 정책 생성"
    Koral을 이용해 Kubernetes Cluster용 네트워크 정책을 신규로 생성할 경우, 반드시 위의 설정 내용을 참고하여 생성합니다. 위의 설정 내용 중 주로 변경되는 설정은 '네트워크 속도'와 'VLAN 지정'이 될 것입니다. 나머지 설정 및 지원되는 서비스는 위의 설정 정보를 참고하여 적용합니다. 

### Docker Hub

Koral은 Kubernetes Cluster를 생성할 때, 최신의 Kubernetes Cluster를 효과적으로 적용하고, 다양한 Docker 이미지를 사용할 수 있도록 하기 위해 기본적으로 Docker Hub를 Docker Registry로 사용합니다. 

즉, Kubernetes Cluster를 구성하기 위해 필요한 애플리케이션 이미지를 다운로드 하고, Kubernetes Cluster가 Docker Hub를 사용하기 위해서는 해당 클러스터가 인터넷에 연결되어 있어야 합니다. 

Koral을 사용하기 전에 Kubernetes Cluster에 연결하고자 하는 네트워크가 인터넷에 연결되어 있는지 반드시 확인해야 합니다. 

## 서비스 아키텍처

### 서비스 오퍼링

### 노드 구성 및 SSH Key

### 클러스터 크기 및 확장

### 초기 네트워크 설정

### 클러스터 액세스


## Kubernetes 버전 지원 

### 바이너리 ISO 생성 스크립트

### Kubernetes 버전 업그레이드
