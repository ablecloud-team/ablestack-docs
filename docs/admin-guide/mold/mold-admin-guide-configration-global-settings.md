
# 글로벌 설정

## 개요
Mold 환경 전체에 적용되는 글로벌 설정 항목을 확인하고 수정할 수 있는 기능을 제공합니다.

![글로벌 설정](../../assets/images/admin-guide/mold/configration/global-settings/mold-admin-guide-configration-global-settings-1-1.png){ .imgCenter .imgBorder }

## 글로벌 설정 메뉴 주요 기능
* 환경 설정 확인 및 변경
    * 각 설정 항목은 키(Key), 설명, 현재 값(Value)으로 표시됩니다.
* 설정 초기화
    * 각 설정 항목의 오른쪽에 있는 원형 화살표(⟳) 버튼을 눌러 기본값으로 되돌릴 수 있습니다.

## 설정 카테고리 설명
<style>
  .highlight-box {
    background-color: #fbe4d5;
    padding: 2px 6px;
    border-radius: 4px;
    border: 1px solid #f0c5b5;
    font-family: monospace;
  }
</style>

* All Settings
    * 모든 글로벌 설정 항목을 한 화면에서 볼 수 있습니다.
* Access
    * 사용자 접근 제어 및 계정 관리 관련 설정 항목입니다.
<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Account</th>
        <th>Account allow expose host hostname (account.allow.expose.host.hostname)</th>
        <th>가상 머신 내부에서 하이퍼바이저 호스트명을 확인할 수 있게 합니다. 디버깅, 로깅, 모니터링, 보안 및 감사에 이용할 수 있습니다. <span style="color:red;">&lt;주의&gt; 호스트 정보를 알게 되면, 내부 구조 노출로 이어질 수 있습니다.</span> 여러 사용자가 공유하는 클라우드에서는 이 설정을 <span class="highlight-box">false</span>로 유지하는 것이 일반적입니다.</th>
    </tr>    
    <tr>
        <th>Account</th>
        <th>Account cleanup interval (account.cleanup.interval)</th>
        <th>비활성화된 계정의 리소스(가상 머신, 볼륨, 스냅샷 등)를 삭제하는 작업의 주기입니다. 활성 계정의 리소스에는 영향을 주지 않습니다.</th>
    </tr>      
    <tr>
        <th>Account</th>
        <th>Enable account settings for domain (enable.account.settings.for.domain)</th>
        <th>도메인 관리자에게 계정 설정 변경 권한을 줍니다. 계정의 리소스 제한, 템플릿 공유, 시스템 IP 사용 등을 변경할 수 있게 됩니다.</th>
    </tr>          
    <tr>
        <th>Account</th>
        <th>Max account cpus (max.account.cpus)</th>
        <th>하나의 계정이 생성할 수 있는 가상 머신의 총 vCPU입니다. 이미 생성된 가상 머신에는 영향을 주지 않고, 새로운 가상 머신 생성 또는 확장 시 적용됩니다.</th>
    </tr>             
    <tr>
        <th>Account</th>
        <th>Max account memory (max.account.memory)</th>
        <th>하나의 계정이 점유할 수 있는 가상 머신의 총 메모리량 입니다. 이미 생성된 가상 머신에는 영향을 주지 않고, 새로운 가상 머신 생성 또는 확장 시 적용됩니다.(단위 MiB)</th>
    </tr>                  
    <tr>
        <th>Account</th>
        <th>Max account networks (max.account.networks)</th>
        <th>하나의 계정이 생성할 수 있는 네트워크의 수를 제한합니다. 이미 생성된 네트워크에는 영향을 주지 않고, 새로운 네트워크 생성 시 적용됩니다.</th>
    </tr>                   
    <tr>
        <th>Account</th>
        <th>Max account primary storage (max.account.primary.storage)</th>
        <th>하나의 계정이 사용할 수 있는 기본 스토리지의 용량을 제한합니다. 이미 생성된 볼륨에는 영향을 주지 않고, 새로운 볼륨 생성 시 적용됩니다.(단위 GiB)</th>
    </tr>                
    <tr>
        <th>Account</th>
        <th>Max account projects (max.account.projects)</th>
        <th>하나의 계정이 생성할 수 있는 프로젝트의 수를 제한합니다. 이미 생성된 프로젝트에는 영향을 주지 않고, 새로운 프로젝트 생성 시 적용됩니다.</th>
    </tr>                              
    <tr>
        <th>Account</th>
        <th>Max account public ips (max.account.public.ips)</th>
        <th>하나의 계정이 점유할 수 있는 Public IP 수를 제한합니다. 이미 할당된 IP에는 영향을 주지 않고, 새로운 IP 할당 시 적용됩니다.</th>
    </tr>         
    <tr>
        <th>Account</th>
        <th>Max account secondary storage (max.account.secondary.storage)</th>
        <th>하나의 계정이 사용할 수 있는 세컨 스토리지 용량을 제한합니다. 이미 사용된 용량에는 영향을 주지 않고, 새로운 비운용 데이터(템플릿, ISO, 스냅샷) 저장 시 적용됩니다.(단위 GiB)</th>
    </tr>                                      
    <tr>
        <th>Account</th>
        <th>Max account snapshots (max.account.snapshots)</th>
        <th>하나의 계정이 생성할 수 있는 스냅샷의 수를 제한합니다. 이미 생성된 스냅샷에는 영향을 주지 않고, 새로운 스냅샷 저장 시 적용됩니다.</th>
    </tr>                                
    <tr>
        <th>Account</th>
        <th>Max account templates (max.account.templates)</th>
        <th>하나의 계정이 생성할 수 있는 템플릿의 수를 제한합니다. 이미 생성된 템플릿에는 영향을 주지 않고, 새로운 템플릿 저장 시 적용됩니다.</th>
    </tr>            
    <tr>
        <th>Account</th>
        <th>Max account user vms (max.account.user.vms)</th>
        <th>하나의 계정이 생성할 수 있는 게스트 가상 머신의 수를 제한합니다. 이미 생성된 가상 머신에는 영향을 주지 않고, 새로운 가상 머신 생성 시 적용됩니다.</th>
    </tr>                               
    <tr>
        <th>Account</th>
        <th>Max account volumes (max.account.volumes)</th>
        <th>하나의 계정이 생성할 수 있는 볼륨의 수를 제한합니다. 이미 생성된 볼륨에는 영향을 주지 않고, 새로운 볼륨 생성 시 적용됩니다.</th>
    </tr>   
    <tr>
        <th>Account</th>
        <th>Max account vpcs (max.account.vpcs)</th>
        <th>하나의 계정이 생성할 수 있는 VPC의 수를 제한합니다. 이미 생성된 VPC에는 영향을 주지 않고, 새로운 VPC 생성 시 적용됩니다.</th>
    </tr>  
    <tr>
        <th>Domain</th>
        <th>Allow domain admins to create tagged offerings (allow.domain.admins.to.create.tagged.offerings)</th>
        <th>도메인 관리자에게 태그가 설정된 오퍼링을 생성하는 권한을 줍니다. 호스트 태그가 설정된 오퍼링은 특정 호스트에 가상 머신을 배치할 수 있습니다.</th>
    </tr>                                       
    <tr>
        <th>Domain</th>
        <th>Allow user view all domain accounts (allow.user.view.all.domain.accounts)</th>
        <th>일반 사용자에게 자신의 도메인 내 모든 계정을 조회할 수 있는 권한을 줍니다. 조회 권한만 부여되며, 다른 계정의 리소스의 접근하거나 수정할 수 있는 권한은 포함하지 않습니다.</th>
    </tr>                                       
    <tr>
        <th>Domain</th>
        <th>Enable domain settings for child domain (enable.domain.settings.for.child.domain)</th>
        <th>상위 도메인의 정책이 하위 도메인에 적용되는지 여부입니다. 리소스 제한, 오퍼링 접근, 템플릿 공유 정책 등이 자동 적용됩니다. 도메인 관리자의 권한 범위와 격리 수준에 직접적인 영향이 미치므로, 멀티 테넌시 환경에서는 <span class="highlight-box">false</span>를 유지하는 것이 바람직합니다.</th>
    </tr>             
    <tr>
        <th>Domain</th>
        <th>Guest domain suffix (guest.domain.suffix)</th>
        <th>게스트 가상 머신에 적용되느 DNS접미사입니다. 모든 게스트 네트워크에 기본적으로 적용됩니다. 도메인, 계정, 네트워크, Zone 수준에서는 개별적으로 덮어쓰기가 가능합니다. Ablestack 내부 DNS 이름 구성에만 적용되며, 외부 DNS 에는 영향을 주지 않습니다. DNS 서버가 Ablestack 의 설정을 반영하도록 구성되어 있어야 합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Guest domain suffix (guest.domain.suffix)</th>
        <th>게스트 가상 머신에 적용되느 DNS접미사입니다. 모든 게스트 네트워크에 기본적으로 적용됩니다. 도메인, 계정, 네트워크, Zone 수준에서는 개별적으로 덮어쓰기가 가능합니다. Ablestack 내부 DNS 이름 구성에만 적용되며, 외부 DNS 에는 영향을 주지 않습니다. DNS 서버가 Ablestack 의 설정을 반영하도록 구성되어 있어야 합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain cpus (max.domain.cpus)</th>
        <th>도메인에서 할당 가능한 CPU 코어 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain memory (max.domain.memory)</th>
        <th>도메인에서 할당 가능한 메모리 용량의 상한을 정합니다.(단위 MiB)</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain networks (max.domain.networks)</th>
        <th>도메인에서 생성 가능한 네트워크 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain primary storage (max.domain.primary.storage)</th>
        <th>도메인에서 사용 가능한 기본스토리지 용량의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain projects (max.domain.projects)</th>
        <th>도메인에서 생성 가능한 프로젝트 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain public ips (max.domain.public.ips)</th>
        <th>도메인에서 사용할 수 있는 퍼블릭 IP 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain secondary storage (max.domain.secondary.storage)</th>
        <th>도메인에서 사용 가능한 2차 스토리지 용량의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain snapshots (max.domain.snapshots)</th>
        <th>도메인에서 생성 가능한 스냅샷 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain templates (max.domain.templates)</th>
        <th>도메인에서 배포 가능한 템플릿 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain user vms (max.domain.user.vms)</th>
        <th>도메인에서 배포 가능한 가상머신 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain volumes (max.domain.volumes)</th>
        <th>도메인에서 생성 가능한 볼륨 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Max domain vpcs (max.domain.vpcs)</th>
        <th>도메인에서 생성 가능한 VPC 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Metadata allow expose domain (metadata.allow.expose.domain)</th>
        <th>true 로 정할 경우, 가상머신의 도메인이 메타데이터에서 보이게 됩니다.</th>
    </tr>     
    <tr>
        <th>Domain</th>
        <th>Monitoring wall portal domain (monitoring.wall.portal.domain)</th>
        <th>모니터링 서비스 Wall 접속 페이지</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project cpus (max.project.cpus)</th>
        <th>프로젝트에서 사용 가능한 CPU 코어 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project memory (max.project.memory)</th>
        <th>프로젝트에서 사용 가능한 메모리 용량의 상한을 정합니다.(단위 MiB)</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project networks (max.project.networks)</th>
        <th>프로젝트에서 생성 가능한 네트워크 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project primary storage (max.project.primary.storage)</th>
        <th>프로젝트에서 사용 가능한 기본 스토리지 용량의 상한을 저앟ㅂ니다.(단위 GiB)</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project public ips (max.project.public.ips)</th>
        <th>프로젝트에서 사용할 수 있는 퍼블릭 IP 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project secondary storage (max.project.secondary.storage)</th>
        <th>프로젝트에서 사용 가능한 2차 스토리지 용량의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project snapshots (max.project.snapshots)</th>
        <th>프로젝트에서 생성 가능한 스냅샷 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project templates (max.project.templates)</th>
        <th>프로젝트에서 배포 가능한 템플릿 수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project user vms (max.project.user.vms)</th>
        <th>프로젝트에서 배포 가능한 가상머신 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project volumes (max.project.volumes)</th>
        <th>프로젝트에서 생성 가능한 볼륨 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Max project vpcs (max.project.vpcs)</th>
        <th>프로젝트에서 생성 가능한 VPC 갯수의 상한을 정합니다.</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project email sender (project.email.sender)</th>
        <th>프로젝트 초대 이메일을 보낼 때 표시될 발신자</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project invite required (project.invite.required)</th>
        <th>프로젝트에 계정 추가시 초대 여부를 확인할지 정합니다. 기본값은 false</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project invite timeout (project.invite.timeout)</th>
        <th>프로젝트 초대 만료시간. 기본값 1일 - 86400 초 </th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project smtp enabledSecurityProtocols (project.smtp.enabledSecurityProtocols)</th>
        <th>smtp 연결시 사용할 프로토콜 버전을 지정합니다. 공백으로 구분합니다; 예시) "TLSv1 TLSv1.1". 지원 프로토콜: SSLv2Hello, SSLv3, TLSv1, TLSv1.1, TLSv1.2</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project smtp host (project.smtp.host)</th>
        <th>smtp 서버</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project smtp password (project.smtp.password)</th>
        <th>smtp 비밀번호</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project smtp port (project.smtp.port)</th>
        <th>smtp 포트</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project smtp useAuth (project.smtp.useAuth)</th>
        <th>메일 발송시 smtp 인증 필요</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project smtp username (project.smtp.username)</th>
        <th>(project.smtp.useAuth)가 true 일 경우, 인증에 사용될 유저명</th>
    </tr>     
    <tr>
        <th>Project</th>
        <th>Project smtp useStartTLS (project.smtp.useStartTLS)</th>
        <th>(project.smtp.useAuth)가 true 일 경우, StartTLS 를 통해 연결을 암호화합니다.</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap basedn (ldap.basedn)</th>
        <th>LDAP 에 사용할 base dn</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap bind password (ldap.bind.password)</th>
        <th>바인드 계정의 비밀번호</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap bind principal (ldap.bind.principal)</th>
        <th>바인드 계정</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap email attribute (ldap.email.attribute)</th>
        <th>이메일 주소를 가져올 속성값</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap firstname attribute (ldap.firstname.attribute)</th>
        <th>이름을 가져올 속성값</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap group object (ldap.group.object)</th>
        <th>그룹으로 지정할 객체</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap group user uniquemember (ldap.group.user.uniquemember)</th>
        <th>각 멤버를 식별할 수 있는 속성값</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap lastname attribute (ldap.lastname.attribute)</th>
        <th>성을 가져올 속성값</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap nested groups enable (ldap.nested.groups.enable)</th>
        <th>중첩 그룹도 조회합니다.</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap provider (ldap.provider)</th>
        <th>LDAP 서비스 종류; 예시) openldap, microsoftad</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap read timeout (ldap.read.timeout)</th>
        <th>밀리초로 계산된 LDAP 연결 제한시간</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap request page size (ldap.request.page.size)</th>
        <th>사용자 검색 요청시 한 번에 가져올 사용자 수</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap search group principle (ldap.search.group.principle)</th>
        <th>사용자가 반드시 속해야 하는 그룹</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap truststore (ldap.truststore)</th>
        <th>SSL 연결시 사용할 truststore 위치</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap truststore password (ldap.truststore.password)</th>
        <th>truststore 비밀번호</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap user memberof attribute (ldap.user.memberof.attribute)</th>
        <th>그룹을 나타내는 사용자의 속성값</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap user object (ldap.user.object)</th>
        <th>LDAP 에서 사용할 유저의 속성값</th>
    </tr>     
    <tr>
        <th>LDAP</th>
        <th>Ldap username attribute (ldap.username.attribute)</th>
        <th>LDAP 에서 사용할 유저명의 속성값</th>
    </tr>     
                   
</table>    
* Compute
    * CPU, 메모리 관리 등 컴퓨팅 자원 관련 설정 항목입니다.
* Storage
    * 스토리지 관리, 볼륨 관리 등 저장소 관련 설정 항목입니다.
* Network
    * 네트워크 관리 및 트래픽 제어 관련 설정 항목입니다.
* Hypervisor
    * 하이퍼바이저 유형별 특성 및 호스트 관리 관련 설정 항목입니다.
* Management Server
    * 관리 서버의 동작 방식과 관련된 설정 항목입니다.
* System VMs
    * 시스템 VM(예: 가상 라우터, 콘솔 프록시 등) 관련 설정 항목입니다.
* Infrastructure
    * 인프라 구성 및 운영 환경 설정 항목입니다.
* Miscellaneous
    * 기타 분류되지 않은 일반적인 설정 항목입니다.
