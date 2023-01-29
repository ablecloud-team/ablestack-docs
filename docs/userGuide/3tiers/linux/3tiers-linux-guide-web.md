ABLESTACK Mold를 이용한 **이중화를 통한 고가용성 기능을 제공하는 리눅스 기반의 3계층 구조** 의 [구성 단계](../3tiers-linux-guide-prepare#_5) 중, 마지막 단계인 WEB 구성에 대한 문서입니다.

가상머신에 도커 컨테이너를 이용하여 Nginx를 활용한 WEB서버 2개를 구성하고 1 개의 가상머신에 NFS 스토리지를 생성하여 WEB에서 구동시킬 웹소스를 저장, 공유합니다. 이를 하나의 클러스터로 구성하는 방법은 다음과 같은 절차로 진행됩니다.

- Affinity 그룹 생성
- 가상머신 생성
- 데이터 디스크 설정
- 보안 설정
- NFS 스토리지 가상머신 구성
- WEB 가상머신 구성
- 로드 밸런서(부하 분산) 설정


## Affinity 그룹 생성
가상머신을 생성하기 전, Anti Affinity 그룹을 생성하여 어느하나의 서브넷에 속한 VM들이 특정 호스트 한 곳에 몰려 실행하도록 하거나 반대로 몰려 실행되지 않도록 합니다. 이중화를 위해 Affinity 그룹을 anti-affinity 유형으로 WEB, WAS, DB 각각 추가해야합니다. 이를 위해 **컴퓨트 > Affinity 그룹** 화면으로 이동하여 **새 Affinity 그룹 추가** 버튼을 클릭합니다. 클릭하게되면 다음과 같은 입력항목을 확인할 수 있습니다.

<figure markdown>
![3tier-linux-architecture-add-affinity-group](../../../../assets/images/3tier-linux-architecture-add-affinity-group.png)
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


## 가상머신 생성
ABLESTACK Mold는 기본적으로 템플릿을 이용해 가상머신을 생성하고 사용하는 것을 권장합니다. 따라서 관리용 가상머신을 생성하기 전에 먼저 "[가상머신 사용 준비](../../vms/centos-guide-prepare-vm.md)" 단계를 통해 CentOS 기반의 가상머신 템플릿 이미지를 생성하여 등록하는 절차를 수행한 후 VM을 생성해야 합니다.

가상머신을 추가하기 위해 **컴퓨트 > 가상머신** 화면으로 이동하여 **가상머신 추가** 버튼을 클릭합니다. **새 가상머신** 마법사 페이지가 표시됩니다. 
해당 페이지에서는 **템플릿을 이용한 VM 생성** 문서를 참고하여 가상머신을 생성합니다.

!!! info "템플릿을 이용한 VM 생성"
    템플릿을 이용한 가상머신 추가를 위해 [템플릿을 이용한 VM 생성](../../../vms/centos-guide-add-and-use-vm#vm) 문서를 참고하십시오.

입력 항목 예시는 다음과 같습니다.

- WEB 가상머신 1

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Rocky Linux 9.0 기본 이미지 템플릿** * Rocky Linux release 9.0 (Blue Onyx)
    - 컴퓨트 오퍼링 : **1C-2GB-RBD-HA**
    - 데이터 디스크 : * 디폴트로 생성합니다.
    - 네트워크 : **web** * VPC명이 일치되는지 확인합니다.
        - IP: **192.168.1.11**
    - SSH 키 쌍 : **3tier_linux_keypair** 
    - 확장 모드 : 
        - Affinity 그룹 :  **ablecloud-3tier-linux-web**
    - 이름 : **ablecloud-3tier-linux-web-01**

- WEB 가상머신 2

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Rocky Linux 9.0 기본 이미지 템플릿** * Rocky Linux release 9.0 (Blue Onyx)
    - 컴퓨트 오퍼링 : **1C-2GB-RBD-HA**
    - 데이터 디스크 : * 디폴트로 생성합니다.
    - 네트워크 : **web** * VPC명이 일치되는지 확인합니다.
        - IP: **192.168.1.12**
    - SSH 키 쌍 : **3tier_linux_keypair** 
    - 확장 모드 : 
        - Affinity 그룹 :  **ablecloud-3tier-linux-web**
    - 이름 : **ablecloud-3tier-linux-web-02**

- NFS 스토리지 가상머신

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Rocky Linux 9.0 기본 이미지 템플릿** * Rocky Linux release 9.0 (Blue Onyx)
    - 컴퓨트 오퍼링 : **1C-2GB-RBD-HA**
    - 데이터 디스크 : **100GB-WB-RBD** 
    - 네트워크 : **web** * VPC명이 일치되는지 확인합니다.
        - IP: **192.168.1.13**
    - SSH 키 쌍 : **3tier_linux_keypair** 
    - 확장 모드 : * 디폴트로 생성합니다.
    - 이름 : **ablecloud-3tier-linux-web-storage**

    !!! warning "스토리지 가상머신의 Affinity 그룹 적용"
        **스토리지 가상머신의 Anti-Affinity 그룹 적용은 권장되지 않습니다.** 어떠한 이유로 스토리지 가상머신을 실행 중이던 호스트가 중단될 경우, 스토리지 가상머신은 다른 호스트로 이관을 하게 되는데 이 때 Anti-Affinity가 적용되어 스토리지 가상머신이 재기동되지 않을 수 있습니다.


## 데이터 디스크 설정
안정적인 운영을 위해 기본 RootDisk가 아닌 고용량의 스펙을 가진 디스크로의 데이터 저장이 필요합니다. 이를위한 사전작업으로 가상머신 생성 시 추가했던 데이터 디스크에 대한 사용을 위해 ["데이터 디스크 설정"](../3tiers-linux-guide-db#_2) 문서를 참고하여 수행합니다.

???+ note
    NFS 스토리지 가상머신에만 데이터 디스크 설정을 수행합니다.


## 보안 설정
생성한 가상머신에 대해 보안 설정을 하여 허용되지 않은 접근을 차단하고 필요한 서비스만 운영할 수 있도록 설정합니다.

???+ note
    WEB 가상머신 1, 2 및 스토리지 가상머신에 대해 실행 및 설정을 적용합니다.

### 네트워크 방화벽 해제 
방화벽은 들어오고 나가는 네트워크 트래픽을 모니터링하고 필터링하는 방법입니다. 특정 트래픽을 허용할지 차단할지 결정하는 일련의 보안 규칙을 정의하여 작동합니다.
CentOS 운영체제에서는 firewald라는 이름의 방화벽 데몬과 함께 제공됩니다.

`firewall-cmd` 명령어를 이용하여 samba 서비스에 대한 방화벽을 해제하고 `--permanent` 옵션을 사용하여 영구적으로 적용합니다. 
``` linenums="1" 
$ firewall-cmd --zone=public --add-service={nfs,mountd,rpc-bind}
$ firewall-cmd --reload
```

???+ info
    nfs, mountd, rpc-bind 서비스는 각각 TCP 포트 2049, 20048 그리고 111을 사용합니다.


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






