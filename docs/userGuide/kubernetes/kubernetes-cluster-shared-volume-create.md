# 공유 볼륨 설정

Kubernetes Node에서 사용할 공유 볼륨 설정을 설명합니다. 볼륨 공유는 NFS Protocol을 이용하여 공유하며, Ubuntu Desktop을
이용하여 공유 설정을 진행 합니다.

## Ubuntu Desktop SSH 설정

!!! Info
      Ubuntu OS 설치 가이드는 다른 [문서]()로 대체하며 해당 문서에서는 제공하지 않습니다.

1. Ubuntu Desktop Console 에서 아래 명령어를 이용하여 SSH Server 를 설치 합니다.
   ```shell
   sudo apt-get install openssh-server
   ```
2. ssh 방화벽 설정을 위해 아래 명령어를 입력 합니다.
   ```shell
   sudo ufw allow ssh
   ```
3. Mold에서 **네트워크 > 가상머신용 네트워크** 화면에서 Kubernetes용 네트워크를 선택 후 **Public IP 주소** 탭
   화면으로 이동하여 **IP 주소** 를 클릭하여 설정 화면으로 이동합니다.
   ![kubernetes-cluster-shared-volume-create-01](../../assets/images/kubernetes-cluster-shared-volume-create-01.png){:.center }
4. **포트 포워딩** 탭에서 **사설 포트**, **Public 포트** 각각 입력란에 **22**, **2221** 입력 후 **추가**
   버튼을 클릭 하여 Ubuntu Desktop 을 선택 후 **확인** 버튼을 클릭 합니다.
   ![kubernetes-cluster-shared-volume-create-02](../../assets/images/kubernetes-cluster-shared-volume-create-02.png){:.center }
   ![kubernetes-cluster-shared-volume-create-03](../../assets/images/kubernetes-cluster-shared-volume-create-03.png){:.center }
5. 아래 명령어를 이용하여 SSH 접속을 합니다.
   ```shell
      ssh -p 2221 kubernetes@10.10.1.61
   ```
!!! info
     해당 아이피 및 포트는 예시 입니다.

## Ubuntu Desktop NFS 서비스 설치 및 설정

1. NFS Server 및 portmap 서비스를 설치.

   ```shell
      sudo apt-get -y install nfs-kernel-server portmap
   ```
2. 공유 폴더 생성

   ```shell
      mkdir kubernetes
   ```
3. 공유 폴더 권한 설정

   ```shell
      sudo vi /etc/exports
   ```

   exports 파일 오픈 후 아래 설정을 입력합니다.
   ```shell
      /kubernetes *(rw,no_root_squash)
   ```

## Kubernetes Node에 NFS 마운트

!!! Info
     본문에서는 Kubernetes Node에 NFS 볼륨 마운트 진행을 한번만 진행 하지만 각 Node 수만큼 반복하여 진행 해야 합니다.

!!! Info
     Node 접속 정보는 Mold의 **컴퓨트 > 쿠버네테스** 화면에서 **가상머신** 탭에서 확인이 가능합니다.

1. Node SSH 접속

   ![kubernetes-cluster-shared-volume-create-04](../../assets/images/kubernetes-cluster-shared-volume-create-04.png){:.center }

   ```shell
   ssh -i [SSH Key 파일명] cloud@[public IP] -p [SSH 포트]
   ```
   SSH key 파일명 : SSH key 생성된 파일명
   public IP : 네트워크에서 생성된 public IP
   SSH 포트 : 각 Node별로 포트포워딩된 포트. 위 이미지 기준으로 **SSH 포트**

   ```
   ssh -i ablecloud.key cloud@10.10.1.61 -p 2222
   ```
2. fstab 정보 등록

   ```shell
   sudo vi /etc/fstab
   ```
   파일 오픈 후 아래 내용 추가

   ```
   10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
   ```
3. NFS mount

   ```shell
   sudo mount -a
   ```