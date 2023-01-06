본 문서는 ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조"를 구성하기 위한 단계 중, 3 단계인 가상머신 구성 준비에 대한 문서입니다.

1. VPC 및 서브넷 생성: VPC(Virtual Private Cloud)를 생성하고 서브넷(Subnet)을 생성합니다.
2. 가상머신 생성: 생성된 서브넷에서 WEB, WAS, DB 각각 3대(총 9대)의 가상머신을 SSHKeyPair 및 Affinity을 설정하여 추가합니다.
3. ==티어 구성 준비: 생성된 가상머신의 터미널에 접속하고 데이터 디스크 볼륨 구성을 합니다.==
4. 티어 별 WEB, WAS, DB 구성:
      1. DB: 갈레라 클러스터(Galera Cluster)를 활용하여 동기 방식의 복제구조를 사용하는 멀티마스터 DB를 구성합니다.
      2. WAS: 도커 컨테이너를 이용하여 NodeJS를 활용한 WAS를 구성합니다.
      3. WEB: 도커 컨테이너를 이용하여 Nginx를 활용한 WAS를 구성합니다.
5. LB 구성: 동일 서브넷 상의 VM들을 하나의 Public IP를 생성하여 LB로 구성합니다.


## 가상머신 터미널 접근

이전 단계에서 생성한 데이터베이스를 구성할 3개의 VM에 원격 접속합니다.
리눅스 커널에 접근하기 위한 방법으로 터미널 애플리케이션 또는 Cube, Mold를 통해 접근합니다.

- 터미널 애플리케이션, SSH 원격 접속을 통한 접근
    - 이전 단계에서 생성한 퍼블릭 IP로 터미널 애플리케이션 실행하여 root 계정으로 접속합니다.

- Mold의 콘솔을 통한 접근
    - 콘솔 실행하여 root 계정으로 접속합니다. (Mold -> 가상머신 -> 접속하고자하는 VM 선택 -> 콘솔 버튼 클릭)

- Cube의 터미널 메뉴를 통한 접근

    !!! info "Cube 터미널"
        ABLESTACK Cube에 접속한 후 "터미널 메뉴"를 사용하여 터미널에 접근할 수 있습니다. 
        [Cube 터미널](../../../../administration/cube/terminal-guide) 문서를 참고하십시오.

## 가상머신 데이터 디스크 설정
### ABLESTACK Cube에 접속
가상머신 생성 시 추가하였던 데이타 디스크를 설정하고 사용하기 위해 ABLESTACK Cube에 접속합니다.

!!! info "ABLESTACK Cube에 접속"
    ABLESTACK Cube에 접속을 위해 해당 VM의 "cockpit.socket" 서비스를 `$ systemctl start cockpit.socket` 명령어를 통해 실행한 후 
    [Cube 로그인](../../../../administration/cube/userinterface-guide#_1) 문서를 참고하여 접속하십시오.

### 파티션 설정
ABLESTACK Cube의 "저장소" 메뉴를 클릭한 후 아래의 절차를 통해 추가한 데이터 디스크의 파티션을 생성합니다.

1. 사용할 데이터 디스크를 `드라이브` 섹션에서 선택합니다.
2. `파티션 테이블 만들기` 을 클릭하여 초기화를 합니다.
3. `파티션 만들기` 를 클릭하여 해당 디스크에 파티션을 생성합니다. 파티션 만들기 예제는 다음과 같습니다.
   1. 이름: `datadisk1`
   2. 유형: `XFS`
   3. 크기: `100GiB` (최대 값)
   4. 적재지점(마운트 위치): `/mnt/data`
   5. 마운트 옵션: `지금 마운트`
   6. 암호화: `암호화 없음`

해당 과정을 통해 포멧, 마운트, 부팅 시 자동 마운트 설정이 적용됩니다.

!!! info "ABLESTACK Cube에서의 파티션 생성"
    ABLESTACK Cube에서의 파티션 생성을 위해 [Cube 파티션 생성](../../../../administration/cube/userinterface-guide#_1) 문서를 참고하십시오.