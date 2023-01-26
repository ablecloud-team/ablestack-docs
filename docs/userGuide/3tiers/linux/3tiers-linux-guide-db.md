본 문서는 ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조" [구성 단계](../3tiers-linux-guide-prepare#_5) 중, 세 번째 단계인 DB 구성에 대한 문서입니다.

MariaDB를 구성하고 동기방식으로 데이터를 복제하는 갈레라 클러스터(Galera Cluster)를 활용하여 3개의 DB 가상머신을 한 클러스터로 이중화 구성하는 방법은 다음과 같은 절차로 실행됩니다.

- 가상머신 생성
- 데이터 디스크 설정
- MariaDB 구성
- Galera Cluster 설정
- 부하분산(LB) 설정

## 가상머신 생성
ABLESTACK Mold는 기본적으로 템플릿을 이용해 가상머신을 생성하고 사용하는 것을 권장합니다. 따라서 관리용 가상머신을 생성하기 전에 먼저 "[가상머신 사용 준비](../../vms/centos-guide-prepare-vm.md)" 단계를 통해 CentOS 기반의 가상머신 템플릿 이미지를 생성하여 등록하는 절차를 수행한 후 VM을 생성해야 합니다.

가상머신을 추가하기 위해 `컴퓨트 > 가상머신` 화면으로 이동하여 `가상머신 추가` 버튼을 클릭합니다. "새 가상머신" 마법사 페이지가 표시됩니다. 
해당 페이지에서는 "템플릿을 이용한 VM 생성" 문서를 참고하여 가상머신을 생성합니다.

!!! info "템플릿을 이용한 VM 생성"
    템플릿을 이용한 가상머신 추가를 위해 [템플릿을 이용한 VM 생성](../../../vms/centos-guide-add-and-use-vm#vm) 문서를 참고하십시오.

입력 항목 예시는 다음과 같습니다.

- DB 가상머신 1

    - 배포 인프라 선택 : `Zone`
    - 템플릿/ISO : `Rocky Linux 9.0 기본 이미지 템플릿` * Rocky Linux release 9.0 (Blue Onyx)
    - 컴퓨트 오퍼링 : `1C-2GB-RBD-HA`
    - 데이터 디스크 : `100GB-WB-RBD` * MariaDB의 데이터가 저장되는 경로로 사용됩니다.
    - 네트워크 : `db` * VPC명이 일치되는지 확인합니다.
        - IP: 192.168.3.11
    - SSH 키 쌍 : `3tier_linux_keypair` 
    - 확장 모드 : ` ` * 디폴트 값으로 생성합니다.
    - 이름 : `ablecloud-3tier-linux-db-01`

- DB 가상머신 2

    - 배포 인프라 선택 : `Zone`
    - 템플릿/ISO : `Rocky Linux 9.0 기본 이미지 템플릿` * Rocky Linux release 9.0 (Blue Onyx)
    - 컴퓨트 오퍼링 : `1C-2GB-RBD-HA`
    - 데이터 디스크 : `100GB-WB-RBD` * MariaDB의 데이터가 저장되는 경로로 사용됩니다.
    - 네트워크 : `db` * VPC명이 일치되는지 확인합니다.
        - IP: 192.168.3.12
    - SSH 키 쌍 : `3tier_linux_keypair` 
    - 확장 모드 : ` ` * 디폴트 값으로 생성합니다.
    - 이름 : `ablecloud-3tier-linux-db-02`

- DB 가상머신 3

    - 배포 인프라 선택 : `Zone`
    - 템플릿/ISO : `Rocky Linux 9.0 기본 이미지 템플릿` * Rocky Linux release 9.0 (Blue Onyx)
    - 컴퓨트 오퍼링 : `1C-2GB-RBD-HA`
    - 데이터 디스크 : `100GB-WB-RBD` * MariaDB의 데이터가 저장되는 경로로 사용됩니다.
    - 네트워크 : `db` * VPC명이 일치되는지 확인합니다.
        - IP: 192.168.3.13
    - SSH 키 쌍 : `3tier_linux_keypair` 
    - 확장 모드 : ` ` * 디폴트 값으로 생성합니다.
    - 이름 : `ablecloud-3tier-linux-db-03`


## 데이터 디스크 설정
안정적인 운영을 위해 기본 RootDisk가 아닌 고용량의 스펙을 가진 디스크로의 데이터 저장이 필요합니다. 이를 위한 사전작업으로 가상머신 생성 시 추가했던 데이터 디스크를 설정합니다.

다음과 같은 절차로 데이터 디스크를 설정합니다.

- fdisk -l 명령어를 이용하여 현재 디스크 현황과 파티션 현황을 확인합니다.
``` linenums="1"
$ fdisk -l
```

- fdisk -l 명령어 실행 결과 디스크 "/dev/sdb"에 아무런 파티션이 없는 상태인 것을 확인합니다.
``` linenums="1" hl_lines="13-17"
Disk /dev/sda: 100 GiB, 107374182400 bytes, 209715200 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xfc3d5b0c

Device     Boot   Start       End   Sectors Size Id Type
/dev/sda1  *       2048   2099199   2097152   1G 83 Linux
/dev/sda2       2099200 209715199 207616000  99G 8e Linux LVM

Disk /dev/sdb: 100 GiB, 107374182400 bytes, 209715200 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

- fdisk 명령어를 이용하여 "/dev/sdb" 디스크에 파티션 설정을 합니다.
``` linenums="1"
$ fdisk /dev/sdb
```

- n 을 입력하여 새로운 파티션을 생성하고 p를 입력하여 주 파티션으로 선택합니다.
``` linenums="1" 
Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): 
```

- 파티션 번호를 설정하는 단계입니다. 기본 값인 "1"을 입력하거나 엔터로 넘어갈 수 있습니다.
``` linenums="1"
Partition number (1-4, default 1): 
```

- 시작할 섹터를 지정할 수 있습니다. 기본 값을 입력하거나 엔터로 넘어갈 수 있습니다.
``` linenums="1"
First sector (2048-143305919, default 2048): 
Using default value 2048
```

- 파티션의 용량을 설정합니다. 디스크 전체를 하나의 파티션으로 생성할 경우 기본 값을 입력하거나 엔터로 넘어갈 수 있습니다.
``` linenums="1"
First sector (2048-143305919, default 2048): 
Using default value 2048
```

- "w"를 입력하여 파티션 정보를 디스크에 적용합니다.
``` linenums="1"
Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
```

- fdisk -l 명령어 실행하여 변경된 파티션 정보를 확인합니다. 
``` linenums="1"
$ fdisk -l
```

- 생성된 파티션 "/dev/sdb1" 를 확인할 수 있습니다.
``` linenums="1" hl_lines="9-10"
Disk /dev/sdb: 100 GiB, 107374182400 bytes, 209715200 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x1fd9e01f

Device     Boot Start       End   Sectors Size Id Type
/dev/sdb1        2048 209715199 207616000 100G 83 Linux
```

- mkfs 명령어를 이용하여 "/dev/sdb1" 파티션에 xfs 파일 시스템을 생성합니다.
``` linenums="1" 
$ mkfs.xfs /dev/sdb1
```

- 정상 적으로 파일 시스템이 생성되었는지 "fsck -N"  명령어를 통해 확인합니다.
``` linenums="1" 
$ fsck -N /dev/sdb1
```

- xfs 파일 시스템이 있는 것을 확인할 수 있습니다.
``` linenums="1" 
fsck from util-linux 2.37.4
[/usr/sbin/fsck.xfs (1) -- /dev/sdb1] fsck.xfs /dev/sdb1
```

- /dev/sdb1 파티션을 /mnt/data 경로에 마운트를 적용합니다. 마운트할 경로에 폴더가 없다면 먼저 생성한 후 적절한 권한을 부여한 후 마운트를 적용합니다.
``` linenums="1" 
$ mkdir /mnt/data
$ chmod -R 1777 /mnt/data
$ mount /dev/sdb1 /mnt/data
```

- 정상 적으로 마운트가 적용되었는지 확인합니다.
``` linenums="1" 
$ mount | grep "sdb1"
```

- "/mnt/data"에 적상적으로 마운트 적용된 것을 확인할 수 있습니다.
``` linenums="1" 
/dev/sdb1 on /mnt/data type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota)
```







## 보안 설정
### 네트워크 방화벽 해제 (DB Node 1, 2, 3 모든 VM에 설정합니다.)
ABLESTACK Cube의 "네트워킹" 메뉴를 클릭한 후 아래의 절차를 통해 네트워크 방화벽을 해제합니다.

1. 방화벽 섹션에서 "규칙 및 영역 편집" 버튼을 클릭합니다.
2. 설정할 네트워크 연결장치의 "서비스 추가" 버튼을 클릭합니다.
3. "galera" 를 검색한 후 해당 서비스를 추가합니다.
    ![3tier-linux-architecture-db-nw-firewall-02](../../../../assets/images/3tier-linux-architecture-db-nw-firewall-02.png)

!!! info "ABLESTACK Cube에서의 방화벽 설정"
    ABLESTACK Cube에서의 파티션 생성을 위해 [Cube 방화벽 서비스 활성화](../../../../administration/cube/networking-guide#_27) 문서를 참고하십시오.

### selinux 설정
가상머신 [터미널](../../../../administration/cube/3tiers-linux-guide-use-vm#_1) 접근 후 아래의 절차를 통해 SELinux 정책을 강제에서 허용으로 영구적으로 변경합니다.
/etc/sysconfig/selinux 를 vi 편집기로 열어 정보를 변경합니다.
``` 
$ vi /etc/sysconfig/selinux
```
SELINUX 값을 disabled로 변경합니다.
``` title="selinux"  linenums="1"
SELINUX=disabled
```

### MariaDB 구성 (3node 동일)
#### MariaDB 패키지 설치를 위한 yum Repo 등록하기
/etc/yum.repos.d/mariadb.repo 를 vi 편집기로 열어 Repo 정보를 입력합니다.
``` 
$ vi /etc/yum.repos.d/mariadb.repo
```
Rocky Linux 9.0의 경우 아래의 내용을 추가합니다. 다른 운영체제인 경우 [MariaDB Repository Link](https://mariadb.org/download/?t=repo-config){:target="_blank"} 를 클릭하여 확인 후 적용합니다.
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
``` 
$ systemctl enable mariadb.service # (1)!
$ systemctl start mariadb.service # (2)!
```

1.  VM 부팅 시 서비스를 자동 시작하도록 활성화합니다.
2.  MariaDB 서비스를 시작합니다.

#### MariaDB 보안 설정
``` 
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

    Remove anonymous users? [Y/n] Y  [익명의 접근을 막을 것인지? 보안을 위해 Y 또는 편의를 위해 N을 선택]
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

``` 
$ mariadb -u root -p

Enter password: 패스워드 입력
```

``` 
MariaDB [(none)]> use mysql;
MariaDB [(none)]> grant all privileges on *.* to 'root'@'%'identified by '[패스워드 입력]'; # (1)!
MariaDB [(none)]> flush privileges;  # (2)!
```

1. 모든 db 및 테이블에 접근권한을 설정합니다.
2. 현재 사용중인 MariaDB의 캐시를 지우고 새로운 설정을 적용하기 위해 사용합니다. 


#### DB data 폴더 경로 변경하기
추가한 데이터 디스크로 DB 폴더를 변경하기 위해 먼저 기존 DB data 경로를 확인합니다.

1. MariaDB에 접속하여 DB data 경로를 확인합니다.
    ``` 
    $ mariadb -u root -p

    Enter password: 패스워드 입력
    ```
    ``` 
    MariaDB [(none)]> select @@datadir;
    ```

2. MariaDB에서 로그아웃한 후 MariaDB 서비스를 정지합니다.
    ``` 
    $ systemctl stop mariadb
    ```

3. 새로운 Data 디렉토리에 데이터를 복사합니다. 현 예시에서는 경로가 /var/lib/mysqld에서 /mnt/data/mysql 로 설정합니다.)
    ``` 
    $ rsync -av /var/lib/mysql /mnt/data/
    $ chown -R mysql:mysql /mnt/data/mysql
    ```

4. my.cnf 파일을 수정하여 MariaDB의 data 디렉토리 경로를 변경합니다.
    ``` 
    $ vi /etc/my.cnf
    ```

    아래의 내용으로 변경합니다.
    ``` title="my.cnf"  linenums="1"
    [client-server]
    datadir=/home/data/mysql
    socket=/home/data/mysql/mysql.sock
    ```

5. SELinux 보안 설정 및 context 추가
    ``` 
    $ semanage fcontext -a -t mysqld_db_t "/data/mysql(/.*)?"
    $ restorecon -R /data/mysql
    ```

6. MariaDB 서비스를 시작합니다.
    ``` 
    $ systemctl restart mariadb
    ```

7. MariaDB에 접속한 후 변경된 DB data 경로를 확인합니다.
    ``` 
    MariaDB [(none)]> select @@datadir;
    ```

8. 기존 data 디렉토리 삭제합니다.
    ``` 
    $ rm -R /var/lib/mysql
    ```

#### Galera Cluster 설정
Galera Cluster를 구성합니다.

MariaDB 서비스를 중지합니다.
``` 
$ systemctl stop mariadb.service
```

MariaDB 설정 파일을 변경합니다.
``` 
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
```
$ galera_new_cluster
```

마스터 노드 2, 3의 MariaDB 서비스를 시작합니다.
```
$ systemctl restart mariadb.service
```

#### Galera Cluster 설정 확인
MariaDB에 접속합니다.

```
$ mariadb -u root -p

Enter password: 패스워드 입력
```
갈레라 클러스터를 구성하는 전체 노드의 IP 주소 목록을 확인합니다.
```
MariaDB [(none)]> show variables like 'wsrep_cluster_address';
```
출력된 결과 값을 확인합니다.

```
+-----------------------+-----------------------------------------------+
| Variable_name         | Value                                         |
+-----------------------+-----------------------------------------------+
| wsrep_cluster_address | gcomm://10.10.1.81, 10.10.1.82, 10.10.1.83 |
+-----------------------+-----------------------------------------------+
```
