# 시작하기
ABLESTACK을 설치하기 위해서는 ABLESTACK의 아키텍처를 알고 있어야 합니다.

- [ABLESTACK 기본구조](../architecture/ablestack-basic-structure.md)  
- [호스트 아키텍처](../architecture/host-architecture.md)  
- [네트워크 아키텍처](../architecture/network-architecture.md)  

## 사전준비 사항
ABLESTACK을 설치하고 구성하기 위해서는 다음과 같은 구성 요소들이 사전에 준비되어 있어야 합니다

- ABLESTACK이 설치될 최소 3식의 x86 기반의 호스트 서버가 준비 되어 있어야 합니다.
- 서버간 네트워크 연결을 위한 10G 스위치 및 10G 용 케이블이 준비 되어 있어야 합니다.

## 설치 전 확인 사항
- 호스트와 스위치간의 네트워크 연결이 정상적으로 되어 있어야 합니다.
- 스위치의 MTU설정은 최소 9000이상으로 셋팅 되어 있어야 합니다.

!!! 주의사항 Warning
    호스트와 스위치 연결한 Port의 램프가 정상 상태인지 확인을 해야하며, 호스트에 ABLESTACK을 구성하기 전에 스위치의 Glue Network(Cluster, Server, Client) Port는 MTU 9000이상 셋팅이 되여 있어야 합니다.

!!! 팁 Tip
    ABLESTACK구성시 스위치의 MTU 설정은 9000으로 맞춰서 설정하기보다 스위치에서 허용하는 최대의 MTU 설정할 수 있도록 권장하고 있습니다.

!!! 팁 Tip
    ABLESTACK구성시 3대의 호스트의 IPMI를 스위치에 연결 한 후에 노트북을 이용하여 각 호스트의 IPMI에 접속하여 콘솔을 이용하면 조금더 쉽게 설치를 할 수 있습니다.

## 설치 절차 요약
설치를 위한 물리적인 구성이 완료되었다면 다음과 같은 절차에 의하여 ABLESTACK 설치를 시작합니다.  
1. [ABLESTACK Cube 설치 진행](./install-guide-cube.md)  
2. [ABLESTACK Cell 설치 진행](./install-guide-cell.md)  
3. [ABLESTACK Glue 설치 진행](./install-guide-glue.md)  
4. [ABLESTACK Mold 설치 진행](./install-guide-mold.md)