## VM 생성

VM을 생성하는 단계에서는 크게 아래 절차에 의해 실행됩니다.

1. Affinity 그룹 3개(Web, Was, DB)를 생성합니다.
2. 모든 VM을 제어하기 위한 SSH-Key를 생성합니다.
3. VM을 생성하기 위한 템플릿을 생성하거나 업로드합니다.
4. VM을 생성합니다. (Web, Was, DB구성을 위한 VM 각 3대, 총 9대의 VM을 생성)
5. 각 VM에 Public IP를 할당합니다.

### Affinity 그룹 생성
VM 생성하기 전, Anti Affinity 그룹을 생성하여 어느하나의 Tier에 속한 모든 VM들이 특정 호스트에 몰려 실행되지 않도록 합니다.
Affinity 그룹을 추가하기 위해 `컴퓨트 > Affinity 그룹` 화면으로 이동하여 `새 Affinity 그룹 추가` 버튼을 클릭합니다.
클릭하게되면 다음과 같은 입력항목을 확인할 수 있습니다. 

![3tier-linux-architecture-add-affinity-group](../../../../assets/images/3tier-linux-architecture-add-affinity-group.png)

1. 이름 : 기본값으로 선택합니다.
2. 설명 : CentOS 기본 가상머신 템플릿 이미지를 다음의 그림과 같이 선택합니다. 
3. 유형 : 적정한 컴퓨트 오퍼링을 선택합니다. (2 vCore, 4GB 이상 권장)

새 Affinity 그룹 추가 대화상자에서의 입력 항목 예제는 다음과 같습니다.

- 이름 : `ablecloud-3tier-linux-web`
- 설명 : `3tiers-linux의 web 구성 시 사용되는 Affinity 그룹입니다.`
- 유형 : `1C-2GB-RBD-HA`

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
- 공개키: ``    * 공란으로 두어 새롭게 생성합니다.
- 도메인 아이디: `` * 공란으로 두어 디폴트 값으로 생성합니다.


### 템플릿을 이용한 VM 생성
ABLESTACK Mold는 기본적으로 템플릿을 이용해 가상머신을 생성하고 사용하는 것을 권장합니다. 따라서 가상머신을 생성하기 전에 먼저 "[가상머신 사용 준비](../../vms/centos-guide-prepare-vm.md)" 단계를 통해 CentOS 기반의 가상머신 템플릿 이미지를 생성하여 등록하는 절차를 수행한 후 VM을 생성해야 합니다. 

가상머신을 추가하기 위해 `컴퓨트 > 가상머신` 화면으로 이동하여 `가상머신 추가` 버튼을 클릭합니다. "새 가상머신" 마법사 페이지가 표시됩니다. 해당 페이지에서는 다음과 같은 절차로 가상머신을 생성합니다. 

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
1. Public IP를 VM에 할당합니다.
2. Public IP에 Static NAT을 활성화합니다.


!!! info "VPC에 대한 새 Public IP 주소 획득"
    [VPC에 대한 새 Public IP 주소 획득](../../../../administration/cube/terminal-guide) 문서를 참고하여 접속하십시오.