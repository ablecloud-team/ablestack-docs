# NFS-Ganesha 관리 

Glue 대시보드는 CephFS 또는 RGW를 백 스토어로 사용하는 NFS Ganesha 내보내기를 관리할 수 ​​있습니다. Glue 대시보드에서이 기능을 활성화하려면 NFS-Ganesha 서비스가 구성되는 방식과 관련하여 충족 되어야하는 몇 가지 가정이 있습니다.

대시 보드는 Ceph 클러스터의 RADOS 개체에 저장된 NFS-Ganesha 구성 파일을 관리합니다. NFS-Ganesha는 구성의 일부를 Ceph 클러스터에 저장해야합니다.

이러한 구성 파일은 아래 규칙을 따릅니다.

각 내보내기 블록은 export-<id\>라는 자체 RADOS 개체에 저장되어야합니다. <id\>는 내보내기 구성의 Export_ID 속성과 일치해야합니다. 그리고 각 NFS-Ganesha 서비스 데몬은 conf-<daemon_id\>라는 RADOS 개체가 있어야합니다. <daemon_id\>는 데몬 인스턴스를 고유하게 식별해야하는 임의의 문자열입니다 (예: 데몬이 실행중인 호스트 이름). 각 conf-<daemon_id\> 개체에는 NFS-Ganesha 데몬이 제공해야 하는 내보내기에 대한 RADOS URL이 포함 되어 있습니다.

이러한 URL은 다음과 같은 형식입니다.
!!! info "URL 형식"
    %url rados://<pool_name\>[/<namespace\>]/export-<id\>

conf-<daemon_id\>및 export-<id\>개체는 모두 동일한 RADOS 풀/네임 스페이스에 저장되어야합니다.


## 대시보드에서 NFS-Ganesha 구성
Glue 대시보드에서 NFS-Ganesha 내보내기를 관리하려면 대시보드는 구성 개체가 저장된 RADOS 풀과 네임 스페이스를 알아야 합니다. 그러면 Glue 대시보드는 위에 설명 된 명명 규칙에 따라 액세스 할 수 있습니다.

NFS-Ganesha 객체 위치를 구성하는 대시보드 명령은 다음과 같습니다.
???+ example "NFS-Ganesha 객체 위치 구성"
    ceph dashboard set-ganesha-clusters-rados-pool-namespace <pool_name\>[/<namespace\>]

위의 명령을 실행하면 Glue 대시보드는 NFS-Ganesha 구성 개체를 찾을 수 있으며 웹 UI를 통해 내보내기를 관리 할 수 ​​있습니다.
???+ tip
    NFS 공유를 위한 전용 풀을 사용해야 합니다.
    
    그렇지 않고 NFS 개체가 단일 풀에 많은 다른 개체와 함께 저장되는 경우에는 공유 목록에 문제가 발생할 수 있습니다.

## 여러 NFS-Ganesha 클러스터 지원
Glue 대시보드는 다른 NFS-Ganesha 클러스터에 속하는 NFS-Ganesha 내보내기 관리도 지원합니다.
NFS-Ganesha 클러스터는 동일한 내보내기를 공유하는 NFS-Ganesha 서비스 데몬 그룹입니다. NFS-Ganesha 클러스터는 독립적이며 서로 내보내기 구성을 공유하지 않습니다.

각 NFS-Ganesha 클러스터는 고유 한 RADOS 풀 / 네임 스페이스에 구성 개체를 저장하여 구성을 격리해야합니다.

각 NFS-Ganesha 클러스터의 구성 위치를 지정하기 위해 위와 동일한 명령을 사용하지만 다른 값 패턴을 사용할 수 있습니다.
???+ example "다른 패턴 값을 사용하여 구성"

    ceph dashboard set-ganesha-clusters-rados-pool-namespace <cluster_id\>:<pool_name\>[/<namespace\>]\(,<cluster_id\>:<pool_name\>[/<namespace\>])*

<cluster_id\>는 NFS-Ganesha 클러스터를 고유하게 식별해야 하는 임의의 문자열입니다.
여러 NFS-Ganesha 클러스터로 Glue 대시보드를 구성 할 때 웹 UI를 통해 내보내기가 속한 클러스터를 선택할 수 있습니다.

## ORCHESTRATOR에서 배포한 NFS-GANESHA 클러스터 지원
Glue 대시보드는 Orchestrator에서 배포 한 NFS-Ganesha 클러스터를 관리하는 데 사용할 수 있으며 자동으로 감지합니다.

Orchestrator를 사용하여 NFS-Ganesha 클러스터를 배포하는 방법에 대한 자세한 내용은 Stateless 서비스 (MDS/RGW/NFS/rbd-mirror/iSCSI)를 참조하세요.

특히, Cephadm 백엔드를 사용하여 NFS-Ganesha 클러스터를 배포하는 방법은 NFS Ganesha 배포를 참조하시기 바랍니다.