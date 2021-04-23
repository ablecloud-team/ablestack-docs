# Cloud 관리

## 태그를 사용하여 클라우드에서 리소스 구성
태그는 클라우드의 리소스에 대한 메타 데이터를 저장하는 키-값 쌍입니다. 태그는 리소스를 분류하는 데 유용합니다. 예를 들어 사용자의 거주 도시를 나타내는 값으로 사용자 VM에 태그를 지정할 수 있습니다. 이 경우 키는 "city"이고 값은 "Toronto"또는 "Tokyo"가 될 수 있습니다. 그런 다음 Mold에 요청하여 지정된 태그가 있는 모든 리소스를 찾을 수 있습니다. 예를 들어 특정 도시의 사용자를 위한 VM입니다.

사용자 가상 머신, 볼륨, 스냅샷, 게스트 네트워크, 템플릿, ISO, 방화벽 규칙, 포트 전달 규칙, 퍼블릭 IP 주소, 보안 그룹,로드 밸런서 규칙, 프로젝트, VPC, 네트워크 ACL 또는 고정 경로에 태그를 지정할 수 있습니다. 원격 액세스 VPN에는 태그를 지정할 수 없습니다.

UI 또는 API 명령 createTags, deleteTags 및 listTags를 통해 태그로 작업할 수 있습니다. 각 리소스에 대해 여러 태그를 정의할 수 있습니다. 정의할 수 있는 태그 수에는 제한이 없습니다. 각 태그의 길이는 최대 255 자입니다. 사용자는 자신이 소유 한 리소스에 태그를 정의할 수 있으며 관리자는 클라우드의 모든 리소스에 태그를 정의할 수 있습니다.

선택적인 입력 매개 변수인 "tags"는 많은 list * API 명령에 존재합니다. 다음 예는 이 새 매개 변수를 사용하여 region = canada 또는 태그 city = Toronto 태그가 있는 모든 볼륨을 찾는 방법을 보여줍니다.

````
command=listVolumes
   &listAll=true
   &tags[0].key=region
   &tags[0].value=canada
   &tags[1].key=city
   &tags[1].value=Toronto
````
다음 API 명령에는 "태그"입력 매개 변수가 있습니다.

- listVirtualMachines
- listVolumes
- listSnapshots
- listNetworks
- listTemplates
- listIsos
- listFirewallRules
- listPortForwardingRules
- listPublicIpAddresses
- listSecurityGroups
- listLoadBalancerRules
- listProjects
- listVPCs
- listNetworkACLs
- listStaticRoutes

## CPU 소켓 리포트
PRODUCT는 하나 이상의 물리적 CPU 소켓을 포함하는 여러 유형의 호스트를 관리합니다. CPU 소켓은 클라우드 인프라 라이선스 및 청구에 사용되는 측정 단위로 간주됩니다. PRODUCT는 청구 목적으로 CPU 소켓 통계를 수집하기 위해 UI 및 API 지원을 모두 제공합니다. 인프라 탭에는 CPU 소켓에 대한 새 탭이 있습니다. 클라우드 크기를 반영하는 PRODUCT에서 관리하는 CPU 소켓에 대한 통계를 볼 수 있습니다. CPU 소켓 페이지는 각 호스트 유형에 사용되는 호스트 및 소켓의 수를 제공합니다.

1. PRODUCT UI에 로그인합니다.
2. 왼쪽 탐색 모음에서 인프라를 클릭합니다.
3. CPU 소켓에서 모두보기를 클릭합니다.
   
    CPU 소켓 페이지가 표시됩니다. 이 페이지에는 하이퍼 바이저 유형에 따라 호스트 및 CPU 소켓 수가 표시됩니다.

## 데이터베이스 구성 변경
Mold 관리 서버는 /etc/cloudstack/management/db.properties 파일에 데이터베이스 구성 정보 (예 : 호스트 이름, 포트, 자격 증명)를 저장합니다. 변경 사항을 적용하려면 각 Management Server에서 이 파일을 편집 한 다음 Management Server를 다시 시작하십시오.

## 데이터베이스 비밀번호 변경
Mold에서 사용하는 MySQL 계정의 비밀번호를 변경해야 할 수 있습니다. 그렇다면 MySQL에서 비밀번호를 변경 한 다음 암호화된 비밀번호를 /etc/cloudstack/management/db.properties 에 추가해야합니다.

1. 암호를 변경하기 전에 해당 구성 요소를 배포 한 경우 Mold의 관리 서버 및 사용 엔진을 중지해야합니다.
    ````
    # service cloudstack-management stop
    # service cloudstack-usage stop
    ````
2. 다음으로 MySQL 서버에서 Mold 사용자의 비밀번호를 업데이트합니다.
    ````
    # mysql -u root -p
    ````
   
    MySQL 셸에서 비밀번호를 변경하고 권한을 플러시합니다.
   
    ````
    update mysql.user set password=PASSWORD("newpassword123") where User='cloud';
    flush privileges;
    quit;
    ````
3. 다음 단계는 비밀번호를 암호화하고 암호화된 비밀번호를 Mold의 데이터베이스 구성 ( /etc/cloudstack/management/db.properties)에 복사하는 것 입니다.
    ````
    # java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.2.jar \ org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh \ input="newpassword123" password="`cat /etc/cloudstack/management/key`" \ verbose=false
    ````

## 파일 암호화 유형
이것은 파일 암호화 유형에 대한 것입니다. 웹 암호화 유형을 사용하는 경우 password =”management_server_secret_key”를 사용합니다.

1. 이제 새 암호 텍스트로 /etc/cloudstack/management/db.properties 를 업데이트합니다. 텍스트 편집기에서 /etc/cloudstack/management/db.properties 를 열고 다음 매개 변수를 업데이트하십시오.
    ````
    db.cloud.password=ENC(encrypted_password_from_above)
    db.usage.password=ENC(encrypted_password_from_above)
    ````
2. 새 비밀번호를 복사 한 후 이제 Mold(필요하다면 usage engine도 함께)을 시작할 수 있습니다. 
    ````
    # service cloudstack-management start
    # service cloud-usage start
    ````

## 관리자 경고
시스템은 클라우드 관리에 도움이되는 경고 및 이벤트를 제공합니다. 경고는 관리자에게 보내는 알림으로 일반적으로 이메일로 전달되어 관리자에게 클라우드에서 오류가 발생했음을 알립니다. 경고 동작을 구성 할 수 있습니다.

이벤트는 클라우드의 모든 사용자 및 관리자 작업을 추적합니다. 예를 들어 모든 게스트 VM 시작은 관련 이벤트를 생성합니다. 이벤트는 Management Server의 데이터베이스에 저장됩니다.

다음과 같은 경우 관리자에게 이메일이 발송됩니다.

- 관리 서버 클러스터의 CPU, 메모리 또는 저장소 리소스가 부족합니다.
- 관리 서버가 3 분 이상 호스트에서 하트 비트를 잃음
- 호스트 클러스터의 CPU, 메모리 또는 스토리지 리소스가 부족합니다.

### 외부 SNMP 및 Syslog 관리자로 경고 보내기
Mold UI의 대시 보드에 관리자 경고를 표시하고 이메일로 보내는 것 외에도 Mold는 동일한 경고를 외부 SNMP 또는 Syslog 관리 소프트웨어로 보낼 수도 있습니다. 이는 SNMP 또는 Syslog 관리자를 사용하여 클라우드를 모니터링하려는 경우 유용합니다.

보낼 수 있는 경고는 다음과 같습니다.

다음은 경고 유형 번호 목록입니다. 현재 경보는 listAlerts를 호출하여 찾을 수 있습니다.
````
MEMORY = 0 // Available Memory below configured threshold
````
````
CPU = 1 // Unallocated CPU below configured threshold
````
````
STORAGE =2 // Available Storage below configured threshold
````
````
STORAGE_ALLOCATED = 3 // Remaining unallocated Storage is below configured threshold
````
````
PUBLIC_IP = 4 // Number of unallocated virtual network public IPs is below configured threshold
````
````
PRIVATE_IP = 5 // Number of unallocated private IPs is below configured threshold
````
````
SECONDARY_STORAGE = 6 //  Available Secondary Storage in availability zone is below configured threshold
````
````
HOST = 7 // Host related alerts like host disconnected
````
````
USERVM = 8 // User VM stopped unexpectedly
````
````
DOMAIN_ROUTER = 9 // Domain Router VM stopped unexpectedly
````
````
CONSOLE_PROXY = 10 // Console Proxy VM stopped unexpectedly
````
````
ROUTING = 11 // Lost connection to default route (to the gateway)
````
````
STORAGE_MISC = 12 // Storage issue in system VMs
````
````
USAGE_SERVER = 13 // No usage server process running
````
````
MANAGMENT_NODE = 14 // Management network CIDR is not configured originally
````
````
DOMAIN_ROUTER_MIGRATE = 15 // Domain Router VM Migration was unsuccessful
````
````
CONSOLE_PROXY_MIGRATE = 16 // Console Proxy VM Migration was unsuccessful
````
````
USERVM_MIGRATE = 17 // User VM Migration was unsuccessful
````
````
VLAN = 18 // Number of unallocated VLANs is below configured threshold in availability zone
````
````
SSVM = 19 // SSVM stopped unexpectedly
````
````
USAGE_SERVER_RESULT = 20 // Usage job failed
````
````
STORAGE_DELETE = 21 // Failed to delete storage pool
````
````
UPDATE_RESOURCE_COUNT = 22 // Failed to update the resource count
````
````
USAGE_SANITY_RESULT = 23 // Usage Sanity Check failed
````
````
DIRECT_ATTACHED_PUBLIC_IP = 24 // Number of unallocated shared network IPs is low in availability zone
````
````
LOCAL_STORAGE = 25 // Remaining unallocated Local Storage is below configured threshold
````
````
RESOURCE_LIMIT_EXCEEDED = 26 //Generated when the resource limit exceeds the limit. Currently used for recurring snapshots only
````

API 명령 (listAlerts)을 호출하여 최신 목록을 표시 할 수도 있습니다.

**SNMP 경고 세부 정보**

지원되는 프로토콜은 SNMP 버전 2입니다.

각 SNMP 트랩에는 message, podId, dataCenterId, clusterId 및 generationTime 정보가 포함됩니다.

**Syslog 경고 세부 정보**

Mold는 모든 경고에 대해 syslog 메시지를 생성합니다. 각 syslog 메시지는 다음 형식으로 alertType, message, podId, dataCenterId 및 clusterId 필드를 포함합니다. 필드에 유효한 값이 없으면 포함되지 않습니다.
````
Date severity_level Management_Server_IP_Address/Name  alertType:: value dataCenterId:: value  podId:: value  clusterId:: value  message:: value
````
예를 들면 :
````
Mar  4 10:13:47    WARN    localhost    alertType:: managementNode message:: Management server node 127.0.0.1 is up
````
**SNMP 및 Syslog 관리자 구성**

Mold에서 경고를 수신하도록 하나 이상의 SNMP 관리자 또는 Syslog 관리자를 구성하려면 :

1. SNMP 관리자의 경우 SNMP 관리자 시스템에 Mold MIB 파일을 설치합니다. 이것은 SNMP OID를 사용자가 더 쉽게 읽을 수 있는 트랩 유형에 매핑합니다. 파일은 공개적으로 사용 가능해야합니다. 이 파일을 설치하는 방법에 대한 자세한 내용은 SNMP 관리자와 함께 제공된 설명서를 참조하십시오.

2. /etc/cloudstack/management/log4j-cloud.xml 파일을 편집하십시오.
````
# vi /etc/cloudstack/management/log4j-cloud.xml
````
3. 아래 표시된 구문을 사용하여 항목을 추가하십시오. SNMP 관리자를 추가하는지 아니면 Syslog 관리자를 추가하는지에 따라 적절한 예를 따르십시오. 여러 외부 관리자를 지정하려면 IP 주소 및 기타 구성 값을 쉼표 (,)로 구분하십시오.
    
    !!! Note
        권장되는 최대 SNMP 또는 Syslog 관리자 수는 각각 20 개입니다.

    다음 예는 IP 주소 10.1.1.1 및 10.1.1.2에서 두 개의 SNMP 관리자를 구성하는 방법을 보여줍니다. 자신의 IP 주소, 포트 및 커뮤니티를 대체하십시오. 다른 값 (이름, 임계 값, 클래스 및 레이아웃 값)은 변경하지 마십시오.
    ````
    <appender name="SNMP" class="org.apache.cloudstack.alert.snmp.SnmpTrapAppender">
      <param name="Threshold" value="WARN"/>  <!-- Do not edit. The alert feature assumes WARN. -->
      <param name="SnmpManagerIpAddresses" value="10.1.1.1,10.1.1.2"/>
      <param name="SnmpManagerPorts" value="162,162"/>
      <param name="SnmpManagerCommunities" value="public,public"/>
      <layout class="org.apache.cloudstack.alert.snmp.SnmpEnhancedPatternLayout"> <!-- Do not edit -->
        <param name="PairDelimeter" value="//"/>
        <param name="KeyValueDelimeter" value="::"/>
      </layout>
    </appender>
    ````
    다음 예는 IP 주소 10.1.1.1 및 10.1.1.2에서 두 개의 Syslog 관리자를 구성하는 방법을 보여줍니다. 자신의 IP 주소로 대체하십시오. Facility를 LOCAL0-LOCAL7과 같은 syslog 정의 값으로 설정할 수 있습니다. 다른 값은 변경하지 마십시오.
    ````
    <appender name="ALERTSYSLOG">
      <param name="Threshold" value="WARN"/>
      <param name="SyslogHosts" value="10.1.1.1,10.1.1.2"/>
      <param name="Facility" value="LOCAL6"/>
      <layout>
        <param name="ConversionPattern" value=""/>
      </layout>
    </appender>
    ````

4. 클라우드에 여러 관리 서버 노드가있는 경우이 단계를 반복하여 모든 인스턴스에서 log4j-cloud.xml을 편집하십시오.
5. 관리 서버가 실행되는 동안 이러한 변경을 수행 한 경우 변경 사항이 적용될 때까지 몇 분 정도 기다리십시오.

문제 해결 : 적절한 시간이 지난 후에도 구성된 SNMP 또는 Syslog 관리자에 경고가 나타나지 않으면 log4j-cloud.xml의 <appender> 항목 구문에 오류가있을 수 있습니다. 형식과 설정이 올바른지 확인하십시오.

**SNMP 또는 Syslog 관리자 삭제**

Mold에서 더 이상 경고를 수신하지 않도록 외부 SNMP 관리자 또는 Syslog 관리자를 제거하려면 /etc/cloudstack/management/log4j-cloud.xml 파일에서 해당 항목을 제거하십시오.

## 네트워크 도메인 이름 사용자 지정
루트 관리자는 선택적으로 네트워크, 계정, 도메인, 영역 또는 전체 Mold 설치 수준에서 사용자 지정 DNS 접미사를 할당할 수 있으며 도메인 관리자는 자신의 도메인 내에서이를 수행할 수 있습니다. 사용자 정의 도메인 이름을 지정하고 적용하려면 다음 단계를 따르십시오.

1. 원하는 범위에서 DNS 접미사 설정
    - 네트워크 수준에서 DNS 접미사는 새 네트워크를 만들 때 UI를 통해 할당 되거나 Mold API의 updateNetwork 명령을 사용하여 할당될 수 있습니다 .
    - 계정, 도메인 또는 영역 수준에서 적절한 Mold API 명령 (createAccount, editAccount, createDomain, editDomain, createZone 또는 editZone)을 사용하여 DNS 접미사를 할당할 수 있습니다.
    - 전역 수준에서 구성 매개 변수 guest.domain.suffix를 사용합니다. Mold API 명령 updateConfiguration을 사용할 수도 있습니다. 이 전역 구성을 수정 한 후 관리 서버를 다시 시작하여 새 설정을 적용하십시오.
2. 새 DNS 접미사를 기존 네트워크에 적용하려면 Mold API 명령 updateNetwork를 호출합니다. 새 네트워크를 생성하는 동안 DNS 접미사가 지정된 경우이 단계는 필요하지 않습니다.

사용되는 네트워크 도메인의 소스는 다음 규칙에 따라 다릅니다.

- 모든 네트워크에서 네트워크 도메인이 네트워크 자체 구성의 일부로 지정된 경우 해당 값이 사용됩니다.
- 계정 별 네트워크의 경우 계정에 지정된 네트워크 도메인이 사용됩니다. 아무 것도 지정하지 않으면 시스템은 도메인, 영역 및 전역 구성에서 해당 순서로 값을 찾습니다.
- 도메인 별 네트워크의 경우 도메인에 지정된 네트워크 도메인이 사용됩니다. 지정되지 않은 경우 시스템은 영역 및 전역 구성에서 값을 순서대로 찾습니다.
- 영역 별 네트워크의 경우 영역에 지정된 네트워크 도메인이 사용됩니다. 지정되지 않은 경우 시스템은 전역 구성에서 값을 찾습니다.

## 관리 서버 중지 및 다시 시작
루트 관리자는 때때로 Management Server를 중지했다가 다시 시작해야합니다.

예를 들어, 글로벌 구성 매개 변수를 변경 한 후 다시 시작해야합니다. 관리 서버 노드가 여러 개인 경우 모든 노드를 다시 시작하여 새 매개 변수 값을 클라우드 전체에 일관되게 적용하십시오.

관리 서버를 중지하려면 관리 서버 노드의 운영 체제 프롬프트에서 다음 명령을 실행하십시오.
````
# service cloudstack-management stop
````
관리 서버를 시작하려면 :
````
# service cloudstack-management start
````





