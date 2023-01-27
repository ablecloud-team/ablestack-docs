ABLESTACK Mold를 이용한 **이중화를 통한 고가용성 기능을 제공하는 리눅스 기반의 3계층 구조** 의 [구성 단계](../3tiers-linux-guide-prepare#_5) 중, 두 번째 단계인 관리용 가상머신 생성에 대한 문서입니다.

보안을 강화하고 WEB, WAS, DB를 효율적으로 구성하고 관리하기 위해 별도의 관리용 가상머신을 생성합니다. 3계층 구조의 모든 가상머신들에 대한 외부로부터의 접근은 관리용 가상머신을 통해 이루어지며 SSH Key 쌍을 생성하고 적용해 키파일로 가상머신에 접속합니다.

관리용 가상머신을 구성하는 단계는 다음과 같은 절차로 실행됩니다.

- SSH-KeyPair 생성: 보다 안전한 가상머신 연결 환경을 제공하기 위해 SSH-Key를 생성합니다.
- 가상머신 생성: 템플릿 이미지를 생성하고 등록한 후, 템플릿을 이용하여 가상머신을 생성합니다.
- 네트워크 설정: 관리용 가상머신에 Public IP를 할당합니다.

## SSH-KeyPair 생성
SSH KeyPair를 생성하여 3 Tier 구조상의 VM들을 보다 안전하고 명확하게 접속 및 관리할 수 있습니다.
먼저 이 기능을 사용하기 위한 전제조건으로 SSH Key 관리 프로그램 설치된 템플릿을 생성하고 VM을 생성해야 기능이 적용됩니다. [비밀번호/SSH Key 관리기능 추가](../../../vms/centos-guide-ssh-key-use#ssh-key) 문서를 참고하십시오.

SSH Key 쌍을 추가하기 위해 **컴퓨트 > SSH 키 쌍 생성** 버튼을 클릭합니다. 아래 문서를 참고하여 같은 절차로 SSH 키 쌍을 생성합니다.

!!! info "SSH KeyPair 생성"
    SSH Key 생성을 위해 [SSH Key 생성](../../../vms/centos-guide-ssh-key-use#ssh-key_2) 문서를 참고하십시오.

입력 항목 예제는 다음과 같습니다.

- 이름: **3tier_linux_keypair**
- 공개키:  * 공란으로 두어 새롭게 생성합니다.
- 도메인 아이디:  * 디폴트 값으로 생성합니다.


## 가상머신 생성
ABLESTACK Mold는 기본적으로 템플릿을 이용해 가상머신을 생성하고 사용하는 것을 권장합니다. 따라서 관리용 가상머신을 생성하기 전에 먼저 "[가상머신 사용 준비](../../vms/centos-guide-prepare-vm.md)" 단계를 통해 CentOS 기반의 가상머신 템플릿 이미지를 생성하여 등록하는 절차를 수행한 후 VM을 생성해야 합니다.

가상머신을 추가하기 위해 **컴퓨트 > 가상머신** 화면으로 이동하여 **가상머신 추가** 버튼을 클릭합니다. **새 가상머신** 마법사 페이지가 표시됩니다. 
해당 페이지에서는 "템플릿을 이용한 VM 생성" 문서를 참고하여 가상머신을 생성합니다.

!!! info "템플릿을 이용한 VM 생성"
    템플릿을 이용한 가상머신 추가를 위해 [템플릿을 이용한 VM 생성](../../../vms/centos-guide-add-and-use-vm#vm) 문서를 참고하십시오.

입력 항목 예시는 다음과 같습니다.

- 관리 가상머신 1
    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Rocky Linux 9.0 기본 이미지 템플릿** * Rocky Linux release 9.0 (Blue Onyx)
    - 컴퓨트 오퍼링 : **1C-2GB-RBD-HA**
    - 데이터 디스크 : **100GB-WB-RBD** 
    - 네트워크 : **web** * 외부와 통신 가능하도록 WEB 서브넷에 추가합니다.
    - SSH 키 쌍 : **3tier_linux_keypair** 
    - 확장 모드 :  * 디폴트 값으로 생성합니다.
    - 이름 : **ablecloud-3tier-linux-manage**

## 네트워크 설정
생성한 관리용 가상머신에 Public IP를 할당하여 외부에서 허용되는 포트로만 접속할 수 있도록 설정합니다.
이를 위해 아래 절차로 Public IP를 할당합니다.

- **네트워크 > VPC > Public IP 주소** 탭에서 **새 IP 주소 가져오기** 를 클릭하여 Public IP를 할당합니다.
- **네트워크 > VPC > Public IP 주소** 탭에서 새로 할당받은 Public IP 클릭하여 포트포워딩를 설정합니다.

!!! info "VPC에 대한 새 Public IP 할당 방법"
    - VPC에 Public IP 할당하기 위해 [VPC에 대한 새 Public IP 주소 획득](../../../../administration/mold/network&traffic-mngt-guide#vpc-public-ip) 문서를 참고하십시오.

!!! info "Public IP의 포트포워딩를 설정 방법"
    - VPC에서 할당된 Public IP에 포트포워딩를 설정하기 위해 [VPC에 포트 포워딩 규칙 추가](../../../../administration/mold/network&traffic-mngt-guide#vpc_3) 문서를 참고하십시오.

관리용 가상머신을 활용하기 위한 포트포워딩 추가 예시는 다음과 같습니다.

|      | 사설 포트 | Public 포트 | 프로토콜 | VM    |
| -----| --------| -----------| -------| -------|
| SSH  | 22      | 22         | TCP    | ablecloud-3tier-linux-manage |