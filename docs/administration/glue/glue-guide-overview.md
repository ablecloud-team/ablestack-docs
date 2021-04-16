# GLUE


## 개요


GLUE는 웹 기반 분산 스토리지 관리/모니터링 서비스입니다.

본 서비스는 CherryPy framework와 REST API를 백엔드로 사용하며, Angular/TypeScript를 사용하여 WebUI를 제작하였습니다.

### 제공하는 기능

GLUE는 다음과 같은 기능을 제공합니다.

-   **다중 사용자 및 역할 관리**: GLUE는 여러 사용자에게 각기 다른 권한(역할)을 제공합니다.
    사용자 계정과 역할은 WebUI를 통해 관리 됩니다. GLUE는 암호 보안을 위해 여려가지 방식을 제공합니다. 암호 복잡성규칙, 초기 로그인후 암호변경, 암호의 기간제한등
    자세한 내용은 [[사용자 역할 관리]] 메뉴얼을 참조하세요.
-   **SSL/TLS 지원**: GLUE와 브라우저간의 모든 HTTP통신은 SSL을 통해 암호화됩니다. 기본적으로 자체 서명 인증서를 사용하지만, CA를 통해 서명된 인증서를
    불러올 수 있습니다. 자세한 내용은 [[SSL-TLS지원]]을 참조하세요
-   **Auditing**: The GLUE backend can be configured to log all
    `PUT`, `POST` and `DELETE` API requests in the Ceph audit log. See
    :ref:`GLUE-auditing` for instructions on how to enable this
    feature.
-   **Internationalization (I18N)**: The language used for GLUE
    text can be selected at run-time.

The Ceph GLUE offers the following monitoring and management
capabilities:

-   **Overall cluster health**: Display performance and capacity metrics
    as well as cluster status.
-   **Embedded Grafana GLUEs**: Ceph GLUE `Grafana`\_
    GLUEs may be embedded in external applications and web pages to
    surface information and performance metrics gathered by the
    :ref:`mgr-prometheus` module. See :ref:`GLUE-grafana` for
    details on how to configure this functionality.
-   **Cluster logs**: Display the latest updates to the cluster's event
    and audit log files. Log entries can be filtered by priority, date
    or keyword.
-   **Hosts**: Display a list of all cluster hosts along with their
    storage drives, which services are running, and which version of
    Ceph is installed.
-   **Performance counters**: Display detailed service-specific
    statistics for each running service.
-   **Monitors**: List all Mons, their quorum status, and open sessions.
-   **Monitoring**: Enable creation, re-creation, editing, and
    expiration of Prometheus' silences, list the alerting configuration
    and all configured and firing alerts. Show notifications for firing
    alerts.
-   **Configuration Editor**: Display all available configuration
    options, their descriptions, types, default and currently set
    values. These may be edited as well.
-   **Pools**: List Ceph pools and their details (e.g. applications,
    pg-autoscaling, placement groups, replication size, EC profile,
    CRUSH rulesets, quotas etc.)
-   **OSDs**: List OSDs, their status and usage statistics as well as
    detailed information like attributes (OSD map), metadata,
    performance counters and usage histograms for read/write operations.
    Mark OSDs up/down/out, purge and reweight OSDs, perform scrub
    operations, modify various scrub-related configuration options,
    select profiles to adjust the level of backfilling activity. List
    all drives associated with an OSD. Set and change the device class
    of an OSD, display and sort OSDs by device class. Deploy OSDs on new
    drives and hosts.
-   **Device management**: List all hosts known by the orchestrator.
    List all drives attached to a host and their properties. Display
    drive health predictions and SMART data. Blink enclosure LEDs.
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

Overview of the GLUE Landing Page
<sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup><sup>\^</sup></sup>\^

Displays overall cluster status, performance, and capacity metrics.
Shows instant feedback for changes in the cluster and provides easy
access to subpages of the GLUE.

.. \_GLUE-landing-page-status:

Status """"""

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

.. \_GLUE-landing-page-capacity:

Capacity """"""""

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

.. \_GLUE-landing-page-performance:

Performance """""""""""

-   **Client READ/Write**: Displays an overview of client input and
    output operations.
-   **Client Throughput**: Displays the data transfer rates to and from
    Ceph clients.
-   **Recovery throughput**: Displays rate of cluster healing and
    balancing operations.
-   **Scrubbing**: Displays light and deep scrub status.

Supported Browsers
<sup><sup>\^</sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup>\^\^

Ceph GLUE is primarily tested and developed using the following web
browsers:

<table>
<col width="61%" />
<col width="38%" />
<thead>
<tr class="header">
<th align="left">Browser</th>
<th align="left">Versions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><code>Chrome &lt;https://www.google.com/chrome/&gt;</code>_ and <code>Chromium &lt;https://www.chromium.org/&gt;</code>_ based browsers</p></td>
<td align="left"><p>latest 2 major versions</p></td>
</tr>
<tr class="even">
<td align="left"><p><code>Firefox &lt;https://www.mozilla.org/firefox/&gt;</code>_</p></td>
<td align="left"><p>latest 2 major versions</p></td>
</tr>
<tr class="odd">
<td align="left"><p><code>Firefox ESR &lt;https://www.mozilla.org/firefox/enterprise/&gt;</code>_</p></td>
<td align="left"><p>latest major version</p></td>
</tr>
</tbody>
</table>

While Ceph GLUE might work in older browsers, we cannot guarantee
compatibility and recommend keeping your browser up to date.

Enabling
--------

If you have installed `ceph-mgr-GLUE` from distribution packages,
the package management system should take care of installing all
required dependencies.

If you're building Ceph from source and want to start the GLUE from
your development environment, please see the files `README.rst` and
`HACKING.rst` in the source directory `src/pybind/mgr/GLUE`.

Within a running Ceph cluster, the Ceph GLUE is enabled with::

\$ ceph mgr module enable GLUE

Configuration
-------------

.. \_GLUE-ssl-tls-support:

SSL/TLS Support
<sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>

All HTTP connections to the GLUE are secured with SSL/TLS by
default.

To get the GLUE up and running quickly, you can generate and
install a self-signed certificate::

\$ ceph GLUE create-self-signed-cert

Note that most web browsers will complain about self-signed certificates
and require explicit confirmation before establishing a secure
connection to the GLUE.

To properly secure a deployment and to remove the warning, a certificate
that is issued by a certificate authority (CA) should be used.

For example, a key pair can be generated with a command similar to::

\$ openssl req -new -nodes -x509  
-subj "/O=IT/CN=ceph-mgr-GLUE" -days 3650  
-keyout GLUE.key -out GLUE.crt -extensions v3\_ca

The `GLUE.crt` file should then be signed by a CA. Once that is
done, you can enable it for Ceph manager instances by running the
following commands::

\$ ceph GLUE set-ssl-certificate -i GLUE.crt \$ ceph GLUE
set-ssl-certificate-key -i GLUE.key

If unique certificates are desired for each manager instance, the name
of the instance can be included as follows (where `$name` is the name of
the `ceph-mgr` instance, usually the hostname)::

\$ ceph GLUE set-ssl-certificate
*n**a**m**e* − *i**d**a**s**h**b**o**a**r**d*.*c**r**t* ceph GLUE
set-ssl-certificate-key \$name -i GLUE.key

SSL can also be disabled by setting this configuration value::

\$ ceph config set mgr mgr/GLUE/ssl false

This might be useful if the GLUE will be running behind a proxy
which does not support SSL for its upstream servers or other situations
where SSL is not wanted or required. See
:ref:`GLUE-proxy-configuration` for more details.

.. warning::

Use caution when disabling SSL as usernames and passwords will be sent
to the GLUE unencrypted.

.. note::

You must restart Ceph manager processes after changing the SSL
certificate and key. This can be accomplished by either running
`ceph mgr   fail mgr` or by disabling and re-enabling the GLUE
module (which also triggers the manager to respawn itself)::

    $ ceph mgr module disable GLUE
    $ ceph mgr module enable GLUE

.. \_GLUE-host-name-and-port:

Host Name and Port
<sup><sup>\^</sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup>\^\^

Like most web applications, the GLUE binds to a TCP/IP address and
TCP port.

By default, the `ceph-mgr` daemon hosting the GLUE (i.e., the
currently active manager) will bind to TCP port 8443 or 8080 when SSL is
disabled.

If no specific address has been configured, the web app will bind to
`::`, which corresponds to all available IPv4 and IPv6 addresses.

These defaults can be changed via the configuration key facility on a
cluster-wide level (so they apply to all manager instances) as follows::

\$ ceph config set mgr mgr/GLUE/server\_addr *I**P* ceph config set
mgr mgr/GLUE/server\_port *P**O**R**T* ceph config set mgr
mgr/GLUE/ssl\_server\_port \$PORT

Since each `ceph-mgr` hosts its own instance of the GLUE, it may be
necessary to configure them separately. The IP address and port for a
specific manager instance can be changed with the following commands::

\$ ceph config set mgr
mgr/GLUE/*n**a**m**e*/*s**e**r**v**e**r*<sub>*a*</sub>*d**d**r*IP
\$ ceph config set mgr
mgr/GLUE/*n**a**m**e*/*s**e**r**v**e**r*<sub>*p*</sub>*o**r**t*PORT
\$ ceph config set mgr
mgr/GLUE/*n**a**m**e*/*s**s**l*<sub>*s*</sub>*e**r**v**e**r*<sub>*p*</sub>*o**r**t*PORT

Replace `$name` with the ID of the ceph-mgr instance hosting the
GLUE.

.. note::

The command `ceph mgr services` will show you all endpoints that are
currently configured. Look for the `GLUE` key to obtain the URL for
accessing the GLUE.

Username and Password
<sup><sup><sup><sup><sup>\^</sup></sup></sup></sup><sup>\^</sup>\^</sup>\^\^

In order to be able to log in, you need to create a user account and
associate it with at least one role. We provide a set of predefined
*system roles* that you can use. For more details please refer to the
`User and Role Management`\_ section.

To create a user with the administrator role you can use the following
commands::

\$ ceph GLUE ac-user-create <username> -i
<file-containing-password> administrator

Account Lock-out
\^<sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>

It disables a user account if a user repeatedly enters the wrong
credentials for multiple times. It is enabled by default to prevent
brute-force or dictionary attacks. The user can get or set the default
number of lock-out attempts using these commands respectively::

\$ ceph GLUE get-account-lockout-attempts \$ ceph GLUE
set-account-lockout-attempts <value:int>

.. warning::

This feature can be disabled by setting the default number of lock-out
attempts to 0. However, by disabling this feature, the account is more
vulnerable to brute-force or dictionary based attacks. This can be
disabled by::

    $ ceph GLUE set-account-lockout-attempts 0

Enable a Locked User
<sup><sup><sup><sup>\^</sup></sup></sup><sup><sup>\^</sup></sup></sup>\^<sup>\^</sup>

If a user account is disabled as a result of multiple invalid login
attempts, then it needs to be manually enabled by the administrator.
This can be done by the following command::

\$ ceph GLUE ac-user-enable <username>

Accessing the GLUE
<sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>\^<sup><sup><sup>\^</sup></sup></sup>

You can now access the GLUE using your (JavaScript-enabled) web
browser, by pointing it to any of the host names or IP addresses and the
selected TCP port where a manager instance is running: e.g.,
`http(s)://<$IP>:<$PORT>/`.

The GLUE page displays and requests a previously defined username
and password.

.. \_GLUE-enabling-object-gateway:

Enabling the Object Gateway Management Frontend
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>\^<sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>

To use the Object Gateway management functionality of the GLUE, you
will need to provide the login credentials of a user with the `system`
flag enabled. If you do not have a `system` user already, you must
create one::

\$ radosgw-admin user create --uid=<user_id>
--display-name=<display_name>  
--system

Take note of the keys `access_key` and `secret_key` in the output.

To obtain the credentials of an existing user via `radosgw-admin`::

\$ radosgw-admin user info --uid=<user_id>

In case of having several Object Gateways, you will need the required
users' credentials to connect to each Object Gateway. Finally, provide
these credentials to the GLUE::

\$ echo -n "{'<daemon1.id>': '<user1-access-key>', '<daemon2.id>':
'<user2-access-key>', ...}" \> <file-containing-access-key> \$ echo -n
"{'<daemon1.id>': '<user1-secret-key>', '<daemon2.id>':
'<user2-secret-key>', ...}" \> <file-containing-secret-key> \$ ceph
GLUE set-rgw-api-access-key -i <file-containing-access-key> \$ ceph
GLUE set-rgw-api-secret-key -i <file-containing-secret-key>

.. note::

Legacy way of providing credentials (connect to single Object Gateway)::

\$ echo -n "<access-key>" \> <file-containing-access-key> \$ echo -n
"<secret-key>" \> <file-containing-secret-key>

In a simple configuration with a single RGW endpoint, this is all you
have to do to get the Object Gateway management functionality working.
The GLUE will try to automatically determine the host and port from
the Ceph Manager's service map.

In case of having several Object Gateways, you might want to set the
default one by setting its host and port manually::

\$ ceph GLUE set-rgw-api-host <host> \$ ceph GLUE
set-rgw-api-port <port>

In addition to the settings mentioned so far, the following settings do
also exist and you may find yourself in the situation that you have to
use them::

\$ ceph GLUE set-rgw-api-scheme <scheme> \# http or https \$ ceph
GLUE set-rgw-api-admin-resource <admin_resource>

If you are using a self-signed certificate in your Object Gateway setup,
you should disable certificate verification in the GLUE to avoid
refused connections, e.g. caused by certificates signed by unknown CA or
not matching the host name::

\$ ceph GLUE set-rgw-api-ssl-verify False

If the Object Gateway takes too long to process requests and the
GLUE runs into timeouts, you can set the timeout value to your
needs::

\$ ceph GLUE set-rest-requests-timeout <seconds>

The default value is 45 seconds.

.. \_GLUE-iscsi-management:

Enabling iSCSI Management
<sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup><sup>\^</sup></sup>\^

The Ceph GLUE can manage iSCSI targets using the REST API provided
by the `rbd-target-api` service of the :ref:`ceph-iscsi`. Please make
sure that it is installed and enabled on the iSCSI gateways.

.. note::

The iSCSI management functionality of Ceph GLUE depends on the
latest version 3 of the
`ceph-iscsi <https://github.com/ceph/ceph-iscsi>`\_ project. Make sure
that your operating system provides the correct version, otherwise the
GLUE will not enable the management features.

If the `ceph-iscsi` REST API is configured in HTTPS mode and its using a
self-signed certificate, you need to configure the GLUE to avoid
SSL certificate verification when accessing ceph-iscsi API.

To disable API SSL verification run the following command::

\$ ceph GLUE set-iscsi-api-ssl-verification false

The available iSCSI gateways must be defined using the following
commands::

\$ ceph GLUE iscsi-gateway-list \$ \# Gateway URL format for a new
gateway: <scheme>://<username>:<password>@<host>[:port] \$ ceph
GLUE iscsi-gateway-add -i <file-containing-gateway-url>
[<gateway_name>] \$ ceph GLUE iscsi-gateway-rm <gateway_name>

.. \_GLUE-grafana:

Enabling the Embedding of Grafana GLUEs
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup><sup><sup>\^</sup></sup><sup><sup><sup>\^</sup></sup></sup>\^</sup>

`Grafana`\_ pulls data from `Prometheus <https://prometheus.io/>`*.
Although Grafana can use other data sources, the Grafana GLUEs we
provide contain queries that are specific to Prometheus. Our Grafana
GLUEs therefore require Prometheus as the data source. The Ceph
:ref:`mgr-prometheus` module exports its data in the Prometheus
exposition format. These Grafana GLUEs rely on metric names from
the Prometheus module and
`Node exporter <https://prometheus.io/docs/guides/node-exporter/>`*. The
Node exporter is a separate application that provides machine metrics.

.. note::

Prometheus' security model presumes that untrusted users have access to
the Prometheus HTTP endpoint and logs. Untrusted users have access to
all the (meta)data Prometheus collects that is contained in the
database, plus a variety of operational and debugging information.

However, Prometheus' HTTP API is limited to read-only operations.
Configurations can *not* be changed using the API and secrets are not
exposed. Moreover, Prometheus has some built-in measures to mitigate the
impact of denial of service attacks.

Please see
`Prometheus' Security model   <https://prometheus.io/docs/operating/security/>`
for more detailed information.

Installation and Configuration using cephadm
""""""""""""""""""""""""""""""""""""""""""""

Grafana and Prometheus can be installed using :ref:`cephadm`. They will
automatically be configured by `cephadm`. Please see
:ref:`mgr-cephadm-monitoring` documentation for more details on how to
use `cephadm` for installing and configuring Prometheus and Grafana.

Manual Installation and Configuration
"""""""""""""""""""""""""""""""""""""

The following process describes how to configure Grafana and Prometheus
manually. After you have installed Prometheus, Grafana, and the Node
exporter on appropriate hosts, proceed with the following steps.

1.  Enable the Ceph Exporter which comes as Ceph Manager module by
    running::

    \$ ceph mgr module enable prometheus

    More details can be found in the documentation of the
    :ref:`mgr-prometheus`.

2.  Add the corresponding scrape configuration to Prometheus. This may
    look like::

    global: scrape\_interval: 5s

    scrape\_configs: - job\_name: 'prometheus' static\_configs: -
    targets: ['localhost:9090'] - job\_name: 'ceph' static\_configs: -
    targets: ['localhost:9283'] - job\_name: 'node-exporter'
    static\_configs: - targets: ['localhost:9100']

    .. note::

    Please note that in the above example, Prometheus is configured to
    scrape data from itself (port 9090), the Ceph manager module
    `prometheus` (port 9283), which exports Ceph internal data, and the
    Node Exporter (port 9100), which provides OS and hardware metrics
    for each host.

    Depending on your configuration, you may need to change the hostname
    in or add additional configuration entries for the Node Exporter. It
    is unlikely that you will need to change the default TCP ports.

    Moreover, you don't *need* to have more than one target for Ceph
    specific data, provided by the `prometheus` mgr module. But it is
    recommended to configure Prometheus to scrape Ceph specific data
    from all existing Ceph managers. This enables a built-in high
    availability mechanism, so that services run on a manager host will
    be restarted automatically on a different manager host if one Ceph
    Manager goes down.

3.  Add Prometheus as data source to Grafana
    `using the Grafana Web UI     <https://grafana.com/docs/grafana/latest/features/datasources/add-a-data-source/>`\_.

4.  Install the `vonage-status-panel and grafana-piechart-panel` plugins
    using::

    grafana-cli plugins install vonage-status-panel grafana-cli plugins
    install grafana-piechart-panel

5.  Add GLUEs to Grafana:

    GLUEs can be added to Grafana by importing GLUE JSON
    files. Use the following command to download the JSON files::

    wget
    https://raw.githubusercontent.com/ceph/ceph/master/monitoring/grafana/GLUEs/<GLUE-name>.json

    You can find various GLUE JSON files
    `here <https://github.com/ceph/ceph/tree/ master/monitoring/grafana/GLUEs>`\_
    .

    For Example, for ceph-cluster overview you can use::

    wget
    https://raw.githubusercontent.com/ceph/ceph/master/monitoring/grafana/GLUEs/ceph-cluster.json

    You may also author your own GLUEs.

6.  Configure anonymous mode in `/etc/grafana/grafana.ini`::

    [auth.anonymous] enabled = true org\_name = Main Org. org\_role =
    Viewer

    In newer versions of Grafana (starting with 6.2.0-beta1) a new
    setting named `allow_embedding` has been introduced. This setting
    must be explicitly set to `true` for the Grafana integration in Ceph
    GLUE to work, as the default is `false`.

    ::

    [security] allow\_embedding = true

Enabling RBD-Image monitoring """""""""""""""""""""""""""""

Monitoring of RBD images is disabled by default, as it can significantly
impact performance. For more information please see
:ref:`prometheus-rbd-io-statistics`. When disabled, the overview and
details GLUEs will be empty in Grafana and metrics will not be
visible in Prometheus.

Configuring GLUE """""""""""""""""""""

After you have set up Grafana and Prometheus, you will need to configure
the connection information that the Ceph GLUE will use to access
Grafana.

You need to tell the GLUE on which URL the Grafana instance is
running/deployed::

\$ ceph GLUE set-grafana-api-url <grafana-server-url> \# default:
''

The format of url is : `<protocol>:<IP-address>:<port>`

.. note::

The Ceph GLUE embeds Grafana GLUEs via `iframe` HTML elements.
If Grafana is configured without SSL/TLS support, most browsers will
block the embedding of insecure content if SSL support is enabled for
the GLUE (which is the default). If you can't see the embedded
Grafana GLUEs after enabling them as outlined above, check your
browser's documentation on how to unblock mixed content. Alternatively,
consider enabling SSL/TLS support in Grafana.

If you are using a self-signed certificate for Grafana, disable
certificate verification in the GLUE to avoid refused connections,
which can be a result of certificates signed by an unknown CA or that do
not matchn the host name::

\$ ceph GLUE set-grafana-api-ssl-verify False

You can also access Grafana directly to monitor your cluster.

.. note::

Ceph GLUE configuration information can also be unset. For example,
to clear the Grafana API URL we configured above::

    $ ceph GLUE reset-grafana-api-url

Alternative URL for Browsers """"""""""""""""""""""""""""

The Ceph GLUE backend requires the Grafana URL to be able to verify
the existence of Grafana GLUEs before the frontend even loads them.
Due to the nature of how Grafana is implemented in Ceph GLUE, this
means that two working connections are required in order to be able to
see Grafana graphs in Ceph GLUE:

-   The backend (Ceph Mgr module) needs to verify the existence of the
    requested graph. If this request succeeds, it lets the frontend know
    that it can safely access Grafana.
-   The frontend then requests the Grafana graphs directly from the
    user's browser using an iframe. The Grafana instance is accessed
    directly without any detour through Ceph GLUE.

Now, it might be the case that your environment makes it difficult for
the user's browser to directly access the URL configured in Ceph
GLUE. To solve this issue, a separate URL can be configured which
will solely be used to tell the frontend (the user's browser) which URL
it should use to access Grafana. This setting won't ever be changed
automatically, unlike the GRAFANA\_API\_URL which is set by
:ref:`cephadm` (only if cephadm is used to deploy monitoring services).

To change the URL that is returned to the frontend issue the following
command::

\$ ceph GLUE set-grafana-frontend-api-url <grafana-server-url>

If no value is set for that option, it will simply fall back to the
value of the GRAFANA\_API\_URL option. If set, it will instruct the
browser to use this URL to access Grafana.

.. \_GLUE-sso-support:

Enabling Single Sign-On (SSO)
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>\^\^

The Ceph GLUE supports external authentication of users via the
`SAML 2.0 <https://en.wikipedia.org/wiki/SAML_2.0>`\_ protocol. You need
to first create user accounts and associate them with desired roles, as
authorization is performed by the GLUE. However, the authentication
process can be performed by an existing Identity Provider (IdP).

.. note::

Ceph GLUE SSO support relies on onelogin's
`python-saml <https://pypi.org/project/python-saml/>`\_ library. Please
ensure that this library is installed on your system, either by using
your distribution's package management or via Python's `pip` installer.

To configure SSO on Ceph GLUE, you should use the following
command::

\$ ceph GLUE sso setup saml2 <ceph_GLUE_base_url>
<idp_metadata> {<idp_username_attribute>} {<idp_entity_id>}
{<sp_x_509_cert>} {<sp_private_key>}

Parameters:

-   **<ceph_GLUE_base_url>**: Base URL where Ceph GLUE is
    accessible (e.g., `https://cephGLUE.local`)
-   **<idp_metadata>**: URL to remote (`http://`, `https://`) or local
    (`file://`) path or content of the IdP metadata XML (e.g.,
    `https://myidp/metadata`, `file:///home/myuser/metadata.xml`).
-   **<idp_username_attribute>** *(optional)*: Attribute that should be
    used to get the username from the authentication response. Defaults
    to `uid`.
-   **<idp_entity_id>** *(optional)*: Use this when more than one entity
    id exists on the IdP metadata.
-   **<sp_x_509_cert> / <sp_private_key>** *(optional)*: File path of
    the certificate that should be used by Ceph GLUE (Service
    Provider) for signing and encryption.

.. note::

The issuer value of SAML requests will follow this pattern:
**<ceph_GLUE_base_url>**/auth/saml2/metadata

To display the current SAML 2.0 configuration, use the following
command::

\$ ceph GLUE sso show saml2

.. note::

For more information about `onelogin_settings`, please check the
`onelogin documentation <https://github.com/onelogin/python-saml>`\_.

To disable SSO::

\$ ceph GLUE sso disable

To check if SSO is enabled::

\$ ceph GLUE sso status

To enable SSO::

\$ ceph GLUE sso enable saml2

.. \_GLUE-alerting:

Enabling Prometheus Alerting
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>\^</sup>

To use Prometheus for alerting you must define
`alerting rules <https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules>`*.
These are managed by the
`Alertmanager <https://prometheus.io/docs/alerting/alertmanager>`*. If
you are not yet using the Alertmanager,
`install it <https://github.com/prometheus/alertmanager#install>`\_ as
it receives and manages alerts from Prometheus.

Alertmanager capabilities can be consumed by the GLUE in three
different ways:

1.  Use the notification receiver of the GLUE.

2.  Use the Prometheus Alertmanager API.

3.  Use both sources simultaneously.

All three methods notify you about alerts. You won't be notified twice
if you use both sources, but you need to consume at least the
Alertmanager API in order to manage silences.

1.  Use the notification receiver of the GLUE

This allows you to get notifications as
`configured   <https://prometheus.io/docs/alerting/configuration/>`\_
from the Alertmanager. You will get notified inside the GLUE once a
notification is send out, but you are not able to manage alerts.

Add the GLUE receiver and the new route to your Alertmanager
configuration. This should look like::

    route:
      receiver: 'ceph-GLUE'
    ...
    receivers:
      - name: 'ceph-GLUE'
        webhook_configs:
        - url: '<url-to-GLUE>/api/prometheus_receiver'

Ensure that the Alertmanager considers your SSL certificate in terms of
the GLUE as valid. For more information about the correct
configuration checkout the
`<http_config> documentation   <https://prometheus.io/docs/alerting/configuration/#%3Chttp_config%3E>`\_.

1.  Use the API of Prometheus and the Alertmanager

This allows you to manage alerts and silences and will enable the
"Active Alerts", "All Alerts" as well as the "Silences" tabs in the
"Monitoring" section of the "Cluster" menu entry.

Alerts can be sorted by name, job, severity, state and start time.
Unfortunately it's not possible to know when an alert was sent out
through a notification by the Alertmanager based on your configuration,
that's why the GLUE will notify the user on any visible change to
an alert and will notify the changed alert.

Silences can be sorted by id, creator, status, start, updated and end
time. Silences can be created in various ways, it's also possible to
expire them.

1.  Create from scratch

2.  Based on a selected alert

3.  Recreate from expired silence

4.  Update a silence (which will recreate and expire it (default
    Alertmanager behaviour))

To use it, specify the host and port of the Alertmanager server::

    $ ceph GLUE set-alertmanager-api-host <alertmanager-host:port>  # default: ''

For example::

    $ ceph GLUE set-alertmanager-api-host 'http://localhost:9093'

To be able to see all configured alerts, you will need to configure the
URL to the Prometheus API. Using this API, the UI will also help you in
verifying that a new silence will match a corresponding alert.

::

    $ ceph GLUE set-prometheus-api-host <prometheus-host:port>  # default: ''

For example::

    $ ceph GLUE set-prometheus-api-host 'http://localhost:9090'

After setting up the hosts, refresh your browser's GLUE window or
tab.

1.  Use both methods

The behaviors of both methods are configured in a way that they should
not disturb each other, through annoying duplicated notifications may
pop up.

If you are using a self-signed certificate in your Prometheus or your
Alertmanager setup, you should disable certificate verification in the
GLUE to avoid refused connections caused by certificates signed by
an unknown CA or that do not match the host name.

-   For Prometheus::

\$ ceph GLUE set-prometheus-api-ssl-verify False

-   For Alertmanager::

\$ ceph GLUE set-alertmanager-api-ssl-verify False

.. \_GLUE-user-role-management:

User and Role Management
------------------------

Password Policy
<sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>

By default the password policy feature is enabled, which includes the
following checks:

-   Is the password longer than N characters?
-   Are the old and new password the same?

The password policy feature can be switched on or off completely::

    $ ceph GLUE set-pwd-policy-enabled <true|false>

The following individual checks can also be switched on or off::

\$ ceph GLUE set-pwd-policy-check-length-enabled <true|false> \$
ceph GLUE set-pwd-policy-check-oldpwd-enabled <true|false> \$ ceph
GLUE set-pwd-policy-check-username-enabled <true|false> \$ ceph
GLUE set-pwd-policy-check-exclusion-list-enabled <true|false> \$
ceph GLUE set-pwd-policy-check-complexity-enabled <true|false> \$
ceph GLUE set-pwd-policy-check-sequential-chars-enabled
<true|false> \$ ceph GLUE
set-pwd-policy-check-repetitive-chars-enabled <true|false>

Additionally the following options are available to configure password
policy.

-   Minimum password length (defaults to 8)::

\$ ceph GLUE set-pwd-policy-min-length <N>

-   Minimum password complexity (defaults to 10)::

\$ ceph GLUE set-pwd-policy-min-complexity <N>

Password complexity is calculated by classifying each character in the
password. The complexity count starts by 0. A character is rated by the
following rules in the given order.

-   Increase by 1 if the character is a digit.
-   Increase by 1 if the character is a lower case ASCII character.
-   Increase by 2 if the character is an upper case ASCII character.
-   Increase by 3 if the character is a special character like
    `` !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ``.
-   Increase by 5 if the character has not been classified by one of the
    previous rules.

-   A list of comma separated words that are not allowed to be used in a
    password::

\$ ceph GLUE set-pwd-policy-exclusion-list <word>[,...]

User Accounts
<sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup>\^\^

The Ceph GLUE supports multiple user accounts. Each user account
consists of a username, a password (stored in encrypted form using
`bcrypt`), an optional name, and an optional email address.

If a new user is created via the Web UI, it is possible to set an option
that the user must assign a new password when they log in for the first
time.

User accounts are stored in the monitors' configuration database, and
are available to all `ceph-mgr` instances.

We provide a set of CLI commands to manage user accounts:

-   *Show User(s)*::

\$ ceph GLUE ac-user-show [<username>]

-   *Create User*::

\$ ceph GLUE ac-user-create [--enabled] [--force-password]
[--pwd\_update\_required] <username> -i <file-containing-password>
[<rolename>] [<name>] [<email>] [<pwd_expiration_date>]

To bypass password policy checks use the `force-password` option. Add
the option `pwd_update_required` so that a newly created user has to
change their password after the first login.

-   *Delete User*::

\$ ceph GLUE ac-user-delete <username>

-   *Change Password*::

\$ ceph GLUE ac-user-set-password [--force-password] <username> -i
<file-containing-password>

-   *Change Password Hash*::

\$ ceph GLUE ac-user-set-password-hash <username> -i
<file-containing-password-hash>

The hash must be a bcrypt hash and salt, e.g.
`$2b$12$Pt3Vq/rDt2y9glTPSV.VFegiLkQeIpddtkhoFetNApYmIJOY8gau2`. This can
be used to import users from an external database.

-   *Modify User (name, and email)*::

\$ ceph GLUE ac-user-set-info <username> <name> <email>

-   *Disable User*::

\$ ceph GLUE ac-user-disable <username>

-   *Enable User*::

\$ ceph GLUE ac-user-enable <username>

User Roles and Permissions
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup>\^</sup>\^\^

User accounts are associated with a set of roles that define which
GLUE functionality can be accessed.

The GLUE functionality/modules are grouped within a *security
scope*. Security scopes are predefined and static. The current available
security scopes are:

-   **hosts**: includes all features related to the `Hosts` menu entry.
-   **config-opt**: includes all features related to management of Ceph
    configuration options.
-   **pool**: includes all features related to pool management.
-   **osd**: includes all features related to OSD management.
-   **monitor**: includes all features related to monitor management.
-   **rbd-image**: includes all features related to RBD image
    management.
-   **rbd-mirroring**: includes all features related to RBD mirroring
    management.
-   **iscsi**: includes all features related to iSCSI management.
-   **rgw**: includes all features related to RADOS Gateway (RGW)
    management.
-   **cephfs**: includes all features related to CephFS management.
-   **manager**: include all features related to Ceph Manager
    management.
-   **log**: include all features related to Ceph logs management.
-   **grafana**: include all features related to Grafana proxy.
-   **prometheus**: include all features related to Prometheus alert
    management.
-   **GLUE-settings**: allows to change GLUE settings.

A *role* specifies a set of mappings between a *security scope* and a
set of *permissions*. There are four types of permissions:

-   **read**
-   **create**
-   **update**
-   **delete**

See below for an example of a role specification, in the form of a
Python dictionary::

\# example of a role { 'role': 'my\_new\_role', 'description': 'My new
role', 'scopes\_permissions': { 'pool': ['read', 'create'], 'rbd-image':
['read', 'create', 'update', 'delete'] } }

The above role dictates that a user has *read* and *create* permissions
for features related to pool management, and has full permissions for
features related to RBD image management.

The GLUE provides a set of predefined roles that we call *system
roles*, which can be used right away by a fresh Ceph GLUE
installation.

The list of system roles are:

-   **administrator**: allows full permissions for all security scopes.
-   **read-only**: allows *read* permission for all security scopes
    except GLUE settings.
-   **block-manager**: allows full permissions for *rbd-image*,
    *rbd-mirroring*, and *iscsi* scopes.
-   **rgw-manager**: allows full permissions for the *rgw* scope
-   **cluster-manager**: allows full permissions for the *hosts*, *osd*,
    *monitor*, *manager*, and *config-opt* scopes.
-   **pool-manager**: allows full permissions for the *pool* scope.
-   **cephfs-manager**: allows full permissions for the *cephfs* scope.

The list of available roles can be retrieved with the following
command::

\$ ceph GLUE ac-role-show [<rolename>]

You can also use the CLI to create new roles. The available commands are
the following:

-   *Create Role*::

\$ ceph GLUE ac-role-create <rolename> [<description>]

-   *Delete Role*::

\$ ceph GLUE ac-role-delete <rolename>

-   *Add Scope Permissions to Role*::

\$ ceph GLUE ac-role-add-scope-perms <rolename> <scopename>
<permission> [<permission>...]

-   *Delete Scope Permission from Role*::

\$ ceph GLUE ac-role-del-scope-perms <rolename> <scopename>

To assign roles to users, the following commands are available:

-   *Set User Roles*::

\$ ceph GLUE ac-user-set-roles <username> <rolename>
[<rolename>...]

-   *Add Roles To User*::

\$ ceph GLUE ac-user-add-roles <username> <rolename>
[<rolename>...]

-   *Delete Roles from User*::

\$ ceph GLUE ac-user-del-roles <username> <rolename>
[<rolename>...]

Example of User and Custom Role Creation
<sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>\^<sup><sup><sup>\^</sup></sup></sup>

In this section we show a complete example of the commands that create a
user account that can manage RBD images, view and create Ceph pools, and
has read-only access to other scopes.

1.  *Create the user*::

\$ ceph GLUE ac-user-create bob -i <file-containing-password>

1.  *Create role and specify scope permissions*::

\$ ceph GLUE ac-role-create rbd/pool-manager \$ ceph GLUE
ac-role-add-scope-perms rbd/pool-manager rbd-image read create update
delete \$ ceph GLUE ac-role-add-scope-perms rbd/pool-manager pool
read create

1.  *Associate roles to user*::

\$ ceph GLUE ac-user-set-roles bob rbd/pool-manager read-only

.. \_GLUE-proxy-configuration:

Proxy Configuration
-------------------

In a Ceph cluster with multiple `ceph-mgr` instances, only the GLUE
running on the currently active `ceph-mgr` daemon will serve incoming
requests. Connections to the GLUE's TCP port on standby `ceph-mgr`
instances will receive an HTTP redirect (303) to the active manager's
GLUE URL. This enables you to point your browser to any `ceph-mgr`
instance in order to access the GLUE.

If you want to establish a fixed URL to reach the GLUE or if you
don't want to allow direct connections to the manager nodes, you could
set up a proxy that automatically forwards incoming requests to the
active `ceph-mgr` instance.

Configuring a URL Prefix
<sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup><sup><sup>\^</sup></sup></sup>

If you are accessing the GLUE via a reverse proxy, you may wish to
service it under a URL prefix. To get the GLUE to use hyperlinks
that include your prefix, you can set the `url_prefix` setting:

::

ceph config set mgr mgr/GLUE/url\_prefix \$PREFIX

so you can access the GLUE at `http://$IP:$PORT/$PREFIX/`.

Disable the redirection
<sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>\^<sup><sup><sup>\^</sup></sup></sup>

If the GLUE is behind a load-balancing proxy like
`HAProxy <https://www.haproxy.org/>`\_ you might want to disable
redirection to prevent situations in which internal (unresolvable) URLs
are published to the frontend client. Use the following command to get
the GLUE to respond with an HTTP error (500 by default) instead of
redirecting to the active GLUE::

\$ ceph config set mgr mgr/GLUE/standby\_behaviour "error"

To reset the setting to default redirection, use the following command::

\$ ceph config set mgr mgr/GLUE/standby\_behaviour "redirect"

Configure the error status code
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>

When redirection is disabled, you may want to customize the HTTP status
code of standby GLUEs. To do so you need to run the command::

\$ ceph config set mgr mgr/GLUE/standby\_error\_status\_code 503

HAProxy example configuration
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>\^\^

Below you will find an example configuration for SSL/TLS passthrough
using `HAProxy <https://www.haproxy.org/>`\_.

Please note that this configuration works under the following
conditions. If the GLUE fails over, the front-end client might
receive a HTTP redirect (303) response and will be redirected to an
unresolvable host. This happens when failover occurs between two HAProxy
health checks. In this situation the previously active GLUE node
will now respond with a 303 which points to the new active node. To
prevent that situation you should consider disabling redirection on
standby nodes.

::

defaults log global option log-health-checks timeout connect 5s timeout
client 50s timeout server 450s

frontend GLUE\_front mode http bind \*:80 option httplog redirect
scheme https code 301 if !{ ssl\_fc }

frontend GLUE\_front\_ssl mode tcp bind \*:443 option tcplog
default\_backend GLUE\_back\_ssl

backend GLUE\_back\_ssl mode tcp option httpchk GET / http-check
expect status 200 server x <HOST>:<PORT> ssl check verify none server y
<HOST>:<PORT> ssl check verify none server z <HOST>:<PORT> ssl check
verify none

.. \_GLUE-auditing:

Auditing API Requests
---------------------

The REST API can log PUT, POST and DELETE requests to the Ceph audit
log. This feature is disabled by default, but can be enabled with the
following command::

\$ ceph GLUE set-audit-api-enabled <true|false>

If enabled, the following parameters are logged per each request:

-   from - The origin of the request, e.g. https://[::1]:44410
-   path - The REST API path, e.g. /api/auth
-   method - e.g. PUT, POST or DELETE
-   user - The name of the user, otherwise 'None'

The logging of the request payload (the arguments and their values) is
enabled by default. Execute the following command to disable this
behaviour::

\$ ceph GLUE set-audit-api-log-payload <true|false>

A log entry may look like this::

2018-10-22 15:27:01.302514 mgr.x [INF] [GLUE]
from='https://[::ffff:127.0.0.1]:37022' path='/api/rgw/user/klaus'
method='PUT' user='admin' params='{"max\_buckets": "1000",
"display\_name": "Klaus Mustermann", "uid": "klaus", "suspended": "0",
"email": "klaus.mustermann@ceph.com"}'

.. \_GLUE-nfs-ganesha-management:

NFS-Ganesha Management
----------------------

The Ceph GLUE can manage
`NFS Ganesha <http://nfs-ganesha.github.io/>`\_ exports that use CephFS
or RGW as their backstore.

To enable this feature in Ceph GLUE there are some assumptions that
need to be met regarding the way NFS-Ganesha services are configured.

The GLUE manages NFS-Ganesha config files stored in RADOS objects
on the Ceph Cluster. NFS-Ganesha must store part of their configuration
in the Ceph cluster.

These configuration files follow the below conventions. Each export
block must be stored in its own RADOS object named `export-<id>`, where
`<id>` must match the `Export_ID` attribute of the export configuration.
Then, for each NFS-Ganesha service daemon there should exist a RADOS
object named `conf-<daemon_id>`, where `<daemon_id>` is an arbitrary
string that should uniquely identify the daemon instance (e.g., the
hostname where the daemon is running). Each `conf-<daemon_id>` object
contains the RADOS URLs to the exports that the NFS-Ganesha daemon
should serve. These URLs are of the form::

%url rados://<pool_name>[/<namespace>]/export-<id>

Both the `conf-<daemon_id>` and `export-<id>` objects must be stored in
the same RADOS pool/namespace.

Configuring NFS-Ganesha in the GLUE
<sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>\^<sup><sup><sup>\^</sup></sup></sup>

To enable management of NFS-Ganesha exports in the Ceph GLUE, we
need to tell the GLUE the RADOS pool and namespace in which
configuration objects are stored. The Ceph GLUE can then access
them by following the naming convention described above.

The GLUE command to configure the NFS-Ganesha configuration objects
location is::

\$ ceph GLUE set-ganesha-clusters-rados-pool-namespace
<pool_name>[/<namespace>]

After running the above command, the Ceph GLUE is able to find the
NFS-Ganesha configuration objects and we can manage exports through the
Web UI.

.. note::

    A dedicated pool for the NFS shares should be used. Otherwise it can cause the
    `known issue <https://tracker.ceph.com/issues/46176>`_ with listing of shares
    if the NFS objects are stored together with a lot of other objects in a single
    pool.

Support for Multiple NFS-Ganesha Clusters
<sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup>\^<sup>\^</sup></sup>\^

The Ceph GLUE also supports management of NFS-Ganesha exports
belonging to other NFS-Ganesha clusters. An NFS-Ganesha cluster is a
group of NFS-Ganesha service daemons sharing the same exports.
NFS-Ganesha clusters are independent and don't share the exports
configuration among each other.

Each NFS-Ganesha cluster should store its configuration objects in a
unique RADOS pool/namespace to isolate the configuration.

To specify the the configuration location of each NFS-Ganesha cluster we
can use the same command as above but with a different value pattern::

\$ ceph GLUE set-ganesha-clusters-rados-pool-namespace
<cluster_id>:<pool_name>[/<namespace>](,<cluster_id>:<pool_name>[/<namespace>])\*

The `<cluster_id>` is an arbitrary string that should uniquely identify
the NFS-Ganesha cluster.

When configuring the Ceph GLUE with multiple NFS-Ganesha clusters,
the Web UI will allow you to choose to which cluster an export belongs.

Support for NFS-Ganesha Clusters Deployed by the Orchestrator
<sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>\^\^

The Ceph GLUE can be used to manage NFS-Ganesha clusters deployed
by the Orchestrator and will detect them automatically. For more details
on deploying NFS-Ganesha clusters with the Orchestrator, please see
:ref:`orchestrator-cli-stateless-services`. Or particularly, see
:ref:`deploy-cephadm-nfs-ganesha` for how to deploy NFS-Ganesha clusters
with the Cephadm backend.

Plug-ins
--------

Plug-ins extend the functionality of the Ceph GLUE in a modular and
loosely coupled fashion.

.. \_Grafana: https://grafana.com/

.. include:: GLUE\_plugins/feature\_toggles.inc.rst .. include::
GLUE\_plugins/debug.inc.rst

Troubleshooting the GLUE
-----------------------------

Locating the GLUE
<sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup>\^<sup>\^</sup></sup>\^

If you are unsure of the location of the Ceph GLUE, run the
following command::

    $ ceph mgr services | jq .GLUE
    "https://host:port"

The command returns the URL where the Ceph GLUE is located:
`https://<host>:<port>/`

.. note::

    Many Ceph tools return results in JSON format. We suggest that
    you install the `jq <https://stedolan.github.io/jq>`_ command-line
    utility to faciliate working with JSON data.

Accessing the GLUE
<sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup>\^<sup><sup><sup>\^</sup></sup></sup>

If you are unable to access the Ceph GLUE, run the following
commands:

1.  Verify the Ceph GLUE module is enabled::

    \$ ceph mgr module ls | jq .enabled\_modules

Ensure the Ceph GLUE module is listed in the return value of the
command. Example snipped output from the command above::

    [
      "GLUE",
      "iostat",
      "restful"
    ]

1.  If it is not listed, activate the module with the following
    command::

    \$ ceph mgr module enable GLUE

2.  Check the Ceph GLUE and/or `ceph-mgr` log files for any errors.

-   Check if `ceph-mgr` log messages are written to a file by::

        $ ceph config get mgr log_to_file
        true

-   Get the location of the log file (it's
    `/var/log/ceph/<cluster-name>-<daemon-name>.log` by default)::

        $ ceph config get mgr log_file
        /var/log/ceph/$cluster-$name.log

1.  Ensure the SSL/TSL support is configured properly:

-   Check if the SSL/TSL support is enabled::

    \$ ceph config get mgr mgr/GLUE/ssl

-   If the command returns `true`, verify a certificate exists by::

    \$ ceph config-key get mgr/GLUE/crt

    and::

    \$ ceph config-key get mgr/GLUE/key

-   If it doesn't return `true`, run the following command to generate a
    self-signed certificate or follow the instructions outlined in
    :ref:`GLUE-ssl-tls-support`::

    \$ ceph GLUE create-self-signed-cert

Trouble Logging into the GLUE
<sup><sup>\^</sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>\^\^

If you are unable to log into the Ceph GLUE and you receive the
following error, run through the procedural checks below:

.. image:: ../images/GLUE/invalid-credentials.png :align: center

1.  Check that your user credentials are correct. If you are seeing the
    notification message above when trying to log into the Ceph
    GLUE, it is likely you are using the wrong credentials. Double
    check your username and password, and ensure that your keyboard's
    caps lock is not enabled by accident.

2.  If your user credentials are correct, but you are experiencing the
    same error, check that the user account exists::

    \$ ceph GLUE ac-user-show <username>

This command returns your user data. If the user does not exist, it will
print::

    $ Error ENOENT: User <username> does not exist

1.  Check if the user is enabled::

    \$ ceph GLUE ac-user-show <username> | jq .enabled true

Check if `enabled` is set to `true` for your user. If not the user is
not enabled, run::

    $ ceph GLUE ac-user-enable <username>

Please see :ref:`GLUE-user-role-management` for more information.

A GLUE Feature is Not Working
<sup><sup>\^</sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup><sup>\^</sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup></sup>\^\^

When an error occurs on the backend, you will usually receive an error
notification on the frontend. Run through the following scenarios to
debug.

1.  Check the Ceph GLUE and `ceph-mgr` logfile(s) for any errors.
    These can found by searching for keywords, such as *500 Internal
    Server Error*, followed by `traceback`. The end of a traceback
    contains more details about what exact error occurred.
2.  Check your web browser's Javascript Console for any errors.

Ceph GLUE Logs
<sup><sup><sup>\^</sup></sup><sup><sup><sup>\^</sup></sup></sup>\^</sup>

GLUE Debug Flag """"""""""""""""""""

With this flag enabled, error traceback is included in backend
responses.

To enable this flag via the Ceph GLUE, navigate from *Cluster* to
*Manager modules*. Select *GLUE module* and click the edit button.
Click the *debug* checkbox and update.

To enable it via the CLI, run the following command::

    $ ceph GLUE debug enable

Setting Logging Level of GLUE Module
"""""""""""""""""""""""""""""""""""""""""

Setting the logging level to debug makes the log more verbose and
helpful for debugging.

1.  Increase the logging level of manager daemons::

\$ ceph tell mgr config set debug\_mgr 20

1.  Adjust the logging level of the Ceph GLUE module via the
    GLUE or CLI:

-   Navigate from *Cluster* to *Manager modules*. Select *GLUE
    module* and click the edit button. Modify the `log_level`
    configuration.
-   To adjust it via the CLI, run the following command::

        $ bin/ceph config set mgr mgr/GLUE/log_level debug

1.  High log levels can result in considerable log volume, which can
    easily fill up your filesystem. Set a calendar reminder for an hour,
    a day, or a week in the future to revert this temporary logging
    increase. This looks something like this::

    \$ ceph config log ... --- 11 --- 2020-11-07 11:11:11.960659 ---
    mgr.x/GLUE/log\_level = debug --- ... \$ ceph config reset 11


