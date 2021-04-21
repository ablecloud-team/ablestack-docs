# GLUE 사용자 인터페이스

## 개요


GLUE는 웹 기반 분산 스토리지 관리/모니터링 서비스입니다.

본 서비스는 CherryPy framework와 REST API를 백엔드로 사용하며, Angular/TypeScript를 사용하여 WebUI를 제작하였습니다.

접속하는 URL은 다음과 같습니다.

 ``` 
  https://SCVM ip:8443 
 ```
!!! tip
    클러스터링된 모든 scvm을 통하여 접속할 수 있으며 /etc/hosts 파일을 참조하여 IP를 알 수 있습니다.

![glue-login-webui](../../assets/images/glue_login_webUI.png)


### 제공하는 기능

GLUE는 다음과 같은 기능을 제공합니다.

-   **다중 사용자 및 역할 관리**: GLUE는 여러 사용자에게 각기 다른 권한(역할)을 제공합니다.
    사용자 계정과 역할은 WebUI를 통해 관리 됩니다. GLUE는 암호 보안을 위해 여려가지 방식을 제공합니다. 암호 복잡성규칙, 초기 로그인후 암호변경, 암호의 기간제한등
    자세한 내용은 [사용자 역할 관리]() 메뉴얼을 참조하세요.
-   **SSL/TLS 지원**: GLUE와 브라우저간의 모든 HTTP통신은 SSL을 통해 암호화됩니다. 기본적으로 자체 서명 인증서를 사용하지만, CA를 통해 서명된 인증서를
    불러올 수 있습니다. 자세한 내용은 [SSL-TLS지원]()을 참조하세요
-   **감사**: GLUE는 모든 `PUT`, `POST`, `DELETE` API 요청에 대해 감사기록을 남길 수 있습니다.
    설정방법은 [`GLUE-auditing`]() 문서를 참고하세요.
-   **다국어화 (I18N)**: 실행중 GLUE의 언어를 변경할 수 있습니다.

GLUE 는 다음과 같은 관리/모니터링 기능을 제공합니다.

-   **전체 클러스터의 상태**: 성능과 용량, 그리고 클러스터의 작동 상태에 대해 표시합니다.
-   **Grafana 대시보드**: `mgr-prometheus` 모듈을 사용해 외부 어플리케이션/웹페이지에 GLUE의 상태를 포함시킬 수 있습니다.
    자세한 내용은 [`GLUE-grafana`]()을 참고하세요.
-   **클러스터 로그**: 클러스터의 최근 활동과 감사이력을 기록합니다. 로그는 중요도, 날짜, 키워드로 필터링이 가능합니다.
-   **호스트**: 클러스터에 소속된 호스트와 디스크드라이브, 작동중인 서비스에 대한 정보를 표시합니다.
-   **성능 카운터**: 동작중인 각 서비스별 상세한 통계를 보여줍니다.
-   **모니터**: 모든 스토리지 모니터와 열린 세션, quorum(정족수) 상태를 보여줍니다.
-   **모니터링**: Prometheus를 사용하여 경고를 생성, 수정, 삭제등을 진행하고 발생한 경고를 표시합니다.
-   **설정 편집기**: 모든 사용가능한 설정과 그것에 대한 설명, 타입, 기본값 그리고 현재 설정된 값을 보여주고, 수정합니다.
-   **Pools**: 모든 스토리지풀의 목록과 상세내용을 보여줍니다. (배치그룹, 복제 크기, CRUSH 규칙, 제한량등)
-   **OSDs**: OSD의 목록과 상태, 사용통계와 상세 정보들을 보여줍니다. 상세정보에는 속성, 메타데이터, 성능통계, 읽기/쓰기 사용량 그래프등이 있습니다.
    또한, OSD를 up/down/out 시키거나 삭제, 가중치 변경, 정합성 검사등의 설정 작업도 가능합니다.
    OSD에 연결된 드라이브의 목록을 보거나, OSD의 클래스를 지정하고, 정렬해서 볼 수 있으며, 새로운 드라이브와 호스트를 배포할 수도 있습니다.
-   **장치 관리**: orchestrator에 알려진 모든 호스트와, 해당 호스트에 연결된 모든 드라이브를 표시합니다.
    각 드라이브의 SMART 데이터등의 성능상태를 확인하고, 디스크의 LED를 제어해 물리적인 드라이브를 찾을 수도 있습니다.,
-   **iSCSI**: List all hosts that run the TCMU runner service, display
    all images and their performance characteristics (read/write ops,
    traffic). Create, modify, and delete iSCSI targets (via
    `ceph-iscsi`). Display the iSCSI gateway status and info about
    active initiators. See :ref:`GLUE-iscsi-management` for
    instructions on how to configure this feature.
-   **RBD**: List all RBD images and their properties (size, objects,
    features). Create, copy, modify and delete RBD images (incl.
    snapshots) and manage RBD namespaces. Define various I/O or
    bandwidth limitation settings on a global, per-pool or per-image
    level. Create, delete and rollback snapshots of selected images,
    protect/unprotect these snapshots against modification. Copy or
    clone snapshots, flatten cloned images.
-   **RBD mirroring**: Enable and configure RBD mirroring to a remote
    Ceph server. List active daemons and their status, pools and RBD
    images including sync progress.
-   **CephFS**: List active file system clients and associated pools,
    including usage statistics. Evict active CephFS clients. Manage
    CephFS quotas and snapshots. Browse a CephFS directory structure.
-   **Object Gateway**: List all active object gateways and their
    performance counters. Display and manage (add/edit/delete) object
    gateway users and their details (e.g. quotas) as well as the users'
    buckets and their details (e.g. placement targets, owner, quotas,
    versioning, multi-factor authentication). See
    :ref:`GLUE-enabling-object-gateway` for configuration
    instructions.
-   **NFS**: Manage NFS exports of CephFS file systems and RGW S3
    buckets via NFS Ganesha. See :ref:`GLUE-nfs-ganesha-management`
    for details on how to enable this functionality.
-   **Ceph Manager Modules**: Enable and disable Ceph Manager modules,
    manage module-specific configuration settings.

### Overview of the GLUE Landing Page


Displays overall cluster status, performance, and capacity metrics.
Shows instant feedback for changes in the cluster and provides easy
access to subpages of the GLUE.

#### Status

-   **Cluster Status**: Displays overall cluster health. In case of any
    error it displays a short description of the error and provides a
    link to the logs.
-   **Hosts**: Displays the total number of hosts associated to the
    cluster and links to a subpage that lists and describes each.
-   **Monitors**: Displays mons and their quorum status and open
    sessions. Links to a subpage that lists and describes each.
-   **OSDs**: Displays object storage daemons (ceph-osds) and the
    numbers of OSDs running (up), in service (in), and out of the
    cluster (out). Provides links to subpages providing a list of all
    OSDs and related management actions.
-   **Managers**: Displays active and standby Ceph Manager daemons
    (ceph-mgr).
-   **Object Gateway**: Displays active object gateways (RGWs) and
    provides links to subpages that list all object gateway daemons.
-   **Metadata Servers**: Displays active and standby CephFS metadata
    service daemons (ceph-mds).
-   **iSCSI Gateways**: Display iSCSI gateways available, active (up),
    and inactive (down). Provides a link to a subpage showing a list of
    all iSCSI Gateways.


#### Capacity

-   **Raw Capacity**: Displays the capacity used out of the total
    physical capacity provided by storage nodes (OSDs).
-   **Objects**: Displays the number and status of RADOS objects
    including the percentages of healthy, misplaced, degraded, and
    unfound objects.
-   **PG Status**: Displays the total number of placement groups and
    their status, including the percentage clean, working, warning, and
    unknown.
-   **Pools**: Displays pools and links to a subpage listing details.
-   **PGs per OSD**: Displays the number of placement groups assigned to
    object storage daemons.

#### Performance

-   **Client READ/Write**: Displays an overview of client input and
    output operations.
-   **Client Throughput**: Displays the data transfer rates to and from
    Ceph clients.
-   **Recovery throughput**: Displays rate of cluster healing and
    balancing operations.
-   **Scrubbing**: Displays light and deep scrub status.

### Supported Browsers


Ceph GLUE is primarily tested and developed using the following web
browsers:

<table>
<col style="width: 61%;" />
<col style="width: 38%;" />
<thead>
<tr class="header">
<th style="text-align: left;">Browser</th>
<th style="text-align: left;">Versions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p><code>Chrome &lt;https://www.google.com/chrome/&gt;</code>_ and <code>Chromium &lt;https://www.chromium.org/&gt;</code>_ based browsers</p></td>
<td style="text-align: left;"><p>latest 2 major versions</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p><code>Firefox &lt;https://www.mozilla.org/firefox/&gt;</code>_</p></td>
<td style="text-align: left;"><p>latest 2 major versions</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p><code>Firefox ESR &lt;https://www.mozilla.org/firefox/enterprise/&gt;</code>_</p></td>
<td style="text-align: left;"><p>latest major version</p></td>
</tr>
</tbody>
</table>

While Ceph GLUE might work in older browsers, we cannot guarantee
compatibility and recommend keeping your browser up to date.

