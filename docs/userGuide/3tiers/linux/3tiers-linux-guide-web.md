본 문서는 ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조"를 구성하기 위한 단계 중, 4.2 단계인 WAS 구성에 대한 문서입니다.

1. VPC 및 서브넷 생성: VPC(Virtual Private Cloud)를 생성하고 서브넷(Subnet)을 생성합니다.
2. 가상머신 생성: 생성된 서브넷에서 WEB, WAS, DB 각각 3대(총 9대)의 가상머신을 SSHKeyPair 및 Affinity을 설정하여 추가합니다.
3. 티어 구성 준비: 생성된 가상머신의 터미널에 접속하고 데이터 디스크 볼륨 구성을 합니다.
4. ==티어 별 WEB, WAS, DB 구성:==
      1. DB: 갈레라 클러스터(Galera Cluster)를 활용하여 동기 방식의 복제구조를 사용하는 멀티마스터 DB를 구성합니다.
      2. WAS: 도커 컨테이너를 이용하여 NodeJS와 Samba 스토리지를 활용한 WAS를 구성합니다.
      3. ==WEB: 도커 컨테이너를 이용하여 Nginx와 NFS 스토리지를 활용한 WEB를 구성합니다.==
5. LB 구성: 하나의 Public IP를 생성하여 동일 서브넷 상의 VM들의 이중화를 위해 LB를 구성합니다.

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
3. "nfs", "mountd", "rpc-bind" 를 검색한 후 해당 서비스를 추가합니다.
    ![3tier-linux-architecture-web-nw-firewall-01](../../../../assets/images/3tier-linux-architecture-web-nw-firewall-01.png)

!!! info "ABLESTACK Cube에서의 방화벽 설정"
    ABLESTACK Cube에서의 방화벽 설정을 위해 [Cube 방화벽 서비스 활성화](../../../../administration/cube/networking-guide#_27) 문서를 참고하십시오.

### NFS 스토리지 Node 구성 (가상머신 3에서만 수행합니다)
NFS 스토리지가 설치되어 WEB Node 1, 2와 데이터를 공유할 NFS 스토리지 Node에서 아래 절차를 수행합니다.
#### NFS Server 패키지 설치
``` 
$ dnf install nfs-utils
```

#### 공유 폴더 생성
WEB 컨테이너와 파일을 공유할 NFS 스토리지의 공유폴더를 생성하고 적절한 권한을 부여합니다.
스토리지 공유폴더 경로 예시는 `/mnt/data/nfs` 입니다.
``` 
$ mkdir -p /mnt/data/nfs
$ chmod -R 777 /mnt/data/nfs
```

#### NFS 스토리지 설정
공유하려는 디렉토리와 서버 설정을 위해 `/etc/exports` 를 vi 편집기로 열어 정보를 입력합니다.
``` 
$ vi /etc/exports
```
모든 사용자 또는 특정 범위 IP 사용자 접근 여부를 설정합니다.
``` title="exports"  linenums="1"
# 모든 사용자 접근 허용 시
/mnt/data/nfs *(rw,sync,no_root_squash) 

# 특정 범위 IP 사용자 접근 허용 시
# /mnt/data/nfs 10.10.1.0/24(rw,sync,no_root_squash) 
```

#### NFS Server 서비스 시작
NFS Server Node의 NFS Server 서비스를 등록하고 시작합니다.
``` 
$ systemctl enable nfs-server.service
$ systemctl start nfs-server.service
```

#### NFS 스토리지 설정 적용
윗 단계에서 설정한 `/etc/exports` 파일을 적용합니다.
```
exportfs -arv
```

### WEB Node 1, 2 구성

#### NFS 스토리지 패키지 설치
``` 
$ dnf install nfs-utils nfs4-acl-tools
```

#### NFS Server의 마운트 정보를 확인합니다.
```
showmount -e 10.10.1.63
```

#### 공유할 폴더 생성
NFS 디렉터리를 마운트할 로컬 마운트 경로를 생성합니다.
``` 
$ mkdir -p /mnt/data/mount-nfs
$ chmod -R 777 /mnt/data/mount-nfs
```

추가적으로 재부팅 시 자동으로 마운트가 적용되도록 합니다.
이를 위해 `/etc/fstab` 를 vi 편집기로 열어 아래 예시를 참고하여 설정 정보를 추가합니다.
```
$ vi  /etc/fstab
```

``` title="fstab"  linenums="1"
10.10.1.63:/mnt/data/nfs /mnt/data/mount-nfs nfs defaults 0 0

# nfs: 프로토콜
# /mnt/data/mount-nfs: 마운트할 위치
```

#### Nginx 컨테이너 이미지 다운로드
WEB Node 1,2 에서 실행할 Nginx 컨테이너 이미지를 다운로드 받습니다.

```
$ podman pull docker.io/nginx:stable
```

#### Nginx 컨테이너 (WEB) 실행 
WEB Node 1,2 에서 다운로드한 Nginx 컨테이너 이미지를 실행합니다.

```
$ podman run -d -p 6060:6000 --name nginx-server --restart always -v /mnt/data/mount-nfs:/usr/share/nginx/html/ docker.io/nginx:stable

# run: 컨테이너를 실행합니다.
# -p: 포트포워딩 (외부:내부)
# --name: 컨테이너 이름
# --restart: 컨테이너 오류 시, 항상 재시작
# -v: 컨테이너의 특정 폴더와 로컬의 폴더를 서로 공유
# docker.io/nginx:stablet: 다운로드한 이미지 이름
```

#### Nginx 컨테이너 (WEB) VM 부팅 시 자동실행
서비스를 생성하는 방법으로 VM 부팅 시 해당 컨테이너가 자동으로 실행하도록 할 수 있습니다.
```
$ podman generate systemd nginx-server  > /etc/systemd/system/nginx-server.service
$ systemctl enable nginx-server.service
$ systemctl daemon-reload
```

#### Nginx 설정파일 수정 (proxy_pass 변경)
Nginx를 WAS의 Reverse Proxy로 설정해야합니다.
이를 위해 `/mnt/data/mount-nfs/nginx.conf` 를 vi 편집기로 생성하고 아래 내용을 추가하고 변경합니다.
```
$ vi  /mnt/data/mount-nfs/nginx.conf
```
하이라이트된 listen 포트와 proxy_pass 주소는 각 설정 맞게 유의하여 변경합니다.

??? note "클릭하여 Nginx의 설정정보를 확인합니다."

    ```  title="nginx.conf"  linenums="1" hl_lines="35 41"
    user  nginx;
    worker_processes  auto;

    error_log  /var/log/nginx/error.log notice;
    pid        /var/run/nginx.pid;


    events {
        worker_connections  1024;
    }


    http {
        include       /etc/nginx/mime.types;
        default_type  application/octet-stream;

        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                            '$status $body_bytes_sent "$http_referer" '
                            '"$http_user_agent" "$http_x_forwarded_for"';

        access_log  /var/log/nginx/access.log  main;

        sendfile        on;
        #tcp_nopush     on;

        keepalive_timeout  65;

        include /etc/nginx/conf.d/*.conf;

        charset           utf-8;

        server {
            charset utf-8;
            server_name localhost;
            listen 6000;
            location / {
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
                proxy_set_header X-NginX-Proxy true;
                proxy_pass http://10.10.1.170:5000;
                proxy_redirect off;
            }

            gzip on;
            gzip_comp_level 2;
            gzip_proxied any;
            gzip_min_length  1000;
            gzip_disable     "MSIE [1-6]\."
            gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
        }
    }
    ```   


#### 컨테이너 Nginx 설정파일과 교체
실행 중인 Nginx 컨테이너 설정파일을 전 단계에서 생성한 파일로 덮어쓰기합니다.
```
$ podman cp /mnt/data/mount-nfs/nginx.conf nginx-server:/etc/nginx/nginx.conf
```

### 클라이언트 접근
`http://{{publicIp}}:6060`에 접속하여 정상 작동 되는 지 확인합니다.






