본 문서는 ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조"를 구성하기 위한 단계 중, 2 단계인 가상머신 생성에 대한 문서입니다.

1. VPC 및 서브넷 생성: VPC(Virtual Private Cloud)를 생성하고 서브넷(Subnet)을 생성합니다.
2. ==가상머신 생성: 생성된 서브넷에서 WEB, WAS, DB 각각 3대(총 9대)의 가상머신을 SSHKeyPair 및 Affinity을 설정하여 추가합니다.==
3. 티어 구성 준비: 생성된 가상머신의 터미널에 접속하고 데이터 디스크 볼륨 구성을 합니다.
4. 티어 별 WEB, WAS, DB 구성:
      1. DB: 갈레라 클러스터(Galera Cluster)를 활용하여 동기 방식의 복제구조를 사용하는 멀티마스터 DB를 구성합니다.
      2. WAS: 도커 컨테이너를 이용하여 NodeJS와 Samba 스토리지를 활용한 WAS를 구성합니다.
      3. WEB: 도커 컨테이너를 이용하여 Nginx와 NFS 스토리지를 활용한 WEB를 구성합니다.
5. LB 구성: 하나의 Public IP를 생성하여 동일 서브넷 상의 VM들의 이중화를 위해 LB를 구성합니다.

## VM 생성

VM을 생성하는 단계에서는 크게 아래 절차에 의해 실행됩니다.

1. Affinity 그룹 3개(Web, Was, DB)를 생성합니다.
2. 모든 VM을 제어하기 위한 SSH-Key를 생성합니다.
3. VM을 생성하기 위한 템플릿을 생성하거나 업로드합니다.
4. VM을 생성합니다. (Web, Was, DB구성을 위한 VM 각 3대, 총 9대의 VM을 생성)
5. 각 VM에 Public IP를 할당합니다.

### Affinity 그룹 생성
VM 생성하기 전, Anti Affinity 그룹을 생성하여 어느하나의 서브넷에 속한 VM들이 특정 호스트 한 곳에 몰려 실행하도록 하거나 반대로 몰려 실행되지 않도록 합니다.
이중화를 위해 Affinity 그룹을 anti-affinity 유형으로 WEB, WAS, DB 각각 추가해야합니다. 이를 위해 `컴퓨트 > Affinity 그룹` 화면으로 이동하여 `새 Affinity 그룹 추가` 버튼을 클릭합니다.
클릭하게되면 다음과 같은 입력항목을 확인할 수 있습니다. 

![3tier-linux-architecture-add-affinity-group](../../../../assets/images/3tier-linux-architecture-add-affinity-group.png)

1. 이름 : 서브넷을 분별할 수 있는 Affinity 그룹 이름을 입력합니다.
2. 설명 : Affinity 그룹에 대한 설명을 입력합니다.
3. 유형 : Affinity 그룹에 대한 유형을 선택합니다. Anti 여부를 선택할 수 있습니다. 

새 Affinity 그룹 추가 대화상자에서의 입력 항목 예제는 다음과 같습니다.

- 이름 : `ablecloud-3tier-linux-web`
- 설명 : `3tiers-linux의 web 구성 시 사용되는 Affinity 그룹입니다.`
- 유형 : `host anti-affinity (Strict)`

!!! info "Affinity 그룹 유형"
    host anti-affinity:	가능한 한 서로 다른 호스트에 인스턴스를 배포합니다.

    host affinity: 가능한 한 동일한 호스트에 인스턴스를 배포합니다.

    * Non-Strict 옵션은 마지막 실행 호스트를 고려하여 실행됩니다.

### SSH KeyPair 생성
SSH KeyPair를 생성하여 3 Tier 구조 구성 시 생성한 VM들을 보다 안전하고 명확하게 접속 및 관리할 수 있습니다.
먼저 이 기능을 사용하기 위한 전제조건으로 SSH Key 관리 프로그램 설치된 템플릿을 생성하고 VM을 생성해야 기능이 적용됩니다. [비밀번호/SSH Key 관리기능 추가](../../../vms/centos-guide-ssh-key-use#ssh-key) 문서를 참고하십시오.

SSH Key 쌍을 추가하기 위해 `컴퓨트` > `SSH 키 쌍 생성` 버튼을 클릭합니다. 아래 문서를 참고하여 같은 절차로 SSH 키 쌍을 생성합니다.

!!! info "SSH KeyPair 생성"
    SSH Key 생성을 위해 [SSH Key 생성](../../../vms/centos-guide-ssh-key-use#ssh-key_2) 문서를 참고하십시오.

입력 항목 예제는 다음과 같습니다.

- 이름: `3tier_linux_keypair`
- 공개키: ` ` * 공란으로 두어 새롭게 생성합니다.
- 도메인 아이디: ` ` * 공란으로 두어 디폴트 값으로 생성합니다.


### 템플릿을 이용한 VM 생성
ABLESTACK Mold는 기본적으로 템플릿을 이용해 가상머신을 생성하고 사용하는 것을 권장합니다. 따라서 가상머신을 생성하기 전에 먼저 "[가상머신 사용 준비](../../vms/centos-guide-prepare-vm.md)" 단계를 통해 CentOS 기반의 가상머신 템플릿 이미지를 생성하여 등록하는 절차를 수행한 후 VM을 생성해야 합니다. 생성할 수 있는 방법은 다음과 같이 두 가지가 있으며 한 방법을 선택하여 수행합니다.

1. 서브넷을 선택한 후 가상머신을 생성합니다. `네트워크 > VPC > 서브넷 선택 > 네트워크 탭` 에서 가상머신 추가 버튼을 클릭하면 "새 가상머신" 마법사 페이지가 표시됩니다.
2. `컴퓨트 > 가상머신` 화면으로 이동하여 `가상머신 추가` 버튼을 클릭하면 "새 가상머신" 마법사 페이지가 표시됩니다.

해당 페이지에서는 다음과 같은 절차로 가상머신을 생성합니다.

!!! info "템플릿을 이용한 VM 생성"
    템플릿을 이용한 가상머신 추가를 위해 [템플릿을 이용한 VM 생성](../../../vms/centos-guide-add-and-use-vm#vm) 문서를 참고하십시오.

입력 항목 예제는 다음과 같습니다.

- 배포 인프라 선택 : `Zone`
- 템플릿/ISO : `Rocky Linux 9.0 기본 이미지 템플릿`
- 컴퓨트 오퍼링 : `1C-2GB-RBD-HA`
- 데이터 디스크 : `100GB-WB-RBD`
- 네트워크 : `web`
- SSH 키 쌍 : `3tier_linux_keypair` 
- 확장 모드 
    - Affinity 그룹 설정: `ablecloud-3tier-linux-web`
- 상세 : `가상머신 이름 및 그룹 등의 설정`

### VPC에 Public IP 할당
생성한 각 VM에 Public IP를 할당하여 외부에서 접속할 수 있도록 합니다.
이를 위해 아래 절차로 Public IP를 할당합니다.

1. `네트워크 > VPC > 서브넷 선택 > Public IP 주소 탭` 에서 `새 IP 주소 가져오기`를 클릭하여 Public IP를 할당합니다.
2. `네트워크 > VPC > 서브넷 선택 > Public IP 주소 탭` 에서 생성한 Public IP에 대해 Static NAT을 활성화합니다. Static NAT을 활성화하여 Public IP와 Private IP를 1:1로 맵핑하여 포트포워딩 작업없이 Public IP를 사용할 수 있습니다.

!!! info "VPC에 대한 새 Public IP와 Static NAT설정"
    - VPC에 Public IP 할당하기 위해 [VPC에 대한 새 Public IP 주소 획득](../../../../administration/mold/network&traffic-mngt-guide#vpc-public-ip) 문서를 참고하십시오.
    - VPC에 Static NAT을 활성화하기 위해 [VPC에 대한 Static NAT을 활성화](../../../../administration/mold/network&traffic-mngt-guide#vpc-static-nat) 문서를 참고하십시오.