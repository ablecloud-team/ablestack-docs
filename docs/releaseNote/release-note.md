# 릴리즈 노트

이 문서에는 ABLESTACK 전체 제품의 이번 릴리즈에 대한 새로운 기능, 업그레이드 정보, 기타 특정 정보에 대한 정보가 포함되어 있습니다. 제품의 설치, 관리, 사용에 대한 정보는 해당 문서를 참고해야 합니다. 

## Bronto의 새로운 기능 요약

ABLESTACK Bronto (2.0)은 ABLESTACK의 LTS 릴리즈로 다수의 새로운 기능과 기능 개선이 포함되어 있습니다. 핵심적인 새기능은 다음과 같습니다. 

- Works : ABLESTACK 사용자에게 최종 사용자 데스크톱 환경을 제공하기 위한 Desktop 서비스 기능
- Wall : ABLESTACK의 관리자가 실시간으로 인프라를 모니터링하고, 사용자가 생성한 가상머신을 모니터링할 수 있는 기능
- Koral : Kubernetes 클러스터에 대한 오토스케일링을 지원
- Koral : Kubernetes 1.23 릴리즈 지원
- Mold : Rocky Linux, OpenSUSE, SUSE Linux에 탑재된 KVM 하이퍼바이저 지원
- Mold : 가상머신의 CPU/RAM 동적 확장에 대한 세분화된 제어
- Mold : 생성한 자원에 대해 코멘트를 남겨 사용자 간 상호 작용 지원
- Mold : 자원에 대한 사용자 정의 아이콘을 지원
- Mold : 유저인터페이스를 통해 그룹으로 자원에 액션을 명령하고, 상태를 조회할 수 있음
- Mold : L2 네트워크를 영구(Persistent) 모드로 생성할 수 있음
- Mold : 네트워크 오퍼링에 MAC 학습 모드를 추가할 수 있음
- Glue : UI를 이용해 iSCSI Target 게이트웨이를 생성할 수 있음
- Glue : 오브젝트 게이트웨이를 이용해 WORM 스토리지 기능을 사용할 수 있음
- Common : Glue 스토리지만으로 모든 인프라에 대한 고가용성을 제공함

## 주요 변경 사항

### ABLESTACK Works

ABLESTACK Works는 Bronto 버전에서 새롭게 추가된 서비스로 최종사용자에게 Desktop as a Service를 제공하기 위한 기능입니다. Works는 ABLESTACK 확장 기능으로 별도의 라이선스를 통해 제공됩니다. 

Works는 다음과 같은 특징 및 기능을 포함합니다. 

- 최소한의 가상자원을 이용해 사용자 도메인 기반의 가상 데스크톱 서비스를 제공합니다.
- Mold를 기반으로 DaaS를 제공하기 때문에 멀티 하이퍼바이저를 지원합니다. 
- 자체적인 디렉토리 서비스를 이용하기 때문에 도메인 관리를 위한 별도의 Active Directory 서버가 필요하지 않습니다.
- 도메인 단위의 관리자 포털과 사용자 단위의 사용자 포털을 웹 기반으로 제공합니다. 
- 사용자는 웹 브라우저를 이용해 가상 데스크톱을 사용할 수 있어 별도의 클라이언트가 필요하지 않습니다. 
- 사용자에게 전용으로 할당된 데스크톱 서비스를 제공합니다. 
- 모든 구성요소가 자동으로 배포되어, 사용자가 별도의 수동 배포작업을 진행할 필요가 없습니다. 

Works의 아키텍처 및 주요 기능의 사용 방법은 다음의 문서를 참고하십시오.

- Works 아키텍처 : [아키텍처 문서 바로가기](/architecture/book-of-works){:target="_blank"}
- Works 설치 : [시작하기 문서 바로가기](/getting-started/install-guide-works){:target="_blank"}
- Works 관리자/사용자 가이드 : [관리자가이드 바로가기](/administration/works/admin-login){:target="_blank"}, [사용자가이드 바로가기](/administration/works/user-login){:target="_blank"}

### ABLESTACK Wall

ABLESTACK Wall은 Bronto 버전에서 새롭게 추가된 확장 기능으로 ABLESTACK 인프라 관리자 및 사용자에게 물리적인 Cube 인프라 및 가상머신의 실시간 모니터링 정보 및 임계치에 따른 알림을 제공합니다. 

Wall은 다음과 같은 특징 및 기능을 제공합니다. 

- ABLESTACK 클러스터를 구성할 때 마법사를 이용해 자동으로 배포됩니다.
- SMTP 서버를 이용해 임계치에 의한 알림을 메일로 제공합니다. 
- 인프라 관리자를 위한 호스트, 가상머신 등에 대한 실시간 모니터링을 제공합니다. 
- 사용자를 위해 사용자가 생성한 가상머신에 대한 실시간 모니터링을 제공합니다. 
- Mold UI를 이용해 모니터링 대시보드에 바로 접속이 가능합니다. 
- 가상머신 목록 및 상세정보 화면에서 가상머신 실시간 모니터링에 접속이 가능합니다. 
- 알림을 받기 위한 임계치는 사용자가 직접 설정할 수 있습니다. 

Wall의 아키텍처 및 주요 기능의 사용 방법은 다음의 문서를 참고하십시오.

- Wall 아키텍처 : [아키텍처 문서 바로가기](/architecture/book-of-wall){:target="_blank"}
- Wall 설치 : [시작하기 문서 바로가기](/getting-started/install-guide-wall){:target="_blank"}
- Wall 관리가이드 : [관리가이드 바로가기](/administration/wall/userinterface-guide){:target="_blank"}

### ABLESTACK Koral

ABLESTACK Koral은 Mold를 이용해 사용자가 원클릭으로 Kubernetes 클러스터를 자동으로 배포할 수 있도록 통합된 기능입니다. 이를 통해 사용자는 컨테이너 기반의 애플리케이션을 Kubernetes 클러스터를 사용해 실행할 수 있게 됩니다. 사용자는 이를 통해 복잡한 Kubernetes 클러스터 배포 과정을 생략할 수 있고, 애플리케이션 개발에 더욱 집중할 수 있게 됩니다. 

금번 Bronto 버전에서 이러한 Koral 기능에 대한 개선이 포함되어 있습니다. 바로 클러스터에 대한 자동 확장(AutoScale)을 지원하는 것입니다. 이 기능은 퍼블릭 클라우드 제공자(AWS, GCE 등)를 통해 제공되는 기능과 동일한 기능으로 노드에서 리소스 부족으로 인해 Pod 배포가 실패하는 경우 가상 노드를 자동으로 확장하고, 더 이상 리소스를 사용하지 않을 경우 자동으로 가상 노드를 제거하는 작업을 지원합니다. 

Mold 사용자는 Koral을 통해 Kuberentes 클러스터를 배포할 때 AutoScale 기능의 활성화 여부를 선택할 수 있고, 최소 노드 크기와 최대 노드 크기를 선택하여 클러스터를 해당 범위 내에서 자동으로 축소하거나 확장할 수 있게 됩니다. 

!!! info "Kubernetes AutoScale 지원 버전"
    Kubernetes AutoScale에 대한 지원은 Kubernetes의 AutoScale 기능에 의존합니다. 해당 기능은 Kubernetes 1.16.0 이상에서 지원됩니다. 따라서 Koral을 통해 Kubernetes 클러스터를 배포할 때 해당 클러스터의 Kubernetes 버전을 반드시 확인해야 합니다. 

    Kubernetes AutoScale 기능은 별도의 설치 절차 없이 자동으로 클러스터에 설치되며, 이를 위해 인터넷 연결이 필요합니다. 

## 호환성 매트릭스

### 호환되는 하이퍼바이저 버전

Mold는 자체적으로 제공되는 Cell 하이버파이저 외에 다양한 하이퍼바이저를 지원합니다. Mold에 의해 통합 관리될 수 있는 하이퍼바이저는 다음과 같습니다. 

- KVM : Ubuntu 18.04 LTS, 20.04 LTS, CentOS 7, 8, RHEL 7, 8, Rocky Linux 8, openSUSE Leap 15, SUSE Linux Enterprise Server 15
- Citrix Hypervisor : 최신 핫픽스가 적용된 7.x, 8.x 버전
- XCP-ng : 7.x, 8.x
- VMWare : 6.x, 7.x

Mold에 의해 통합 관리 되지는 않으나, Glue를 통한 SDS를 구성하여 비관리형 HCI를 제공할 수 있는 하이퍼바이저는 다음과 같습니다. 

- 위의 Mold가 통합관리하는 모든 하이퍼바이저
- Hyper-V : Windows 2016 이상, Hyper-V 2016 이상

### 호환되는 외장 스토리지

ABLESTACK Mold는 Glue SDS 외에 다양한 외장 스토리지를 연결할 수 있도록 지원하여 효과적으로 클라우드 환경을 운영할 수 있도록 지원합니다. 블록 스토리지로 사용할 수 있도록 지원되는 외장스토리지는 다음과 같습니다. 

- VMWare, XenServer
    - 표준 iSCSI
    - 표준 NFS
- Cell, KVM
    - 표준 iSCSI
    - 표준 NFS/POSIX호환 스토리지
    - GluesterFS
    - SolidFire
    - Ceph RBD
    - Datera
    - Cloudbyte
    - Nexenta
    - Dell PowerFlex
    - LINSTOR
