본 문서는 ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조"를 구성하기 위한 단계 중, 4.1 단계인 DB 구성에 대한 문서입니다.

1. VPC 및 서브넷 생성
2. 가상머신 생성
3. 가상머신 디스크 설정
4. ==가상머신 WEB, WAS, DB 구성==
      1. ==DB 구성==
      2. WAS 구성
      3. WEB 구성
5. LB 구성

## 가상머신 터미널 접근

이전 단계에서 생성한 데이터베이스를 구성할 3개의 VM에 원격 접속합니다.
리눅스 커널에 접근하기 위한 방법으로 터미널 애플리케이션 또는 Mold의 콘솔을 통해 접근합니다.

- 터미널 애플리케이션을 통한 접근
    - 퍼블릭 IP를 생성합니다.(Mold -> 네트워크 -> vpc 선택 -> 퍼블릭 아이피 탭 -> 퍼블릭 아이피 가져오기 -> 스테틱 NAT 활성화 클릭 -> 서브넷 선택 -> vm1 선택)
    - 터미널 애플리케이션 실행하여 root 계정으로 접속합니다.

- Mold의 콘솔을 통한 접근
    - 콘솔 실행하여 root 계정으로 접속합니다. (Mold -> 가상머신 -> 접속하고자하는 VM 선택 -> 콘솔 버튼 클릭)

- Cube의 터미널 메뉴를 통한 접근

    !!! info "Cube 터미널"
        ABLESTACK Cube에 접속한 후 "터미널 메뉴"를 사용하여 터미널에 접근할 수 있습니다. 
        [Cube 터미널](../../../../administration/cube/terminal-guide) 문서를 참고하여 접속하십시오.

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
   1. 이름: `datadisk`
   2. 유형: `XFS`
   3. 크기: `100GiB` (최대 값)
   4. 적재지점(마운트 위치): `/mnt/data`
   5. 마운트 옵션: `지금 마운트`
   6. 암호화: `암호화 없음`

해당 과정을 통해 포멧, 마운트, 부팅 시 자동 마운트 설정이 적용됩니다.

!!! info "ABLESTACK Cube에서의 파티션 생성"
    ABLESTACK Cube에서의 파티션 생성을 위해 [Cube 파티션 생성](../../../../administration/cube/userinterface-guide#_1) 문서를 참고하십시오.

## 보안 설정
### 네트워크 방화벽 해제
ABLESTACK Cube의 "네트워킹" 메뉴를 클릭한 후 아래의 절차를 통해 네트워크 방화벽을 해제합니다.

1. 방화벽 섹션에서 "규칙 및 영역 편집" 버튼을 클릭합니다.
2. 설정할 네트워크 연결장치의 "서비스 추가" 버튼을 클릭합니다.
3. "galera" 를 검색한 후 해당 서비스를 추가합니다.
    ![3tier-linux-architecture-db-nw-firewall-02](../../../../assets/images/3tier-linux-architecture-db-nw-firewall-02.png)

!!! info "ABLESTACK Cube에서의 방화벽 설정"
    ABLESTACK Cube에서의 파티션 생성을 위해 [Cube 방화벽 서비스 활성화](../../../../administration/cube/networking-guide#_27) 문서를 참고하십시오.

### selinux 설정
가상머신 터미널 접근 후 아래의 절차를 통해 SELinux 정책을 강제에서 허용으로 영구적으로 변경합니다.
/etc/sysconfig/selinux 를 vi 편집기로 열어 정보를 변경합니다.
``` linuxconfig
$ vi /etc/sysconfig/selinux
```
SELINUX 값을 disabled로 변경합니다.
``` title="selinux"  linenums="1"
SELINUX=disabled
```

## DB 설치 및 구성
아래의 구조로 DB를 구성합니다.

![3tier-linux-architecture-db-nw-firewall-02](../../../../assets/images/3tier-linux-architecture-db-01.png)


### MariaDB 구성 (3node 동일)
#### MariaDB 패키지 설치를 위한 yum Repo 등록하기
/etc/yum.repos.d/mariadb.repo 를 vi 편집기로 열어 Repo 정보를 입력합니다.
``` linuxconfig
$ vi /etc/yum.repos.d/mariadb.repo
```
Rocky Linux 9.0의 경우 아래의 내용을 추가합니다.
``` title="mariadb.repo"  linenums="1"
# MariaDB 10.9 RedHat repository list - created 2022-11-30 05:38 UTC
# https://mariadb.org/download/
[mariadb]
name = MariaDB
baseurl = https://tw1.mirror.blendbyte.net/mariadb/yum/10.9/rhel9-amd64
gpgkey=https://tw1.mirror.blendbyte.net/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

#### MariaDB 패키지 설치
``` linuxconfig
$ dnf install MariaDB-server MariaDB-client
```
#### MariaDB 시작
``` yaml
$ systemctl enable mariadb.service # (1)!
$ systemctl start mariadb.service # (2)!
```

1.  VM 부팅 시 서비스를 자동 시작하도록 활성화합니다.
2.  MariaDB 서비스를 시작합니다.

#### MariaDB 보안 설정
``` yaml
$ mariadb-secure-installation
```

??? note "클릭하여 MariaDB의 보안설정 방법을 확인합니다."

    ```  linenums="1"
    Enter current password for root (enter for none):  [패스워드가 없기 때문에 엔터]
    OK, successfully used password, moving on...

    ※ 이 부분은 버전에 따라 안 나올 수 있습니다.
    Setting the root password or using the unix_socket ensures that nobody
    can log into the MariaDB root user without the proper authorisation.

    You already have your root account protected, so you can safely answer 'n'.
    Switch to unix_socket authentication [Y/n] Y  [MariaDB 실행 시 통신 소켓 생성 여부? Y 엔터]

    

    Enabled successfully!
    Reloading privilege tables..
    ... Success!


    You already have your root account protected, so you can safely answer 'n'.

    Change the root password? [Y/n] Y  [DB ROOT 패스워드 설정할 것인가? Y 엔터]

    New password:  패스워드 입력
    Re-enter new password:  재확인 패스워드 입력
    Password updated successfully!
    Reloading privilege tables..
    ... Success!

    By default, a MariaDB installation has an anonymous user, allowing anyone
    to log into MariaDB without having to have a user account created for
    them.  This is intended only for testing, and to make the installation
    go a bit smoother.  You should remove them before moving into a
    production environment.

    Remove anonymous users? [Y/n] Y  [익명의 접근을 막을 것인지? 보안을 위해 Y 엔터]
    ... Success!


    Normally, root should only be allowed to connect from 'localhost'.  This
    ensures that someone cannot guess at the root password from the network.

    Disallow root login remotely? [Y/n] Y  [DB ROOT 원격을 막을 것인지? 보안을 위해 Y 엔터]

    ... Success!

    By default, MariaDB comes with a database named 'test' that anyone can
    access.  This is also intended only for testing, and should be removed
    before moving into a production environment.

    Remove test database and access to it? [Y/n] Y

    [Test 용으로 생성된 데이터베이스를 삭제할 것인가? Y 엔터]

    - Dropping test database...
    ... Success!
    - Removing privileges on test database...
    ... Success!

    Reloading the privilege tables will ensure that all changes made so far
    will take effect immediately.

    Reload privilege tables now? [Y/n] Y  [현재 설정한 값을 적용할 것인지? 당연히 Y 엔터]

    ... Success!

    Cleaning up...

    All done!  If you've completed all of the above steps, your MariaDB
    installation should now be secure.

    Thanks for using MariaDB!  [설정 완료]
    ```

#### DB 외부접속 허용
MariaDB에 접속합니다.

``` yaml
$ mariadb -u root -p

Enter password: 패스워드 입력
```

``` yaml
MariaDB [(none)]> use mysql;
MariaDB [(none)]> grant all privileges on *.* to 'root'@'%'identified by '[패스워드 입력]'; # (1)!
MariaDB [(none)]> flush privileges;  # (2)!
```

1. 모든 db 및 테이블에 접근권한을 설정합니다.
2. 현재 사용중인 MariaDB의 캐시를 지우고 새로운 설정을 적용하기 위해 사용합니다. 


#### DB data 폴더 경로 변경하기
추가한 데이터 디스크로 DB 폴더를 변경합니다.

MariaDB 서비스를 중지합니다.
``` yaml
$ systemctl stop mariadb.service
```

#### Galera Cluster 설정 Node1,2,3(동일하게 설정)
Galera Cluster를 구성합니다.

??? note "마스터 노드 1, 2, 3 모두 동일하게 설정 및 실행합니다."

MariaDB 서비스를 중지합니다.
``` yaml
$ systemctl stop mariadb.service
```

MariaDB 설정 파일을 변경합니다.
``` yaml
$ vi /etc/my.cnf.d/server.cnf 
```

??? note "클릭하여 MariaDB의 설정 정보를 확인합니다."
    아래 예제를 참고하여 설정 정보를 변경합니다.
    ``` kconfig linenums="1" hl_lines="7 9 23"
    [galera]
    ## 기존 설정 값을 수정합니다.
    #
    # galear cluster 사용여부
    wsrep_on = ON
    # libgalera_smm.so 모듈 위치
    wsrep_provider = /usr/lib64/galera-4/libgalera_smm.so
    # 동기화 진행할 IP 리스트 (Master Node 1, 2, 3의 Public IP값을 입력합니다.)
    wsrep_cluster_address = gcomm://10.10.1.81, 10.10.1.82, 10.10.1.83
    # 기본 스토리지 엔진
    default_storage_engine=InnoDB
    # auto increment의 값 잠금방식 (0/1/2 중 택)
    innodb_autoinc_lock_mode=2
    # IP 접근설정
    bind-address=0.0.0.0
    # 바이너리 로그파일 형식
    binlog_format = ROW
    # log 사용여부
    general_log=ON
    # log 위치 설정
    log-error=/var/lib/mysql/error.log
    # 동기화할 노드들의 그룹명 (노드마다 동일하게 설정)
    wsrep_cluster_name = Cluster
    ```

#### Galera Cluster 및 DB 서비스 시작

??? Warning "노드 별 DB 시작 순서에 유의하여 아래 명령어를 실행합니다."

먼저 마스터 노드 1의 galera cluster를 먼저 시작합니다.
``` yaml
$ galera_new_cluster
```

마스터 노드 2, 3의 MariaDB 서비스를 시작합니다.
``` yaml
$ systemctl restart mariadb.service
```

#### Galera Cluster 설정 확인
MariaDB에 접속합니다.

``` yaml
$ mariadb -u root -p

Enter password: 패스워드 입력
```

``` yaml
MariaDB [(none)]> show variables like 'wsrep_cluster_address';
```

### DB 장애 복구
