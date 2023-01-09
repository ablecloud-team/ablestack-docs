본 문서는 ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조"를 구성하기 위한 단계 중, 4.2 단계인 WAS 구성에 대한 문서입니다.

1. VPC 및 서브넷 생성: VPC(Virtual Private Cloud)를 생성하고 서브넷(Subnet)을 생성합니다.
2. 가상머신 생성: 생성된 서브넷에서 WEB, WAS, DB 각각 3대(총 9대)의 가상머신을 SSHKeyPair 및 Affinity을 설정하여 추가합니다.
3. 티어 구성 준비: 생성된 가상머신의 터미널에 접속하고 데이터 디스크 볼륨 구성을 합니다.
4. ==티어 별 WEB, WAS, DB 구성:==
      1. DB: 갈레라 클러스터(Galera Cluster)를 활용하여 동기 방식의 복제구조를 사용하는 멀티마스터 DB를 구성합니다.
      2. WAS: 도커 컨테이너를 이용하여 NodeJS와 Samba 스토리지를 활용한 WAS를 구성합니다.
      3. ==WEB: 도커 컨테이너를 이용하여 Nginx와 NFS 스토리지를 활용한 WEB를 구성합니다.==
5. LB 구성: 동일 서브넷 상의 VM들을 하나의 Public IP를 생성하여 LB로 구성합니다.

## WAS 구성
아래의 구조로 WEB를 구성합니다.

가상머신 1: 

   - 개요: WEB Node 1 역할을 할 가상머신 1개 생성합니다.
   - Public 아이피 주소: 10.10.1.61

가상머신 2: 

   - 개요: WEB Node 2 역할을 할 가상머신 1개 생성합니다.
   - Public 아이피 주소: 10.10.1.62


가상머신 3: 

   - 개요: NFS 스토리지 Node로써 WEB Node 1, 2에서 사용되는 파일을 저장, 공유하는 공용스토리지 역할을 할 가상머신 1개 생성합니다.
   - Public 아이피 주소: 10.10.1.63

WEB 아키텍처 
![3tier-linux-architecture-web-01](../../../../assets/images/3tier-linux-architecture-web-01.png)

## 보안 설정
### 네트워크 방화벽 해제 (모든 WEB VM에 설정)
ABLESTACK Cube의 "네트워킹" 메뉴를 클릭한 후 아래의 절차를 통해 네트워크 방화벽을 해제합니다.

1. 방화벽 섹션에서 "규칙 및 영역 편집" 버튼을 클릭합니다.
2. 설정할 네트워크 연결장치의 "서비스 추가" 버튼을 클릭합니다.
3. "nfs" 를 검색한 후 해당 서비스를 추가합니다.
    ![3tier-linux-architecture-web-nw-firewall-01](../../../../assets/images/3tier-linux-architecture-web-nw-firewall-01.png)

!!! info "ABLESTACK Cube에서의 방화벽 설정"
    ABLESTACK Cube에서의 방화벽 설정을 위해 [Cube 방화벽 서비스 활성화](../../../../administration/cube/networking-guide#_27) 문서를 참고하십시오.

### NFS 스토리지 Node 구성 (가상머신 3에서만 수행합니다)
NFS 스토리지가 설치되어 WEB Node 1, 2와 데이터를 공유할 NFS 스토리지 Node에서 아래 절차를 수행합니다.
#### NFS Server 패키지 설치
``` yaml
$ dnf install nfs-utils
```

#### 공유 폴더 생성
WEB 컨테이너와 파일을 공유할 NFS 스토리지의 공유폴더를 생성하고 적절한 권한을 부여합니다.
스토리지 공유폴더 경로 예시는 `/mnt/data/nfs` 입니다.
``` yaml
$ mkdir /mnt/data/nfs
$ chmod -R 777 /mnt/data/nfs
```

#### NFS 스토리지 설정
공유하려는 디렉토리와 서버 설정을 위해 `/etc/exports` 를 vi 편집기로 열어 정보를 입력합니다.
``` 
$ vi /etc/exports
```
모든 사용자 또는 특정 범위 IP 사용자 접근 여부를 설정합니다.
``` yaml
# 모든 사용자 접근 허용 시
/mnt/data/nfs *(rw,sync,no_root_squash) 

# 특정 범위 IP 사용자 접근 허용 시
# /mnt/data/nfs 10.10.1.0/24(rw,sync,no_root_squash) 
```

#### NFS Server 서비스 시작
NFS Server Node의 NFS Server 서비스를 등록하고 시작합니다.
``` yaml
$ systemctl enable nfs-server.service
$ systemctl start nfs-server.service
```

#### NFS 스토리지 설정 적용
윗 단계에서 설정한 `/etc/exports` 파일을 적용합니다.
```
exportfs -arv
```

### WEB Node 1, 2 구성

#### SAMBA 패키지 설치
``` yaml
$ dnf install samba samba-client cifs-utils
```

#### 공유할 폴더 생성
WAS Node 3 (Samba Storage Node)와 파일을 공유할 폴더를 생성합니다.
``` yaml
$ mkdir /mnt/data/shared_folder
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
```
username=user1
password=Ablecloud1!
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
$ vi  /etc/fstab
```

``` 
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
$ podman pull docker.io/stardom3645/nodejs-server:latest
```

#### NodeJs 컨테이너 (WAS) 실행 
WAS Node 1,2 에서 다운로드한 NodeJs 컨테이너 이미지를 실행합니다.
해당 이미지는 윗 단계에서 다운로드한 샘플 웹소스를 구동하기 위해 제작된 커스터마이즈된 이미지입니다.

```
$ podman run -d -p 5000:3000 -p 8081:8081 --name nodejs-server --restart always -v /mnt/data/shared_folder:/usr/src/app stardom3645/nodejs-server:latest

# run: 컨테이너를 실행합니다.
# -p: 포트포워딩 (외부:내부)
# --name: 컨테이너 이름
# --restart: 컨테이너 오류 시, 재시작 방법
# -v: 컨테이너의 특정 폴더와 로컬의 폴더를 서로 공유
# "stardom3645/nodejs-server:latest": 다운로드한 이미지 이름
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






