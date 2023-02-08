ABLESTACK Mold를 이용한 "이중화를 통한 고가용성 기능을 제공하는 3계층 구조" 구성 단계 중, 네 번째 단계인 WEB 구성에 대한 문서입니다.

WEB 서버의 이중화 구성은 NodeJS와 SMB 스토리지를 활용하며 구성하는 단계는 다음과 같은 절차로 실행됩니다.

- 가상머신 생성
- 데이터 디스크 설정
- SMB 구성 및 공유폴더 설정(SMB-SVR)
- NginX 설치 및 설정(NODE1, NODE2)
- 로드 밸런서(부하 분산) 설정

## 가상머신 생성

ABLESTACK Mold는 기본적으로 템플릿을 이용해 가상머신을 생성하고 사용하는 것을 권장합니다. 먼저 Windows 기반의 가상머신 템플릿 이미지를 생성하여 등록하는 절차를 수행한 후 VM을 생성해야 합니다.

가상머신을 추가하기 위해 **컴퓨트 > 가상머신** 화면으로 이동하여 **가상머신 추가** 버튼을 클릭합니다. "새 가상머신" 마법사 페이지가 표시됩니다. 해당 페이지에서는 "템플릿을 이용한 VM 생성" 문서를 참고하여 가상머신을 생성합니다.

!!! info "템플릿을 이용한 VM 생성"
    템플릿을 이용한 가상머신 추가를 위해 [템플릿을 이용한 VM 생성](../../../vms/windows-guide-add-and-use-vm#vm) 문서를 참고하십시오.

- SMB 가상머신(SMB-SVR)

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Windows Server 2022 기본 이미지 템플릿**
    - 컴퓨트 오퍼링 : **2C-4GB-RBD-HA**
    - 데이터 디스크 : **50GB-WB-RBD**
    - 네트워크 : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.61
    - 이름 : **Windows-3tier-web-smb-svr**

- WEB 가상머신 1(NODE1)

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Windows Server 2022 기본 이미지 템플릿**
    - 컴퓨트 오퍼링 : **2C-4GB-RBD-HA**
    - 네트워크1(통신용) : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.62
    - 이름 : **Windows-3tier-web-node01**

- WEB 가상머신 2(NODE2)

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **Windows Server 2022 기본 이미지 템플릿**
    - 컴퓨트 오퍼링 : **2C-4GB-RBD-HA**
    - 네트워크1(통신용) : **사용자가이드용-격리네트워크**
        - IP: 10.1.1.63
    - 이름 : **Windows-3tier-web-node02**

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

## SMB 구성 및 공유폴더 설정(SMB-SVR)

다른 시스템에서 디스크나 프린터 등의 자원을 공유하기 위해 SMB를 구성하고 해당 서버에 접근할 수 있도록 공유폴더로 설정합니다.

SMB 구성을 위해 서버 관리자 > 관리 > '역할 및 기능 추가' 버튼을 클릭합니다.

<center>
![3tier-windows-was-1](../../../assets/images/3tier-windows/3tier-windows-was-1.png){ width="600" }
</center>

설치 유형을 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-was-2](../../../assets/images/3tier-windows/3tier-windows-was-2.png){ width="600" }
</center>

대상 서버를 선택하고 '다음' 버튼을 클릭합니다.

<center>
![3tier-windows-was-3](../../../assets/images/3tier-windows/3tier-windows-was-3.png){ width="600" }
</center>

'다음' 버튼을 클릭합니다.

<center>
![3tier-windows-was-4](../../../assets/images/3tier-windows/3tier-windows-was-4.png){ width="600" }
</center>

서버 기능에서 'SMB 1.0/CIFS File Sharing Support'를 선택합니다.

<center>
![3tier-windows-was-5](../../../assets/images/3tier-windows/3tier-windows-was-5.png){ width="600" }
</center>

폴더 공유를 위해 제어판 > 고급 공유 설정을 선택합니다.

<center>
![3tier-windows-was-6](../../../assets/images/3tier-windows/3tier-windows-was-6.png){ width="600" }
</center>

Function Discovery Resource Publication 서비스 상태를 확인합니다.

<center>
![3tier-windows-was-7](../../../assets/images/3tier-windows/3tier-windows-was-7.png){ width="600" }
</center>

서비스 우클릭 > 시작 유형을 '자동'으로 선택하고 '확인' 버튼을 클릭합니다.

<center>
![3tier-windows-was-8](../../../assets/images/3tier-windows/3tier-windows-was-8.png){ width="600" }
</center>

공유 폴더를 생성할 드라이버를 선택하여 우클릭 > 새로 만들기 > 폴더를 클릭합니다.

<center>
![3tier-windows-was-9](../../../assets/images/3tier-windows/3tier-windows-was-9.png){ width="600" }
</center>

폴더이름을 변경합니다.

<center>
![3tier-windows-was-10](../../../assets/images/3tier-windows/3tier-windows-was-10.png){ width="600" }
</center>

폴더 우클릭 > '공유' 버튼을 클릭합니다.
<center>
![3tier-windows-was-11](../../../assets/images/3tier-windows/3tier-windows-was-11.png){ width="600" }
</center>

폴더를 공유할 사용자를 입력하고 '추가' 버튼을 클릭합니다.

<center>
![3tier-windows-was-12](../../../assets/images/3tier-windows/3tier-windows-was-12.png){ width="600" }
</center>

'공유' 버튼을 클릭합니다.

<center>
![3tier-windows-was-13](../../../assets/images/3tier-windows/3tier-windows-was-13.png){ width="600" }
</center>

'완료' 버튼을 클릭합니다.

<center>
![3tier-windows-was-14](../../../assets/images/3tier-windows/3tier-windows-was-14.png){ width="600" }
</center>

NODE1, NODE2에서 공유폴더의 주소를 입력하여 공유된 것을 볼수있습니다.(컴퓨터이름 또는 서버IP)

<center>
![3tier-windows-was-15](../../../assets/images/3tier-windows/3tier-windows-was-15.png){ width="600" }
</center>

공유폴더가 나타납니다.

<center>
![3tier-windows-was-16](../../../assets/images/3tier-windows/3tier-windows-was-16.png){ width="600" }
</center>

## NginX 설치(NODE1, NODE2)

클라이언트 요청을 받아 웹서버를 실행하도록 NginX를 설치합니다.

NginX를 다운로드 및 설치합니다.

<center>
![3tier-windows-web-1](../../../assets/images/3tier-windows/3tier-windows-web-1.png){ width="600" }
</center>

Nginx 설정정보를 변경하고 서비스를 재실행합니다.

<center>
![3tier-windows-web-3](../../../assets/images/3tier-windows/3tier-windows-web-3.png){ width="600" }
</center>

## 로드 밸런서(부하 분산) 설정

Mold 사용자 또는 관리자는 Public IP에서 수신된 트래픽을 하나 이상의 VM에 분산시키는 부하 분산 규칙을 만들 수 있습니다. 사용자는 규칙을 만들고 알고리즘을 지정하며 VM 집합에 규칙을 할당합니다.

!!! info "로드 밸런서 규칙 추가"
    로드 밸런서 규칙 추가를 위해 [로드 밸런서 규칙 추가](../../../../administration/mold/network&traffic-mngt-guide#_23) 문서를 참고하십시오.

다음과 같은 규칙으로 부하분산을 설정합니다.

- 부하분산 규칙

    - 이름 : **windows-web**
    - Public 포트 : **3000**
    - 사설 포트 : **3000**
    - 알고리즘 : **Round-robin**
    - 프로토콜 : **TCP**
    - 가상머신 추가 : **Windows-3tier-web-node01**, **Windows-3tier-web-node02**

<center>
![3tier-windows-web-4](../../../assets/images/3tier-windows/3tier-windows-web-4.png){ width="600" }
</center>