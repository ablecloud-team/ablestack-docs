
# 일반 가상화 Mold 설치진행

!!! danger
    이 문서는 기술지원 용도의 문서입니다. 기술지원 엔지니어가 아닌 사용자가 조작할 때 시스템에 문제가 발생할 수 있습니다.
    해당 설치과정에 사용되는 IP 및 입력 정보는 예시이며, 현장에 맞게 수정하시기 바랍니다.

일반 가상화 Mold 설치 진행 가이드 입니다.
이 문서에서는 일반 가상화 Mold 용 가상머신 생성 및 Mold 웹콘솔을 이용하여 Zone 구성까지 가이드 하고 있습니다.
일반 가상화 Cube 의 웹콘솔과 일반 가상화 Mold 웹콘솔을 이용하여 진행이 되며 웹 접속 IP는 별도의 표시를 하지 않고 진행됩니다.
기존에 구성된 IP 정보에 맞게 웹콘솔을 접속 하시면 됩니다.

## ABLESTACK 메인 화면
![ABLESTACK 메인 화면](../assets/images/install-guide-general-virtualization-mold-01.png){ align=center }
- 왼쪽 ABLESTACK 메뉴 클릭시 보이는 화면입니다.

!!! note
    일반 가상화 클러스터는 1식의 이상 호스트로 구성되어야 합니다.

    이 문서에서는 3식의 호스트를 기준으로 가이드를 제공하고 있습니다.

## 라이선스 관리(1번 호스트)
!!! check
    라이선스를 등록하기 위해서는 ABLECLOUD로부터 발급된 라이선스 파일이 필요합니다.
    라이선스 관련 문의 사항은 ABLECLOUD 고객 지원 번호 및 이메일로 문의해 주시기 바랍니다.

1. 라이선스 등록
    ![라이선스 등록](../assets/images/install-guide-general-virtualization-mold-license1-01.png){ align=center }
    - 구축 전, 발급 받은 **트라이얼 라이선스 파일** 을 등록 해줍니다.

2. 라이선스 확인
    ![라이선스 확인](../assets/images/install-guide-general-virtualization-mold-license1-02.png){ align=center }
    - 등록된 라이선스 정보를 확인할 수 있는 화면입니다.

## 클러스터 구성 준비(1번 호스트)

1. 개요
    ![클러스터 구성 준비 개요](../assets/images/install-guide-general-virtualization-mold-02.png){ align=center }
    - 상단 리본의 **클러스터 구성 준비** 링크를 클릭하면 보이는 화면입니다.
    - 일반 가상화를 구성을 하는데 필요한 정보를 입력 받아 클러스터 구성을 준비하는 마법사 화면입니다.
    - **다음** 버튼을 눌러 클러스터 구성 준비를 시작합니다.

2. 클러스터 종류
    ![클러스터 종류](../assets/images/install-guide-general-virtualization-mold-03.png){ align=center }
    - 클러스터 종류를 설정하는 화면입니다.
    - **ABLESTACK-VM** 를 선택합니다.
    - **다음** 버튼을 클릭하여 클러스터 종류를 선택합니다.

3. SSH Key 파일(신규생성)
    ![SSH Key 파일](../assets/images/install-guide-general-virtualization-mold-04.png){ align=center }
    - 모든 호스트 및 가상 머신은 동일한 SSH Key 를 공유하고 있어야 구성이 가능합니다.
    - **SSH Key 준비 방법** 에서 **신규 생성** 을 선택하고 **다음** 버튼을 클릭하여 신규 SSH Key 를 생성합니다.

4. 클러스터 구성 파일
    ![클러스터 구성 파일](../assets/images/install-guide-general-virtualization-mold-05.png){ align=center }
    - 클러스터 구성 설정하는 화면입니다. **클러스터 호스트 구분** 을 **신규 클러스터 호스트** 로 선택한다.
    - **클러스터 구성 파일 준비** 에서 **신규 생성** 을 선택합니다.
    - **현재 호스트명** 은 해당 호스트의 이름을 자동으로 불러옵니다.
    - **구성 호스트 수** 3대로 입력합니다.
    - **클러스터 구성 프로파일** 호스트 명 및 IP 정보를 입력 합니다.
    ![클러스터 구성 파일1](../assets/images/install-guide-general-virtualization-mold-05-1.png){ align=center }
    - **CCVM 관리 IP** 정보를 입력 합니다.
    - **관리 NIC CIDR** 정보를 입력 합니다.
    - **관리 NIC Gateway** 정보를 입력 합니다.
    - **관리 NIC DNS** 정보를 입력 합니다.
    - 위 항목을 입력 및 확인 후에 **다음** 버튼을 클릭합니다.

    !!! info
        idx 순서에 맞게 호스트 명과 ip 정보를 입력해야 합니다.<br/>
        현재 호스트명을 자동으로 불러오며, 클러스터 구성 프로파일에 현재 호스트명과 동일한 호스트 명이 존재해야 합니다.<br/>
        호스트 파일을 신규로 구성 호스트 수를 선택하면 하단의 호스트 파일에 호스트 수 만큼의 예제 항목이 생성됩니다.<br/>

    !!! example
        - 호스트 프로파일 예제

        idx | 호스트 명 | 호스트 IP |
        :---: | :-------: | :-------:
        1 | ablecube1 | 10.10.12.1
        2 | ablecube2 | 10.10.12.2
        3 | ablecube3 | 10.10.12.3


5. 시간서버

    !!! info
        일반 가상화 시간서버는 매우 중요한 역할을 합니다. </br>
        시간동기화가 맞지 않으면 스토리지 데이터들의 무결성 확보에 치명적일 수 있습니다.</br>
        따라서 시간서버는 반드시 구성해야합니다.</br>
        인터넷등 외부 통신이 가능한 환경이어서 외부 공인된 시간서버(NTP)에 접속이 가능하거나 내부에 별도의 시간서버(NTP)가 존재하는 경우에는 "외부 시간 서버"를 입력하여 진행하고, 없으시면 "다음" 으로 넘어가시면 됩니다.</br>
        폐쇄적인 네트워크 환경으로 외부 공인된 시간서버와 통신이 불가하고 내부에 별도의 시간서버가 없을 경우에는 일반 가상화애서 자체적으로 시간서버를 구성합니다.

    ![시간 서비](../assets/images/install-guide-general-virtualization-mold-06.png){ align=center }

    - 시간 서버 구성하는 화면입니다.
    - 클러스터 구성 정보를 토대로 시간 서버 입력값을 기본 세팅합니다.
    - 기본적으로 idx1 = Master Server, idx2 = Second Server, idx3 이상 = Other Server로 설정 됩니다.
    - **외부 시간서버** 가 존재하는 경우에는 입력 하고, 존재하지 않을 경우에는 빈칸으로 남겨두고 넘어 갑니다.

6. 설정확인
    ![설정확인](../assets/images/install-guide-general-virtualization-mold-07.png){ align=center }
    - 구성 준비에 입력값에 대한 설정을 확인하는 화면입니다.
    - 설정된 값을 확인 후 이상이 없는 경우 **완료** 버튼을 클릭합니다.

7. 완료
    ![진행](../assets/images/install-guide-general-virtualization-mold-08.png){ align=center }
    - 클러스터 구성 준비 3단계 진행상황을 확인합니다.
    - 정상적으로 끝날 경우 완료 화면이 호출 됩니다.

    ![완료](../assets/images/install-guide-general-virtualization-mold-09.png){ align=center }

    - 1번 호스트의 사전구성 완료 화면입니다.
    - **Private SSH Key**, **Public SSH Key**, **클러스터 구성 프로파일** 을 재사용하기 위하여 링크를 클릭하여 다운로드 합니다.

!!! info
    SSH Key 및 클러스터 구성 프로파일을 다운로드 한 후에 2번 호스트, 3번 호스트 구성시 다운로드한 파일을 재사용 해야 정상적으로 구성이 됩니다.

## 라이선스 관리(2번 호스트)
!!! check
    라이선스를 등록하기 위해서는 ABLECLOUD로부터 발급된 라이선스 파일이 필요합니다.
    라이선스 관련 문의 사항은 ABLECLOUD 고객 지원 번호 및 이메일로 문의해 주시기 바랍니다.

1. 라이선스 등록
    ![라이선스 등록](../assets/images/install-guide-general-virtualization-mold-license2-01.png){ align=center }
    - 구축 전, 발급 받은 **트라이얼 라이선스 파일** 을 등록 해줍니다.

2. 라이선스 확인
    ![라이선스 확인](../assets/images/install-guide-general-virtualization-mold-license2-02.png){ align=center }
    - 등록된 라이선스 정보를 확인할 수 있는 화면입니다.

## 클러스터 구성 준비(2번  호스트)

!!! info
    2번 호스트 구성 방법 입니다. (기본적인 절차는 1번 호스트와 동일합니다)

1. 개요
   ![클러스터 구성 준비 개요](../assets/images/install-guide-general-virtualization-mold-10.png){ align=center }
    - 상단 리본의 **클러스터 구성 준비** 링크를 클릭하면 보이는 화면입니다.
    - 일반 가상화 구성을 하는데 필요한 정보를 입력 받아 클러스터 구성을 준비하는 마법사 화면입니다.
    - **다음** 버튼을 눌러 클러스터 구성 준비를 시작합니다.

2. 클러스터 종류
    ![클러스터 종류](../assets/images/install-guide-general-virtualization-mold-11.png){ align=center }
    - 클러스터 종류를 설정하는 화면입니다.
    - **ABLESTACK-VM** 를 선택합니다.
    - **다음** 버튼을 클릭하여 클러스터 종류를 선택합니다.

3. SSH Key 파일(기존파일사용)
   ![SSH Key 파일](../assets/images/install-guide-general-virtualization-mold-12.png){ align=center }
    - 모든 호스트 및 가상 머신은 동일한 SSH Key 를 공유하고 있어야 구성이 가능합니다.
    - **SSH Key 준비 방법** 에서 **기존 파일 사용** 을 선택하고 **SSH 개인 Key** 와 **SSH 공개 Key** 를 **파일 선택** 버튼을 눌러 1번 호스트 클러스터 구성 준비 단계에서
    다운로드한 SSH Key 를 등록합니다.

    !!! info
        SSH 개인 Key 파일 명은 **id_rsa**, SSH 공개 Key 파일명은 **id_rsa.pub** 으로 고정되어 있습니다.
        다운로드한 Key 의 파일 명을 수정할 경우 등록이 불가능 합니다.

3. 클러스터 구성 파일
    ![클러스터 구성 파일](../assets/images/install-guide-general-virtualization-mold-13.png){ align=center }
    - 클러스터 구성 설정하는 화면입니다. **클러스터 호스트 구분** 을 **신규 클러스터 호스트** 로 선택한다.
    - **클러스터 구성 파일 준비** 에서 **기존 파일 사용** 을 선택합니다.
    - **클러스터 구성 파일** 에서 cluster.json 파일을 업로드 클러스터 정보를 자동입력 합니다.
    - **현재 호스트명** 은 해당 호스트의 이름을 자동으로 불러옵니다.
    - **구성 호스트 수** 는 기존 파일 사용 선택시 수정 불가능 상태가 됩니다.
    - **클러스터 구성 프로파일** 정보를 확인합니다.
    ![클러스터 구성 파일1](../assets/images/install-guide-general-virtualization-mold-14.png){ align=center }
    - **CCVM 관리 IP** 정보를 입력 합니다.
    - **관리 NIC CIDR** 정보를 입력 합니다.
    - **관리 NIC Gateway** 정보를 입력 합니다.
    - **관리 NIC DNS** 정보를 입력 합니다.
    - 위 항목을 입력 및 확인 후에 **다음** 버튼을 클릭합니다.

    !!! info
        idx 순서에 맞게 호스트 명과 ip 정보를 입력해야 합니다.<br/>
        현재 호스트명을 자동으로 불러오며, 클러스터 구성 프로파일에 현재 호스트명과 동일한 호스트 명이 존재해야 합니다.<br/>
        호스트 파일을 신규로 구성 호스트 수를 선택하면 하단의 호스트 파일에 호스트 수 만큼의 예제 항목이 생성됩니다.<br/>

    !!! example
        - 호스트 프로파일 예제

        idx | 호스트 명 | 호스트 IP |
        :---: | :-------: | :-------: |
        1 | ablecube1 | 10.10.12.1 |
        2 | ablecube2 | 10.10.12.2 |
        3 | ablecube3 | 10.10.12.3 |

4. 시간서버
   ![Host 파일](../assets/images/install-guide-general-virtualization-mold-15.png){ align=center }
    - 시간 서버 구성하는 화면입니다.
    - 클러스터 구성 정보를 토대로 시간 서버 입력값을 기본 세팅합니다.
    - **외부 시간서버** 가 존재할 경우, 자동으로 기본 셋팅합니다.
    - 기본적으로 idx1 = Master Server, idx2 = Second Server, idx3 이상 = Other Server로 설정 됩니다.

5. 설정확인
   ![설정확인](../assets/images/install-guide-general-virtualization-mold-16.png){ align=center }
    - 구성 준비에 입력값에 대한 설정을 확인하는 화면입니다.
    - 설정된 값을 확인 후 이상이 없는경우 **완료** 버튼을 클릭합니다.

6. 완료
    ![진행](../assets/images/install-guide-general-virtualization-mold-17.png){ align=center }
    - 클러스터 구성 준비 3단계 진행상황을 확인합니다.
    - 정상적으로 끝날 경우 완료 화면이 호출 됩니다.

    ![완료](../assets/images/install-guide-general-virtualization-mold-18.png){ align=center }

    - 2번 호스트의 사전구성 완료 화면입니다.

    !!! info
        SSH Key 및  클러스터 구성 파일은 1번 호스트에서 다운로드 하셨다면 해당 화면에서 다운로드 하지 않으셔도 됩니다.

## 라이선스 관리(3번 호스트)
!!! check
    라이선스를 등록하기 위해서는 ABLECLOUD로부터 발급된 라이선스 파일이 필요합니다.
    라이선스 관련 문의 사항은 ABLECLOUD 고객 지원 번호 및 이메일로 문의해 주시기 바랍니다.

1. 라이선스 등록
    ![라이선스 등록](../assets/images/install-guide-general-virtualization-mold-license3-01.png){ align=center }
    - 구축 전, 발급 받은 **트라이얼 라이선스 파일** 을 등록 해줍니다.

2. 라이선스 확인
    ![라이선스 확인](../assets/images/install-guide-general-virtualization-mold-license3-02.png){ align=center }
    - 등록된 라이선스 정보를 확인할 수 있는 화면입니다.

## 클러스터 구성 준비(3번  호스트)

!!! info
    3번 호스트 구성 방법 입니다. (절차는 2번 호스트와 동일합니다)

1. 개요
   ![클러스터 구성 준비 개요](../assets/images/install-guide-general-virtualization-mold-19.png){ align=center }
    - 상단 리본의 **클러스터 구성 준비** 링크를 클릭하면 보이는 화면입니다.
    - 일반 가상화 구성을 하는데 필요한 정보를 입력 받아 클러스터 구성을 준비하는 마법사 화면입니다.
    - **다음** 버튼을 눌러 클러스터 구성 준비를 시작합니다.

2. 클러스터 종류
    ![클러스터 종류](../assets/images/install-guide-general-virtualization-mold-20.png){ align=center }
    - 클러스터 종류를 설정하는 화면입니다.
    - **ABLESTACK-VM** 를 선택합니다.
    - **다음** 버튼을 클릭하여 클러스터 종류를 선택합니다.

3. SSH Key 파일(기존파일사용)
   ![SSH Key 파일](../assets/images/install-guide-general-virtualization-mold-21.png){ align=center }
    - 모든 호스트 및 가상 머신은 동일한 SSH Key 를 공유하고 있어야 구성이 가능합니다.
    - **SSH Key 준비 방법** 에서 **기존 파일 사용** 을 선택하고 **SSH 개인 Key** 와 **SSH 공개 Key** 를 **파일 선택** 버튼을 눌러 1번 호스트 클러스터 구성 준비 단계에서
    다운로드한 SSH Key 를 등록합니다.

    !!! info
        SSH 개인 Key 파일 명은 **id_rsa**, SSH 공개 Key 파일명은 **id_rsa.pub** 으로 고정되어 있습니다.
        다운로드한 Key 의 파일 명을 수정할 경우 등록이 불가능 합니다.

3. 클러스터 구성 파일
    ![클러스터 구성 파일](../assets/images/install-guide-general-virtualization-mold-22.png){ align=center }
    - 클러스터 구성 설정하는 화면입니다. **클러스터 호스트 구분** 을 **신규 클러스터 호스트** 로 선택한다.
    - **클러스터 구성 파일 준비** 에서 **기존 파일 사용** 을 선택합니다.
    - **클러스터 구성 파일** 에서 cluster.json 파일을 업로드 클러스터 정보를 자동입력 합니다.
    - **현재 호스트명** 은 해당 호스트의 이름을 자동으로 불러옵니다.
    - **구성 호스트 수** 는 기존 파일 사용 선택시 수정 불가능 상태가 됩니다.
    - **클러스터 구성 프로파일** 정보를 확인합니다.
    ![클러스터 구성 파일1](../assets/images/install-guide-general-virtualization-mold-23.png){ align=center }
    - **CCVM 관리 IP** 정보를 입력 합니다.
    - **관리 NIC CIDR** 정보를 입력 합니다.
    - **관리 NIC Gateway** 정보를 입력 합니다.
    - **관리 NIC DNS** 정보를 입력 합니다.
    - 위 항목을 입력 및 확인 후에 **다음** 버튼을 클릭합니다.

    !!! info
        idx 순서에 맞게 호스트 명과 ip 정보를 입력해야 합니다.<br/>
        현재 호스트명을 자동으로 불러오며, 클러스터 구성 프로파일에 현재 호스트명과 동일한 호스트 명이 존재해야 합니다.<br/>
        호스트 파일을 신규로 구성 호스트 수를 선택하면 하단의 호스트 파일에 호스트 수 만큼의 예제 항목이 생성됩니다.<br/>

    !!! example
        - 호스트 프로파일 예제

        idx | 호스트 명 | 호스트 IP |
        :---: | :-------: | :-------: |
        1 | ablecube1 | 10.10.12.1 |
        2 | ablecube2 | 10.10.12.2 |
        3 | ablecube3 | 10.10.12.3 |

4. 시간서버
   ![Host 파일](../assets/images/install-guide-general-virtualization-mold-24.png){ align=center }
    - 시간 서버 구성하는 화면입니다.
    - 클러스터 구성 정보를 토대로 시간 서버 입력값을 기본 세팅합니다.
    - **외부 시간서버** 가 존재할 경우, 자동으로 기본 셋팅합니다.
    - 기본적으로 idx1 = Master Server, idx2 = Second Server, idx3 이상 = Other Server로 설정 됩니다.

5. 설정확인
   ![설정확인](../assets/images/install-guide-general-virtualization-mold-25.png){ align=center }
    - 구성 준비에 입력값에 대한 설정을 확인하는 화면입니다.
    - 설정된 값을 확인 후 이상이 없는경우 **완료** 버튼을 클릭합니다.

6. 완료
    ![진행](../assets/images/install-guide-general-virtualization-mold-26.png){ align=center }
    - 클러스터 구성 준비 3단계 진행상황을 확인합니다.
    - 정상적으로 끝날 경우 완료 화면이 호출 됩니다.

    ![완료](../assets/images/install-guide-general-virtualization-mold-27.png){ align=center }

    - 3번 호스트의 사전구성 완료 화면입니다.

    !!! info
        SSH Key 및  클러스터 구성 파일은 1번 호스트에서 다운로드 하셨다면 해당 화면에서 다운로드 하지 않으셔도 됩니다.

## 클라우드센터 가상머신 배포 전 필수 사항
!!! warning
    클라우드센터 가상머신 배포 전, 반드시 외부 스토리지 디스크와의 연결이 되었는지 확인해야 합니다.

!!! info
    반드시 외부 스토리지가 이중화로 되어 있을 경우에만, 해당 다중 경로 활성화를 실행합니다.

    이중화가 되어 있지 않을 경우에는 해당 사항을 넘어 갑니다.

    모든 호스트에 외부 스토리지가 정상적으로 연결되었는지 확인한 후, 다중 경로를 활성화하세요.

1. 다중 경로 활성화
    ![다중 경로 활성화](../assets/images/install-guide-general-virtualization-mold-28.png){ align=center }
    - 이중화된 외부 스토리지를 사용하는 클라우드센터 가상 머신을 구축할 때, 이 버튼을 활성화하면 모든 호스트에서 여러 개의 디스크를 동기화하여 다중 경로(Multipath)로 구성합니다.
    - 이를 통해 스토리지 경로를 최적화하고, 보다 안정적이고 효율적인 스토리지 접근을 보장합니다.
    - 다중 경로를 꼭 활성화한 후 다음 단계를 진행하세요.

## 클라우드센터 가상머신 배포
![클라우드센터 가상머신 배포](../assets/images/install-guide-general-virtualization-mold-29.png){ align=center }
- 클라우드센터 가상머신을 배포하기 위한 화면입니다. 상단 상태 리본의 클라우드센터 가상머신 배포 링크를 클릭합나다.

1. 개요
    ![클라우드센터 가상머신 배포 개요](../assets/images/install-guide-general-virtualization-mold-30.png){ align=center }
    - 클라우드센터 가상머신 배포 개요 화면입니다. 개요의 내용을 확인 후 **다음** 버튼을 클릭합니다.

2. 클라우드센터 가상머신 설정 - 클러스터 민감도
    ![클라우드센터 가상머신 설정 - 클러스터 민감도](../assets/images/install-guide-general-virtualization-mold-31.png){ align=center }
    - 클라우드센터 가상머신의 클러스터 민감도를 설정하는 화면입니다.
    - **클라스터 민감도(초)** 입력란에 0 ~ 300초 사이에 해당하는 숫자를 입력하세요.

    !!! info
        클러스터 민감도 - 이는 노드 간 통신 지연, 장애 감지 속도, 장애 시 클러스터의 반응 방식 등을 결정하는 중요한 요소입니다.

        예를 들어, 네트워크 상태가 불안정한 환경에서는 타이머 값을 조정하여 오탐(false positive)을 줄이고, 반대로 빠른 장애 감지가 필요한 경우 보다 민감하게 설정할 수 있습니다.

        최소 0초에서 최대 300초 사이 시간 범위 내에 입력하시길 바랍니다.

3. 클라우드센터 가상머신 설정 - 컴퓨트
    ![클라우드센터 가상머신 설정 - 컴퓨트](../assets/images/install-guide-general-virtualization-mold-32.png){ align=center }
    - 클라우드센터 가상머신의 컴퓨트 설정하는 화면입니다.
    - **CPU Core** 선택 박스는 **8 vCore**, **Memory** 선택 박스는 **16 GiB** 를 선택 하고 **다음** 버튼을 클릭합니다.

    !!! tip
        클라우드센터 가상머신의 Compute 자원은 클라우드센터가 관리해야 할 호스트의 수에 따라 탄력적으로 선택합니다.
        가상머신이 컨트롤 할 호스트의 수가 **10개 미만** 이면 **8 vCore** 를, **그 이상** 이면 **16 vCore** 를 선택하십시오.
        메모리는 컨트롤할 호스트의 수가 **10개** 미만이면 **16GiB** 를, **10 ~ 20개** 이면 **32GiB** 를, **21개 이상** 이면 **64GiB** 를 선택해야 합니다.
        ROOT Disk의 크기는 **500GiB** 를 디스크가 **Thin Provisioning** 방식으로 제공됩니다.

4. 클라우드센터 가상머신 설정 - 네트워크
    ![클라우드센터 가상머신 설정 - 네트워크](../assets/images/install-guide-general-virtualization-mold-33.png){ align=center }
    - 클라우드센터 가상머신의 네트워크 설정하는 화면입니다.
    - **관리네트워크** 선택 박스에서 **bridge0** 을 선택하고 **다음** 버튼을 클릭합니다.

    !!! info
        관리 네트워크와 서비스 네트워크가 분리되여 있는 경우 그리고 외부에서 클라우드센터 웹콘솔에 접근해야 하는경우에는 **네트워크 구성** 항목에서
        **서비스네트워크** 항목을 체크하신 후에 **서비스네트워크** 선택 박스에서 해당되는 **브릿지** 를 선택하셔야 합니다.

5. 클라우드센터 가상머신 설정 - 디스크
    ![클라우드센터 가상머신 설정 - 디스크](../assets/images/install-guide-general-virtualization-mold-34.png){ align=center }
    - 클라우드센터 가상머신의 디스크를 설정하는 화면입니다.
    - **GFS용 디스크 구성 대상 장치** 체크 박스에서 해당 하는 디스크를 선택한 후, **다음** 버튼을 클릭합니다.

    !!! tip
        디스크 이름, 디스크 상태, 디스크 종류, 용량, 디스크 정보, 디스크 wwn 으로 구분 되어 있습니다.

    !!! info
        GFS2 스토리지를 기반으로 가상 머신을 생성하며, 해당 디스크에서 직접 작업을 수행할 수 있습니다. 이를 통해 여러 호스트에서 동시에 접근 가능하며, 안정적이고 효율적인 스토리지 운영이 가능합니다.

6. 추가 네트워크 정보
    ![추가 네트워크 정보](../assets/images/install-guide-general-virtualization-mold-35.png){ align=center }
    - 클라우드센터 가상머신 추가 네트워크 정보를 설정하는 화면입니다.
    - **클러스터 구성 파일 준비** 해당 호스트 파일 사용으로 자동 선택되며, ablecube 호스트 설정 정보를 자동으로 읽어와 클러스터 구성 정보 및 네트워크 IP 정보를 세팅합니다.
    - **호스트명(CCVM)** 을 입력 및 확인합니다.
    - **관리 NIC IP** 를 입력 및 확인합니다.
    - **다음** 버튼을 클릭합니다.

    !!! info
        클라우드센터 가상머신 배포시 ablecube 호스트에서 설정파일 읽어와 일부 정보를 자동세팅되며 입력 정보를 정확히 확인해야 합니다.
        해당 화면의 IP 정보 는 예제 입니다. IP 정보는 사이트 정보에 맞춰서 수정해야 합니다.

7. IPMI 정보
    ![IPMI 정보](../assets/images/install-guide-general-virtualization-mold-36.png){ align=center }
    - **각 IPMI 자격 증명** 에 따라 선택한 후, 해당하는 **IPMI IP** , **아이디** 및 **비밀번호** 를 입력합니다.
    - **다음** 버튼을 클릭합니다.

    !!! tip
        각 IPMI 자격 증명이 다르면 개별 자격 증명을 선택하고, 똑같다면 공통 자격 증명을 선택합니다.

5. SSH Key 정보
    ![SSH Key 정보](../assets/images/install-guide-general-virtualization-mold-37.png){ align=center }
    - SSH Key 정보를 확인하는 화면입니다.
    - 클러스터 구성시 호스트에 등록된 호스트의 키 정보로 자동세팅됩니다.

6. 장애조치 클러스터 설정
    ![장애조치 클러스터 설정](../assets/images/install-guide-general-virtualization-mold-38.png){ align=center }
    - 장애조치 클러스터 설정하는 화면 입니다.
    - **호스트 #1정보**, **호스트 #2정보**, **호스트 #3정보** 에는 **호스트 PN IP #1**, **호스트 PN IP #2**, **호스트 PN IP #3** 자동으로 세팅이 되며 입력 정보를 정확히 확인하고 **다음** 버튼을 클릭합니다.

    !!! info
        클라우드센터 장애조치 클러스터는 최대 3개의 호스트를 지정할 수 있습니다.

7. 설정확인
    ![설정확인](../assets/images/install-guide-general-virtualization-mold-39.png){ align=center }
    - 클라우드센터 가상머신 배포전 설정을 확인하는 화면입니다.
    - 설정정보를 확인 후 **배포** 버튼을 클릭 합니다.

8. 배포
    ![배포](../assets/images/install-guide-general-virtualization-mold-40.png){ align=center }
    - 클라우드센터 가상머신 배포 진행상황을 확인 할 수 있는 화면입니다.

9. 완료
    ![완료](../assets/images/install-guide-general-virtualization-mold-41.png){ align=center }
    - 클라우드센터 가상머신 배포가 완료 후 일반 가상화 Cube 웹콘솔에서 클라우드센터 클러스터 상태 카드 항목에서 **클러스터 상태** 가 **Health Ok**,
      클라우드센터 가상머신 상태 카드에서 **가상머신상태** 가 **Running** 인지 확인하셔야 합니다.

## 클라우드센터 가상머신 웹콘솔 구성
클라우드센터 웹콘솔 구성을 하기 위해서는 **Bootstrap** 우선 실행해야 하며 **Bootstrap** 실행 후 클라우드센터 웹콘솔 화면을 이용하여 클라우드센터 구성을 하실수 있습니다.

1. Bootstrap 실행전
    ![Bootstrap 실행전](../assets/images/install-guide-general-virtualization-mold-42.png){ align=center }
    - Bootstrap 실행전 화면입니다. 상단의 리본 화면에서 **클라우드 센터에 연결할 수 있도록 클라우드센터 VM Bootstrap 실행 작업을 실행하십시오.** 문구가 보인다면
    클라우드센터 Bootstrap을 실행할 수 있습니다.

2. Bootstrap 실행
    ![Bootstrap 실행](../assets/images/install-guide-general-virtualization-mold-43.png){ align=center }
    - Bootstrap 실행 화면입니다. 클라우드센터 클러스터 상태 카드에서 메뉴버튼을 클릭하여 **클라우드센터 구성하기** 버튼을 클릭합니다.
    - **실행** 버튼을 클릭하여 Bootstrap을 실행합니다.

    !!! important
        Bootstrap 은 1개의 호스트에서만 실행 됩니다. 1번 호스트에서 실행이 된경우에는 2번, 3번 호스트에서는 **Bootstrap 실행** 버튼이 사라지게 됩니다.

3. Bootstrap 완료
    ![Bootstrap 완료](../assets/images/install-guide-general-virtualization-mold-44.png){ align=center }
    - Bootstrap 실행 후 완료 화면입니다.
    - 상단 리본 화면에서 **클라우드센터 연결**, **모니터링센터 구성** 링크가 보인다면 정상적으로 실행된 상태 입니다.
    - **클라우드센터 연결** 링크를 클릭하여 클라우드센터 웹콘솔에 접속 하실 수 있습나다.

## 클라우드센터 Zone 구성
클라우드센터 웹콘솔을 이용한 Zone 구성 진행 절차에 대하여 가이드하고 있습니다.
해당 문서에서는 Zone 구성까지만 설명을 하고 있으며 Zone 구성 이후의 클라우드센터 웹콘솔 사용방법은 다른 문서를 참고하시기 바랍니다.

![클라우드센터연결](../assets/images/install-guide-general-virtualization-mold-45.png){ align=center }
- Bootstrap 실행 완료 후 상단의 리본 창에서 **클라우드센터 연결** 링크를 클릭합니다.

!!! info
    Bootstrap을 실행 후, 약 2분 내외로 서비스가 올라오기 때문에 "클라우드센터에 정상적으로 연결되지 않습니다. 클라우드센터 서비스 상태를 확인하거나, 잠시 후에 다시 시도해주십시오." 문구가 나타나면 잠시 대기 했다가 재접속 하시길 바랍니다.

1. 클라우드센터 로그인
    ![클라우드센터 로그인](../assets/images/install-guide-general-virtualization-mold-46.png){ align=center }
    - 클라우드 센터 로그인 화면입니다.
    - **사용자 이름** 에는 **admin**, **비밀번호** 는 **password** 를 입력하고 **로그인** 버튼을 클릭하면 접속할 수 있습니다.

2. 클라우드센터 admin 비밀번호 변경
    ![클라우드센터 admin 비밀번호 변경](../assets/images/install-guide-general-virtualization-mold-47.png){ align=center }
    - 관리자 계정의 비밀번호를 변경하는 화면입니다. **새 비밀번호**, **비밀번호 확인 입력** 에 동일한 비밀번호를 입력 후 **확인**
    버튼을 클릭합니다.

3. 클라우드센터 Zone 유형 선택
    ![클라우드센터 Zone 유형 선택](../assets/images/install-guide-general-virtualization-mold-48.png){ align=center }
    - **Zone** 의 유형을 선택하는 화면입니다.
    - **Core** 을 선택한 후에 **다음** 버튼을 클릭합니다.
    ![클라우드센터 Zone Type 선택](../assets/images/install-guide-general-virtualization-mold-49.png){ align=center }
    - **Core Zone** 의 유형을 선택하는 화면입니다.
    - **확장** 을 선택한 후에 **다음** 버튼을 클릭합니다．

4. 클라우드센터 Zone 정보
   ![클라우드센터 Zone 정보](../assets/images/install-guide-general-virtualization-mold-50.png){ align=center }
    - Zone 에 대한 정보를 입력하는 화면 입니다.
    - **이름** 에는 **Zone** 을 입력합니다.
    - **IPv4 DNS1** 에는 **8.8.8.8** 을 입력합니다.
    - **내부 DNS 1** 에는 **8.8.8.8** 을 입력합니다.
    - 입력 정보 확인 후에 **다음** 버튼을 클릭 합니다.

5. 클라우드센터 Zone 물리 네트워크
   ![클라우드센터 Zone 물리 네트워크](../assets/images/install-guide-general-virtualization-mold-51.png){ align=center }
    - Zone 의 네트워크 정보를 입력하는 화면입니다.
    - 입력된 정보를 확인 후 **다음** 버튼을 클릭합니다.

6. 클라우드센터 Zone 서비스용 네트워크 정보
    ![클라우드센터 Zone 서비스용 네트워크 정보](../assets/images/install-guide-general-virtualization-mold-52.png){ align=center }
    - Zone 의 서비스용 네트워크 정보를 입력 하는 화면입니다.
    - **게이트웨이** 항목에는 **10.10.0.1**, **넷마스크** 항목에는 **255.255.0.0**, **시작 IP 주소** 항목에는 **10.10.12.5** **종료 IP 주소** 항목에는 **10.10.12.6** 을 입력하고 **추가** 버튼을 클릭합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

    !!! check
        여기서 시작, 종료 IP 주소는 Mold의 System VM의 필요한 2개 외부 IP 입니다.

        사용자에 맞게 남은 2개의 IP를 입력하시길 바랍니다.

7. 클라우드센터 Pod 네트워크 정보
    ![클라우드센터 Pod 네트워크 정보](../assets/images/install-guide-general-virtualization-mold-53.png){ align=center }
    - Pod 네트워크 정보를 입력하는 화면 입니다.
    - **Pod 이름** 항목에는 **Pod** 를 입력합니다.
    - **예약된 시스템 게이트웨이** 항목에는 **10.10.0.1** 을 입력합니다.
    - **예약된 시스템 넷마스크** 항목에는 **255.255.0.0** 을 입력합니다.
    - **예약된 시스템 시작 IP 주소** 항목에는 **10.10.12.7** 을 입력합니다.
    - **예약된 시스템 종료 IP 주소** 항목에는 **10.10.12.8** 을 입력합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

8. 클라우드센터 가상머신용 네트워크 정보
    ![클라우드센터 가상머신용 네트워크 정보](../assets/images/install-guide-general-virtualization-mold-54.png){ align=center }
    - 가상머신용 네트워크 정보를 입력하는 화면입니다.
    - **VLAN 범위** 에 **101**, **300** 을 입력합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

    !!! tip
        VLAN을 사용 하지 않는다면, 범위에 1 - 1 을 넣으셔도 무방합니다.

9. 클라우드센터 클러스터 정보
   ![클라우드센터 클러스터 정보](../assets/images/install-guide-general-virtualization-mold-55.png){ align=center }
    - 클라우드센터 클러스터 정보를 입력하는 화면입니다.
    - **클러스터 이름** 항목에 **Cluster** 를 입력합니다.
    - **CPU 아키텍처** 란에 **AMD 64 bits (x84_64)** 서버 사양에 맞게 선택합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

10. 클라우드센터 호스트 추가
    ![클라우드센터 호스트 추가](../assets/images/install-guide-general-virtualization-mold-56.png){ align=center }
    - 클라우드센터에 호스트를 추가하는 화면 입니다.
    - **호스트 이름** 항목에는 **10.10.12.1** 을 입력합니다.
    - **사용자 이름** 항목에는 **root** 를 입력합니다.
    - **비밀번호** 항목에는 **비밀번호** 를 입력합니다.
    - **태그** 항목에는 **ablecube1** 을 입력합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

11. 클라우드센터 기본스토리지 추가
    ![클라우드센터 기본스토리지 추가](../assets/images/install-guide-general-virtualization-mold-57.png){ align=center }
    - 기본 스토리지 추가하는 화면입니다.
    - **이름** 항목에는 **Primary** 를 입력합니다.
    - **범위** 선택 박스에는 **cluster** 을 선택합니다.
    - **제공자** 선택 박스에는 **DefaultPrimary** 를 선택합니다.
    - **프로토콜** 선택 박스에는 **SharedMountPoint** 를 선택합니다.
    - **경로** 항목에는 **/mnt/glue-gfs** 를 입력합니다.

    !!! tip
        경로 항목을 확인 할려면 ABLESTACK Cube 대시보드 화면에서 GFS 디스크 상태에서 마운트 경로를 확인하시면 됩니다.
        ![경로 확인](../assets/images/install-guide-general-virtualization-mold-58.png){ align=center }
        상세 정보 확인은 해당 경로를 클릭하면 확인할 수 있습니다.

    - **스토리지 태그** 항목에는 **glue-gfs** 를 입력합니다.

12. 클라우드센터 2차 스토리지 추가
    ![클라우드센터 2차 스토리지 추가](../assets/images/install-guide-general-virtualization-mold-59.png){ align=center }
    - 2차 스토리지를 추가하는 화면입니다.
    - **제공자** 선택 박스에서 **NFS** 를 선택 합니다.
    - **이름** 항목에는 **Secondary** 를 입력합니다.
    - **서버** 항목에는 **10.10.12.10** (ccvm mngt ip) 를 입력합니다.
    - **경로** 항목에는 **/nfs/secondary** 를 입력합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

13. 클라우드센터 Zone 추가중
    ![클라우드센터 Zone 추가중](../assets/images/install-guide-general-virtualization-mold-60.png){ align=center }
    - zone 추가 중 화면 입니다.

14. ablecube2 호스트 추가
    ![호스트 추가](../assets/images/install-guide-general-virtualization-mold-61.png){ align=center }
    - 클라우드센터 ablecube2 호스트를 추가하는 화면 입니다.
    - **Zone 이름** 항목에는 **Zone** 을 선택합니다.
    - **Pod 이름** 항목에는 **Pod** 을 선택합니다.
    - **클러스터** 항목에는 **Cluster** 를 선택합니다.
    - **호스트 이름** 항목에는 **ablecloud2** 를 입력합니다.
    - **사용자 이름** 항목에는 **root** 를 입력합니다.
    - **비밀번호** 항목에는 **비밀번호** 를 입력합니다.
    - **호스트 태그** 항목에는 **ablecube2** 를 입력합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

14. ablecube3 호스트 추가
    ![호스트 추가](../assets/images/install-guide-general-virtualization-mold-62.png){ align=center }
    - 클라우드센터 ablecube3 호스트를 추가하는 화면 입니다.
    - **Zone 이름** 항목에는 **Zone** 을 선택합니다.
    - **Pod 이름** 항목에는 **Pod** 을 선택합니다.
    - **클러스터** 항목에는 **Cluster** 를 선택합니다.
    - **호스트 이름** 항목에는 **ablecloud3** 를 입력합니다.
    - **사용자 이름** 항목에는 **root** 를 입력합니다.
    - **비밀번호** 항목에는 **비밀번호** 를 입력합니다.
    - **호스트 태그** 항목에는 **ablecube3** 를 입력합니다.
    - 입력한 정보를 확인 후 **다음** 버튼을 클릭합니다.

15. 호스트 라이선스 확인
    ![호스트 라이선스 확인](../assets/images/install-guide-general-virtualization-mold-check-license.png){ align=center }
    - 해당 하는 호스트 이름을 클릭하여 라이선스 유효기간을 확인할 수 있습니다.