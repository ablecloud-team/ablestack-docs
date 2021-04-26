# Glue 설정 가이드
내용을 준비하고 있습니다. 불편을 드려 죄송합니다.

## 활성화

If you have installed `ceph-mgr-GLUE` from distribution packages,
the package management system should take care of installing all
required dependencies.

If you're building Ceph from source and want to start the GLUE from
your development environment, please see the files `README.rst` and
`HACKING.rst` in the source directory `src/pybind/mgr/GLUE`.

Within a running Ceph cluster, the Ceph GLUE is enabled with::

\$ ceph mgr module enable GLUE

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
*name − idashboard.crt* ceph GLUE
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





