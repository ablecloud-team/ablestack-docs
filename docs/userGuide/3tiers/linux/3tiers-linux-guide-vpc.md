본 문서는 ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조"를 구성하기 위한 단계 중, 1 단계인 VPC 및 서브넷 구성에 대한 문서입니다.

1. ==VPC 및 서브넷 생성: VPC(Virtual Private Cloud)를 생성하고 서브넷(Subnet)을 생성합니다.==
2. 가상머신 생성: 생성된 서브넷에서 WEB, WAS, DB 각각 3대(총 9대)의 가상머신을 SSHKeyPair 및 Affinity을 설정하여 추가합니다.
3. 티어 구성 준비: 생성된 가상머신의 터미널에 접속하고 데이터 디스크 볼륨 구성을 합니다.
4. 티어 별 WEB, WAS, DB 구성:
      1. DB: 갈레라 클러스터(Galera Cluster)를 활용하여 동기 방식의 복제구조를 사용하는 멀티마스터 DB를 구성합니다.
      2. WAS: 도커 컨테이너를 이용하여 NodeJS를 활용한 WAS를 구성합니다.
      3. WEB: 도커 컨테이너를 이용하여 Nginx를 활용한 WAS를 구성합니다.
5. LB 구성: 동일 서브넷 상의 VM들을 하나의 Public IP를 생성하여 LB로 구성합니다.

## VPC (Virtual Private Cloud) 및 서브넷 생성

VPC (Virtual Private Cloud)는 Mold 사용자의 전용 가상 네트워크이며 Mold에서 다른 가상 네트워크와 논리적으로 분리되어있는 공간입니다. 기존의 물리적 네트워크와 유사한하게 사용자가 IP 주소 범위와 VPC 범위를 설정한 후, 서브넷을 추가하여 구성합니다. 이를 위해 다음의 단계와 정보로 구성됩니다.

- VPC 생성
- 서브넷 생성

### VPC 생성

VPC를 생성하기 위해 `네트워크 >  VPC` 화면으로 이동하여 ` VPC 추가` 버튼을 클릭합니다.

!!! info "VPC 생성 방법"
    VPC 생성에 대한 정보는 [가상 사설 클라우드 추가](../../../../administration/mold/network&traffic-mngt-guide#_30) 문서를 참고하십시오.

<!-- <center>
![centos-19-vm-wizard-01](../../../../assets/images/mold-nw&traffic-add-vpc.png){ width="600" }
</center> -->

VPC 추가 대화상자에서의 입력 항목 예제는 다음과 같습니다.

  - 이름: `ablecloud-vpc-01`
  - 설명: `3tiers-linux 구성을 위한 VPC입니다.`
  - Zone: `Zone1`
  - CIDR: `192.168.0.0/16`
  - 네트워크 도메인 : `cs5cloud.internal`
  - VPC 오퍼링 : `예: Default VPC offering`


### 서브넷 추가

서브넷(Subnet)은 VPC를 더 작은 단위로 나누는 과정입니다. 서브넷은 VPC안에 있는 VPC보다 더 작은 단위이기때문에 넷마스크가 더 높게되고 아이피범위가 더 작은 값을 갖게됩니다.

!!! info "서브넷 추가 방법"
    서브넷 추가에 대한 정보는 [서브넷 추가](../../../../administration/mold/network&traffic-mngt-guide#_31) 문서를 참고하십시오.

서브넷을 추가하기 위해 `네트워크 >  VPC` 화면으로 이동하여 윗 단계에서 생성한 VPC를 선택하고 `새 서브넷 추가`를 클릭합니다.

VPC 추가 대화상자는 VPC를 생성하기 위한 항목을 필요로 합니다. 입력 항목은 다음과 같습니다.

#### WEB 서브넷 추가
  - 이름 : `web`
  - 네트워크 오퍼링 : `VPC 네트워크에 대한 기본 격리 네트워크오퍼링`
  - 게이트웨이 : `192.168.1.1`
  - 넷 마스크 : `255.255.255.0`

#### WAS 서브넷 추가
  - 이름 : `was`
  - 네트워크 오퍼링 : `VPC 네트워크에 대한 기본 격리 네트워크오퍼링`
  - 게이트웨이 : `192.168.2.1`
  - 넷 마스크 : `255.255.255.0`

#### DB 서브넷 추가
- 이름 : `db`
- 네트워크 오퍼링 : `VPC 네트워크에 대한 기본 격리 네트워크오퍼링`
- 게이트웨이 : `192.168.3.1`
- 넷 마스크 : `255.255.255.0`


다음은 VPC 구성 예시입니다.

![VPC 구성 예시](../../../../assets/images/3tier-linux-architecture-vpc-example.png)