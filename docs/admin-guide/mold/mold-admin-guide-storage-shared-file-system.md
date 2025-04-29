
# 공유 파일 시스템

## 개요

NFS를 통해 마운트할 수 있는 관리 공유 파일 시스템을 설정할 수 있습니다.
사용자는 서비스 제공, 디스크 제공, 파일 시스템 형식 및 네트워크를 선택할 수 있습니다.


공유 파일 시스템은 지정된 서비스 제공이 있는 인스턴스에 배포됩니다.
제공된 디스크 제공을 사용하여 데이터 볼륨이 생성되고 인스턴스에 연결됩니다.
사용자는 사용할 파일 시스템(XFS, EXT4)을 지정할 수 있습니다.

파일 시스템은 데이터 볼륨에 생성되고 NFS를 통해 내보내집니다.
게스트 네트워크의 모든 인스턴스는 공유 파일 시스템을 마운트하고 읽고 쓸 수 있습니다.

## 공유 파일 시스템 목록 조회
1. 공유 파일 시스템 목록을 확인하는 화면입니다. 생성된 공유 파일 시스템 목록을 확인하거나 공유 파일 시스템 생성 버튼을 클릭하여 공유 파일 시스템을 생성하실 수 있습니다.
    ![공유 파일 시스템 목록 조회](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-dashboard.png){ .imgCenter .imgBorder }

    !!! info
        매트릭 버튼을 활성화할 때 해당 디스크에 대한 상세 정보를 공유 파일 시스템 목록에서 확인할 수 있습니다.


        프로젝트 버튼을 활성화할 때 해당 프로젝트에 대한 정보를 공유 파일 시스템 목록에서 확인할 수 있습니다.

## 공유 파일 시스템 생성
1. 스토리지의 공유 파일 시스템에 상단의 공유 파일 시스템 생성 버튼을 클릭합니다.
    ![공유 파일 시스템 생성 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-create-01.png){ .imgCenter .imgBorder }
2. 공유 파일 시스템 생성 버튼을 클릭한 화면입니다.
    ![공유 파일 시스템 생성](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-create-02.png){ .imgCenter .imgBorder }
    - **소유자 유형:** 소유자 유형을 선택합니다.
    - **도메인:** 도메인을 선택합니다.
    - **계정:** 계정을 선택합니다.
    - **이름:** 이름을 입력합니다.
    - **설명:** 설명을 입력합니다.
    - **Zone:** Zone을 선택합니다.
    - **파일 시스템:** 파일 시스템을 선택합니다.
    - **네트워크:** 네트워크를 선택합니다.
    - **디스크 오퍼링:** 디스크 오퍼링을 선택합니다.
    - **크기:** 크기를 입력합니다.
    - **가상머신용 컴퓨트 오퍼링:** 가상머신용 컴퓨트 오퍼링을 선택합니다.

    !!! info
        네트워크, 디스크 오퍼링, 가상머신용 컴퓨트 오퍼링 경우, 미리 사전에 생성되어 있어야 합니다.

        <span style="font-size:20px">👉 &nbsp;&nbsp;🔗[네트워크 생성 가이드](../mold-admin-guide-network-guest-networks/#_4)</span>

        <span style="font-size:20px">👉 &nbsp;&nbsp;🔗[디스크 오퍼링 생성 가이드](../mold-admin-guide-offerings-disk-offerings/#_4)</span>

        <span style="font-size:20px">👉 &nbsp;&nbsp;🔗[가상머신용 컴퓨트 오퍼링 생성 가이드](../mold-admin-guide-offerings-compute-offerings/#_4)</span>

## 공유 파일 시스템 업데이트
1. 공유 파일 시스템 상세 오른쪽 상단의 공유 파일 시스템 업데이트 버튼을 클릭합니다.
    ![공유 파일 시스템 업데이트 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-update-01.png){ .imgCenter .imgBorder }
2. 공유 파일 시스템 업데이트 버튼을 클릭한 화면입니다.
    ![공유 파일 시스템 업데이트](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-update-02.png){ .imgCenter .imgBorder }
    - **이름:** 이름을 입력합니다.
    - **설명:** 설명을 입력합니다.

## 공유 파일 시스템 파기
1. 공유 파일 시스템 상세 오른쪽 상단의 공유 파일 시스템 파기 버튼을 클릭합니다.
    ![공유 파일 시스템 파기](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-destroy-01.png){ .imgCenter .imgBorder }
2. 공유 파일 시스템 파기 버튼을 클릭한 화면입니다.
    ![공유 파일 시스템 파기](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-destroy-02.png){ .imgCenter .imgBorder }

    !!! danger
        공유 파일 시스템에서 작업한 모든 데이터가 삭제됩니다. 삭제 전에 반드시 다시 확인해 주세요!

### VM에 네트워크 추가
2. VM에 네트워크 추가 버튼을 클릭한 화면입니다.
    ![VM에 네트워크 추가](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-network-info-vm-network-add.png){ .imgCenter .imgBorder }
    - **네트워크:** 네트워크를 선택합니다.
    - **IP 주소:** IP 주소를 입력합니다.

    !!! info
        해당 네트워크를 기본값으로 설정하면 최우선으로 사용됩니다.

### IP 주소 변경
3. 해당 네트워크의 **+** 버튼을 클릭하여 IP 주소 변경 버튼을 클릭합니다.
    ![IP 주소 변경 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-network-info-ip-change-01.png){ .imgCenter .imgBorder }
4. IP 주소 변경 버튼을 클릭한 화면입니다.
    ![IP 주소 변경](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-network-info-ip-change-02.png){ .imgCenter .imgBorder }

### 보조 IP 편집
5. 해당 네트워크의 **+** 버튼을 클릭하여 보조 IP 편집 버튼을 클릭합니다.
    ![보조 IP 편집 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-network-info-ip-seconde-update-01.png){ .imgCenter .imgBorder }
6. 보조 IP 편집 버튼을 클릭한 화면입니다.
    ![보조 IP 편집](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-network-info-ip-seconde-update-02.png){ .imgCenter .imgBorder }

## 공유 파일 시스템 시작
!!! check
    공유 파일 시스템이 **정지된 상태** 일 경우, 활성화됩니다.

1. 공유 파일 시스템 상세 오른쪽 상단의 공유 파일 시스템 시작 버튼을 클릭합니다.
    ![공유 파일 시스템 시작 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-start-01.png){ .imgCenter .imgBorder }
2. 공유 파일 시스템 시작 버튼을 클릭한 화면입니다.
    ![공유 파일 시스템 시작](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-start-02.png){ .imgCenter .imgBorder }

## 공유 파일 시스템 중지
!!! check
    공유 파일 시스템이 **실행중** 일 경우, 활성화됩니다.

1. 공유 파일 시스템 상세 오른쪽 상단의 공유 파일 시스템 중지 버튼을 클릭합니다.
    ![공유 파일 시스템 중지 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-stop-01.png){ .imgCenter .imgBorder }
2. 공유 파일 시스템 중지 버튼을 클릭한 화면입니다.
    ![공유 파일 시스템 중지](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-stop-02.png){ .imgCenter .imgBorder }

## 공유 파일 시스템 재시작
1. 공유 파일 시스템 상세 오른쪽 상단의 공유 파일 시스템 재시작 버튼을 클릭합니다.
    ![공유 파일 시스템 재시작 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-restart-01.png){ .imgCenter .imgBorder }
2. 공유 파일 시스템 재시작 버튼을 클릭한 화면입니다.
    ![공유 파일 시스템 재시작](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-restart-02.png){ .imgCenter .imgBorder }

## 디스크 오퍼링 변경
1. 공유 파일 시스템 상세 오른쪽 상단의 디스크 오퍼링 변경 버튼을 클릭합니다.
    ![디스크 오퍼링 변경 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-disk-offering-change-01.png){ .imgCenter .imgBorder }
2. 디스크 오퍼링 변경 버튼을 클릭한 화면입니다.
    ![디스크 오퍼링 변경](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-disk-offering-change-02.png){ .imgCenter .imgBorder }
    - **디스크 오퍼링:** 디스크 오퍼링을 선택합니다.
    - **크기:** 를 입력합니다.

    !!! info
        고정 디스크 오퍼링을 선택할 시, 해당 크기는 오퍼링에서 고정으로 할당된 값으로 만들어 집니다.

        <span style="font-size:20px">👉 &nbsp;&nbsp;🔗[디스크 오퍼링 생성 가이드](../mold-admin-guide-offerings-disk-offerings/#_4)</span>

## 서비스 오퍼링 변경
!!! check
    공유 파일 시스템이 **정지된 상태** 일 경우, 활성화됩니다.

1. 공유 파일 시스템 상세 오른쪽 상단의 서비스 오퍼링 변경 버튼을 클릭합니다.
    ![서비스 오퍼링 변경 버튼](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-service-offering-change-01.png){ .imgCenter .imgBorder }
2. 서비스 오퍼링 변경 버튼을 클릭한 화면입니다.
    ![서비스 오퍼링 변경](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-service-offering-change-02.png){ .imgCenter .imgBorder }
    - **컴퓨트 오퍼링:** 디스크 오퍼링을 선택합니다.

!!! info
    서비스 오퍼링을 변경할 경우, 미리 사전에 생성되어 있어야 합니다.

    <span style="font-size:20px">👉 &nbsp;&nbsp;🔗[컴퓨트 오퍼링 생성 가이드](../mold-admin-guide-offerings-compute-offerings/#_4)</span>

## 공유 파일 시스템 상세 탭
1. 공유 파일 시스템에 대한 상세 정보를 확인하는 화면입니다. 해당 공유 파일 시스템에 대한 크기, UUID, 이름 등 상세 정보를 확인할 수 있습니다.
    ![공유 파일 시스템 상세 탭](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-detail-info.png){ .imgCenter .imgBorder }

## 공유 파일 시스템 액세스 탭
1. 공유 파일 시스템에 대한 액세스 정보를 확인하는 화면입니다. 해당 공유 파일 시스템에 대한 마운트 정보를 확인할 수 있습니다.
    ![공유 파일 시스템 액세스 탭](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-access-info.png){ .imgCenter .imgBorder }


## 공유 파일 시스템 네트워크 탭
1. 공유 파일 시스템에 대한 네트워크 정보를 확인하는 화면입니다. 해당 공유 파일 시스템에 대한 네트워크 정보를 확인할 수 있습니다.
    ![공유 파일 시스템 네트워크 탭](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-network-info.png){ .imgCenter .imgBorder }

## 공유 파일 시스템 매트릭 탭
1. 공유 파일 시스템에 대한 매트릭 정보를 확인하는 화면입니다. 해당 공유 파일 시스템에 대한 CPU, Memory, Network 등 할당량 및 사용량을 확인할 수 있습니다.
    ![공유 파일 시스템 매트릭 탭1](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-metric-info-01.png){ .imgCenter .imgBorder }
    ![공유 파일 시스템 매트릭 탭2](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-metric-info-02.png){ .imgCenter .imgBorder }

    !!! info
        사용자가 원하는 시간과 단위 등을 커스터마이징 할 수 있습니다.

## 공유 파일 시스템 이벤트 탭
1. 공유 파일 시스템에 대한 이벤트 정보를 확인하는 화면입니다. 해당 공유 파일 시스템에 대한 유형 및 생성일 등 확인할 수 있습니다.
    ![공유 파일 시스템 이벤트 탭](../../assets/images/admin-guide/mold/storage/shared-file-system/shared-file-system-event-info.png){ .imgCenter .imgBorder }

## 용어사전
