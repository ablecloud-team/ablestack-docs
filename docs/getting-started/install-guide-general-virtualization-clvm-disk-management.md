
# 일반 가상화 CLVM 디스크 관리

!!! danger
    이 문서는 기술지원 용도의 문서입니다. 기술지원 엔지니어가 아닌 사용자가 조작할 때 시스템에 문제가 발생할 수 있습니다.

일반 가상화 CLVM 디스크 관리 가이드입니다.이 문서에서는 구축된 일반 가상화 환경에서 추가적인 CLVM 디스크 생성, 삭제, 조회로 관리를 위한 절차를 가이드 하고 있습니다.
ABLESTACK Cube의 웹콘솔 및 Mold의 웹콘솔을 이용하여 진행이 되며, 웹 접속 IP는 별도의 표시를 하지 않고 진행됩니다. 기존에 구성된 IP 정보에 맞게 웹콘솔을 접속 하시면 됩니다.

## ABLESTACK Cube 메인 화면
![ABLESTACK Cube 메인 화면](../assets/images/install-guide-general-virtualization-gfs-disk-management-main.png){ align=center }
- 왼쪽 ABLESTACK 메뉴 클릭시 보이는 화면입니다.

## 일반 가상화 CLVM 디스크 관리

### CLVM 디스크 추가
!!! info
    CLVM 디스크를 추가하려면, 사용되는 디스크를 연결이 선행 되어야 합니다.

    wwn으로 해당 디스크를 찾아 선택하시면 됩니다.

1. ABLESTACK Cube 화면
    ![ABLESTACK Cube 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-01.png){ align=center }
    - CLVM 디스크 상태란의 CLVM 디스크 추가를 클릭합니다.
2. CLVM 디스크 추가 화면
    ![CLVM 디스크 추가 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-02.png){ align=center }
    - 사용할 디스크들을 선택합니다.
    !!! warning
        여러 디스크를 선택하면, 각 디스크에 대해 순차적으로 볼륨 그룹이 자동 생성됩니다.

        만약 용량을 크게 하고 싶다면, 외부 스토리지에서 미리 크게 만든 후 연결 해야합니다.

    !!! tip
        디스크 이름, 디스크 상태, 디스크 종류, 용량, 디스크 정보, 디스크 wwn 으로 구분 되어 있습니다.

3. CLVM 디스크 추가 진행 화면
    ![CLVM 디스크 추가 진행 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-03.png){ align=center }
    - 선택한 디스크들을 CLVM 디스크로 추가하는 과정입니다.
4. Mold 기본 스토리지 화면
    ![Mold 기본 스토리지 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-04.png){ align=center }
    - ccvm_mngt_ip:8080 으로 접속하여 로그인 후, **인프라스트럭쳐** 에 **기본 스토리지** 를 클릭합니다.
    - 기본 스토리지 추가 버튼을 클릭합니다.

5. Mold 기본 스토리지 추가 진행 화면
    ![Mold 기본 스토리지 추가 진행 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-05.png){ align=center }
    - **범위** 항목에는 **클러스터** 를 선택합니다.
    - **Zone** 항목에는 **Zone** 을 선택합니다.
    - **Pod** 항목에는 **Pod** 를 선택합니다.
    - **클러스터** 항목에는 **Cluster** 를 선택합니다.
    - **이름** 항목에는 Cube에서  CLVM 디스크 정보에서 보이는 **vg_clvm1** 을 입력합니다.
    - **제공자** 항목에는 **DefaultPrimary** 를 선택합니다.
    - **프로토콜** 항목에는 **CLVM** 를 선택합니다.
    - **볼륨그룹** 항목에는 Cube에서 선행 작업된 마운트 경로인 **vg_clvm1** 를 입력합니다.
    - **스토리지 태그** 항목에는 이름 항목과 동일하게 **vg_clvm1** 를 입력하여 선택합니다.

6. Mold 기본 스토리지 추가 완료 화면
    ![Mold 기본 스토리지 추가 완료 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-06.png){ align=center }
    - 추가 완료가 되면, 해당 하는 마운트 경로의 컬럼이 생겨나며, 상태가 **UP** 으로 나타납니다.

7. Mold 디스크 오퍼링 화면
    ![Mold 디스크 오퍼링 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-07.png){ align=center }
    - **서비스 오퍼링** 에서 **디스크 오퍼링** 을 클릭한 화면입니다.

8. Mold 디스크 오퍼링 추가 진행 화면
    ![Mold 디스크 오퍼링 추가 진행 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-08.png){ align=center }
    - **디스크 오퍼링 추가** 버튼을 클릭합니다.
    - **이름** 을 입력합니다.
    - **스토리지 유형** 은 **shared** 로 클릭합니다.
    - **프로비저닝 유형** 은 **Thin 프로비저닝** 을 클릭합니다.
    - **사용자지정 디스크 크기** 버튼을 활성화 합니다.
    - **Qos 유형** 에서 **없음** 을 클릭합니다.
    - **Write-cache 유형** 은 **디스크 캐시 없음** 을 클릭합니다.
    - **스토리지 태그** 는 **vg_clvm1** 으로 기본 스토리지에서 추가된 스토리지 태그를 선택합니다.

9. Mold 디스크 오퍼링 추가 완료 화면
    ![Mold 디스크 오퍼링 추가 완료 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-09.png){ align=center }
    - 사용 할 수 있는 디스크 오퍼링이 추가 완료된 화면입니다.

10. Mold 스토리지 화면
    ![Mold 스토리지 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-10.png){ align=center }
    - **스토리지** 에서 **볼륨** 을 클릭한 화면입니다.

11. Mold 볼륨 생성 화면
    ![Mold 볼륨 생성 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-11.png){ align=center }
    - **이름** 을 입력합니다.
    - **디스크 오퍼링** 을 선택합니다.
    - **크기** 를 입력합니다.
    !!! tip
        이름은 혼동을 피하기 위해 Cube에서 생성한 명칭과 동일하게 유지하는 것이 가장 명확하고 일관성 있는 방식입니다.
    ![Mold 볼륨 생성 화면1](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-12.png){ align=center }
    - **디스크 연결** 을 클릭합니다.
    ![Mold 볼륨 생성 화면2](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-13.png){ align=center }
    - 해당 하는 **VM ID** 를 선택합니다.
    - **확인** 을 클릭합니다.

12. Mold 볼륨 연결 화면
    ![Mold 볼륨 연결 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-14.png){ align=center }
    - **상태, VM이름, 스토리지** 의 정보를 확인합니다.
    ![Mold 볼륨 연결 화면1](../assets/images/install-guide-general-virtualization-clvm-disk-management-add-15.png){ align=center }
    - 콘솔화면에서도 확인하실 수 있습니다.

### CLVM 디스크 삭제
!!! danger
    디스크를 삭제하면 저장된 모든 데이터가 영구적으로 삭제되며 복구할 수 없습니다.

    데이터가 필요한 경우, 삭제 전에 반드시 백업을 완료하세요.

1. Mold 스토리지 화면
    ![Mold 스토리지 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-04.png){ align=center }
    - **스토리지** 에서 **볼륨** 을 클릭한 화면입니다.

2. Mold 볼륨 연결 해제 화면
    ![Mold 볼륨 연결 해제 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-05.png){ align=center }
    - 해당 하는 볼륨의 옵션을 클릭한 후, **디스크 분리** 버튼을 클릭합니다.
    ![Mold 볼륨 연결 해제 화면1](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-06.png){ align=center }
    - **확인** 버튼을 클릭합니다.

3. Mold 볼륨 삭제
    ![Mold 볼륨 삭제 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-07.png){ align=center }
    - 해당 하는 볼륨의 옵션을 클릭한 후, **볼륨 파기** 버튼을 클릭합니다.
    ![Mold 볼륨 삭제 화면1](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-08.png){ align=center }
    - **제거** 버튼을 활성화합니다.
    - **확인** 버튼을 클릭합니다.
    ![Mold 볼륨 삭제 화면3](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-09.png){ align=center }
    - 해당 볼륨이 삭제된 화면입니다.

4. Mold 디스크 오퍼링 화면
    ![Mold 디스크 오퍼링 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-10.png){ align=center }
    - **서비스 오퍼링** 에서 **디스크 오퍼링** 을 클릭한 화면입니다.
5. Mold 디스크 오퍼링 삭제 진행 화면
    ![Mold 디스크 오퍼링 삭제 진행 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-11.png){ align=center }
    - 해당 **디스크 오퍼링** 의 옵션을 선택하여 **디스크 오퍼링 비활성화** 를 클릭합니다.
    ![Mold 디스크 오퍼링 삭제 진행 화면1](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-12.png){ align=center }
    - **확인** 을 클릭합니다.
6. Mold 디스크 오퍼링 삭제 완료 화면
    ![Mold 디스크 오퍼링 삭제 완료 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-13.png){ align=center }
    - 해당 **디스크 오퍼링** 이 삭제된 화면입니다.

7. Mold 기본 스토리지 화면
    ![Mold 기본 스토리지 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-14.png){ align=center }
    - **인프라스트럭쳐** 에 **기본 스토리지** 를 클릭한 화면입니다.
8. Mold 기본 스토리지 삭제 진행 화면
    ![Mold 기본 스토리지 삭제 진행 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-15.png){ align=center }
    - 해당 하는 **기본 스토리지** 의 옵션을 선택하여 **유지보수 모드 활성화** 를 클릭합니다.
    ![Mold 기본 스토리지 삭제 진행 화면1](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-16.png){ align=center }
    - 상태에서 **유지보수 모드** 가 활성화된 화면입니다.
    ![Mold 기본 스토리지 삭제 진행 화면2](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-17.png){ align=center }
    - 해당 하는 **기본 스토리지** 의 옵션을 선택하여 **기본 스토리지 삭제** 를 클릭합니다.
    ![Mold 기본 스토리지 삭제 진행 화면3](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-18.png){ align=center }
    - **확인** 버튼을 클릭합니다.
9. Mold 기본 스토리지 삭제 완료 화면
    ![Mold 기본 스토리지 삭제 완료 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-19.png){ align=center }
    - 해당 하는 **기본 스토리지** 가 삭제된 화면입니다.

10. ABLESTACK Cube 화면
    ![ABLESTACK Cube 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-01.png){ align=center }
    - CLVM 디스크 상태란의 CLVM 디스크 삭제 클릭합니다.
11. CLVM 디스크 삭제 화면
    ![CLVM 디스크 삭제 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-02.png){ align=center }
    - 사용할 디스크를 선택합니다.
    !!! warning
        선택한 디스크의 모든 데이터가 영구적으로 삭제됩니다. 삭제된 데이터는 복구가 불가능하니, 반드시 신중하게 확인 후 진행하시기 바랍니다.
12. CLVM 디스크 삭제 완료 화면
    ![CLVM 디스크 삭제 완료 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-delete-03.png){ align=center }
    - 선택한 CLVM 디스크가 삭제된 화면입니다.

### CLVM 디스크 조회
1. ABLESTACK Cube 화면
    ![ABLESTACK Cube 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-read-01.png){ align=center }
    - ABLESTACK Cube 화면 입니다.
2. CLVM 디스크 조회 화면
    ![CLVM 디스크 조회 화면](../assets/images/install-guide-general-virtualization-clvm-disk-management-read-02.png){ align=center }
    - GFS 디스크 상태에서 CLVM 디스크 정보를 클릭합니다.
    - 클릭시 볼륨 그룹 이름, 물리 볼륨 이름, 용량, wwn 정보를 확인하실 수 있습니다.