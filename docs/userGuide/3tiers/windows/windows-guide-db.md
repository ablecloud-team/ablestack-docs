ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조" 구성 단계 중, 두 번째 단계인 DB 구성에 대한 문서입니다.

DB 서버의 이중화 구성은 MSCS(Microsoft Cluster Service)를 활용한 Failover Cluster 방식으로 구성합니다.
MSSQL을 구성하고 MSCS 방식을 활용하여 이중화 구성하는 방법은 다음과 같은 절차로 수행됩니다.

- 가상머신 생성
- 데이터 디스크 설정
- AD 서버 구성(AD-SVR)
- AD Join(NODE1, NODE2)
- iSCSI 서버 구성(AD-SVR)
- iSCSI 가상디스크 연결 - 초기자 구성(NODE1, NODE2)
- Failover Cluster 구성(NODE1, NODE2)
- MSSQL 설치(NODE1, NODE2)
- SSMS 설치(AD-SVR)
- 샘플코드 스키마 실행

## 가상머신 생성

ABLESTACK Mold는 기본적으로 템플릿을 이용해 가상머신을 생성하고 사용하는 것을 권장합니다. 먼저 Windows 기반의 가상머신 템플릿 이미지를 생성하여 등록하는 절차를 수행한 후 VM을 생성해야 합니다.

!!! note "MSCS 구성에 필요한 노드 개수"
    MSCS 방식을 동작하기 위해서는 최소 3개의 노드(가상머신)가 필요합니다.
    MSCS 방식은 두 개 이상의 노드를 클러스터로 묶어 하나가 실패하면 MSCS가 Failover Cluster를 수행하여 클러스터에 있는 다른 노드로 상태 데이터를 전송하고 서비스를 시작하는 방식입니다. Failover Cluster를 사용하기 위해서는 모든 노드가 하나의 디스크를 공유하는 방식으로 구성해야 하므로 N개의 노드와 공유 볼륨 서버 1개가 필요합니다.

가상머신을 추가하기 위해 **컴퓨트 > 가상머신** 화면으로 이동하여 **가상머신 추가** 버튼을 클릭합니다. "새 가상머신" 마법사 페이지가 표시됩니다. 해당 페이지에서는 "템플릿을 이용한 VM 생성" 문서를 참고하여 가상머신을 생성합니다.

!!! info "템플릿을 이용한 VM 생성"
    템플릿을 이용한 가상머신 추가를 위해 [템플릿을 이용한 VM 생성](../../../vms/    windows-guide-add-and-use-vm#vm) 문서를 참고하십시오.

- AD 가상머신(AD-SVR)

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Windows Server 2022 기본 이미지 템플릿**
    - 컴퓨트 오퍼링 : **2C-4GB-RBD-HA**
    - 데이터 디스크 : **50GB-WB-RBD** * iSCSI 디스크 공유에 사용됩니다.
    - 네트워크 : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.40
    - 이름 : **Windows-3tier-db-ad**

- DB 가상머신 1(NODE1)

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Windows Server 2022 기본 이미지 템플릿**
    - 컴퓨트 오퍼링 : **4C-8GB-RBD-HA**
    - 네트워크1(통신용) : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.184
    - 네트워크2(하트비트용) : **사용자가이드용-격리네트워크2**
        - IP: 10.1.2.85
    - 네트워크3(DB 클러스터용-MSSQL 설치시 네트워크 설정) : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.170
    - 이름 : **Windows-3tier-db-node01**

- DB 가상머신 2(NODE2)

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Windows Server 2022 기본 이미지 템플릿**
    - 컴퓨트 오퍼링 : **4C-8GB-RBD-HA**
    - 네트워크1(통신용) : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.99
    - 네트워크2(하트비트용) : **사용자가이드용-격리네트워크2**
        - IP: 10.1.2.136
    - 네트워크3(DB 클러스터용-MSSQL 설치시 네트워크 설정) : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.170
    - 이름 : **Windows-3tier-db-node02**

## 데이터 디스크 설정

안정적인 운영을 위해 기본 RootDisk가 아닌 고용량의 스펙을 가진 디스크로의 데이터 저장이 필요합니다. 이를 위한 사전작업으로 가상머신 생성 시 추가했던 데이터 디스크를 설정합니다.

다음과 같은 절차로 데이터 디스크를 설정합니다.

서버 관리자 > 도구 > '컴퓨터 관리' 버튼을 클릭합니다.

<center>
![3tier-windows-disk-3](../../../assets/images/3tier-windows/3tier-windows-disk-3.png){ width="600" }
</center>

가상머신 생성 시 추가했던 데이터 디스크 우클릭 > '온라인' 버튼을 클릭합니다.

<center>
![3tier-windows-disk-5](../../../assets/images/3tier-windows/3tier-windows-disk-5.png){ width="600" }
</center>

디스크 우클릭 > '디스크 초기화' 버튼을 클릭합니다.

<center>
![3tier-windows-disk-6](../../../assets/images/3tier-windows/3tier-windows-disk-6.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-disk-7](../../../assets/images/3tier-windows/3tier-windows-disk-7.png){ width="600" }
</center>

디스크 우클릭 > '새 단순 볼륨' 버튼을 클릭합니다.

<center>
![3tier-windows-disk-8](../../../assets/images/3tier-windows/3tier-windows-disk-8.png){ width="600" }
</center>

디스크 정보를 확인합니다.

<center>
![3tier-windows-disk-9](../../../assets/images/3tier-windows/3tier-windows-disk-9.png){ width="600" }
</center>

## AD 서버 구성(AD-SVR)

AD(Active Directory)는 Microsoft에서 만든 디렉토리 서비스로 사용자들의 계정정보, 정책, 서비스에 대한 정보를 가지고 있는 데이터베이스이자 서비스집합입니다. 도메인 생성을 위해 먼저 AD 서버를 구성합니다.

가상머신의 컴퓨터 이름을 변경합니다.

<center>
![3tier-windows-db-1](../../../assets/images/3tier-windows/3tier-windows-db-1.png){ width="600" }
</center>

서버 관리자 > 관리 > '역할 및 기능 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-2](../../../assets/images/3tier-windows/3tier-windows-db-2.png){ width="600" }
</center>

역할 및 기능 추가 마법사 페이지에서 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-3](../../../assets/images/3tier-windows/3tier-windows-db-3.png){ width="600" }
</center>

설치 유형을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-4](../../../assets/images/3tier-windows/3tier-windows-db-4.png){ width="600" }
</center>

대상 서버를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-5](../../../assets/images/3tier-windows/3tier-windows-db-5.png){ width="600" }
</center>

서버 역할에서 'Active Directory Domain Services'를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-6](../../../assets/images/3tier-windows/3tier-windows-db-6.png){ width="600" }
</center>

'기능 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-7](../../../assets/images/3tier-windows/3tier-windows-db-7.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-8](../../../assets/images/3tier-windows/3tier-windows-db-8.png){ width="600" }
</center>

기능 선택에서 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-9](../../../assets/images/3tier-windows/3tier-windows-db-9.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-10](../../../assets/images/3tier-windows/3tier-windows-db-10.png){ width="600" }
</center>

'설치' 버튼을 클릭합니다.

<center>
![3tier-windows-db-11](../../../assets/images/3tier-windows/3tier-windows-db-11.png){ width="600" }
</center>

설치가 완료되면 '닫기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-12](../../../assets/images/3tier-windows/3tier-windows-db-12.png){ width="600" }
</center>

서버 관리자 > 대시보드 상단의 '알림'을 클릭합니다.

<center>
![3tier-windows-db-13](../../../assets/images/3tier-windows/3tier-windows-db-13.png){ width="600" }
</center>

'이 서버를 도메인 컨트롤러로 승격' 버튼을 클릭합니다.

<center>
![3tier-windows-db-14](../../../assets/images/3tier-windows/3tier-windows-db-14.png){ width="600" }
</center>

AD의 루트 도메인 이름을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-15](../../../assets/images/3tier-windows/3tier-windows-db-15.png){ width="600" }
</center>

DSRM 암호를 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-16](../../../assets/images/3tier-windows/3tier-windows-db-16.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-17](../../../assets/images/3tier-windows/3tier-windows-db-17.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-18](../../../assets/images/3tier-windows/3tier-windows-db-18.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-19](../../../assets/images/3tier-windows/3tier-windows-db-19.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-20](../../../assets/images/3tier-windows/3tier-windows-db-20.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-21](../../../assets/images/3tier-windows/3tier-windows-db-21.png){ width="600" }
</center>

서버를 재시작합니다.

<center>
![3tier-windows-db-22](../../../assets/images/3tier-windows/3tier-windows-db-22.png){ width="600" }
</center>

서버 관리자 > 도구 > 'Active Directory 사용자 및 컴퓨터' 버튼을 클릭합니다.

<center>
![3tier-windows-db-23](../../../assets/images/3tier-windows/3tier-windows-db-23.png){ width="600" }
</center>

도메인명 > Users 우클릭 > 사용자 > '새로 만들기' 버튼을 클릭합니다.
<center>
![3tier-windows-db-24](../../../assets/images/3tier-windows/3tier-windows-db-24.png){ width="600" }
</center>

사용자 로그온 이름을 입력하고 '다음' 버튼을 클릭합니다.
<center>
![3tier-windows-db-25](../../../assets/images/3tier-windows/3tier-windows-db-25.png){ width="600" }
</center>

비밀번호를 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-26](../../../assets/images/3tier-windows/3tier-windows-db-26.png){ width="600" }
</center>

'마침' 버튼을 클릭합니다.

<center>
![3tier-windows-db-27](../../../assets/images/3tier-windows/3tier-windows-db-27.png){ width="600" }
</center>

mscs 사용자 우클릭 > '속성' 버튼을 클릭합니다.

<center>
![3tier-windows-db-28](../../../assets/images/3tier-windows/3tier-windows-db-28.png){ width="600" }
</center>

소속 그룹을 클릭합니다.

<center>
![3tier-windows-db-29](../../../assets/images/3tier-windows/3tier-windows-db-29.png){ width="600" }
</center>

'추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-30](../../../assets/images/3tier-windows/3tier-windows-db-30.png){ width="600" }
</center>

Domain Admins를 입력하고 '이름 확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-31](../../../assets/images/3tier-windows/3tier-windows-db-31.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-32](../../../assets/images/3tier-windows/3tier-windows-db-32.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-33](../../../assets/images/3tier-windows/3tier-windows-db-33.png){ width="600" }
</center>

## AD Join(NODE1, NODE2)

AD에서 만든 계정으로 접근하기위해 NODE1, NODE2를 AD 서버에 Join합니다.

제어판 > 네트워크 및 인터넷 > 네트워크 연결에서 IPv4의 DNS 주소는 AD 서버의 IP를 입력하고 '확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-34](../../../assets/images/3tier-windows/3tier-windows-db-34.png){ width="600" }
</center>

서버 관리자 > 로컬 서버 > 컴퓨터 이름을 클릭합니다.

<center>
![3tier-windows-db-35](../../../assets/images/3tier-windows/3tier-windows-db-35.png){ width="600" }
</center>

'변경' 버튼을 클릭합니다.

<center>
![3tier-windows-db-36](../../../assets/images/3tier-windows/3tier-windows-db-36.png){ width="600" }
</center>

컴퓨터 이름 및 도메인을 입력하고 '확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-37](../../../assets/images/3tier-windows/3tier-windows-db-37.png){ width="600" }
</center>

AD서버에서 만든 mscs계정을 입력합니다.

<center>
![3tier-windows-db-38](../../../assets/images/3tier-windows/3tier-windows-db-38.png){ width="600" }
</center>

도메인을 시작합니다.

<center>
![3tier-windows-db-39](../../../assets/images/3tier-windows/3tier-windows-db-39.png){ width="600" }
</center>

재시작 후 mscs계정으로 로그인합니다.

<center>
![3tier-windows-db-40](../../../assets/images/3tier-windows/3tier-windows-db-40.png){ width="600" }
</center>

## iSCSI 서버 구성(AD-SVR)

MSCS 구성에 필요한 공용 디스크를 설치하기 위해 iSCSI를 구성합니다. AD 서버는 iSCSI Target 서버가 됩니다.

서버 관리자 > 관리 > '역할 및 기능 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-41](../../../assets/images/3tier-windows/3tier-windows-db-41.png){ width="600" }
</center>

역할 및 기능 추가 마법사 페이지에서 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-42](../../../assets/images/3tier-windows/3tier-windows-db-42.png){ width="600" }
</center>

설치 유형을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-43](../../../assets/images/3tier-windows/3tier-windows-db-43.png){ width="600" }
</center>

대상 서버를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-44](../../../assets/images/3tier-windows/3tier-windows-db-44.png){ width="600" }
</center>

서버 역할에서 'ISCSI Target Server'를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-45](../../../assets/images/3tier-windows/3tier-windows-db-45.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-47](../../../assets/images/3tier-windows/3tier-windows-db-47.png){ width="600" }
</center>

'설치' 버튼을 클릭합니다.

<center>
![3tier-windows-db-48](../../../assets/images/3tier-windows/3tier-windows-db-48.png){ width="600" }
</center>

서버 관리자 > '파일 및 저장소 서비스'를 클릭합니다.

<center>
![3tier-windows-db-49](../../../assets/images/3tier-windows/3tier-windows-db-49.png){ width="600" }
</center>

작업 > '새 iSCSI 가상 디스크'를 클릭합니다.

<center>
![3tier-windows-db-50](../../../assets/images/3tier-windows/3tier-windows-db-50.png){ width="600" }
</center>

가상 디스크 생성 위치를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-51](../../../assets/images/3tier-windows/3tier-windows-db-51.png){ width="600" }
</center>

가상 디스크 이름을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-52](../../../assets/images/3tier-windows/3tier-windows-db-52.png){ width="600" }
</center>

가상 디스크 크기 및 타입을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-53](../../../assets/images/3tier-windows/3tier-windows-db-53.png){ width="600" }
</center>

가상 디스크가 할당될 iSCSI 대상을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-54](../../../assets/images/3tier-windows/3tier-windows-db-54.png){ width="600" }
</center>

iSCSI 대상 이름을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-55](../../../assets/images/3tier-windows/3tier-windows-db-55.png){ width="600" }
</center>

'추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-56](../../../assets/images/3tier-windows/3tier-windows-db-56.png){ width="600" }
</center>

'찾아보기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-57](../../../assets/images/3tier-windows/3tier-windows-db-57.png){ width="600" }
</center>

'고급' 버튼을 클릭합니다.

<center>
![3tier-windows-db-58](../../../assets/images/3tier-windows/3tier-windows-db-58.png){ width="600" }
</center>

'지금 찾기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-59](../../../assets/images/3tier-windows/3tier-windows-db-59.png){ width="600" }
</center>

클러스터에 참여할 노드(NODE1)를 선택하고 '확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-60](../../../assets/images/3tier-windows/3tier-windows-db-60.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-61](../../../assets/images/3tier-windows/3tier-windows-db-61.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-62](../../../assets/images/3tier-windows/3tier-windows-db-62.png){ width="600" }
</center>

두번째 노드 추가를 위해 '추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-63](../../../assets/images/3tier-windows/3tier-windows-db-63.png){ width="600" }
</center>

'찾아보기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-64](../../../assets/images/3tier-windows/3tier-windows-db-64.png){ width="600" }
</center>

'고급' 버튼을 클릭합니다.

<center>
![3tier-windows-db-65](../../../assets/images/3tier-windows/3tier-windows-db-65.png){ width="600" }
</center>

'지금 찾기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-66](../../../assets/images/3tier-windows/3tier-windows-db-66.png){ width="600" }
</center>

클러스터에 참여할 노드(NODE2)를 선택하고 '확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-67](../../../assets/images/3tier-windows/3tier-windows-db-67.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-68](../../../assets/images/3tier-windows/3tier-windows-db-68.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-69](../../../assets/images/3tier-windows/3tier-windows-db-69.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-70](../../../assets/images/3tier-windows/3tier-windows-db-70.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-71](../../../assets/images/3tier-windows/3tier-windows-db-71.png){ width="600" }
</center>

'만들기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-72](../../../assets/images/3tier-windows/3tier-windows-db-72.png){ width="600" }
</center>

'닫기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-73](../../../assets/images/3tier-windows/3tier-windows-db-73.png){ width="600" }
</center>

쿼럼 디스크 생성을 위해 서버 관리자 > 파일 및 저장소 서비스 > iSCSI에서 작업 > '새 iSCSI 가상 디스크'를 클릭합니다.

<center>
![3tier-windows-db-74](../../../assets/images/3tier-windows/3tier-windows-db-74.png){ width="600" }
</center>

가상 디스크 생성 위치를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-75](../../../assets/images/3tier-windows/3tier-windows-db-75.png){ width="600" }
</center>

가상 디스크 이름을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-76](../../../assets/images/3tier-windows/3tier-windows-db-76.png){ width="600" }
</center>

가상 디스크 크기 및 타입을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-77](../../../assets/images/3tier-windows/3tier-windows-db-77.png){ width="600" }
</center>

가상 디스크가 할당될 iSCSI 대상을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-78](../../../assets/images/3tier-windows/3tier-windows-db-78.png){ width="600" }
</center>

'만들기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-79](../../../assets/images/3tier-windows/3tier-windows-db-79.png){ width="600" }
</center>

'닫기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-80](../../../assets/images/3tier-windows/3tier-windows-db-80.png){ width="600" }
</center>

## iSCSI 가상디스크 연결 - 초기자 구성(NODE1, NODE2)

AD 서버에서 만든 디스크를 할당 받아 사용할 수 있도록 초기자를 구성합니다. Node1, Node2는 iSCSI Client 서버가 됩니다.

서버 관리자 > 도구 > 'iSCSI 초기자'를 선택합니다.

<center>
![3tier-windows-db-81](../../../assets/images/3tier-windows/3tier-windows-db-81.png){ width="600" }
</center>

'예' 버튼을 클릭합니다.

<center>
![3tier-windows-db-82](../../../assets/images/3tier-windows/3tier-windows-db-82.png){ width="600" }
</center>

iSCSI 대상 서버의 IP(DNS)를 입력하고 '빠른 연결' 버튼을 클릭합니다.

<center>
![3tier-windows-db-83](../../../assets/images/3tier-windows/3tier-windows-db-83.png){ width="600" }
</center>

'완료' 버튼을 클릭합니다.

<center>
![3tier-windows-db-84](../../../assets/images/3tier-windows/3tier-windows-db-84.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-85](../../../assets/images/3tier-windows/3tier-windows-db-85.png){ width="600" }
</center>

컴퓨터 관리 > 디스크 관리에서 가상디스크를 확인합니다.

<center>
![3tier-windows-db-86](../../../assets/images/3tier-windows/3tier-windows-db-86.png){ width="600" }
</center>

가상디스크 우클릭 > '온라인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-87](../../../assets/images/3tier-windows/3tier-windows-db-87.png){ width="600" }
</center>

가상디스크 우클릭 > '디스크 초기화' 버튼을 클릭합니다.

<center>
![3tier-windows-db-88](../../../assets/images/3tier-windows/3tier-windows-db-88.png){ width="600" }
</center>

가상디스크 우클릭 > '새 단순 볼륨' 버튼을 클릭합니다.

<center>
![3tier-windows-db-89](../../../assets/images/3tier-windows/3tier-windows-db-89.png){ width="600" }
</center>

가상디스크 우클릭 > '온라인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-90](../../../assets/images/3tier-windows/3tier-windows-db-90.png){ width="600" }
</center>

가상디스크 우클릭 > '디스크 초기화' 버튼을 클릭합니다.

<center>
![3tier-windows-db-91](../../../assets/images/3tier-windows/3tier-windows-db-91.png){ width="600" }
</center>

가상디스크 우클릭 > '새 단순 볼륨' 버튼을 클릭합니다.

<center>
![3tier-windows-db-92](../../../assets/images/3tier-windows/3tier-windows-db-92.png){ width="600" }
</center>

## Failover Cluster 구성(NODE1, NODE2)

Failover Cluster를 통해 클러스터 노드들을 모니터링하여 장애를 감지하고 장애가 발생하면 다른 노드에서 서비스를 제공합니다.

서버 관리자 > 관리 > '역할 및 기능 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-93](../../../assets/images/3tier-windows/3tier-windows-db-93.png){ width="600" }
</center>

역할 및 기능 추가 마법사 페이지에서 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-94](../../../assets/images/3tier-windows/3tier-windows-db-94.png){ width="600" }
</center>

설치 유형을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-95](../../../assets/images/3tier-windows/3tier-windows-db-95.png){ width="600" }
</center>

대상 서버를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-96](../../../assets/images/3tier-windows/3tier-windows-db-96.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-97](../../../assets/images/3tier-windows/3tier-windows-db-97.png){ width="600" }
</center>

서버 기능에서 'Failover Clustering'을 선택합니다.

<center>
![3tier-windows-db-98](../../../assets/images/3tier-windows/3tier-windows-db-98.png){ width="600" }
</center>

'기능 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-99](../../../assets/images/3tier-windows/3tier-windows-db-99.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-100](../../../assets/images/3tier-windows/3tier-windows-db-100.png){ width="600" }
</center>

'설치' 버튼을 클릭합니다.

<center>
![3tier-windows-db-101](../../../assets/images/3tier-windows/3tier-windows-db-101.png){ width="600" }
</center>

'닫기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-102](../../../assets/images/3tier-windows/3tier-windows-db-102.png){ width="600" }
</center>

서버 관리자 > 도구 > '장애 조치 클러스터 관리자'를 클릭합니다.

<center>
![3tier-windows-db-103](../../../assets/images/3tier-windows/3tier-windows-db-103.png){ width="600" }
</center>

'구성의 유효성을 검사' 버튼을 클릭합니다.

<center>
![3tier-windows-db-104](../../../assets/images/3tier-windows/3tier-windows-db-104.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-106](../../../assets/images/3tier-windows/3tier-windows-db-106.png){ width="600" }
</center>

'찾아보기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-107](../../../assets/images/3tier-windows/3tier-windows-db-107.png){ width="600" }
</center>

'고급' 버튼을 클릭합니다.

<center>
![3tier-windows-db-108](../../../assets/images/3tier-windows/3tier-windows-db-108.png){ width="600" }
</center>

'지금 찾기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-109](../../../assets/images/3tier-windows/3tier-windows-db-109.png){ width="600" }
</center>

클러스터를 구성할 노드를 선택하고 '확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-110](../../../assets/images/3tier-windows/3tier-windows-db-110.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-111](../../../assets/images/3tier-windows/3tier-windows-db-111.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-112](../../../assets/images/3tier-windows/3tier-windows-db-112.png){ width="600" }
</center>

테스트 옵션을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-113](../../../assets/images/3tier-windows/3tier-windows-db-113.png){ width="600" }
</center>

테스트 옵션을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-114](../../../assets/images/3tier-windows/3tier-windows-db-114.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-115](../../../assets/images/3tier-windows/3tier-windows-db-115.png){ width="600" }
</center>

'마침' 버튼을 클릭합니다.

<center>
![3tier-windows-db-116](../../../assets/images/3tier-windows/3tier-windows-db-116.png){ width="600" }
</center>

'클러스터 만들기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-117](../../../assets/images/3tier-windows/3tier-windows-db-117.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-118](../../../assets/images/3tier-windows/3tier-windows-db-118.png){ width="600" }
</center>

'찾아보기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-119](../../../assets/images/3tier-windows/3tier-windows-db-119.png){ width="600" }
</center>

'고급' 버튼을 클릭합니다.

<center>
![3tier-windows-db-120](../../../assets/images/3tier-windows/3tier-windows-db-120.png){ width="600" }
</center>

'지금 찾기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-121](../../../assets/images/3tier-windows/3tier-windows-db-121.png){ width="600" }
</center>

클러스터를 구성할 노드를 선택하고 '확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-122](../../../assets/images/3tier-windows/3tier-windows-db-122.png){ width="600" }
</center>

'확인' 버튼을 클릭합니다.

<center>
![3tier-windows-db-123](../../../assets/images/3tier-windows/3tier-windows-db-123.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-124](../../../assets/images/3tier-windows/3tier-windows-db-124.png){ width="600" }
</center>

클러스터 이름을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-125](../../../assets/images/3tier-windows/3tier-windows-db-125.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-126](../../../assets/images/3tier-windows/3tier-windows-db-126.png){ width="600" }
</center>

'마침' 버튼을 클릭합니다.

<center>
![3tier-windows-db-127](../../../assets/images/3tier-windows/3tier-windows-db-127.png){ width="600" }
</center>

서버 관리자 > 관리 > '역할 및 기능 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-93](../../../assets/images/3tier-windows/3tier-windows-db-93.png){ width="600" }
</center>

클러스터에 File Server 역할을 설정하기 위해 클러스터에 참여하는 노드에 역할을 추가합니다. 역할 및 기능 추가 마법사 페이지에서 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-128](../../../assets/images/3tier-windows/3tier-windows-db-128.png){ width="600" }
</center>

설치 유형을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-129](../../../assets/images/3tier-windows/3tier-windows-db-129.png){ width="600" }
</center>

대상 서버를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-130](../../../assets/images/3tier-windows/3tier-windows-db-130.png){ width="600" }
</center>

서버 역할에서 'File Server'를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-131](../../../assets/images/3tier-windows/3tier-windows-db-131.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-132](../../../assets/images/3tier-windows/3tier-windows-db-132.png){ width="600" }
</center>

'설치' 버튼을 클릭합니다.

<center>
![3tier-windows-db-133](../../../assets/images/3tier-windows/3tier-windows-db-133.png){ width="600" }
</center>

'닫기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-134](../../../assets/images/3tier-windows/3tier-windows-db-134.png){ width="600" }
</center>

## MSSQL 설치(NODE1, NODE2)

SQL Server를 설치합니다. NODE1은 'SQL Server 장애 조치(Failover) 클러스터를 새로 설치'를 설치하고, NODE2는 'SQL Server 장애 조치(Failover) 클러스터에 노드 추가'를 설치합니다.

<center>
![3tier-windows-db-135](../../../assets/images/3tier-windows/3tier-windows-db-135.png){ width="600" }
</center>

'사용자 지정'을 클릭합니다.

<center>
![3tier-windows-db-136](../../../assets/images/3tier-windows/3tier-windows-db-136.png){ width="600" }
</center>

'설치' 버튼을 클릭합니다.

<center>
![3tier-windows-db-137](../../../assets/images/3tier-windows/3tier-windows-db-137.png){ width="600" }
</center>

SQL Server 설치 센터에서 '설치'를 클릭합니다.

<center>
![3tier-windows-db-138](../../../assets/images/3tier-windows/3tier-windows-db-138.png){ width="600" }
</center>

'SQL Server 장애 조치(Failover) 클러스터 새로 설치'를 클릭합니다.

<center>
![3tier-windows-db-139](../../../assets/images/3tier-windows/3tier-windows-db-139.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-140](../../../assets/images/3tier-windows/3tier-windows-db-140.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-141](../../../assets/images/3tier-windows/3tier-windows-db-141.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-142](../../../assets/images/3tier-windows/3tier-windows-db-142.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-143](../../../assets/images/3tier-windows/3tier-windows-db-143.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-144](../../../assets/images/3tier-windows/3tier-windows-db-144.png){ width="600" }
</center>

설치할 기능을 선택합니다.

<center>
![3tier-windows-db-145](../../../assets/images/3tier-windows/3tier-windows-db-145.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-146](../../../assets/images/3tier-windows/3tier-windows-db-146.png){ width="600" }
</center>

SQL Server의 네트워크 이름을 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-147](../../../assets/images/3tier-windows/3tier-windows-db-147.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-148](../../../assets/images/3tier-windows/3tier-windows-db-148.png){ width="600" }
</center>

클러스터 디스크를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-149](../../../assets/images/3tier-windows/3tier-windows-db-149.png){ width="600" }
</center>

클러스터 IP를 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-150](../../../assets/images/3tier-windows/3tier-windows-db-150.png){ width="600" }
</center>

서비스 계정의 암호를 입력하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-151](../../../assets/images/3tier-windows/3tier-windows-db-151.png){ width="600" }
</center>

'현재 사용자 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-db-152](../../../assets/images/3tier-windows/3tier-windows-db-152.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-db-153](../../../assets/images/3tier-windows/3tier-windows-db-153.png){ width="600" }
</center>

'설치' 버튼을 클릭합니다.

<center>
![3tier-windows-db-154](../../../assets/images/3tier-windows/3tier-windows-db-154.png){ width="600" }
</center>

'닫기' 버튼을 클릭합니다.

<center>
![3tier-windows-db-155](../../../assets/images/3tier-windows/3tier-windows-db-155.png){ width="600" }
</center>

SQL Server 서비스가 설치되었는지 확인합니다.

<center>
![3tier-windows-db-156](../../../assets/images/3tier-windows/3tier-windows-db-156.png){ width="600" }
</center>

## SSMS 설치(AD-SVR)

Microsoft SQL Server를 관리하기 위해 SSMS(SQL Server Management Studio) 응용 프로그램을 설치합니다.

SSMS를 다운로드합니다.

<center>
![3tier-windows-db-157](../../../assets/images/3tier-windows/3tier-windows-db-157.png){ width="600" }
</center>

'Install' 버튼을 클릭합니다.

<center>
![3tier-windows-db-158](../../../assets/images/3tier-windows/3tier-windows-db-158.png){ width="600" }
</center>

'Restart' 버튼을 클릭합니다.

<center>
![3tier-windows-db-159](../../../assets/images/3tier-windows/3tier-windows-db-159.png){ width="600" }
</center>

SSMS 실행후 접속합니다.

<center>
![3tier-windows-db-160](../../../assets/images/3tier-windows/3tier-windows-db-160.png){ width="600" }
</center>

sql 사용자 계정을 생성합니다. Security > 'New Login'을 클릭합니다.

<center>
![3tier-windows-db-161](../../../assets/images/3tier-windows/3tier-windows-db-161.png){ width="600" }
</center>

sql 사용자 계정의 이름 및 암호를 입력하고 'OK' 버튼을 클릭합니다.

<center>
![3tier-windows-db-162](../../../assets/images/3tier-windows/3tier-windows-db-162.png){ width="600" }
</center>

사용자 계정이 생성됩니다.

<center>
![3tier-windows-db-162](../../../assets/images/3tier-windows/3tier-windows-db-162.png){ width="600" }
</center>

## 샘플코드 스키마 실행

NodeJS 샘플코드 작동을 위해 관련 스키마를 실행합니다.

``` 
-- create database
CREATE DATABASE testdb;

-- create table
create table member
(
idx int IDENTITY(1,1) primary key,
userid varchar(255) not null,
password varchar(255) not null,
email text null,
salt varchar(255) null
);
```