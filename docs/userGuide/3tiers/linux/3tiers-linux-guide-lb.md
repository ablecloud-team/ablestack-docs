ABLESTACK Mold를 이용한 **이중화를 통한 고가용성 기능을 제공하는 리눅스 기반의 3계층 구조** 의를 구성하기 위한 단계 중, 5 단계인 LB 구성에 대한 문서입니다.

1. VPC 및 서브넷 생성: VPC(Virtual Private Cloud)를 생성하고 서브넷(Subnet)을 생성합니다.
2. 가상머신 생성: 생성된 서브넷에서 WEB, WAS, DB 각각 3대(총 9대)의 가상머신을 SSHKeyPair 및 Affinity을 설정하여 추가합니다.
3. 티어 구성 준비: 생성된 가상머신의 터미널에 접속하고 데이터 디스크 볼륨 구성을 합니다.
4. 티어 별 WEB, WAS, DB 구성:
      1. DB: 갈레라 클러스터(Galera Cluster)를 활용하여 동기 방식의 복제구조를 사용하는 멀티마스터 DB를 구성합니다.
      2. WAS: 도커 컨테이너를 이용하여 NodeJS와 Samba 스토리지를 활용한 WAS를 구성합니다.
      3. WEB: 도커 컨테이너를 이용하여 Nginx와 NFS 스토리지를 활용한 WEB를 구성합니다.
5. ==LB 구성: 하나의 Public IP를 생성하여 동일 서브넷 상의 VM들의 이중화를 위해 LB를 구성합니다.==

## 로드 밸런서 추가
각 WEB, WAS, DB Node에 대해 ABLESTACK Mold에서 제공하는 부하분산(로드 밸런서)를 설정하면 Health Check를 통해 장애 여부를 판단하고 노드에 이상이 발생하면 다른 정상 동작중인 노드로 트래픽을 보내주는 Fail-over가 가능합니다. 
이를 위해 VPC에 Public IP 할당하여 외부 부하분산을 설정합니다.

### VPC에 Public IP 할당
구성한 VPC에 Public IP를 할당하여 외부에서 접속할 수 있도록 합니다.
`네트워크 > VPC` 화면으로 이동한 후, 아래 문서를 참고하여 Public IP를 할당합니다.

!!! info "VPC에 대한 새 Public IP 주소 획득"
    - VPC에 Public IP 할당하기 위해 [VPC에 대한 새 Public IP 주소 획득](../../../../administration/mold/network&traffic-mngt-guide#vpc-public-ip) 문서를 참고하십시오.

### 할당받은 Public IP에 부하 분산 추가
할당받은 Public IP를 선택한 후 `부하 분산` 탭을 클릭한 후, 아래 문서를 참고하여 부하 분산을 설정합니다.

!!! info "외부 LB 설정"
    - 할당받은 Public IP에 내부 부하 분산 기능을 설정하기위해 [외부 LB 규칙 생성](../../../../administration/mold/network&traffic-mngt-guide#vpc_2) 문서를 참고하십시오.

부하 분산 설정에서의 입력 항목 예제는 다음과 같습니다.

   1. 이름: `db-lb`
   2. Public 포트: `3306`
   3. 사설 포트: `3306`
   4. 전송원 CIDR: # 디폴트 값을 입력합니다.
   5. 알고리즘: `최소 접속`
   6. 프로토콜: `TCP`
   7. AutoScale: `아니오`
   8. 가상머신 추가: # 서브넷을 선택한 후, VM을 선택합니다.
          ![3tier-linux-architecture-lb-01](../../../../assets/images/3tier-linux-architecture-lb-01.png)

