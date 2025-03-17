펜싱(Fencing)은 Pacemaker 및 HA(고가용성) 클러스터에서 예기치 않게 작동하거나 응답하지 않는 노드를 격리하거나 전원을 종료하여 split-brain 현상을 방지하는 메커니즘을 말합니다. PCS(Pacemaker Cluster Suite)는 Linux에서 고가용성 클러스터를 관리하고 구성하는 도구로써, 클러스터의 안정성과 일관성을 보장하기 위한 기능을 제공합니다.

PCS에서 작동되는 MOLD Fencing Agent(Fence_mold)은 MOLD의 가상머신에 대한 펜싱 기능을 제공하기 위해 개발되었으며 기존 사용되었던 Fence_ipmilan(IPMI 인터페이스)의 아래 명시된 문제점을 극복하기 위해 개발 되었습니다.

  - Mold에서 가상머신 정지 사유를 알지 못하여 Compute Offering 옵션 중 HA옵션을 사용할 수 없습니다.
  - 가상머신이 운영중인 호스트에서 vbmc 포트포워딩으로 인해 해당 가상머신을 다른 호스트로 마이그레이션을 할 수 없습니다.

이와 같은 이유로 Mold에서 위 문제점을 해결 할 수 있는 Mold 용 Fencing Agent를 사용합니다.

## 구성도
Mysql 이중화를 위해 MOLD에서 제공하는 Shared Volume으로 구성된 Linux 환경의 2개의 가상머신을 생성하고 PCS 클러스터를 구성합니다. Node1에서 VIP, Shared Volume의 리소스 소유권을 가지며 Node1이 fencing 처리 될 경우 해당 리소스의 소유권은 Node2로 이전되는 구조입니다.
또한 MOLD Agent는 fencing 기능을 수행하기 위해 MOLD와 통신합니다. 
![rac-prepare](../../../../assets/images/fence_mold/fence-mold-architecture.png){: .center }

## 전제조건
- 가상머신과 Mold간의 통신이 가능해야 합니다.
- 가상머신과 가상머신가의 통신이 가능해야 합니다.
- 해당 Agent는 pcs cluster구성을 이용한 fence agent로 Linux 에서만 사용이 가능합니다.

## 구성요소
### Fencing Agent (Mold Agent)
- 공유 데이터의 무결성을 보장하기 위해 장애가 발생한 노드를 비활성화시키는 기능을 합니다.
- MOLD와 통신하여 장애가 발생한 가상머신을 정상적으로 종료시켜 공유 볼륨과 차단합니다. 

### Shared Volume
- Shared Volume은 Mysql Database File을 모든 Node가 공유할 수 있는 공간입니다. 이 때 Shared Volume에 대한 액세스는 PCS 클러스터에 의해 한 Node만 가능하도록 통제됩니다.

### Virtual IP (VIP)
- PCS에서 관리하는 가상 IP를 말하며 클러스터의 다른 노드로 장애 조치되는 경우에도 클라이언트가 항상 Mysql과 같은 서비스에 연결할 수 있도록 하는 데 사용됩니다.

## 구성 단계
Linux 환경에서의 Pacemaker와 Mold fence agent를 이용한 Mysql 이중화를 구성하는 단계는 다음과 같습니다.

1. 구성 환경
2. Pacemaker 클러스터 구성
3. Shared Volume를 활용한 Mysql 구성
4. MOLD Fence Agent 설치 및 STONITH 구성
5. Mysql 이중화를 위한 PCS Resource 구성

