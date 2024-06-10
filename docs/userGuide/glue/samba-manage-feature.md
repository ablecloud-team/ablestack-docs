!!! note
    ABLESTACK Glue Service는 호스트가 아닌 Storage Center Virtual Machine(SCVM)에서 제공되고 있습니다.

    접속할 경로는 기존에 구성된 Storage Center Virtual Machine(SCVM) IP로 접속 하시면 됩니다.

# Glue Samba 관리
ABLESTACK Glue Service 에서의 Glue Samba 관리 하는 가이드 입니다.
이 문서에서는 ABLESTACK Glue Samba 관리 및 제공되는 기능절차를 가이드 하고 있습니다.
ABLESTACK Cube의 웹콘솔로 진행되며, 웹 접속 IP는 별도의 표시를 하지 않고 진행됩니다.
기존에 구성된 IP 정보에 맞게 웹콘솔을 접속 하시면 됩니다.

## Glue Samba 기능 설명
Glue 가상머신 별 SMB 서비스를 제공 및 활성화 하고 관리할 수 있습니다. 또한 사용자 정보를 관리할 수 있습니다.

## Glue Samba 메인 화면
![Glue Samba 메인 화면](../../assets/images/glue-service/install-guide-glue-smb-main-01.png){ align=center }
- ABLESTACK 메인 화면에서 상단 SMB 메뉴를 클릭한 화면입니다.

!!! note
    서비스 생성, 수정, 삭제 시에는 약간의 지연이 발생할 수 있으며, 상태 및 최신 정보를 확인하려면 새로고침 버튼을 클릭해 주세요.

## Glue Samba 서비스 생성

!!! note
    Glue Samba 서비스를 시작하려면 먼저 Glue FS에 데이터를 저장할 수 있도록 마운트해야 합니다.</br>
    이를 위해 Glue FS Subvolume Group에서 SMB 용도로 생성되었는지 확인하는 것이 중요합니다.</br>
    이 작업이 완료된 후에 Glue Samba 서비스를 생성할 수 있습니다.

!!! info
    Glue Samba 서비스는 두 가지 유형으로 제공됩니다. 일반용과 AD(Active Directory)용입니다. 사용자의 필요에 따라 적절한 유형을 선택할 수 있습니다.</br>
    서비스 생성 시 중요한 주의사항은 항상 초기화 후 생성됩니다. Glue Samba 서비스를 생성할 때는 반드시 초기화 과정을 거친 후에 생성됩니다. 이는 서비스의 안정성과 성능을 보장하기 위한 필수 절차입니다.</br>
    따라서, Glue Samba 서비스를 설정할 때는 초기화 과정이 완료된 후에 서비스를 생성하여 최적의 성능을 유지하시기 바랍니다.

1. Glue Samba 일반용 서비스 생성
    ![Glue Samba 일반용 서비스 생성 준비](../../assets/images/glue-service/install-guide-glue-smb-normal-create-01.png){ align=center }
    - Glue Samba 일반용 서비스 더보기란에 **SMB 서비스 구성** 버튼을 클릭합니다.
    ![Glue Samba 일반용 서비스 생성](../../assets/images/glue-service/install-guide-glue-smb-normal-create-02.png){ align=center }
    - **호스트** 정보를 확인 합니다.
    - **SMB 공유 폴더 명** 정보를 입력 합니다.
    - **SMB 마운트 경로** 정보를 확인 합니다.
    - **GlueFS 이름** 정보를 선택 합니다.
    - **GlueFS 경로** 정보를 선택 합니다.
    - **캐시 정책** 정보를 선택 합니다.
    - **User 이름** 정보를 입력 합니다.
    - **User 비밀번호** 정보를 입력 합니다.
    - 위 항목을 입력 및 확인 후에 **실행** 버튼을 클릭 합니다.
    ![Glue Samba 일반용 서비스 생성 완료](../../assets/images/glue-service/install-guide-glue-smb-normal-create-03.png){ align=center }
    - Glue Samba 일반용 서비스가 구성된 화면입니다.

!!! info
    캐시 정책 : 네트워크 파일 공유에서 클라이언트가 파일을 로컬로 캐싱(저장)하는 방법을 제어합니다.
    이는 파일 서버의 부하를 줄이고, 클라이언트가 네트워크 연결이 불안정하거나 없는 경우에도 파일을 계속 사용할 수 있게 합니다

2. Glue Samba AD용 서비스 생성
    ![Glue Samba AD용 서비스 생성 준비](../../assets/images/glue-service/install-guide-glue-smb-ads-create-01.png){ align=center }
    - Glue Samba 서비스 더보기란에 **SMB 서비스 구성** 버튼을 클릭합니다.
    ![Glue Samba AD용 서비스 생성](../../assets/images/glue-service/install-guide-glue-smb-ads-create-02.png){ align=center }
    - **호스트** 정보를 확인 합니다.
    - **SMB 공유 폴더 명** 정보를 입력 합니다.
    - **SMB 마운트 경로** 정보를 확인 합니다.
    - **GlueFS 이름** 정보를 선택 합니다.
    - **GlueFS 경로** 정보를 선택 합니다.
    - **캐시 정책** 정보를 선택 합니다.
    - **AD 사용** 정보를 체크 합니다.
    - **AD User 이름** 정보를 입력 합니다.
    - **AD User 비밀번호** 정보를 입력 합니다.
    - **AD Realm** 정보를 입력 합니다.
    - **AD DNS IP** 정보를 입력 합니다.
    - 위 항목을 입력 및 확인 후에 **실행** 버튼을 클릭 합니다.
    ![Glue Samba AD용 서비스 생성 완료](../../assets/images/glue-service/install-guide-glue-smb-ads-create-03.png){ align=center }
    - Glue Samba AD용 서비스가 구성된 화면입니다.

!!! info
    Glue Samba AD용 유저 관리는 Glue Samba Service단에서 제공하지 않습니다. AD Server를 가진 윈도우에서 관리 하시길 바랍니다.

3. Glue Samba 다중 구성
    ![Glue Samba 다중 구성 준비](../../assets/images/glue-service/install-guide-glue-smb-multiple-create-01.png){ align=center }
    - Glue Samba 서비스 카드란에 **다중 구성** 버튼을 클릭합니다.
    ![Glue Samba 다중 구성](../../assets/images/glue-service/install-guide-glue-smb-multiple-create-02.png){ align=center }
    - 필요한 **호스트** 정보를 선택 합니다.
    - **SMB 공유 폴더 명** 정보를 입력 합니다.
    - **SMB 마운트 경로** 정보를 확인 합니다.
    - **GlueFS 이름** 정보를 선택 합니다.
    - **GlueFS 경로** 정보를 선택 합니다.
    - **캐시 정책** 정보를 선택 합니다.
    - **AD 사용** 정보를 체크 합니다.
    - **AD User 이름** 정보를 입력 합니다.
    - **AD User 비밀번호** 정보를 입력 합니다.
    - **AD Realm** 정보를 입력 합니다.
    - **AD DNS IP** 정보를 입력 합니다.
    - 위 항목을 입력 및 확인 후에 **실행** 버튼을 클릭 합니다.
    ![Glue Samba 다중 구성 완료](../../assets/images/glue-service/install-guide-glue-smb-multiple-create-03.png){ align=center }
    - Glue Samba AD용 다중 구성 서비스가 구성된 화면입니다.

!!! info
    Glue Samba 일반용 다중 구성도 마찬가지로 호스트를 선택하여 사용하시면 됩니다.

!!! info
    Glue Samba 서비스에는 수정을 제공하지 않습니다.

## Glue Samba 서비스 삭제

1. Glue Samba 서비스 삭제
    ![Glue Samba 서비스 삭제 준비](../../assets/images/glue-service/install-guide-glue-smb-delete-01.png){ align=center }
    - Glue Samba 각 정보의 더보기란을 클릭하면 보이는 화면입니다.
    - **Samba 서비스 삭제** 버튼을 클릭 합니다.
    ![Glue Samba 서비스 삭제](../../assets/images/glue-service/install-guide-glue-smb-delete-02.png){ align=center }
    - **예, 확실히 삭제합니다.** 체크를 활성화 합니다.
    - 위 항목들을 입력 및 확인 후에 **실행** 버튼을 클릭합니다.
    ![Glue Samba 서비스 삭제 완료](../../assets/images/glue-service/install-guide-glue-smb-delete-03.png){ align=center }
    - 삭제가 된 화면입니다.

## Glue Samba 일반용 User 생성

1. Glue Samba 일반용 User 생성
    ![Glue Samba 일반용 User 생성 준비](../../assets/images/glue-service/install-guide-glue-smb-user-create-01.png){ align=center }
    - Glue Samba 서비스 더보기란에 **유저 생성** 버튼을 클릭합니다.
    ![Glue Samba 일반용 User 생성](../../assets/images/glue-service/install-guide-glue-smb-user-create-02.png){ align=center }
    - **사용자 이름** 정보를 입력 합니다.
    - **비밀번호** 정보를 입력 합니다.
    - 위 항목을 입력 및 확인 후에 **실행** 버튼을 클릭 합니다.
    ![Glue Samba 일반용 User 생성 완료](../../assets/images/glue-service/install-guide-glue-smb-user-create-03.png){ align=center }
    - Samba 유저가 구성된 화면입니다.

## Glue Samba 일반용 User 조회 목록

1. Glue Samba 일반용 User 조회 목록
    ![Glue Samba 일반용 User 조회 목록](../../assets/images/glue-service/install-guide-glue-smb-user-select-01.png){ align=center }
    - Glue Samba 각 정보의 더보기란을 클릭하면 보이는 화면입니다.
    - **유저 목록** 버튼을 클릭합니다.
    ![Glue Samba 일반용 User 조회 목록1](../../assets/images/glue-service/install-guide-glue-smb-user-select-02.png){ align=center }
    - 추가된 **유저 이름** 정보를 확인 합니다.
    - 위 항목을 확인 후에 **취소** 버튼을 클릭 합니다.

## Glue Samba 일반용 User 비밀번호 변경

!!! info
    Glue Samba 일반용 서비스에선 유저 관리에 대한 데이터베이스는 따로 관리 하고 있지 않습니다.
    비밀번호 변경을 확인하실려면 윈도우 접속을 통하여 확인하시길 바랍니다.

1. Glue Samba 일반용 User 비밀번호 변경
    ![Glue Samba 일반용 User 비밀번호 변경 준비](../../assets/images/glue-service/install-guide-glue-smb-user-passwd-change-01.png){ align=center }
    - Glue Samba 각 정보의 더보기란을 클릭하면 보이는 화면입니다.
    - **유저 비밀번호 변경** 버튼을 클릭 합니다.
    ![Glue Samba 일반용 User 비밀번호 변경](../../assets/images/glue-service/install-guide-glue-smb-user-passwd-change-02.png){ align=center }
    - **사용자** 정보를 선택 합니다.
    - **비밀번호** 정보를 입력 합니다.
    - **비밀번호 확인** 정보를 재입력 합니다.
    - 위 항목들을 입력 및 확인 후에 **실행** 버튼을 클릭합니다.

## Glue Samba 일반용 User 삭제

1. Glue Samba 일반용 User 삭제
    ![Glue Samba 일반용 User 삭제 준비](../../assets/images/glue-service/install-guide-glue-smb-user-delete-01.png){ align=center }
    - Glue Samba 각 정보의 더보기란을 클릭하면 보이는 화면입니다.
    - **유저 삭제** 버튼을 클릭 합니다.
    ![Glue Samba 일반용 User 삭제](../../assets/images/glue-service/install-guide-glue-smb-user-delete-02.png){ align=center }
    - 삭제할 **사용자** 정보를 선택 합니다.
    - 위 항목들을 입력 및 확인 후에 **실행** 버튼을 클릭합니다.
    ![Glue Samba 일반용 User 삭제 완료](../../assets/images/glue-service/install-guide-glue-smb-user-delete-03.png){ align=center }
    - 삭제가 된 화면입니다.

## Glue Samba 실사용 방법

!!! info
    Glue Samba는 윈도우 실사용 방법만 제공합니다.

### Glue Samba 일반용 및 AD용 서비스 확인
1. Glue Samba 일반용 및 AD용 서비스 확인
    ![Glue Samba 일반용 및 AD용 서비스 확인](../../assets/images/glue-service/install-guide-glue-smb-actual-use-01.png){ align=center }
    - **호스트 및 IP** 정보를 확인 합니다.
    - **상태 및 보안 타입** 정보를 확인 합니다.
    - **SMB 공유 폴더** 정보를 확인 합니다.

### Samba 일반용 윈도우 가상머신 작업
1. Samba 일반용 윈도우 가상머신 작업
    ![윈도우 가상머신 작업](../../assets/images/glue-service/install-guide-glue-smb-actual-use-02.png){ align=center }
    - 사용하실 윈도우에 접속합니다.
    ![윈도우 가상머신 작업1](../../assets/images/glue-service/install-guide-glue-smb-actual-use-03.png){ align=center }
    - **파일 탐색기** 를 클릭 합니다.
    - **내 PC** 에서 마우스 오른쪽 클릭 하여 **네트워크 드라이브 연결** 을 클릭 합니다.
    ![윈도우 가상머신 작업2](../../assets/images/glue-service/install-guide-glue-smb-actual-use-04.png){ align=center }
    - **폴더** 에서 Glue Samba Service를 구성한 **IP** 와 **공유 폴더** 명을 입력 합니다.
    - **로그인할 때 다시 연결** 을 체크 합니다.
    - **다른 자격 증명을 사용하여 연결** 을 체크 합니다.
    - 위 항목들을 입력 및 확인 후에 **마침** 버튼을 클릭합니다.
    ![윈도우 가상머신 작업3](../../assets/images/glue-service/install-guide-glue-smb-actual-use-05.png){ align=center }
    - Glue Samba Service를 생성 할 때, 만들었던 **유저 이름** 과 **유저 패스워드** 를 입력 합니다.
    - 위 항목들을 입력 및 확인 후에 **확인** 버튼을 클릭합니다.
    ![윈도우 가상머신 작업4](../../assets/images/glue-service/install-guide-glue-smb-actual-use-06.png){ align=center }
    - 연결된 화면입니다.
    - **폴더 및 파일** 의 생성, 수정, 삭제가 되는 지 확인 하신 후, 사용 하시면 됩니다.

### Samba AD용 윈도우 가상머신 작업

#### Samba AD Server 구성
1. Samba AD Server 구성
    ![AD 서버 구성1](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-01.png){ align=center }
    - 사용한 OS는 window server 2019 버전 입니다. 사용자에 맞게 구성 하시길 바랍니다.
    - 사용하실 윈도우에 접속합니다.
    - **Add roles and features** 버튼을 클릭 합니다.
    ![AD 서버 구성2](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-02.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성3](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-03.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성4](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-04.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성5](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-05.png){ align=center }
    - **Active Directory Domain Services** 버튼을 체크 합니다.
    - **DNS Server** 버튼을 체크 합니다.
    - 후에 **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성6](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-06.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성7](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-07.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성8](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-08.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성9](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-09.png){ align=center }
    - **Restart the destination server automatically if required** 버튼을 체크 합니다.
    - **Install** 버튼을 클릭 합니다.
    ![AD 서버 구성10](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-10.png){ align=center }
    - **Promote this server to a domain controller** 버튼을 클릭 합니다.
    ![AD 서버 구성11](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-11.png){ align=center }
    - **Add a new forest** 버튼을 체크 합니다.
    - **Root domain name** 입력란엔 설정한 도메인 이름을 입력 합니다.
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성12](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-12.png){ align=center }
    - **Password** 입력란에 설정한 패스워드를 입력 합니다.
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성13](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-13.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성14](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-14.png){ align=center }
    - **NetBIOS domain name** 은 자동으로 설정 됩니다.
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성15](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-15.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성16](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-16.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![AD 서버 구성17](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-17.png){ align=center }
    - **Install** 버튼을 클릭 하여 설치를 진행 합니다.
    ![AD 서버 구성18](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-18.png){ align=center }
    - 모든 설치가 완료 되고, 자동 재시작 후 구성된 화면입니다.

#### Samba Hyper-V 관리자 구성
!!! note
    앞의 구성 부분은 Samba AD용 구성 부분과 동일 합니다.

2. Samba Hyper-V 관리자 구성
    ![hyper-v 서버 구성1](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-19.png){ align=center }
    - **Hyper-V** 버튼을 체크 합니다.
    - 후에 **Next** 버튼을 클릭 합니다.
    ![hyper-v 서버 구성2](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-20.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![hyper-v 서버 구성3](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-21.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![hyper-v 서버 구성4](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-22.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![hyper-v 서버 구성5](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-23.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![hyper-v 서버 구성6](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-24.png){ align=center }
    - **Next** 버튼을 클릭 합니다.
    ![hyper-v 서버 구성7](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-25.png){ align=center }
    - **Restart the destination server automatically if required** 버튼을 체크 합니다.
    - **Install** 버튼을 클릭 합니다.
    ![hyper-v 서버 구성8](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-26.png){ align=center }
    - 모든 설치가 완료 되고, 자동 재시작 후 구성된 화면입니다.

#### Samba AD용 사용 방법
3. Samba AD용 사용 방법
    ![Samba AD용 사용 방법1](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-27.png){ align=center }
    - 왼쪽 상단에 **Hyper-V** 버튼을 클릭 합니다.
    - 해당 서버를 오른쪽 마우스 클릭 하여 **Hyper-V 관리자** 버튼을 클릭 합니다.
    ![Samba AD용 사용 방법2](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-28.png){ align=center }
    - 사용 했던 가상 컴퓨터의 디스크를 찾기 위해 오른쪽 마우스를 클릭 하여 **설정** 을 클릭 합니다.
    ![Samba AD용 사용 방법3](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-29.png){ align=center }
    - 왼쪽 탭에서 복사할 하드 드라이브를 클릭 하여 **경로** 를 복사 합니다.
    ![Samba AD용 사용 방법4](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-30.png){ align=center }
    - **파일 탐색기** 를 사용하여 해당 **경로** 로 접속 합니다.
    - 복사할 디스크를 선택하여 **복사** 를 진행 합니다.
    ![Samba AD용 사용 방법5](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-31.png){ align=center }
    - Samba 공유 폴더에 연결 하기 위해 **내 PC** -> **네트워크 드라이브 연결** 버튼을 클릭 합니다.
    ![Samba AD용 사용 방법6](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-32.png){ align=center }
    - Glue Samba Service 에서 AD용으로 구성된 **Storage Center 가상머신 IP 주소** 와 **공유 폴더명** 을 입력 합니다.
    - **로그인할 때 다시 연결** 및 **다른 자격 증명을 사용하여 연결** 부분을 해당 사항이 있을 경우 체크하여 **마침** 버튼을 클릭 합니다.
    ![Samba AD용 사용 방법7](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-33.png){ align=center }
    - Glue Samba Service에서 생성할 때의 **유저 이름** 과 **패스워드** 를 입력 합니다.
    - **확인** 버튼을 클릭 합니다.
    ![Samba AD용 사용 방법8](../../assets/images/glue-service/install-guide-glue-smb-ads-actual-use-34.png){ align=center }
    - 사용자의 환경에 맞게 **폴더** 를 생성하여 해당 **가상컴퓨터 디스크** 를 복사합니다.