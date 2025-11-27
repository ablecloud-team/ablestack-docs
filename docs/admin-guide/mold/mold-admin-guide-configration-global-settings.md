
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
    <tr>
        <th>SAML</th>
        <th>Saml2 append idpdomain (saml2.append.idpdomain)</th>
        <th>SAML SSO 로 계정/유저 생성시 IdP 를 표시합니다.</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 check signature (saml2.check.signature)</th>
        <th>SAML2 서명을 확인합니다. 검증 실패시 로그인 예외가 발생합니다. 권장되지 않으나 리스크를 감수하고 이전 버전과의 호환성이 필요한 경우 비활성화합니다.</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 default idpid (saml2.default.idpid)</th>
        <th>여러 개의 IdP 가 있을 경우, 기본으로 사용할 IdP entity ID 를 정합니다.</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Ldap username attribute (ldap.username.attribute)</th>
        <th>LDAP 에서 사용할 유저명의 속성값</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 enabled (saml2.enabled)</th>
        <th>SAML2 를 사용합니다.</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 failed login redirect url (saml2.failed.login.redirect.url)</th>
        <th>SAML2 로그인 실패시 리다이렉트될 페이지</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 force authn (saml2.force.authn)</th>
        <th>SAML2 의 로그인시 새로운 인증이 강제됩니다. 하나의 앱(크롬 등)에서 여러 앱이 다른 saml 로그인을 할때 유용합니다.</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 idp metadata url (saml2.idp.metadata.url)</th>
        <th>SAML2 IdP 서비스 메타데이터 XML URL</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 redirect url (saml2.redirect.url)</th>
        <th>SSO 로그인이 성공할 경우 연결할 UI 페이지</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 sigalg (saml2.sigalg)</th>
        <th>SAML 요청시 사용할 알고리즘. 기본은 SHA1, 추가 알고리즘: SHA256, SHA384, SHA512</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 sp contact email (saml2.sp.contact.email)</th>
        <th>SAML2 서비스 문의 메일</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 sp contact person (saml2.sp.contact.person)</th>
        <th>SAML2 서비스 담당자</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 sp id (saml2.sp.id)</th>
        <th>SAML2 서비스 Id</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 sp org name (saml2.sp.org.name)</th>
        <th>SAML2 서비스 조직명</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 sp org url (saml2.sp.org.url)</th>
        <th>SAML2 ABLESTACK 로그아웃 URL</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 sp sso url (saml2.sp.sso.url)</th>
        <th>SAML2 ABLESTACK 로그인 URL</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>SSaml2 timeout (saml2.timeout)</th>
        <th>SAML2 IDP 메타데이터 새로고침 간격, 최소 300 초</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 user attribute (saml2.user.attribute)</th>
        <th>SAML2 응답 처리시 사용자 이름에 사용할 속성명</th>
    </tr>     
    <tr>
        <th>SAML</th>
        <th>Saml2 user sessionkey path (saml2.user.sessionkey.path)</th>
        <th>SAML 유저가 로그인할 때, 세션키 쿠기의 경로 속성명. 없을 경우 (saml2.redirect.url) </th>
    </tr>     
                   
</table>    
* Compute
    * CPU, 메모리 관리 등 컴퓨팅 자원 관련 설정 항목입니다.
<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Virtual Machine</th>
        <th>Affinity processors exclude (affinity.processors.exclude)</th>
        <th>가상머신 할당에서 제외할 호스트 코어를 지정합니다. 호스트 OS와 에이전트 동작이나 네트워크/스토리지 IO를 처리하여 안정적인 관리를 가능하게 하고, 가상머신에 인터럽트없는 코어 집합을 할당할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Affinity processors order (affinity.processors.order)</th>
        <th>호스트 CPU를 가상머신에 할당할 때 어떤 순서로 코어를 배치할지 정합니다. </th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow admin vm on disabled resources (allow.admin.vm.on.disabled.resources)</th>
        <th>비활성화된 클러스터, 파드, 존에 어드민이 가상머신을 배포할 수 있도록 합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow deploy vm if deploy on given host fails (allow.deploy.vm.if.deploy.on.given.host.fails)</th>
        <th>가상머신이 주어진 호스트에서 배포에 실패했을 때, 다른 호스트에서 배포될 수 있게 합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow user expunge recover vm (allow.user.expunge.recover.vm)</th>
        <th>일반 사용자가 가상머신을 완전히 파기하거나 복구할 수 있게 합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow user force stop vm (allow.user.force.stop.vm)</th>
        <th>일반 사용자가 가상머신을 강제로 정지할 수 있게 합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow user view destroyed vm (allow.user.view.destroyed.vm)</th>
        <th>일반 유저가 파기되거나 강제 종료된 자신의 가상머신을 볼 수 있게 합니다. </th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Cluster cpu allocated capacity disablethreshold (cluster.cpu.allocated.capacity.disablethreshold)</th>
        <th>(0과 1사이의 비율로)설정한 값 이상이 되면 해당 클러스터는 더이상 가상머신이 배치되지 않습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Cluster cpu allocated capacity notificationthreshold (cluster.cpu.allocated.capacity.notificationthreshold)</th>
        <th>(0과 1사이의 비율로)설정한 값 이상이 되면 가상머신 배치가 중지될 수 있다는 경고가 뜹니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Cpu overprovisioning factor (cpu.overprovisioning.factor)</th>
        <th>CPU 오버프로비전 비율입니다; 사용가능한 CPU 수는 (실제 CPU 자원)*(오버프로비전 비율) 입니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Enable additional vm configuration (enable.additional.vm.configuration)</th>
        <th>가상머신에 추가적인 설정을 허용합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow additional vm configuration list kvm (allow.additional.vm.configuration.list.kvm)</th>
        <th>KVM에서 허용되는 추가 구성입니다. 쉼표로 구분합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow additional vm configuration list vmware (allow.additional.vm.configuration.list.vmware)</th>
        <th>VMware에서 허용되는 추가 구성입니다. 쉼표로 구분합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Allow additional vm configuration list xenserver (allow.additional.vm.configuration.list.xenserver)</th>
        <th>Xen server에서 허용되는 추가 구성입니다. 쉼표로 구분합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Enable dynamic scale vm (enable.dynamic.scale.vm)</th>
        <th>활성/비활성 운영중 가상머신 확장</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Enable vm network filter allow all traffic (enable.vm.network.filter.allow.all.traffic)</th>
        <th>true로 설정할 경우, 네트워크 ACL/보안 그룹 규칙을 무시하고 unrestricted 상태가 되어 모든 트래픽을 허용합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Instance name (instance.name)</th>
        <th>가상머신이 배포될 때의 명칭.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>List vm default details stats (list.vm.default.details.stats)</th>
        <th>listVirtualMachines API 요청에 명시되지 않은 경우 가상머신 상세 통계를 제공할지 결정합니다. false일 경우, 세부 정보는 기본적으로 [group, nic, secgrp, tmpl, servoff, diskoff, backoff, iso, volume, min, affgrp] 이 됩니다. true일 경우, 통계를 포함한 모든 상세 정보가 반환됩니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Migrate vm across clusters (migrate.vm.across.clusters)</th>
        <th>동일한 클러스터에서 호스트를 찾을 수 없는 경우 가상머신이 다른 클러스터로 마이그레이션될 수 있는지 결정합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Monitoring wall portal vm uri (monitoring.wall.portal.vm.uri)</th>
        <th>모니터링 서비스 Wall 가상머신 URI</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Resource count running vms only (resource.count.running.vms.only)</th>
        <th>자원 제한이 있는 경우 운영 중인 가상머신의 자원만 계산합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Ssh key length (ssh.key.length)</th>
        <th>사용자 SSH 키의 길이를 지정합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>System vm auto reserve capacity (system.vm.auto.reserve.capacity)</th>
        <th>시스템VM 대기용량을 예약할지 결정합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>System vm default hypervisor (system.vm.default.hypervisor)</th>
        <th>시스템VM을 생성하는데 사용할 하이퍼바이저 종류: XenServer, KVM, Hyperv, VirtualBox, Parralels, BareMetal, Ovm, LXC, Any</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>System vm management ip reservation mode strictness (system.vm.management.ip.reservation.mode.strictness)</th>
        <th>활성화될 경우, 시스템VM의 관리 IP 할당이 예약범위 내에서만 할당되며, IP가 부족하거나 충돌할 경우 배포에 실패합니다.(운영 환경 권장) 비활성화될 경우, 범위 밖의 IP 할당이 가능하지만, 예상치 못한 IP 충돌이나 예측 불가능한 배치가 나타날 수 있습니다.(임시/테스트 환경에서만 권장)</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>System vm public ip reservation mode strictness (system.vm.public.ip.reservation.mode.strictness)</th>
        <th>활성화될 경우, 시스템VM의 관리 퍼블릭 IP 할당이 예약범위 내에서만 할당되며, IP가 부족하거나 충돌할 경우 배포에 실패합니다.(운영 환경 권장) 비활성화될 경우, 범위 밖의 IP 할당이 가능하지만, 예상치 못한 IP 충돌이나 예측 불가능한 배치가 나타날 수 있습니다.(임시/테스트 환경에서만 권장)</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>System vm random password (system.vm.random.password)</th>
        <th>관리서버 시작시 시스템VM 비밀번호를 무작위로 설정합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>System vm use local storage (system.vm.use.local.storage)</th>
        <th>시스템VM 을 로컬 스토리지 풀에 배치합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Unmanage vm preserve nics (unmanage.vm.preserve.nics)</th>
        <th>true일 경우, 가상머신을 관리해제할 때, nic(와 MAC 주소)를 제거하지 않습니다. 할당상태이며 예약된 상태는 아닙니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>User vm denied details (user.vm.denied.details)</th>
        <th>일반 사용자가 볼 수 있는 가상머신 설정값입니다. 비어있는 경우, 기본값이 사용됩니다: rootdisksize, cpuOvercommitRatio, memoryOvercommitRatio, Message.ReservedCapacityFreed.Flag</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>User vm readonly details (user.vm.readonly.details)</th>
        <th>콤마로 구분되는 읽기 전용 가상머신 설정/상세 목록</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm allocation algorithm (vm.allocation.algorithm)</th>
        <th>가상머신 배치시 고려되는 호스트 순서 알고리즘입니다. 값은 'random(랜덤)', 'firstfit(조건을 만족하는 첫번째 호스트)', 'userdispersing(분산배치)', 'userconcentratedpod_random(같은 사용자 가상머신을 랜덤 호스트에 모으기)', 'userconcentratedpod_firstfit(같은 사용자의 가상머신을 조건만족하는 첫번째 호스트에 모으기)', 'firstfitleastconsumed(조건을 만족하는 호스트 중 가장 적은 자원을 소비하고 있는 호스트)' 중에 하나입니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm configdrive force host cache use (vm.configdrive.force.host.cache.use)</th>
        <th>true일 경우, ConfigDrive 를 호스트 캐시 스토리지에 생성하도록 강제합니다. 현재 KVM 만 지원합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm configdrive primarypool enabled (vm.configdrive.primarypool.enabled)</th>
        <th>ConfigDrive를 기본 스토리지 풀에 생성해야할 경우. 현재 KVM 만 지원합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm configdrive use host cache on unsupported pool (vm.configdrive.use.host.cache.on.unsupported.pool)</th>
        <th>true일 경우, vm.configdrive.primarypool.enabled 가 true 이고, 기본 스토리지 풀이 ConfigDrive를 지원하지 않으면, ConfigDrive가 호스트 캐시 스토리지에 생성됩니다. </th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm deployment planner (vm.deployment.planner)</th>
        <th>가상머신을 배치하는 배치플래너 알고리즘입니다. 'FirstFitPlanner(조건만족 첫번째 호스트)', 'UserDispersingPlanner(동일 사용자 가상머신 분산배치)', 'UserConcentratedPodPlanner(동일 사용자 가상머신을 하나의 Pod에 집중배치)'</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm destroy forcestop (vm.destroy.forcestop)</th>
        <th>가상머신 삭제시 강제 종료</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk bytes maximum read length (vm.disk.bytes.maximum.read.length)</th>
        <th>디스크의 읽기 요청 한번에 허용되는 최대 길이. 0일 경우 적용되지 않습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk bytes maximum write length (vm.disk.bytes.maximum.write.length)</th>
        <th>디스크의 쓰기 요청 한번에 허용되는 최대 길이. 0일 경우 적용되지 않습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk iops maximum read length (vm.disk.iops.maximum.read.length)</th>
        <th>디스크의 읽기 요청 한번에 허용되는 최대 IOPS. 0일 경우 적용되지 않습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk iops maximum write length (vm.disk.iops.maximum.write.length)</th>
        <th>디스크의 읽기 요청 한번에 허용되는 최대 IOPS. 0일 경우 적용되지 않습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk stats interval (vm.disk.stats.interval)</th>
        <th>가상머신 디스크 통계를 보고하는 간격(초 단위)입니다. 0이나 0보다 작은 값의 경우 비활성화됩니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk stats interval min (vm.disk.stats.interval.min)</th>
        <th>가상머신 디스크 통계를 보고하는 최소 간격(초 단위)입니다. vm.disk.stats.interval 이 이 값보다 작은 경우, 이 값을 사용합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk stats max retention time (vm.disk.stats.max.retention.time)</th>
        <th>가상머신 디스크 통계 기록을 데이터베이스에 기록해두는 최대 시간(분 단위)입니다. 0이나 0보다 작은 값일 경우 비활성화됩니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk stats retention enabled (vm.disk.stats.retention.enabled)</th>
        <th>활성화될 경우, 가상머신 디스크의 통계정보가 데이터베이스에 저장됩니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk throttling bytes_read_rate (vm.disk.throttling.bytes_read_rate)</th>
        <th>사용자 가상머신의 기본 읽기 디스크 IO byte/s</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk throttling bytes_write_rate (vm.disk.throttling.bytes_write_rate)</th>
        <th>사용자 가상머신의 기본 쓰기 디스크 IO byte/s</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk throttling iops_read_rate (vm.disk.throttling.iops_read_rate)</th>
        <th>사용자 가상머신의 기본 읽기 디스크 IO request/s</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm disk throttling iops_write_rate (vm.disk.throttling.iops_write_rate)</th>
        <th>사용자 가상머신의 기본 쓰기 디스크 IO request/s</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm display ovf properties (vm.display.ovf.properties)</th>
        <th>가상머신의 OVF(Open Virtualization Format) 속성을 세부화면에 표시합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm ha alerts enabled (vm.ha.alerts.enabled)</th>
        <th>가상머신 HA 작업에 대한 경고를 활성화합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm ha enabled (vm.ha.enabled)</th>
        <th>가상머신 HA 매니저 활성화, 가상머신 HA 작업(정지, 재시작, 이관, 파기)은 생성될 수 있고 예약된 작업은 실행됩니다; 비활성화된 경우, 새로운 가상머신 HA 작업은 허용되지 않고 예약된 작업은 HA가 재활성화되면 'vm.ha.migration.max.retries' 에 설정된 횟수만큼 재시도됩니다. 'time.between.failures'에 설정된 시간만큼 유지된 후 'time.between.cleanup' 마다 실행되는 클린업 스레드에 의해 파기됩니다. </th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm ha migration max retries (vm.ha.migration.max.retries)</th>
        <th>HA 작업시 가상머신 마이그레이션 최대 시도 횟수</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm instancename flag (vm.instancename.flag)</th>
        <th>가상머신의 호스트명이 하이퍼바이저에 표시됩니다. VMware only</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm job check interval (vm.job.check.interval)</th>
        <th>작업이 완료되었는지 확인하는 간격을 밀리초 단위로 나타냅니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm job lock timeout (vm.job.lock.timeout)</th>
        <th>가상머신 관련 작업(시작, 정지, 이관 등)은 동시성 제어를 위해 락을 필요로 합니다. 이때 락을 획득하기 위해 대기하는 시간을 초 단위로 나타냅니다. 지정된 시간 내에 락을 얻지 못하면 해당 작업은 로직에 따라 실패하거나 재시도합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm job report interval (vm.job.report.interval)</th>
        <th>비동기 가상머신 작업(시작, 정지, 이관, 파기 등)을 처리하는 워커 스레드가 Job의 상태를 보고하는 간격입니다. </th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm job timeout (vm.job.timeout)</th>
        <th>가상머신 작업을 취소 요청하기 전 기다리는 밀리 초 단위 시간입니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm metadata manufacturer (vm.metadata.manufacturer)</th>
        <th>인스턴스 메타데이터에 기록되는 제조사 정보입니다. 임의의 값 변경은 올바른 기능 동작을 방해할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm metadata product (vm.metadata.product)</th>
        <th>인스턴스 메타데이터 기록되는 제품 정보입니다. 임의의 값 변경은 올바른 기능 동작을 방해할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm min cpu speed equals cpu speed divided by cpu overprovisioning factor (vm.min.cpu.speed.equals.cpu.speed.divided.by.cpu.overprovisioning.factor)</th>
        <th>서비스오퍼링에서 제시하는 최소 속도에 상관없이 최소 CPU 속도를 가상머신에 보장합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm min memory equals memory divided by mem overprovisioning factor (vm.min.memory.equals.memory.divided.by.mem.overprovisioning.factor)</th>
        <th>서비스오퍼링에서 제시하는 최소 메모리 용량에 상관없이 최소 메모리 용량을 가상머신에 보장합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm network nic max secondary ipaddresses (vm.network.nic.max.secondary.ipaddresses)</th>
        <th>가상머신 nic 당 지정가능한 보조 ip 수를 정합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm network stats interval (vm.network.stats.interval)</th>
        <th>가상머신 공유 네트워크 통계 보고 간격(초 단위). 0이나 그 이하의 경우 비활성화</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm network stats interval min (vm.network.stats.interval.min)</th>
        <th>가상머신 공유 네트워크 통계 보고 최소 간격(초 단위). vm.network.stats.interval 의 값이 더 작을 경우, 이 값을 사용합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm network throttling rate (vm.network.throttling.rate)</th>
        <th>사용자 가상머신의 기본 네트워크에 적용되는 Mbps/s </th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm op cancel interval (vm.op.cancel.interval)</th>
        <th>작업이 취소되지 않았을 때, 다시 취소 요청하는 간격(초 단위)</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm op cleanup interval (vm.op.cleanup.interval)</th>
        <th>작업을 클린업하는 스레드를 작동시키는 간격(초 단위)</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm op cleanup wait (vm.op.cleanup.wait)</th>
        <th>가상머신 작업이 끝난 후 기록이 삭제되기 전 대기하는 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm op lock state retry (vm.op.lock.state.retry)</th>
        <th>가상머신 작업을 위한 락을 얻기 위해 시도하는 횟수, -1은 무한대</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm op wait interval (vm.op.wait.interval)/th>
        <th>작업이 성공했을 경우 확인하기 위해 기다리는 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm password length (vm.password.length)</th>
        <th>자동으로 생성되는 무작위 비밀번호 길이</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm serviceoffering cpu cores max (vm.serviceoffering.cpu.cores.max)</th>
        <th>서비스오퍼링에서 설정가능한 최대 CPU 코어수. 0은 제한없음</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm serviceoffering ram size max (vm.serviceoffering.ram.size.max)</th>
        <th>서비스오퍼링에서 설정가능한 최대 램 용량. 0은 제한없음</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm stats increment metrics (vm.stats.increment.metrics)</th>
        <th>하이퍼바이저에서 수집하는 가상머신 메트릭(NetworkReadKBs, NetworkWriteKBs, DiskWriteKBs, DiskReadIOs, DiskWriteIOs) 이 누적됩니다. false일 경우 최근 수집된 정보만 표시됩니다. </th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm stats interval (vm.stats.interval)</th>
        <th>가상머신 통계가 에이전트에 의해 수집되는 간격(밀리 초 단위)</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm stats max retention time (vm.stats.max.retention.time)</th>
        <th>가상머신 통계가 데이터베이스에 저장되는 최대 시간. 0이거나 그보다 작은 경우 클린업되지 않음</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm stats user vm only (vm.stats.user.vm.only)</th>
        <th>사용자 가상머신 통계만 수집하고 시스템VM은 제외합니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm strict host tags (vm.strict.host.tags)</th>
        <th>서비스오퍼링의 호스트 태그와 반드시 일치해야 배포하는 태그.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm strict resource limit host tag check (vm.strict.resource.limit.host.tag.check)</th>
        <th>서비스오퍼링의 호스트 태그와 일치하는 호스트에서만 자원제한을 체크하여 가상머신을 배포합니다.false일 경우 태그가 맞지 않아도 자원제한을 확인하여 배포될 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm tranisition wait interval (vm.tranisition.wait.interval)</th>
        <th>가상머신이 상태 전환 중일때 확인하기 위해 기다리는 시간. 너무 짧게 설정하며 상태가 반영되지 않은 시점에 확인을 시도해 잘못된 판정을 내릴 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm user dispersion weight (vm.user.dispersion.weight)</th>
        <th>가상머신 배포시 유저에 따른 분산배치와 자원사용량 기준 가중치. 0에 가까울수록 유저에 따른 분산배치에 가중치, 100에 가까울수록 자원사용량 기준 가중치</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vm userdata max length (vm.userdata.max.length)</th>
        <th>base64로 인코딩된 가상머신 유저데이터의 최대 길이. 기본값은 32768, 최대값은 1048576</th>
    </tr>  
    <tr>
        <th>Virtual Machine</th>
        <th>Vmscheduler jobs expire interval (vmscheduler.jobs.expire.interval)</th>
        <th>가상머신 작업이 대기 중일때 만료처리되는 시간</th>
    </tr>  

</table>
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
