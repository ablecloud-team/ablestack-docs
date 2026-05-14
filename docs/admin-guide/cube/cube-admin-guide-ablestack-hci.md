
# ABLESTACK - HCI

Cube 웹 콘솔의 ABLESTACK 메뉴에서는 HCI로 구성시 스토리지센터 가상머신, 클라우드센터 가상머신 배포와 클러스터를 구성하여 ABLESTACK 가상어플라이언스 관리 및 상태 모니터링을 제공합니다.

## 메뉴 인터페이스 구성

* ABLESTACK 요약 리본
* 스토리지센터 클러스터 상태
* 클라우드센터 클러스터 상태
* 스토리지센터 가상머신 상태
* 클라우드센터 가상머신 상태

![dashboard](../../assets/images/admin-guide/cube/ablestack/hci/dashboard.png)

## ABLESTACK 요약 리본
스토리지 가상머신, 클라우스센터 가상머신의 배포 및 클러스터 구성여부에 따라 현 상태를 메시지로 표현해 줍니다. 각 단계별 수행해야 되는 필수 구성 정보를 확인하여 설치 마법사 및 대시보드 링크를 제공하며 ABLESTACK 가상 어플라이언스 구성에 편의를 제공합니다.

![ribbon](../../assets/images/admin-guide/cube/ablestack/hci/ribbon.png)

**라이센스 관리**

라이센스를 관리하는 기능을 제공합니다.

* 라이센스를 등록
* 라이센스 등록 및 시작일, 만료일 확인

**클러스터 구성 준비**

클러스터 구성 준비를 위한 마법사를 제공합니다.

* 모든 호스트, 가상머신 IP 세팅을 위한 Hosts 파일 생성
* SSH Key 생성
* 시간서버 등록

**클라우드센터 VM 배포**

클라우드센터 가상머신(CCVM) 배포를 위한 마법사를 제공합니다.

* 자원 설정(컴퓨트, 디스크, 네트워크, NIC)
* Hosts 파일 세팅
* SSH Key 설정

**스토리지센터 대시보드 연결**

스토리지센터 대시보드(Glue)로 이동하는 URL 링크를 제공합니다.

**클라우드센터 연결**

클라우드센터VM의 가상화 관리 플랫폼(Mold)으로 이동하는 URL 링크를 제공합니다.

**모니링센터 구성**

모니터링센터 관리 대시보드 Wall 구성을 위한 마법사를 제공합니다.

**모터링센터 대시보드 연결**

모니터링센터 관리 대시보드(Wall)로 이동하는 URL 링크를 제공합니다.

## 스토리지센터 클러스터 상태 조회
스토리지센터 클러스터의 현재 상태와 스토리지 자원의 정보를 확인할 수 있습니다.

![storage-cluster](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster.png)

### 유지보수 모드 설정

스토리지센터 클러스터 유지보수모드 설정을 할 수 있도록 실행하는 버튼입니다.

!!! info
    * 현 상태가 유지보수모드일 경우 버튼이 비활성화됩니다.

![storage-cluster-maintenance-mode-enable](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-maintenance-mode-enable.png)

- **유지보수 모드 설정** 을 클릭합니다.
- **스토리지 클러스터 유지보수 모드 변경** 팝업을 호출합니다.

![storage-cluster-maintenance-mode-change](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-maintenance-mode-change.png)

- **변경** 버튼을 클릭하여 스토리지센터 클러스터 유지보수 모드로 설정합니다.

### 유지보수 모드 해제

스토리지센터 클러스터를 유지보수모드 해제 할 수 있도록 실행하는 버튼입니다.

!!! info
    * 현 상태가 유지보수모드 해제된 경우 버튼이 비활성화됩니다.

![storage-cluster-maintenance-mode-disable](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-maintenance-mode-disable.png)

- **유지보수 모드 해제** 를 클릭합니다.
- **스토리지 클러스터 유지보수 모드 변경** 팝업을 호출합니다.

![storage-cluster-maintenance-mode-change](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-maintenance-mode-change.png)

- **변경** 버튼을 클릭하여 스토리지센터 클러스터 유지보수 모드로 해제합니다.

### 스토리지센터 연결

스토리지 클러스터의 구성이 완료된 후 스토리지센터 대시보드(Glue)로 이동하는 버튼입니다.

!!! info
    * Bootstrap 실행 버튼이 활성화 중일 때 버튼이 숨겨집니다.
    * Bootstrap 실행 후 버튼이 활성화됩니다.

![storage-cluster-storage-center-link](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-storage-center-link.png)

- **스토리지센터 연결** 버튼을 클릭하여 새창으로 스토리지센터 포탈을 연결합니다.

### Bootstrap 실행

스토리지센터 가상머신(SCVM)이 모든 호스트에 설치되고 스토리지 클러스터 자동구성을 위해 실행하는 버튼입니다.

!!! info
    * 호스트 한 곳에서만 실행하면 됩니다.
    * Bootstrap 실행 버튼 클릭 후 정상적으로 종료될 때까지 약 5분이 소요됩니다.
    * Bootstrap 실행 버튼은 초기 활성화 되어있지만 SCVM에 cloudinit 세팅이 완전히 끝나지 않은 경우 실행되지 않습니다.

### 전체 호스트 Glue 설정 업데이트

전체 호스트에 Glue config 설정 파일을 업데이트 합니다.

!!! warning
    * 해당 기능을 통해 모든 호스트에 Glue 설정이 동기화 됩니다. 확인 후 실행해주세요.

![storage-cluster-glue-config-update](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-glue-config-update.png)

- **전체 호스트 Glue 설정 업데이트** 를 클릭합니다.
- **전체 호스트 Glue 설정 업데이트** 팝업을 호출합니다.

![storage-cluster-glue-config-update-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-glue-config-update-confirm.png)

- **실행** 버튼을 클릭하여 전체 호스트 Glue 설정을 업데이트합니다.

### 외부 스토리지 동기화

외부 스토리지와 동기화 할 경우 실행하는 버튼입니다.

!!! warning
    * 해당 장치는 반드시 이중화되어 있어야 합니다. 만약 싱글 패스로 구성되어 있다면 실행하지 마세요.

![storage-cluster-external-storage-sync](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-external-storage-sync.png)

- **외부 스토리지 동기화** 를 클릭합니다.
- **외부 스토리지 동기화** 팝업을 호출합니다.

![storage-cluster-external-storage-sync-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-external-storage-sync-confirm.png)

- **외부 스토리지 설정 확인** 을 활성화 체크하여 실행 버튼을 활성화 합니다. (싱글패스 구성 여부 확인 해야함)
- **실행** 버튼을 클릭하여 외부 스토리지 동기화합니다.

### CLVM 디스크 추가

CLVM 디스크를 추가할 경우 실행하는 버튼입니다.

!!! warning
    * iSCSI 또는 HBA 디스크를 선택해주세요.
    * 여러 디스크를 선택하면, 각 디스크에 대해 순차적으로 볼륨 그룹이 자동 생성됩니다.

![storage-cluster-clvm-disk-add](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-clvm-disk-add.png)

- **CLVM 디스크 추가** 를 클릭합니다.
- **CLVM 디스크 추가** 팝업을 호출합니다.

![storage-cluster-clvm-disk-add-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-clvm-disk-add-confirm.png)

- **CLVM 디스크 구성 대상 장치** 를 선택합니다.
- **추가** 버튼을 클릭하여 CLVM 디스크를 추가합니다.

### CLVM 디스크 삭제

CLVM 디스크를 삭제할 경우 실행하는 버튼입니다.

!!! warning
    * 목록에서 삭제할 장치를 확인후 선택하세요.

![storage-cluster-clvm-disk-delete](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-clvm-disk-delete.png)

- **CLVM 디스크 삭제** 를 클릭합니다.
- **CLVM 디스크 삭제** 팝업을 호출합니다.

![storage-cluster-clvm-disk-delete-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-clvm-disk-delete-confirm.png)

- **목록** 에서 삭제할 장치를 선택합니다.
- **확인** 버튼을 클릭하여 CLVM 디스크를 삭제합니다.

### CLVM 디스크 정보

CLVM 디스크 정보를 확인할 수 있습니다.

![storage-cluster-clvm-disk-list](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-clvm-disk-list.png)

- **CLVM 디스크 정보** 를 클릭합니다.
- **CLVM 디스크 정보** 팝업을 호출합니다.

![storage-cluster-clvm-disk-list-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-clvm-disk-list-confirm.png)

- **목록** 에 CLVM 디스크 목록을 확인할 수 있습니다.
- **확인** 버튼을 클릭하여 CLVM 디스크 정보 팝업을 닫습니다.

### WWN 목록 조회

WWN 목록 정보를 확인할 수 있습니다.

![storage-cluster-wwn-list](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-wwn-list.png)

- **WWN 목록 조회** 를 클릭합니다.
- **WWN 목록** 팝업을 호출합니다.

![storage-cluster-wwn-list-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-wwn-list-confirm.png)

- **확인** 버튼을 클릭하여 WWN 목록 팝업을 닫습니다.

### 전체 시스템 자동 종료

ABLESTACK 전체 시스템을 종료하기 위한 기능으로, CUBE에서 실행되는 절차를 통합하여 자동으로 실행하도록 하는 기능입니다.

!!! info
    * 모든 호스트에서 실행 가능합니다.
    * 클라우드센터 클러스터 상태가 "HEALTH_OK"일 경우 버튼이 활성화됩니다.

!!! warning
    * **Mold에서의 재기동 절차** 중, "호스트 유지보수 모드 설정"까지 관리자가 수동으로 모두 완료한 후 해당 기능을 실행해야 합니다.
    * 각 호스트에 Mount된 볼륨을 관리자가 직접 Umount한 후 해당 기능을 실행해야 합니다.

!!! note
    [Mold 재기동 절차]

    1.  클라우드센터 HA 비활성화
    2.  모든 가상머신 종료
        1.  HA 용도의 가상머신 종료
        2.  사용자 가상머신 종료
    3.  Zone 비활성화
    4.  시스템 VM 종료
    5.  기본스토리지 유지보수 모드 설정
        1.  기본 스토리지 (ha) 유지보수 모드 설정
    6.  호스트 유지보수 모드 설정
        1.  호스트가 유지보수 모드로 변경 되었을 때 다음 호스트 유지보수 모드 설정 진행

![storage-cluster-all-shutdown](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-all-shutdown.png)

- **전체 시스템 자동 종료** 를 클릭합니다.
- **전체 시스템 자동 종료** 팝업을 호출합니다.

![storage-cluster-all-shutdown-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-all-shutdown-confirm.png)

- **볼륨 마은트 해제 확인** 을 선택하여 실행 버튼을 활성화 합니다. (모든 호스트에 마운트 정보 확인후 해제 필요)
- **실행** 버튼을 클릭하여 전체 시스템을 종료합니다.

### Cube 호스트 제거

해당 Cube 호스트 설정정보를 모든 구성요소에서 제거합니다.

!!! warning
    * 다른 호스트의 hosts, cluster.json 파일에 해당 호스트의 정보를 제거합니다.

![storage-cluster-host-conf-remove](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-host-conf-remove.png)

- **Cube 호스트 제거** 를 클릭합니다.
- **Cube 호스트 제거** 팝업을 호출합니다.

![storage-cluster-host-conf-remove-confirm](../../assets/images/admin-guide/cube/ablestack/hci/storage-cluster-host-conf-remove-confirm.png)

- **실행** 버튼을 클릭하여 해당 Cube 호스트의 정보를 제거합니다.

## 클라우드센터 클러스터 상태 조회
Mold(클라우드 관리) 제품의 클러스터 현재 상태와 Cloud Center VM이 실행중인 호스트를 확인 할 수 있습니다.

![cloud-cluster](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster.png)

### 클라우드센터VM 시작

클라우드센터VM을 시작 상태로 변경하기 위한 버튼입니다.

!!! info
    * 클라우드센터VM이 시작 중인 경우 버튼이 비활성화됩니다.

![cloud-cluster-start](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-start.png)

- **클라우드센터VM 시작** 을 클릭합니다.
- **클라우드센터VM 시작** 팝업을 호출합니다.

![cloud-cluster-start-confirm](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-start-confirm.png)

- **실행** 버튼을 클릭하여 해당 클라우드센터VM을 시작합니다.

### 클라우드센터VM 정지

클라우드센터VM을 정지 상태로 변경하기 위한 버튼입니다.

!!! info
    * 클라우드센터VM이 정지 중인 경우 버튼이 비활성화 됩니다.

![cloud-cluster-stop](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-stop.png)

- **클라우드센터VM 정지** 를 클릭합니다.
- **클라우드센터VM 정지** 팝업을 호출합니다.

![cloud-cluster-stop-confirm](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-stop-confirm.png)

- **실행** 버튼을 클릭하여 해당 클라우드센터VM을 정지합니다.

### 클라우드센터 클러스터 클린업

클라우드센터 클러스터 리소스 모니터링 재시작 하기 위한 버튼입니다.

![cloud-cluster-cleanup](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-cleanup.png)

- **클라우드센터 클러스터 클린업** 을 클릭합니다.
- **클라우드센터 클러스터 클린업** 팝업을 호출합니다.

![cloud-cluster-cleanup-confirm](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-cleanup-confirm.png)

- **실행** 버튼을 클릭하여 해당 클라우드센터 클러스터 클린업합니다.

### 클라우드센터VM 마이그레이션

클라우드센터 가상머신(CCVM)을 특정 호스트로 마이그레이션 하기 위한 버튼입니다.

![cloud-cluster-migration](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-migration.png)

- **클라우드센터VM 마이그레이션** 을 클릭합니다.
- **클라우드센터VM 마이그레이션** 팝업을 호출합니다.

![cloud-cluster-migration-confirm](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-migration-confirm.png)

- 마이그레이션할 호스트를 선택합니다.
- **실행** 버튼을 클릭하여 클라우드센터VM을 마이그레이션합니다.

### 클라우드센터 연결

클라우드센터 가상머신(CCVM)의 가상화 관리 플랫폼(Mold)로 연결되는 링크를 제공하는 버튼입니다.

![cloud-cluster-link](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-link.png)

- **클라우드센터 연결** 버튼을 클릭하여 새창으로 클라우드센터 포탈을 연결합니다.

### Bootstrap 실행

클라우드센터 가상머신(CCVM)이 설치되고 클라우드센터 클러스터 자동구성을 위해 실행하는 버튼입니다.

!!! info
    * 호스트 한 곳에서만 실행하면 됩니다.
    * Bootstrap 실행 버튼 클릭 후 정상적으로 종료될 때까지 약 5분이 소요됩니다.
    * Bootstrap 실행 버튼은 초기 활성화 되어있지만 CCVM에 cloudinit 세팅이 완전히 끝나지 않은 경우 실행되지 않습니다.

### 모니터링센터 대시보드 연결

모니터링센터 관리 대시보드(Wall)로 이동하는 URL 링크를 제공합니다.

![cloud-cluster-wall-link](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-wall-link.png)

- **모니터링센터 대시보드 연결** 버튼을 클릭하여 새창으로 모니터링센터 포탈을 연결합니다.

### 모니터링센터 수집 정보 업데이트

모니터링센터 수집 정보를 업데이트하기 위한 기능입니다.

!!! info
    * 호스트가 추가 되거나 업데이트 필요시 cluster 구성정보 기준으로 모니터링센터 수집정보를 재구성 합니다.

![cloud-cluster-monitoring-update](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-monitoring-update.png)

- **모니터링센터 수집 정보 업데이트** 를 클릭합니다.
- **모니터링센터 수집 정보 업데이트** 팝업을 호출합니다.

![cloud-cluster-monitoring-update-confirm](../../assets/images/admin-guide/cube/ablestack/hci/cloud-cluster-monitoring-update-confirm.png)

- **실행** 버튼을 클릭하여 해당 모니터링센터 수집 정보 업데이트합니다.

## 스토리지센터 가상머신 상태 조회
스토리지센터 가상머신(Storage Center VM)의 현재 상태와 자원, 네트워크 정보를 확인 할 수 있습니다.

![scvm-status](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status.png)

### 스토리지센터VM 시작

스토리지센터 가상머신(SCVM)의 시작하기 위한 버튼입니다.

!!! info
    * 스토리지센터 가상머신(SCVM)가 정지 상태일 경우 활성화됩니다.

![scvm-status-start](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-start.png)

- **스토리지센터VM 시작** 을 클릭합니다.
- **스토리지센터 가상머신 상태변경** 팝업을 호출합니다.

![scvm-status-start-confirm](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-start-confirm.png)

- **시작** 버튼을 클릭하여 스토리지센터 가상머신을 시작합니다.

### 스토리지센터VM 정지

스토리지센터 가상머신(SCVM)의 정지하기 위한 버튼입니다.

!!! info
    * 스토리지 클러스터가 유지보수모드 상태이면서 SCVM이 시작 상태일 경우 버튼이 활성화됩니다.

![scvm-status-stop](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-stop.png)

- **스토리지센터VM 정지** 을 클릭합니다.
- **스토리지센터 가상머신 상태변경** 팝업을 호출합니다.

![scvm-status-stop-confirm](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-stop-confirm.png)

- **정지** 버튼을 클릭하여 스토리지센터 가상머신을 정지합니다.

### 스토리지센터VM 삭제

스토리지센터 가상머신(SCVM)의 삭제하기 위한 버튼입니다.

!!! info
    * 스토리지 클러스터가 구성전일 때와 SCVM이 정지 상태일 때 버튼이 활성화됩니다.
    * 스토리지 클러스터가 구성된 경우 삭제 하실 수 없습니다.

![scvm-status-delete](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-delete.png)

- **스토리지센터VM 삭제** 을 클릭합니다.
- **스토리지센터 가상머신 상태변경** 팝업을 호출합니다.

![scvm-status-delete-confirm](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-delete-confirm.png)

- **정지** 버튼을 클릭하여 스토리지센터 가상머신을 삭제합니다.

### 스토리지센터VM 자원변경

스토리지센터 가상머신(SCVM)의 자원변경(CPU, Memory)을 하기 위한 버튼입니다.

!!! info
    * SCVM이 정지 상태일 때 버튼이 활성화됩니다.
    * SCVM 시작시 반영됩니다.

![scvm-status-resource-change](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-resource-change.png)

- **스토리지센터VM 자원변경** 을 클릭합니다.
- **스토리지센터 가상머신 자원변경** 팝업을 호출합니다.

![scvm-status-resource-change-confirm](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-resource-change-confirm.png)

- **CPU** 및 **Memory** 를 변경합니다.
- **변경** 버튼을 클릭하여 스토리지센터 가상머신의 자원을 변경합니다.
- 가상머신 시작후 반영 됩니다.

### 스토리지센터 연결

스토리지센터 가상머신(SCVM)의 Cube 웹 콘솔을 접속하기 위한 링크 버튼입니다.

!!! info
    * SCVM이 Running 상태일 때 버튼이 활성화됩니다.

![scvm-status-vm-link](../../assets/images/admin-guide/cube/ablestack/hci/scvm-status-vm-link.png)

- **스토리지센터VM 연결** 버튼을 클릭하여 새창으로 스토리지센터 VM의 Cube 포탈을 연결합니다.

## 클라우드센터 가상머신 상태 조회

클라우드센터 가상머신(Cloud Center VM)의 현재 상태와 자원, 네트워크 정보를 확인 할 수 있습니다.

![ccvm-status](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status.png)

### 클라우드센터VM 자원변경

클라우드센터 가상머신(CCVM)의 자원변경(CPU, Memory)을 하기 위한 버튼입니다.

!!! info
    * CCVM이 Running 상태일 때 버튼이 활성화됩니다.
    * CCVM 재시작시 반영됩니다.

![ccvm-status-resource-change](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-resource-change.png)

- **클라우드센터VM 자원변경** 을 클릭합니다.
- **클라우드센터 VM 자원변경** 팝업을 호출합니다.

![ccvm-status-resource-change-confirm](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-resource-change-confirm.png)

- **CPU** 및 **Memory** 를 변경합니다.
- **변경** 버튼을 클릭하여 클라우드센터 가상머신의 자원을 변경합니다.
- 가상머신 시작후 반영 됩니다.

### Mold 서비스 제어

클라우드센터VM의 Mold 서비스를 제어하기 위한 버튼입니다.

!!! info
    * CCVM이 시작 상태일 때 버튼이 활성화됩니다.

![ccvm-status-mold-service-controll](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-mold-service-controll.png)

- **Mold 서비스 제어** 을 클릭합니다.
- **Mold 서비스 제어** 팝업을 호출합니다.

![ccvm-status-mold-service-controll-confirm](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-mold-service-controll-confirm.png)

- 제어할 **명령** 을 선택합니다.
- **실행** 버튼을 클릭하여 Mold 서비스를 제어합니다.

### Mold 서비스 제어

클라우드센터VM의 Mold DB를 제어하기 위한 버튼입니다.

!!! info
    * CCVM이 시작 상태일 때 버튼이 활성화됩니다.

![ccvm-status-mold-db-controll](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-mold-db-controll.png)

- **Mold DB 제어** 을 클릭합니다.
- **Mold DB 제어** 팝업을 호출합니다.

![ccvm-status-mold-db-controll-confirm](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-mold-db-controll-confirm.png)

- 제어할 **명령** 을 선택합니다.
- **실행** 버튼을 클릭하여 Mold DB를 제어합니다.

### Mold 세컨더리 용량 추가

클라우드센터VM의 세컨더리 용량을 추가합니다.

!!! info
    * CCVM이 시작 상태일 때 버튼이 활성화됩니다.

!!! waning
    용량 추가 작업시 클라우드센터 가상머신 스냅샷이 모두 삭제되고, 클라우드센터 가상머신을 재시작합니다

![ccvm-status-secondary-size-add](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-secondary-size-add.png)

- **Mold 세컨더리 용량 추가** 을 클릭합니다.
- **Mold 세컨더리 용량 추가** 팝업을 호출합니다.

![ccvm-status-secondary-size-add-confirm](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-secondary-size-add-confirm.png)

- 추가 용량을 입력합니다.
- 경고 안내 확인을 체크 합니다.
- **실행** 버튼을 클릭하여 세컨더리 용량을 추가합니다.

### 클라우드센터VM 스냅샷 백업

클라우드센터VM 이미지를 수동으로 스냅샷 백업하기 위한 버튼입니다.

![ccvm-status-snapshot-backup](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-snapshot-backup.png)

- **클라우드센터VM 스냅샷 백업** 을 클릭합니다.
- **클라우드센터VM 스냅샷 백업** 팝업을 호출합니다.

![ccvm-status-snapshot-backup-confirm](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-snapshot-backup-confirm.png)

- **실행** 버튼을 클릭하여 클라우드센터 가상머신 스냅샷을 생성합니다.

### 클라우드센터VM 스냅샷 백업

클라우드센터VM 이미지를 수동으로 스냅샷 생성하기 위한 버튼입니다.

![ccvm-status-snapshot-backup](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-snapshot-backup.png)

- **클라우드센터VM 스냅샷 백업** 을 클릭합니다.
- **클라우드센터VM 스냅샷 백업** 팝업을 호출합니다.

![ccvm-status-snapshot-backup-confirm](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-snapshot-backup-confirm.png)

- **실행** 버튼을 클릭하여 클라우드센터 가상머신 스냅샷을 생성합니다.

### 클라우드센터VM 스냅샷 복구

클라우드센터VM 이미지를 수동으로 복구하기 위한 버튼입니다.

!!! info
    * CCVM이 정지 상태일 때 버튼이 활성화됩니다.

클라우드센터VM 이미지를 수동으로 스냅샷 복구하기 위한 버튼입니다.

![ccvm-status-snapshot-recovery](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-snapshot-recovery.png)

- **클라우드센터VM 스냅샷 복구** 을 클릭합니다.
- **클라우드센터VM 스냅샷 복구** 팝업을 호출합니다.

![ccvm-status-snapshot-recovery-confirm](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-snapshot-recovery-confirm.png)

- 복구할 시점의 스냅샷을 선택합니다.
- **실행** 버튼을 클릭하여 클라우드센터 가상머신 스냅샷을 생성합니다.

### 클라우드센터VM DB 백업

클라우드센터VM Mold DB를 로컬로 다운로드 받는 기능입니다.

!!! info
    * CCVM이 시작 상태일 때 버튼이 활성화됩니다.

![ccvm-status-db-backup](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-db-backup.png)

- **클라우드센터VM DB 백업** 을 클릭합니다.
- **클라우드센터VM DB 백업** 팝업을 호출합니다.

![ccvm-status-db-backup-1](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-db-backup-1.png)

- **위치** 에 백업 받을 경로를 입력합니다.
- **백업 작업 선택** 에 즉시 백업을 선택합니다.
- **실행** 버튼을 클릭하여 클라우드센터 가상머신 스냅샷을 생성합니다.

![ccvm-status-db-backup-2](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-db-backup-2.png)

- **파일을 다운로드 하려면 클릭하십시오** 를 클릭하여 db sql 파일을 다운로드 받습니다.

![ccvm-status-db-backup-3](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-db-backup-3.png)

- **위치** 에 백업 받을 경로를 입력합니다.
- **백업 작업 선택** 에 정기 백업을 선택합니다.
- **정기 백업 활성화** 를 선택합니다.
- **반복** 주기를 선택합니다.
- **다음에서 실행** 에서 시간을 선택합니다.
- **실행** 버튼을 클릭하여 백업 주기를 설정합니다.

![ccvm-status-db-backup-4](../../assets/images/admin-guide/cube/ablestack/hci/ccvm-status-db-backup-4.png)

- **위치** 에 백업 받을 경로를 입력합니다.
- **백업 작업 선택** 에 백업파일 삭제관리를 선택합니다.
- **백업 삭제 활성화** 를 선택합니다.
- **반복** 주기를 선택합니다.
- **다음에서 실행** 에서 시간을 선택합니다.
- **다음보다 오래된 파일 삭제** 에서 삭제할 파일의 일자를 선택합니다.
- **실행** 버튼을 클릭하여 백업 파일 삭제 주기를 설정합니다.
