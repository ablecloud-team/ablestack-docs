
# 릴리즈 노트

이 문서에는 ABLESTACK 전체 제품의 Cerato (v3.0) 릴리즈에 대한 새로운 기능, 업그레이드 정보, 기타 특징 정보에 대한 정보가 포함되어 있습니다. 제품의 설치, 관리, 사용에 대한 정보는 해당 문서를 참고해야 합니다.

## Cerato의 새 기능 및 변경 기능

ABLESTACK Cerato (v3.0)은 ABLESTACK의 LTS 릴리즈로 다수의 새로운 기능과 기능 개선이 포함되어 있습니다. 핵심적인 새기능은 다음과 같습니다.

### Mold

Cerato Release에는 엔터프라이즈 환경에서의 안정성 및 사용성 개선을 위해 가상머신 복사 기능, 오토스케일링 기능, 가상머신 볼륨 암호화 지원 등의 주요 기능을 포함하여 호환성 향상, 다수의 버그 수정이 포함되어 있습니다.

- 사용자 인터페이스 로그인 성능 및 오류 개선
- Glue 스토리지에 대한 지원 개선(Glue Block, Glue Filesystem 지원) 및 스냅샷 백업 기능 개선
- 가상머신 볼륨에 대한 암호화 지원
- 사용량 계산 및 과금 정책 기능 지원
- 사용자 가상머신에 대한 모니터링 기능 통합
- 가상 로드밸런서에 의한 가상머신 오토스케일링 기능 제공
- 가상머신 생성 시 파라미터와 함께 전달할 수 있는 사용자 데이터 관리 기능 제공
- TPM 장치 지원을 통한 Windows 11 가상머신 지원
- EL9, Rocky9 운영체제 호스트, 가상머신 공식 지원
- 가상라우터에서의 MTU 설정 지원
- EMC Networker 백업/복구 통합
- Glue로 생성된 가상머신 디스크 통계 정보 개선
- VMWare vSphere 8.0 클러스터 통합 관리 지원
- 가상머신 볼륨 성능 개선을 위한 IO Driver 및 io_threads 설정 기능 제공
- 가상머신 클론(Full Copy) 기능 지원

### Glue

Citrix Hypervisor의 Enterprise Edition 지원 및 Microsoft Hyper-V의 고성능 IO 지원을 위해 Client Side Cache를 사용하면서 Persistent Reservation 기능을 포함하는 SMB 공유 스토리지를 지원합니다. 해당 기능을 통해 Citrix Hypervisor 기반 또는 Hyper-V 기반의 가상화 및 가상데스크톱 인프라에 대한 고성능 지원이 가능합니다.

- SMB 프로토콜 지원을 통해 HyperV 및 Citrix Hypervisor 지원
- SMB 프로토콜에 대한 Client Side Cache 지원
- SMB 프로토콜에 대한 Persistent Reservation 지원

### Cell

Cell 하이퍼바이저는 가상머신의 성능을 높이는 개선이 이루어졌습니다. Glue Block 스토리지 연결을 라이브러리 방식에서 Kernel 방식으로 변경하여 IO에 Commit 되는 단계를 줄여 성능을 개선하였고, IO_URING 기술 지원을 적용하여 가상머신에서 발생하는 IO가 해당 호스트의 Cache를 효율적으로 사용할 수 있도록 개선하였습니다.

- Glue Block 연결 아키텍처 변경
    * 가상머신 볼륨 IO 처리 단순화를 위해 Kernel 직접 연결 방식 제공
    * 가상머신 실행 시, 그리고 종료 시 연결된 Kernel 볼륨의 마운트 해제 등의 자동화 지원
- IO_URING 지원을 통한 가상머신 볼륨 성능 개선
    * Kernel 연결된 가상머신 볼륨에 대해 지원
    * Kernel Cache/Buffer를 효과적으로 사용하여 가상머신 성능 극대화

### Wall

Wall은 인프라 및 가상머신에 대한 예측 가능성을 높이기 위한 추세 분석 시각화 기능이 추가되었습니다.

- 호스트, 가상머신 증설 시기 예측 기능 제공
- 스토리지 증설 예측 기능 제공
- 호스트, 가상머신, 스토리지 사용량 추세 분석 기능 제공

### Works

Works는 Windows 기반 환경에서의 전용 클라이언트 제공, 그리고 사용자 편의성 향상, 보안 정책 적용 기능 향상 등의 개선이 이루어졌습니다.

- Windows 환경에서의 전용 클라이언트 연결 제공
- 워크스페이스 단위의 가상머신 생성 및 사용자 할당 지원
- 워크스페이스 단위의 가상머신 정책 설정 지원

### Cube

Cube는 ABLESTACK 클러스터의 전반적인 안정성 향상, 그리고 일부 유지보수 자동화 기능 등의 개선이 이루어졌습니다.

- 시간동기화 기능 개선
- 스토리지 컨트롤러 가상머신에 연결되는 물리 디스크 순서 변경 오류 개선
- 스토리지 컨트롤러 가상머신 상시 감시 기능 제공
- 전체 시스템 자동 종료 기능 지원
- ABLESTACK 배포 기능 및 호스트 추가 기능 개선

### Genie

Genie는 Cerato 릴리즈에서 새로 선보이는 하이브리드 자동화 플랫폼입니다. 다양한 클라우드 서비스를 지원하면서 자동화 스크립트 및 워크플로우를 통해 애플리케이션 배포 및 모니터링을 자동화 합니다. 이번 릴리스에서 제공되는 기능은 다음과 같습니다.

- Cerato에서 신규로 추가된 하이브리드 자동화 기능
- Genie 클러스터 생성 자동화 기능
- Genie 자동화 관리자 포털 제공
- 사전 정의된 자동화 템플릿 제공
- 자동 생성된 애플리케이션 및 가상머신에 대한 통합 모니터링 지원

## 호환성 매트릭스

### 호환되는 하이퍼바이저 버전

Mold는 자체적으로 제공되는 Cell 하이버파이저 외에 다양한 하이퍼바이저를 지원합니다. Mold에 의해 통합 관리될 수 있는 하이퍼바이저는 다음과 같습니다.

- KVM : Ubuntu 18.04 LTS, 20.04 LTS, CentOS 7, 8, RHEL 7, 8, 9, Rocky Linux 8, 9, openSUSE Leap 15, SUSE Linux Enterprise Server 15
- Citrix Hypervisor : 최신 핫픽스가 적용된 7.x, 8.x 버전
- XCP-ng : 7.x, 8.x
- VMWare : 6.x, 7.x, 8.x

Mold에 의해 통합 관리 되지는 않으나, Glue를 통한 SDS를 구성하여 비관리형 HCI를 제공할 수 있는 하이퍼바이저는 다음과 같습니다.

- 위의 Mold가 통합관리하는 모든 하이퍼바이저
- Hyper-V : Windows 2016 이상, Hyper-V 2016 이상

### 호환성이 검증된 가상화 애플리케이션/플랫폼

ABLESTACK은 다음의 가상화 응용 애플리케이션 또는 플랫폼과 호환됩니다.

- Tilon(틸론) DStatsion
- Citrix Virtual Apps & Desktops
- 이노티움 InnoECM

### 호환되는 외장 스토리지

ABLESTACK Mold는 Glue SDS 외에 다양한 외장 스토리지를 연결할 수 있도록 지원하여 효과적으로 클라우드 환경을 운영할 수 있도록 지원합니다. 블록 스토리지로 사용할 수 있도록 지원되는 외장스토리지는 다음과 같습니다.

- VMWare
    - 표준 iSCSI
    - 표준 NFS
- Citrix Hypervisor
    - 표준 iSCSI
    - 표준 NFS
    - SMB
- Microsoft HyperV
    - 표준 iSCSI
    - SMB
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
    - ABLESTACK Glue Block
    - ABLESTACK Glue Filesystem
