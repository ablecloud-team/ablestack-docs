ABLESTACK Mold를 이용한 **이중화를 통한 고가용성 기능을 제공하는 리눅스 기반의 3계층 구조** 의를 구성하기 위한 단계 중, 4.2 단계인 WAS 구성에 대한 문서입니다.

1. VPC 및 서브넷 생성: VPC(Virtual Private Cloud)를 생성하고 서브넷(Subnet)을 생성합니다.
2. 가상머신 생성: 생성된 서브넷에서 WEB, WAS, DB 각각 3대(총 9대)의 가상머신을 SSHKeyPair 및 Affinity을 설정하여 추가합니다.
3. 티어 구성 준비: 생성된 가상머신의 터미널에 접속하고 데이터 디스크 볼륨 구성을 합니다.
4. ==티어 별 WEB, WAS, DB 구성:==
      1. DB: 갈레라 클러스터(Galera Cluster)를 활용하여 동기 방식의 복제구조를 사용하는 멀티마스터 DB를 구성합니다.
      2. ==WAS: 도커 컨테이너를 이용하여 NodeJS를 구성하고 Samba 스토리지를 활용한 WAS를 구성합니다.==
      3. WEB: 도커 컨테이너를 이용하여 Nginx와 NFS 스토리지를 활용한 WEB를 구성합니다.
5. LB 구성: 하나의 Public IP를 생성하여 동일 서브넷 상의 VM들의 이중화를 위해 LB를 구성합니다.

## WAS 구성
아래의 구조로 WAS를 구성합니다.

가상머신 1: 

   - 개요: WAS Node 1 역할을 할 가상머신 1개 생성합니다.
   - Public 아이피 주소: 10.10.1.71

가상머신 2: 

   - 개요: WAS Node 2 역할을 할 가상머신 1개 생성합니다.
   - Public 아이피 주소: 10.10.1.72


가상머신 3: 

   - 개요: Samba Storage Node로써 WAS Node 1, 2에서 사용되는 웹 소스를 저장, 공유하는 공용스토리지 역할을 할 가상머신 1개 생성합니다.
   - Public 아이피 주소: 10.10.1.73

WAS 아키텍처 
![3tier-linux-architecture-was-01](../../../../assets/images/3tier-linux-architecture-was-01.png)

### Affinity 그룹 생성
VM 생성하기 전, Anti Affinity 그룹을 생성하여 어느하나의 서브넷에 속한 VM들이 특정 호스트 한 곳에 몰려 실행하도록 하거나 반대로 몰려 실행되지 않도록 합니다.
이중화를 위해 Affinity 그룹을 anti-affinity 유형으로 WEB, WAS, DB 각각 추가해야합니다. 이를 위해 `컴퓨트 > Affinity 그룹` 화면으로 이동하여 `새 Affinity 그룹 추가` 버튼을 클릭합니다.
클릭하게되면 다음과 같은 입력항목을 확인할 수 있습니다. 

<figure markdown>
![3tier-linux-architecture-add-affinity-group](../../../../assets/images/3tier-linux-architecture-add-affinity-group.png)
<figcaption>새 Affinity 그룹 추가 대화 상자</figcaption>
</figure markdown>

- 이름 : 서브넷을 분별할 수 있는 Affinity 그룹 이름을 입력합니다.
- 설명 : Affinity 그룹에 대한 설명을 입력합니다.
- 유형 : Affinity 그룹에 대한 유형을 선택합니다. Anti 여부를 선택할 수 있습니다. 

새 Affinity 그룹 추가 대화상자에서의 입력 항목 예제는 다음과 같습니다.

- 이름 : `ablecloud-3tier-linux-web`
- 설명 : `3tiers-linux의 web 구성 시 사용되는 Affinity 그룹입니다.`
- 유형 : `host anti-affinity (Strict)`

!!! info "Affinity 그룹 유형"
    host anti-affinity:	가능한 한 서로 다른 호스트에 인스턴스를 배포합니다.

    host affinity: 가능한 한 동일한 호스트에 인스턴스를 배포합니다.

    * Non-Strict 옵션은 마지막 실행 호스트를 고려하여 실행됩니다.






## 보안 설정
### 네트워크 방화벽 해제 (모든 WAS VM에 설정)
ABLESTACK Cube의 "네트워킹" 메뉴를 클릭한 후 아래의 절차를 통해 네트워크 방화벽을 해제합니다.

1. 방화벽 섹션에서 "규칙 및 영역 편집" 버튼을 클릭합니다.
2. 설정할 네트워크 연결장치의 "서비스 추가" 버튼을 클릭합니다.
3. "samba" 를 검색한 후 해당 서비스를 추가합니다.
    ![3tier-linux-architecture-was-nw-firewall-01](../../../../assets/images/3tier-linux-architecture-was-nw-firewall-01.png)

!!! info "ABLESTACK Cube에서의 방화벽 설정"
    ABLESTACK Cube에서의 방화벽 설정을 위해 [Cube 방화벽 서비스 활성화](../../../../administration/cube/networking-guide#_27) 문서를 참고하십시오.

### Samba Storage Node 구성 (가상머신 3에서만 수행합니다)
Samba storage가 설치되어 WAS Node 1, 2와 데이터를 공유할 Samba Storage Node에서 아래 절차를 수행합니다.
#### Samba 패키지 설치
``` 
$ dnf install samba
```

#### 공유 폴더 생성
WAS 컨테이너와 파일을 공유할 SAMBA 스토리지의 공유폴더를 생성하고 적절한 권한을 부여합니다.
스토리지 공유폴더 경로 예시는 `/mnt/data/shared_folder` 입니다.
``` 
$ mkdir -p /mnt/data/shared_folder
$ chmod -R 777 /mnt/data/shared_folder
```

#### Samba 사용자 생성 및 패스워드 설정
리눅스 계정을 생성합니다.
```
$ useradd user1
$ passwd user1
```

리눅스 계정과 동일한 이름으로 samba 계정을 생성합니다.
```
$ smbpasswd -a user1
```

#### 웹 소스 공유폴더에 다운로드
먼저 git 패키지를 설치한 후 생성한 폴더에 Git 소스를 다운로드합니다.
``` 
$ dnf install git
$ git clone https://github.com/stardom3645/3tier_linux_example.git /mnt/data/shared_folder/
```

!!! info "다른 웹소스를 NodeJs 서버에 구동하기"
    위 예시에서 제시된 Git 소스가 아닌 다른 웹소스를 사용하려면 Docker 컨테이니너 이미지에서 해당 웹소스를 구동할 수 있는 이미지이어야 합니다.
    즉 기본 Docker NodeJs 이미지를 해당 웹소스를 구동하도록 Dockerfile을 생성하여 새로 이미지로 빌드하여야합니다.

#### 웹 소스 변경
다운로드 받은 웹 소스의 DB 설정정보를 미리 구성된 DB로 변경합니다.
```
vi /mnt/data/shared_folder/router/signUp/index.js
```
Host, User, Password, Port, Database 정보를 사전에 구성된 DB 정보로 변경합니다.
```  title="index.js"  linenums="1"
// DATABASE setting
var connection = mysql.createPool({
	host: '10.10.1.80',
	user: 'root',
	password: 'PASSWORD!',
	port: '3306',
	database: 'galeradb'
});
```

#### NodeJs 모듈 패키지 설치
NodeJs 서버 구동을 위해 패키지를 설치합니다.
```
$ cd /mnt/data/shared_folder/
$ dnf module install nodejs
$ npm install
```

#### Samba 설정
/etc/samba/smb.conf 를 vi 편집기로 열어 samba 정보를 입력합니다.
``` 
$ vi /etc/samba/smb.conf
```

```   title="smb.conf"  linenums="1"
[user1]
        path = /mnt/data/shared_folder
        # 사용 가능한 공유 목록에 디렉토리를 보여줄지 여부를 설정합니다.
        browseable = yes
        read only = no
        writable = yes
        #user1에 쓰기 권한 부여합니다.
        write list = user1
        # 이 공유에서 새로 만든 파일에 대한 권한을 설정합니다.
        force create mode = 0777
        # 이 공유에서 새로 만든 디렉토리에 대한 권한을 설정합니다.
        force directory mode = 2770
        public = yes
```

#### selinux 디렉토리 보안 설정

``` 
$ setsebool -P samba_enable_home_dirs on                # 삼바 홈 디렉토리 읽기/쓰기 권한 부여
$ setsebool -P samba_export_all_rw on                   # (읽기, 쓰기) 또는 setsebool -P samba_export_all_ro on (읽기만)
$ chcon -R -t samba_share_t /mnt/data/shared_folder     # 하위디렉토리 포함 특정디렉토리 삼바권한부여
```

#### Samba 서비스 시작
Samba Storage Node의 smb 서비스를 시작합니다.
``` 
$ systemctl enable smb
$ systemctl start smb
```

### WAS Node 1, 2 구성

#### Samba 패키지 설치
``` 
$ dnf install samba samba-client cifs-utils
```

#### 공유할 폴더 생성
WAS Node 3 (Samba Storage Node)와 파일을 공유할 폴더를 생성합니다.
``` 
$ mkdir -p /mnt/data/shared_folder
$ chmod -R 777 /mnt/data/shared_folder
```

#### Samba 사용자 생성 및 패스워드 설정
리눅스 계정을 생성합니다.
```
$ useradd user1
$ passwd user1
```

리눅스 계정과 동일한 계정 이름으로 samba 계정을 생성합니다.
```
$ smbpasswd -a user1
```

#### Samba 스토리지 마운트 계정정보 파일 생성
Samba 스토리지 마운트 시, 명령줄에 계정 및 패스워드를 노출하는 대신 계정 정보가 담긴 파일을 생성하여 마운트합니다. 
이를 위해 `.smb.cred` 파일을 생성합니다.

```
$ vi /root/.smb.cred
```

WAS Node 3 (Samba Storage Node)에서 설정한 내용으로 계정정보 파일을 생성합니다.
``` title="smb.conf"  linenums="1"
username=user1
password=PASSWORD # 패스워드를 입력하세요.
```

#### samba 스토리지 마운트
``` 
$ mount -t cifs -o credentials=/root/.smb.cred,vers=3.0 //10.10.1.73/user1 /mnt/data/shared_folder

# cifs: 프로토콜
# credentials: samba 계정정보
# user1: samba 스토리지 정보 (경로 정보 포함된 /etc/samba/smb.conf 내용)
# /mnt/data/shared_folder: 마운트할 위치
```

추가적으로 재부팅 시 자동으로 마운트가 적용되도록 합니다.
이를 위해 `/etc/fstab` 를 vi 편집기로 열어 아래 내용을 추가합니다.
```
$ vi /etc/fstab
```

``` title="fstab"  linenums="1"
//10.10.1.73/user1 /mnt/data/shared_folder cifs credentials=/root/.smb.cred,vers=3.0,iocharset=utf8 0 0

# cifs: 프로토콜
# credentials: samba 계정정보
# user1: samba 스토리지 정보 (경로 정보 포함된 /etc/samba/smb.conf 내용)
# /mnt/data/shared_folder: 마운트할 위치
```


#### NodeJs 컨테이너 이미지 다운로드
WAS Node 1,2 에서 실행할 NodeJs 컨테이너 이미지를 다운로드 받습니다.
해당 이미지는 샘플 웹소스를 구동하기 위해 제작된 커스터마이즈된 이미지로써 `server.js`를 실행합니다.

```
$ podman pull docker.io/ablecloudteam/nodejs-server:linux-0.1
```

#### NodeJs 컨테이너 (WAS) 실행 
WAS Node 1,2 에서 다운로드한 NodeJs 컨테이너 이미지를 실행합니다.
해당 이미지는 윗 단계에서 다운로드한 샘플 웹소스를 구동하기 위해 제작된 커스터마이즈된 이미지입니다.

```
$ podman run -d -p 5000:3000 --name nodejs-server --restart always -v /mnt/data/shared_folder:/usr/src/app ablecloudteam/nodejs-server:linux-0.1

# run: 컨테이너를 실행합니다.
# -d: detached 모드 (컨테이너 백그라운드 실행)
# -p: 포트포워딩 (외부:내부)
# --name: 컨테이너 이름
# --restart: 컨테이너 오류 시, 항상 재시작
# -v: 컨테이너의 특정 폴더와 로컬의 폴더를 서로 공유
# ablecloudteam/nodejs-server:linux-0.1: 다운로드한 이미지 이름
```

#### NodeJs 컨테이너 (WAS) VM 부팅 시 자동실행
서비스를 생성하는 방법으로 VM 부팅 시 해당 컨테이너가 자동으로 실행하도록 할 수 있습니다.
```
$ podman generate systemd nodejs-server  > /etc/systemd/system/nodejs-server.service
$ systemctl enable nodejs-server.service
$ systemctl daemon-reload
```

### 클라이언트 접근
`http://{{publicIp}}:5000`에 접속하여 정상 작동 되는 지 확인합니다.






