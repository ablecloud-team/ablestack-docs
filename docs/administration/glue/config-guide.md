!!! danger
    이 문서는 관리자용 문서입니다. 관리자가 아닌 사용자가 동작시 문제가 발생할수도 있습니다.

# GLUE 설정 가이드
GLUE를 설정하는 방법에 대한 안내입니다.

## SSL/TLS 지원

모든 GLUE의 HTTP 연결은 SSL/TLS를 통해 보안을 유지하는것을 기본으로 합니다.

자체 서명 인증서를 새로 생성하기 위해서는 다음과 같은 명령으로 생성할 수 있습니다.
```shell
$ ceph dashboard create-self-signed-cert
```

!!! note
    대부분의 브라우저들은 이러한 자체 서명 인증서에 대하여 신뢰할 수 없는 인증서로 표시하며, 신규 연결시 확인과정이 필요합니다.

자체서명 인증서에 대한 경고를 제거하고, 정규 인증서를 사용하기 위해서는 다음과 같은 작업이 필요합니다.

1. 인증서 키 쌍 생성
2. 인증서 인증
3. 인증서 적용

다음은 인증서 키 쌍을 생성하기 위한 예시입니다. 다른 도구를 사용하여 키 쌍을 생성하고 인증기관의 인증을 받는 과정은 생략합니다.

```bash
$ openssl req -new -nodes -x509  \
-subj "/O=IT/CN=ceph-mgr-dashboard" -days 3650 \  
-keyout GLUE.key -out GLUE.crt -extensions v3_ca
```

위와 같은 작업을 진행하면 `GLUE.key`, `GLUE.crt` 파일이 생성됩니다.
이러한 `GLUE.crt` 파일은 CA(인증기관)에 의해 인증받아야 합니다.  인증을 받은 뒤 다음 명령어를 통해 해당 인증서를 사용할 수 있습니다.

```bash
$ ceph dashboard set-ssl-certificate -i GLUE.crt
$ ceph dashboard set-ssl-certificate-key -i GLUE.key
```

만약 각각의 manager 에 대해 별도의 인증서가 발급되었다면, 다음과 같은 방법으로 등록할 수 있습니다.(`$name`은 manager의 이름입니다. 보통 hostname이 사용됩니다.)
```bash
$ ceph dashboard set-ssl-certificate $name −i GLUE.crt
$ ceph dashboard set-ssl-certificate-key $name -i GLUE.key
```

다음의 방법으로 SSL 설정을 비활성화 시킬 수 도 있습니다.
```bash
$ ceph config set mgr mgr/dashboard/ssl false
```

이것은 GLUE가 SSL을 지원하지 않는 proxy 뒤에 있거나, 기타 필요한 경우에 사용됩니다.
[`프록시 설정`]('proxyconfig-guide.md#_1') 문서를 통해 자세한 내용을 확인하세요.

!!! warning
    위 방법을 통해 SSL을 비활성화한 경우, 사용자명과 암호가 암호화되지 않은 상태로 전달됩니다.

!!! note
    SSL 인증서와 키를 변경한 경우 반드시 manager 프로세스를 재시작 해야 합니다. 이 과정은
    `ceph mgr fail mgr` 명령을 사용하거나 다음과 같은 GLUE 명령을 사용해 비활성화 후 활성화 하는 방법으로 적용할 수 있습니다.
    ```bash
    $ ceph mgr module disable dashboard
    $ ceph mgr module enable dashboard
    ```

## 호스트명과 port

다른 웹 어플리케이션과 같이 GLUE는 TCP/IP 주소와 TCP 포트가 사용됩니다.

기본적으로 `ceph-mgr` 데몬이  (특히 현재 활성 상태인 mgr이 ) 8443(혹은 SSL을 사용하지 않는다면 8080)번 포트를 사용해 GLUE를 제공합니다.

TCP/IP 주소가 별도로 특정되지 않았다면 웹앱은 `::`, 즉 모든 IPv4및 IPv6 주소로 연결대기 상태가 됩니다.

이러한 기본값은 다음과 같은 전역 설정 변경으로 설정할 수 있습니다.

``` bash
$ ceph config set mgr mgr/GLUE/server_addr $IP
$ ceph config set mgr mgr/GLUE/server_port $PORT
$ ceph config set mgr mgr/GLUE/ssl_server_port $PORT
```

`ceph-mgr`이 각각의 GLUE 인스턴스를 제공하므로 이 값은 다음과 같이 별도로 설정 해야 할 수 있습니다.

``` bash
$ ceph config set mgr mgr/GLUE/$name/server_addr $IP
$ ceph config set mgr mgr/GLUE/$name/server_port $PORT
$ ceph config set mgr mgr/GLUE/$name/ssl_server_port $PORT
```

!!! note
    `ceph mgr services`명령은 현재 설정된 서비스의 연결점을 안내해줍니다. `dashboard`키를 통해 현재 GLUE에 접속할 수 있는 주소를 얻을 수 있습니다.

## 사용자명과 비밀번호


GLUR는 로그인을 하기 위한 사용자를 추가하는 명령어를 제공합니다.
생성되는 계정은 하나 이상의 역할이 지정되어야 합니다. GLUE는 사전에 정의된 *system role*을 제공합니다.
자세한 내용은 [`사용자 및 역할관리`](account&role-guide.md)를 참고하세요.

관리자 역할의 사용자를 만들고 싶으면 다음 명령어를 입력하면 됩니다.

```bash
 $ceph dashboard ac-user-create <username> -i <file-containing-password> administrator
```

## 사용자 잠금

만약 여러번의 잘못된 로그인 시도가 있다면 사용자의 계정은 `brute-force`공격이나 `dictionary`공격을 방지하기 위해 계정에 잠금을 걸게 된다.
이러한 잠금 설정을 변경하기 위해서 다음 명령어를 사용할 수 있습니다.

```bash
$ ceph dashboard get-account-lockout-attempts 
$ ceph bashboard set-account-lockout-attempts <value:int>
```

!!! warning
    이 기능은 다음과 같이 시도횟수를 0으로 변경하면 해제됩니다. 하지만 이 기능을 해제하면, `brute-force`공격이나 `dictionary`공격에 취약해집니다.
    ``` bash
    $ ceph dashboard set-account-lockout-attempts 0
    ```

## 사용자 잠금 해제

만약 사용자가 여러번의 잘못된 로그인 시도로 인해 잠겼다면, 관리자가 다음 명령어를 사용하여 잠금을 해제 할 수 있습니다.
```bash
$ ceph dashboard ac-user-enable <username>
```
## GLUE 접속

사용자는 자바스크립트가 사용가능한 웹 브라우저를 통해 `http(s)://<SCVM IP>:<PORT(기본값:8443)>` 으로 GLUE에 접근 가능합니다.

GLUE의 기본 사용자 계정은 `ablecloud/password` 입니다.


## Object Gateway 관리 콘솔 활성화

Object Gateway 관리 기능을 사용하려면 `system` 플래그가 지정된 사용자 계정이 필요합니다.
만약 아직 `system` 사용자가 없다면 다음과 같이 생성할 수 있습니다.

```shell
$ radosgw-admin user create --uid=<user_id> --display-name=<display_name> --system
```
그 다음 표시되는 `access_key`와 `secret_key`를 기록해 둡니다.

기존 사용자의 키를 얻고자 한다면 다음과 같이 하면 됩니다.
```shell
$ radosgw-admin user info --uid=<user_id\>
```

여러개의 Object Gateway가 있다면 각각 사용자의 인증정보가 있어야 합니다.
다음과 같이 인증정보를 GLUE에 등록할 수 있습니다.
```shell
$ echo -n "{'<daemon1.id\>': '<user1-access-key\>', '<daemon2.id\>': '<user2-access-key\>', ...}" > <file-containing-access-key>
$ echo -n "{'<daemon1.id\>': '<user1-secret-key\>', '<daemon2.id\>': '<user2-secret-key\>', ...}" > <file-containing-secret-key> 
$ ceph dashboard set-rgw-api-access-key -i <file-containing-access-key>
$ ceph dashboard set-rgw-api-secret-key -i <file-containing-secret-key>
```

!!! note
    단일 게이트웨이의 경우 다음과 같이 지정할 수 도 있습니다.
    ```shell
    $ echo -n "<access-key>" > <file-containing-access-key> 
    $ echo -n "<secret-key>" > <file-containing-secret-key>
    ```

단일 RGW 접속점이 있는 간단한 구성에서는 위 작업만 수행하면 GLUE를 통해 Object Gateway 관리 기능을 사용할 수 있습니다.

만일 여러개의 Object Gateway가 있는경우 아래 작업을 통해 기본값을 설정 해 주어야 합니다.

```shell
$ ceph dashboard set-rgw-api-host <host> 
$ ceph dashboard set-rgw-api-port <port>
```

추가로 다음 설정이 필요 할 수도 있습니다.

```shell
$ ceph dashboard set-rgw-api-scheme <scheme> # http or https 
$ ceph dashboard set-rgw-api-admin-resource <admin_resource>
```

다음 설정은 사용해 GLUE가 자체서명 인증서를 사용한 호스트의 접속을 서명되지 않았거나, 호스트이름이 일치하지 않는다고 거부하는것을 방지해야 합니다.

```shell
$ ceph GLUE set-rgw-api-ssl-verify False
```

만약 Object Gateway가 요청을 처리하는데 시간이 오래 걸려 timeout이 발생한다면 다음과 같이 시간을 지정할 수 있습니다.

```shell
$ ceph dashboard set-rest-requests-timeout <seconds>
```
기본값은 45초 입니다.

## iSCSI관리 활성화

GLUE는 [`ceph-iscsi`]()로 구성된 iSCSI target을 `rbd-target-api`의 REST API를 이용하여 관리할 수 있습니다.

!!! note
    GLUE의 iSCSI관리 기능은 [`ceph-iscsi`](https://github.com/ceph/ceph-iscsi) 프로젝트의 최종 3개 버전을 지원합니다.
    

`ceph-iscsi` REST API가 HTTPS mode로 설정되고 자체서명인증서를 사용한다면 GLUE가 ceph-iscsi API에 접근할때 거부하지 않도록 방지해야 합니다.

이러한 SSL 확인 기능을 해제하기 위해서 다음과 같이 합니다.
```shell
$ ceph dashboard set-iscsi-api-ssl-verification false
```

활성화된 iSCSI gateway는 다음과 같이 등록해주어야 합니다.

```shell
$ ceph dashboard iscsi-gateway-list 
$ # 새로운 Gateway URL은 다음과 같은 형식으로 넣습니다. <scheme>://<username>:<password>@<host>[:port] 
$ ceph dashboard iscsi-gateway-add -i <file-containing-gateway-url> [<gateway_name>] 
$ ceph dashboard iscsi-gateway-rm <gateway_name>
```

## GLUE 내장 Grafana 활성화 

`Grafana`는 [`Prometheus`](https://prometheus.io/) 로 부터 데이터를 받아옵니다.
`Prometheus`는 [`mgr-prometheus`]() 모듈이 제공하며, 이것은 [`Node exporter`](https://prometheus.io/docs/guides/node-exporter/>)를 사용해 
장비의 측정값을 수집합니다.

!!! note
    Prometheus의 보안 모델은 신뢰되지 않은 사용자가 HTTP 엔드포인트와 로그에 접속할 수 있다고 가정합니다. 신뢰할 수 없는 사용자는 Prometheus가 수집하는 모든 데이터 및 디버깅 정보를 접근할 수 있습니다. 하지만 이것은 읽기 전용 작업으로 제한됩니다. 자세한 내용은 [`Prometheus의 보안모델`](https://prometheus.io/docs/operating/security/)을 참고하세요.

### Installation and Configuration using cephadm


Grafana and Prometheus can be installed using [`cephadm`.]() They will
automatically be configured by `cephadm`. Please see
[`mgr-cephadm-monitoring`]() documentation for more details on how to
use `cephadm` for installing and configuring Prometheus and Grafana.

### Manual Installation and Configuration


The following process describes how to configure Grafana and Prometheus
manually. After you have installed Prometheus, Grafana, and the Node
exporter on appropriate hosts, proceed with the following steps.

1.  Enable the Ceph Exporter which comes as Ceph Manager module by
    running::

    \$ ceph mgr module enable prometheus

    More details can be found in the documentation of the
    [`mgr-prometheus`]().

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
    `using the Grafana Web UI     <https://grafana.com/docs/grafana/latest/features/datasources/add-a-data-source/\>`\_.

4.  Install the `vonage-status-panel and grafana-piechart-panel` plugins
    using::

    grafana-cli plugins install vonage-status-panel grafana-cli plugins
    install grafana-piechart-panel

5.  Add GLUEs to Grafana:

    GLUEs can be added to Grafana by importing GLUE JSON
    files. Use the following command to download the JSON files::

    wget
    https://raw.githubusercontent.com/ceph/ceph/master/monitoring/grafana/GLUEs/<GLUE-name\>.json

    You can find various GLUE JSON files
    `here <https://github.com/ceph/ceph/tree/ master/monitoring/grafana/GLUEs\>`\_
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

### Enabling RBD-Image monitoring

Monitoring of RBD images is disabled by default, as it can significantly
impact performance. For more information please see
[`prometheus-rbd-io-statistics`.]() When disabled, the overview and
details GLUEs will be empty in Grafana and metrics will not be
visible in Prometheus.

### Configuring GLUE

After you have set up Grafana and Prometheus, you will need to configure
the connection information that the Ceph GLUE will use to access
Grafana.

You need to tell the GLUE on which URL the Grafana instance is
running/deployed::

\$ ceph GLUE set-grafana-api-url <grafana-server-url\> \# default:
''

The format of url is : `<protocol\>:<IP-address\>:<port\>`

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

### Alternative URL for Browsers

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
[`cephadm`]() (only if cephadm is used to deploy monitoring services).

To change the URL that is returned to the frontend issue the following
command::

\$ ceph GLUE set-grafana-frontend-api-url <grafana-server-url\>

If no value is set for that option, it will simply fall back to the
value of the GRAFANA\_API\_URL option. If set, it will instruct the
browser to use this URL to access Grafana.

.. \_GLUE-sso-support:

## Enabling Single Sign-On (SSO)


The Ceph GLUE supports external authentication of users via the
`SAML 2.0 <https://en.wikipedia.org/wiki/SAML_2.0\>`\_ protocol. You need
to first create user accounts and associate them with desired roles, as
authorization is performed by the GLUE. However, the authentication
process can be performed by an existing Identity Provider (IdP).

.. note::

Ceph GLUE SSO support relies on onelogin's
`python-saml <https://pypi.org/project/python-saml/\>`\_ library. Please
ensure that this library is installed on your system, either by using
your distribution's package management or via Python's `pip` installer.

To configure SSO on Ceph GLUE, you should use the following
command::

\$ ceph GLUE sso setup saml2 <ceph_GLUE_base_url\>
<idp_metadata\> {<idp_username_attribute\>} {<idp_entity_id\>}
{<sp_x_509_cert\>} {<sp_private_key\>}

Parameters:

-   **<ceph_GLUE_base_url\>**: Base URL where Ceph GLUE is
    accessible (e.g., `https://cephGLUE.local`)
-   **<idp_metadata\>**: URL to remote (`http://`, `https://`) or local
    (`file://`) path or content of the IdP metadata XML (e.g.,
    `https://myidp/metadata`, `file:///home/myuser/metadata.xml`).
-   **<idp_username_attribute\>** *(optional)*: Attribute that should be
    used to get the username from the authentication response. Defaults
    to `uid`.
-   **<idp_entity_id\>** *(optional)*: Use this when more than one entity
    id exists on the IdP metadata.
-   **<sp_x_509_cert\> / <sp_private_key\>** *(optional)*: File path of
    the certificate that should be used by Ceph GLUE (Service
    Provider) for signing and encryption.

.. note::

The issuer value of SAML requests will follow this pattern:
**<ceph_GLUE_base_url\>**/auth/saml2/metadata

To display the current SAML 2.0 configuration, use the following
command::

\$ ceph GLUE sso show saml2

.. note::

For more information about `onelogin_settings`, please check the
`onelogin documentation <https://github.com/onelogin/python-saml\>`\_.

To disable SSO::

\$ ceph GLUE sso disable

To check if SSO is enabled::

\$ ceph GLUE sso status

To enable SSO::

\$ ceph GLUE sso enable saml2

.. \_GLUE-alerting:

## Enabling Prometheus Alerting


To use Prometheus for alerting you must define
`alerting rules <https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules\>`*.
These are managed by the
`Alertmanager <https://prometheus.io/docs/alerting/alertmanager\>`*. If
you are not yet using the Alertmanager,
`install it <https://github.com/prometheus/alertmanager#install\>`\_ as
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
`configured   <https://prometheus.io/docs/alerting/configuration/\>`\_
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
        - url: '<url-to-GLUE\>/api/prometheus_receiver'

Ensure that the Alertmanager considers your SSL certificate in terms of
the GLUE as valid. For more information about the correct
configuration checkout the
`<http_config\> documentation   <https://prometheus.io/docs/alerting/configuration/#%3Chttp_config%3E\>`\_.

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

    $ ceph GLUE set-alertmanager-api-host <alertmanager-host:port\>  # default: ''

For example::

    $ ceph GLUE set-alertmanager-api-host 'http://localhost:9093'

To be able to see all configured alerts, you will need to configure the
URL to the Prometheus API. Using this API, the UI will also help you in
verifying that a new silence will match a corresponding alert.

::

    $ ceph GLUE set-prometheus-api-host <prometheus-host:port\>  # default: ''

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





