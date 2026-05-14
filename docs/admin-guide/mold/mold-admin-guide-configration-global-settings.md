
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
</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
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
</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
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
</table>   

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
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

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
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

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes service enabled (cloud.kubernetes.service.enabled)</th>
        <th>쿠버네티스 플러그인 활성화. 활성화/비활성화 변경시 관리서버 재시작 필요</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes cluster experimental features enabled (cloud.kubernetes.cluster.experimental.features.enabled)</th>
        <th>Docker private resgistry 와 같은 실험 기능 활성화</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes cluster max size (cloud.kubernetes.cluster.max.size)</th>
        <th>쿠버네티스 클러스터 최대 사이즈</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes cluster network offering (cloud.kubernetes.cluster.network.offering)</th>
        <th>쿠버네티스 클러스터 가상머신이 생성될 격리 네트워크의 네트워크 오퍼링명</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes cluster scale timeout (cloud.kubernetes.cluster.scale.timeout)</th>
        <th>쿠버네티스 클러스터 확장/축소 작업이 완료되는 제한 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes cluster start timeout (cloud.kubernetes.cluster.start.timeout)</th>
        <th>쿠버네티스 클러스터 시작 작업이 완료되어야 하는 제한 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes cluster upgrade retries (cloud.kubernetes.cluster.upgrade.retries)</th>
        <th>가상머신 할당에서 제외할 호스트 코어를 지정합니다. 호스트 OS와 에이전트 동작이나 네트워크/스토리지 IO를 처리하여 안정적인 관리를 가능하게 하고, 가상머신에 인터럽트없는 코어 집합을 할당할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Affinity processors exclude (affinity.processors.exclude)</th>
        <th>쿠버네티스 클러스터 업그레이드 실패시 재시도 횟수(drain node, etcdserver leader changed 등)</th>
    </tr>  
    <tr>
        <th>Kubernetes</th>
        <th>Cloud kubernetes cluster upgrade timeout (cloud.kubernetes.cluster.upgrade.timeout)</th>
        <th>쿠버네티스 클러스터 업그레이드 완료 제한 시간. 노드에서 업그레이드가 진행 중일때는 작업 종료까지 대기</th>
    </tr>  
    
</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>High Availability</th>
        <th>Enable ha storage migration (enable.ha.storage.migration)</th>
        <th>HA 동안 기본 스토리지간 스토리지 마이그레이션 활성화</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Force ha (force.ha)</th>
        <th>가상머신이 HA를 거부해도 강제로 HA합니다.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha checking interval (ha.checking.interval)</th>
        <th>호스트 상태 확인 간격</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha fence builders exclude (ha.fence.builders.exclude)</th>
        <th>호스트 펜싱 빌더중 제외할 목록ㅊ</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha investigators exclude (ha.investigators.exclude)</th>
        <th>호스트 확인 방식 중 제외할 목록</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha investigators order (ha.investigators.order)</th>
        <th>호스트 확인 방식 우선순위</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max concurrent activity check operations (ha.max.concurrent.activity.check.operations)</th>
        <th>관리서버당 동시 확인 작업 수. 활성화된 확인 큐의 스레드 풀 사이즈를 결정합니다.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max concurrent fence operations (ha.max.concurrent.fence.operations)</th>
        <th>관리서버당 동시 펜스 작업 수</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max concurrent health check operations (ha.max.concurrent.health.check.operations)</th>
        <th>관리서버당 동시 헬스체크 작업 수. 헬스체크 큐의 사이즈를 결정합니다.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max concurrent recovery operations (ha.max.concurrent.recovery.operations)
        </th>
        <th>관리서버당 동시 복구 작업 수.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max pending activity check operations (ha.max.pending.activity.check.operations)</th>
        <th>관리서버당 보류중인 활성 확인 작업 수. 활성 확인 큐의 사이즈를 결정합니다.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max pending fence operations (ha.max.pending.fence.operations)</th>
        <th>관리서버당 보류 중인 펜스 작업 수. 펜스 작업 큐의 사이즈를 결정합니다.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max pending health check operations (ha.max.pending.health.check.operations)</th>
        <th>관리서버당 보류 중인 헬스체크 작업 수. 헬스체크 작업 큐의 사이즈를 결정하빈다.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha max pending recovery operations (ha.max.pending.recovery.operations)</th>
        <th>관리서버당 보류 중인 복구 작업 수. 복구 작업 큐의 사이즈를 결정합니다.</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha planners exclude (ha.planners.exclude)</th>
        <th>HA 방식에서 제외할 목록</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha tag (ha.tag)</th>
        <th>HA 전용 호스트 태그</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha vm restart hostup (ha.vm.restart.hostup)</th>
        <th>호스트 상태가 정상으로 돌아왔을 때, 해당 호스트의 가상머신 부팅</th>
    </tr>  
    <tr>
        <th>High Availability</th>
        <th>Ha workers (ha.workers)</th>
        <th>HA 작업 스레드의 수</th>
    </tr>  
    
</table>

* Storage
    * 스토리지 관리, 볼륨 관리 등 저장소 관련 설정 항목입니다.

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Images</th>
        <th>Allow public user templates (allow.public.user.templates)</th>
        <th>일반 사용자가 공개 템플릿을 만들 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Create private template from snapshot wait (create.private.template.from.snapshot.wait)</th>
        <th>스냅샷에서 비공개 템플릿 만들기 작업의 완료 제한 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Create private template from volume wait (create.private.template.from.volume.wait)</th>
        <th>볼륨에서 비공개 템플릿 만들기 작업의 완료 제한 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Max template iso size (max.template.iso.size)</th>
        <th>템플릿 혹은 ISO 다운로드 최대 제한 크기(GB 단위)</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Share public templates with other domains (share.public.templates.with.other.domains)</th>
        <th>도메인간 공개 템플릿 공유</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Template adapter exclude (template.adapter.exclude)</th>
        <th>템플릿 어댑터 제외 목록</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Template preloader pool size (template.preloader.pool.size)</th>
        <th>사전 로딩되는 템플릿 풀 사이즈</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Validate url is resolvable before registering template (validate.url.is.resolvable.before.registering.template)</th>
        <th>템플릿/ISO를 데이터베이스에 등록하기 전 제공된 URL이 접근가능한지 확인하기</th>
    </tr>  
    <tr>
        <th>Images</th>
        <th>Validate url is resolvable before registering template (validate.url.is.resolvable.before.registering.template)</th>
        <th>VNF 템플릿과 어플라이언스 생성</th>
    </tr>  

</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Volume</th>
        <th>Allow diskoffering change during scale vm (allow.diskoffering.change.during.scale.vm)</th>
        <th>디스크 오퍼링이 가상머신의 운영 중 확장 작업 동안 루트 볼륨을 변경할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Allow user expunge recover volume (allow.user.expunge.recover.volume)</th>
        <th>일반 사용자가 그들의 볼륨을 파기하거나 복구할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Copy volume wait (copy.volume.wait)</th>
        <th>볼륨 복제 작업의 완료 제한 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Create volume from snapshot wait (create.volume.from.snapshot.wait)</th>
        <th>스냅샷에서 볼륨 만들기 작업의 완료 제한 시간(초 단위)</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Custom diskoffering size max (custom.diskoffering.size.max)</th>
        <th>사용자 정의 디스크 오퍼링의 최대 할당 디스크</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Custom diskoffering size min (custom.diskoffering.size.min)</th>
        <th>사용자 정의 디스크 오퍼링의 최소 할당 디스크 크기</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Destroy root volume on vm destruction (destroy.root.volume.on.vm.destruction)</th>
        <th>가상머신 파기시 루트 볼륨 파기</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Disk provisioning type strictness (disk.provisioning.type.strictness)</th>
        <th>서비스/디스크 오퍼링에서 설정된 프로비저닝 방식을 지원하는 스토리지 풀에서만 디스크 생성. false 일 경우 디스크에서 지원하는 방식으로 프로비저닝. VMware only</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Storpool volume tags checkup (storpool.volume.tags.checkup)</th>
        <th>StorPool 볼륨의 데이터베이스 확인 및 보고 최소 간격(초 단위)</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Systemvm root disk size (systemvm.root.disk.size)</th>
        <th>시스템VM과 가상라우터의 루트 볼륨 사이즈 제한</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Volume check and repair leaks before use (volume.check.and.repair.leaks.before.use)</th>
        <th>가상머신 부착과 시작 전에 볼륨에 어떤 결함이 있는지 확인하고 복구하기</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Volume resize allowed beyond allocation (volume.resize.allowed.beyond.allocation)</th>
        <th>pool.storage.allocated.capacity.disablethreshold 에서 지정한 볼륨 할당 제한 크기를 볼륨 리사이즈시 넘어설 수 있습니다. 하지만 그 값은 pool.storage.allocated.resize.capacity.disablethreshold 이내로 제한됩니다.</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Volume stats interval (volume.stats.interval)</th>
        <th>볼륨 통계 보고 간격(밀리 초 단위)</th>
    </tr>  
    <tr>
        <th>Volume</th>
        <th>Volume url check (volume.url.check)</th>
        <th>관리서버에서 볼륨 다운로드 전 접근 가능한지 확인.</th>
    </tr>  

</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Snapshot</th>
        <th>Snapshot backup to secondary (snapshot.backup.to.secondary)</th>
        <th>기본 스토리지 스냅샷을 항상 2차 스토리지에 백업합니다. 기본 스토리지에만 스냅샷을 저장하는 것은 KVM + Ceph 에서만 가능합니다.</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Snapshot delta max (snapshot.delta.max)</th>
        <th>몇개의 증분 스냅샷을 허용할지 결정합니다.</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Snapshot max daily (snapshot.max.daily)</th>
        <th>하나의 볼륨 당 하루에 몇 개의 스냅샷을 보관할지 결정합니다. 제한값에 도달할 경우 가장 앞선 스냅샷을 삭제하고 새로운 스냅샷을 저장합니다. 수동 스냅샷은 계산하지 않습니다. 값이 0일 경우, 매일 찍는 스냅샷을 설정할 수 없습니다.</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Snapshot max hourly (snapshot.max.hourly)</th>
        <th>하나의 볼륨 당 매시간 몇 개의 스냅샷을 보관할지 결정합니다. 제한값에 도달할 경우 가장 앞선 스냅샷을 삭제하고 새로운 스냅샷을 저장합니다. 수동 스냅샷은 계산하지 않습니다. 값이 0일 경우, 매시간 찍는 스냅샷을 설정할 수 없습니다.</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Snapshot max monthly (snapshot.max.monthly)</th>
        <th>하나의 볼륨 당 매달 몇 개의 스냅샷을 보관할지 결정합니다. 제한값에 도달할 경우 가장 앞선 스냅샷을 삭제하고 새로운 스냅샷을 저장합니다. 수동 스냅샷은 계산하지 않습니다. 값이 0일 경우, 매달 찍는 스냅샷을 설정할 수 없습니다.</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Snapshot max weekly (snapshot.max.weekly)</th>
        <th>하나의 볼륨 당 매주 몇 개의 스냅샷을 보관할지 결정합니다. 제한값에 도달할 경우 가장 앞선 스냅샷을 삭제하고 새로운 스냅샷을 저장합니다. 수동 스냅샷은 계산하지 않습니다. 값이 0일 경우, 매주 찍는 스냅샷을 설정할 수 없습니다.</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Snapshot poll interval (snapshot.poll.interval)</th>
        <th>관리서버가 스냅샷 상태를 확인하는 간격입니다.</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Snapshot strategies exclude (snapshot.strategies.exclude)</th>
        <th>스냅샷 방식에서 제외할 목록</th>
    </tr>  
    <tr>
        <th>Snapshot</th>
        <th>Storpool snapshot tags checkup (storpool.snapshot.tags.checkup)</th>
        <th>StorPool 스냅샷을 데이터베이스에 보고하고 확인하는 최소 간격이빈다.(초 단위)</th>
    </tr>  

</table>    

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>VM Snapshot</th>
        <th>Vmsnapshot create wait (vmsnapshot.create.wait)</th>
        <th>VM스냅샷 생성 완료 제한 시간</th>
    </tr>  
    <tr>
        <th>VM Snapshot</th>
        <th>Vmsnapshot expire interval (vmsnapshot.expire.interval)</th>
        <th>VM스냅샷 만료 시간(1시간 단위)</th>
    </tr>  
    <tr>
        <th>VM Snapshot</th>
        <th>Vmsnapshot max (vmsnapshot.max)</th>
        <th>하나의 가상머신당 최대 VM스냅샷 갯수</th>
    </tr>  
    <tr>
        <th>VM Snapshot</th>
        <th>VmSnapshot strategies exclude (vmSnapshot.strategies.exclude)</th>
        <th>VM스냅샷 방식 중 제외할 목록</th>
    </tr>  

</table>    

* Network
    * 네트워크 관리 및 트래픽 제어 관련 설정 항목입니다.

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Network</th>
        <th>Allow empty start end ipaddress (allow.empty.start.end.ipaddress)</th>
        <th>시작/종료 IP 주소 없이 네트워크 생성 허용</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Allow subdomain network access (allow.subdomain.network.access)</th>
        <th>서브도메인에서 원도메인 네트워크를 사용할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Allow user list available ips on shared network (allow.user.list.available.ips.on.shared.network)</th>
        <th>일반 사용자가 공유 네트워크에서 사용가능한 IP를 확인할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Check pod cidrs (check.pod.cidrs)</th>
        <th>다른 Pod는 다른 CIDR를 가집니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Cloud dns name (cloud.dns.name)</th>
        <th>가상머신 등에 붙는 기본 DNS명입니다. 호스트명과는 다릅니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Control cidr (control.cidr)</th>
        <th>관리서버와 호스트 간 컨트롤 네트워크 트래픽 전달시 사용하는 CIDR 블록입니다. 기본값은 link-local(169.254.0.0/16)입니다. 여러 Pod 에서 동일 블록 사용시 트래픽이 충돌할 수 있습니다. </th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Direct attach network externalIpAllocator enabled (direct.attach.network.externalIpAllocator.enabled)</th>
        <th>가상머신이 외부 DHCP 서버에 직접 연결됩니다. true로 설정할 경우, externalIpAllocator 플러그인이 구성되어 있어야 IP 를 할당받을 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Direct attach network externalIpAllocator url (direct.attach.network.externalIpAllocator.url)</th>
        <th>externalIpAllocater url</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Direct network no default route (direct.network.no.default.route)</th>
        <th>가상머신이 다이렉트를 네트워크를 통한 기본 라우트를 갖지 않습니다. </th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Direct network stats interval (direct.network.stats.interval)</th>
        <th>트래픽 모니터에서 네트워크 통계를 수집하는 간격</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Execute in sequence network element commands (execute.in.sequence.network.element.commands)</th>
        <th>DhcpEntryCommand, SavePasswordCommand, VmDataCommand 를 순차적으로 실행합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Expose dns externally (expose.dns.externally)</th>
        <th>가상머신과 네트워크 DNS 레코드를 외부에 노출합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>External firewall default capacity (external.firewall.default.capacity)</th>
        <th>외부 방화벽 장비에 허용하는 네트워크 서비스 수.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>External network stats interval (external.network.stats.interval)</th>
        <th>외부 네트워크 통계를 보고하는 간격(초 단위)</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Firewall service provider exclude (firewall.service.provider.exclude)</th>
        <th>방화벽 제공 방식 중 제외할 목록</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Globodns domain templateid (globodns.domain.templateid)</th>
        <th>GloboDNS 에서 도메인 생성시 사용될 템플릿 ID</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Globodns override entries (globodns.override.entries)</th>
        <th>GloboDNS가 템플릿 규칙 대신 강제로 덮어쓰기합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Guest vlan bits (guest.vlan.bits)</th>
        <th>게스트 서브넷 주소 공간에 VLAN ID 를 위해 몇 비트를 예약할지 정합니다. 기본적으로 VLAN은 12비트(0~4096)를 사용합니다. 이보다 작을 경우 VLAN 네트워크 수가 제한될 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Management network cidr (management.network.cidr)</th>
        <th>관리 네트워크의 CIDR 블록</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network acl service provider exclude (network.acl.service.provider.exclude)</th>
        <th>네트워크 ACL 서비스 중 제외할 목록</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network dhcp nondefaultnetwork setgateway guestos (network.dhcp.nondefaultnetwork.setgateway.guestos)</th>
        <th>이 명칭으로 시작하는 게스트OS 기본 네트워크가 아니라도 DHCP 서버에서 게이트웨이 정보를 응답합니다. 리스트는 콤마로 구분합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network disable rpfilter (network.disable.rpfilter)</th>
        <th>도메인 라우터 가상머신의 퍼블릭 인터페이스에서 rp_filter(reserve path filtering)를 비활성화합니다. rp_filter는 리눅스 커널의 보안 기능으로 소스 IP가 예상 경로와 맞지 않을 경우 패킷을 버립니다. 이는 스푸핑 공격 방지에 유용하지만, 비대칭 라우팅이나 다중 네트워크 인터페이스 환경에서는 정상 트래픽을 차단할 수도 있습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network dns basiczone updates (network.dns.basiczone.updates)</th>
        <th>이 설정의 값은 all/pod 2가지 중 하나입니다. . DHCP/DNS 요청이 에이블스택 내의 모든 DHCP 서버에게 가거나, 오로지 하나의 Pod 당 하나의 DHCP 서버로 가게 합니다. 다중 Pod 환경이 아니라면 all 설정이 기본값입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network elements registry exclude (network.elements.registry.exclude)</th>
        <th>네트워크 제공자 중 제외할 목록</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network forged transmits (network.forged.transmits)</th>
        <th>가상머신이 할당된 MAC 주소가 아닌 다른 MAC 주소를 사용할 수 있습니다. 활성화할 경우 변경된 MAC 주소를 필요로 하는 특수 네트워크 기능(VRRP, Heartbeat, LB) 를 사용할 수 있지만 MAC 변조에 따른 보안상 위험을 감수해야 합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network gc interval (network.gc.interval)</th>
        <th>VM이 삭제되거나 네트워크가 더이상 사용되지 않을 때, 해당 리소스는 즉시 제거되지 않고 가비지 컬렉션에 의해 폐기됩니다. 이 가비지 컬렉션의 실행 주기를 설정합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network gc wait (network.gc.wait)</th>
        <th>VM이 삭제되거나 네트워크가 더이상 사용되지 않을 때, 가비지 컬렉션이 실행되기까지 기다리는 시간입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network guest cidr limit (network.guest.cidr.limit)</th>
        <th>게스트 네트워크에서 사용하는 CIDR 블록의 크기를 제한하여, IP 관리의 용이성을 유지하고, DHCP/라우팅 문제 발생 가능성을 낮춥니다. 예) 25로 설정할 경우 /25 /24 /23 가능 /26 /27 /28 불가능</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network gurus exclude (network.gurus.exclude)</th>
        <th>특정 네트워크 비활성화 목록</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network ipv6 prefix subnet cleanup interval (network.ipv6.prefix.subnet.cleanup.interval)</th>
        <th>가상머신이 삭제되거나 네트워크가 더이상 사용되지 않을 때, 해당 IPv6 서브넷은 즉시 해제되지 않고 주기적으로 실행되는 클린업 프로세스에 의해 삭제됩니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network ipv6 search retry max (network.ipv6.search.retry.max)</th>
        <th>가상머신에 IPv6 주소를 할당하기 위해 필요한 서브넷 검색 시도 횟수입니다. </th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer basiczone elb enabled (network.loadbalancer.basiczone.elb.enabled)</th>
        <th>Basic Zone 환경에서 ELB 기능을 활성화하여 외부 네트워크 장비로 로드 밸런싱할 수 있습니다..</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer basiczone elb gc interval minutes (network.loadbalancer.basiczone.elb.gc.interval.minutes)</th>
        <th>Basic Zone 환경에서의 ELB가 비활성화 되었을 때, 이를 삭제하는 가비지 컬렉션의 실행주기입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer basiczone elb network (network.loadbalancer.basiczone.elb.network)</th>
        <th>Basic Zone 에서의 ELB가 사용하는 네트워크를 지정합니다. 네트워크 ID 혹은 이름으로 지정할 수 있습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer basiczone elb vm cpu mhz (network.loadbalancer.basiczone.elb.vm.cpu.mhz)</th>
        <th>Basic Zone 환경의 ELB 인스턴스에 할당될 CPU 성능입니다.(단위 mhz)</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer basiczone elb vm ram size (network.loadbalancer.basiczone.elb.vm.ram.size)</th>
        <th>Basic Zone 환경의 ELB 인스턴스에 할당될 RAM 크기입니다.(단위 MB)</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer basiczone elb vm vcpu num (network.loadbalancer.basiczone.elb.vm.vcpu.num)</th>
        <th>Basic Zone 환경의 ELB 인스턴스에 할당될 vCPU의 코어 갯수입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer haproxy max conn (network.loadbalancer.haproxy.max.conn)</th>
        <th>로드밸런서(haproxy)의 최대 동시 연결 수입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer haproxy stats auth (network.loadbalancer.haproxy.stats.auth)</th>
        <th>로드밸런서(haproxy)의 통계 접근 인증 정보입니다. 형식 username:password</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer haproxy stats port (network.loadbalancer.haproxy.stats.port)</th>
        <th>로드밸런스(haproxy) 통계 접근 포트 번호입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer haproxy stats uri (network.loadbalancer.haproxy.stats.uri)</th>
        <th>로드밸런스(haproxy) 통계 접근 페이지입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network loadbalancer haproxy stats visibility (network.loadbalancer.haproxy.stats.visibility)</th>
        <th>로드밸런스(haproxy) 통계 페이지에 접근할 네트워크입니다. global, guest-network, link-local, disabled, all, default</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network lock timeout (network.lock.timeout)</th>
        <th>네트워크 삭제, 수정, 생성 시에 동시성 문제를 방지하기 위한 네트워크 자원 잠금 시간입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network mac address changes (network.mac.address.changes)</th>
        <th>가상머신 내부에서 MAC 주소 변경이 가능합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network mac learning (network.mac.learning)</th>
        <th>가상머신 NIC 의 MAC 주소 학습을 허용합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network promiscuous mode (network.promiscuous.mode)</th>
        <th>가상머신 NIC 의 무차별 모드를 허용합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network rolling restart (network.rolling.restart)</th>
        <th>네트워크 서비스(Virtual Router, Load Balancer, DHCP)를 재시작할 때, 모든 서비스 인스턴스를 순차적으로 재시작하여 다운타임을 최소화하고, 서비스 연속성을 유지합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network router EnableServiceMonitoring (network.router.EnableServiceMonitoring)</th>
        <th>Virtual Router 내의 모니터링 기능을 활성화합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network rule delete ignoreerror (network.rule.delete.ignoreerror)</th>
        <th>네트워크 룰 삭제시 장비에서 발생하는 오류를 무시합니다. 활성화시 관리 편이성이 증가하지만, 실제로는 장비에 룰이 남아 있을 수 있어 상태 불일치(inconsistency) 위험이 있습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network securitygroups defaultadding (network.securitygroups.defaultadding)</th>
        <th>가상머신을 생성할 때, 기본 보안그룹을 적용합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network securitygroups work cleanup interval (network.securitygroups.work.cleanup.interval)</th>
        <th>보안그룹 룰의 추가/삭제/갱신과 같은 작업이 정리되는 주기입니다. 작업큐가 자주 정리되면 불필요한 작업의 누적이 방지되므로 안정성이 올라갑니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network securitygroups work lock timeout (network.securitygroups.work.lock.timeout)</th>
        <th>보안 그룹 룰(방화벽 규칙 등)을 처리할 때, 여러 스레드가 동시에 처리하지 않도록 잠금을 거는 시간입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network securitygroups work per agent queue size (network.securitygroups.work.per.agent.queue.size)</th>
        <th>각 에이전트(호스트)에서 전달된 보안 그룹 작업큐의 크기를 정합니다. 값이 커지면 대규모 환경에서 많은 작업을 동시에 처리 가능하지만 메모리 사용량이 증가하고 처리가 지연될 가능성이 높아집니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network securitygroups workers pool size (network.securitygroups.workers.pool.size)</th>
        <th>보안 그룹 룰를 병렬로 처리하는 워커 스레드 풀의 크기입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Network throttling rate (network.throttling.rate)</th>
        <th>가상머신 NIC 에 할당되는 네트워크 대역폭 제한입니다. 특정 가상머신이 과도하게 네트워크를 점유하는 것을 방지합니다. 0 -> 제한없음, 양수 -> Mbps</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Proxy cidr (proxy.cidr)</th>
        <th>관리서버가 신뢰할 프록시 서버의 대역입니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Routed ipv4 network cidr auto allocation enabled (routed.ipv4.network.cidr.auto.allocation.enabled)</th>
        <th>Routed Network 생성시 CIDR 블록을 Zone 에 설정된 IPv4 서브넷 풀에서 자동 할당합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Routed network ipv4 max cidr size (routed.network.ipv4.max.cidr.size)</th>
        <th>Routed Network 의 자동 할당 CIDR 블록의 최대 크기를 제한합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Routed network ipv4 min cidr size (routed.network.ipv4.min.cidr.size)</th>
        <th>Routed Network 의 자동 할당 CIDR 블록의 최소 크기를 제한합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Routed network vpc enabled (routed.network.vpc.enabled)</th>
        <th>Routed Network 모드에서 VPC 를 사용합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Use external dns (use.external.dns)</th>
        <th>Virtual Router가 제공하는 DNS 서비스 대신 외부 DNS를 직접 사용합니다. 이때 VR가 제공하는 내부 네트워크 이름 해석은 사용할 수 없습니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Use system guest vlans (use.system.guest.vlans)</th>
        <th>게스트 네트워크에 VLAN를 자동할당합니다. 비활성화할 경우 관리자가 직접 VLAN을 지정해야합니다.</th>
    </tr>  
    <tr>
        <th>Network</th>
        <th>Zone vlan capacity notificationthreshold (zone.vlan.capacity.notificationthreshold)</th>
        <th>사용한 VLAN의 갯수가 임계치에 다다르면 관리자에게 알립니다.</th>
    </tr>  

</table>  

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>DHCP</th>
        <th>Dhcp providers exclude (dhcp.providers.exclude)</th>
        <th>DHCP 서버 제외 목록</th>
    </tr> 
    <tr>
        <th>DHCP</th>
        <th>Externaldhcp vmip max retry (externaldhcp.vmip.max.retry)</th>
        <th>외부 DHCP 서버 사용시 가상머신이 IP를 할당받기 위한 최대 재시도 횟수</th>
    </tr> 
    <tr>
        <th>DHCP</th>
        <th>Externaldhcp vmip retrieval interval (externaldhcp.vmip.retrieval.interval)</th>
        <th>외부 DHCP 서버 사용시 가상머신이 IP를 할당받기 위한 최대 재시도 간격</th>
    </tr> 
    <tr>
        <th>DHCP</th>
        <th>Externaldhcp vmipFetch threadPool max (externaldhcp.vmipFetch.threadPool.max)</th>
        <th>외부 DHCP 서버 사용시 가상머신 IP 할당을 병렬로 처리하는 워커 스레드 당 최대 스레드 풀</th>
    </tr> 
    <tr>
        <th>DHCP</th>
        <th>Externaldhcp vmipfetchtask workers (externaldhcp.vmipfetchtask.workers)</th>
        <th>외부 DHCP 서버 사용시 가상머신 IP 할당을 병렬로 처리하는 워커 스레드 수</th>
    </tr> 
    
</table>  

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>VPC</th>
        <th>Routed ipv4 vpc max cidr size (routed.ipv4.vpc.max.cidr.size)</th>
        <th>Routed Network 모드에서 IPv4 CIDR 블록의 최대 사이즈. 예) 24일 경우: /23 /22 할당 불가</th>
    </tr> 
    <tr>
        <th>VPC</th>
        <th>Routed ipv4 vpc min cidr size (routed.ipv4.vpc.min.cidr.size)</th>
        <th>Routed Network 모드에서 IPv4 CIDR 블록의 최소 사이즈. 예) 24일 경우: /25 /26 할당 불가</th>
    </tr> 
    <tr>
        <th>VPC</th>
        <th>Vpc cleanup interval (vpc.cleanup.interval)</th>
        <th>VPC의 리소스(라우터, 네트워크 룰, IP 할당)는 VPC 제거시 즉시 삭제되지 않고 주기적인 백그라운드 클린업을 통해 처리됩니다.(단위 초)</th>
    </tr> 
    <tr>
        <th>VPC</th>
        <th>Vpc max networks (vpc.max.networks)</th>
        <th>하나의 VPC 안에 생성가능한 네트워크 수</th>
    </tr> 
    <tr>
        <th>VPC</th>
        <th>Vpc providers exclude (vpc.providers.exclude)</th>
        <th>VPC 제공 제외 목록</th>
    </tr> 
    <tr>
        <th>VPC</th>
        <th>Vpc tier name prepend (vpc.tier.name.prepend)</th>
        <th>VPC 내의 게스트 네트워크명에 VPC명을 자동으로 붙입니다.</th>
    </tr> 
    <tr>
        <th>VPC</th>
        <th>Vpc tier name prepend delimiter (vpc.tier.name.prepend.delimiter)</th>
        <th>Vpc tier name prepend (vpc.tier.name.prepend) 가 활성화일 경우, 앞에 붙는 VPC명과 뒤의 네트워크명 사이에 들어가는 특수문자를 정합니다.</th>
    </tr> 

</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>LoadBalancer</th>
        <th>External lb default capacity (external.lb.default.capacity)</th>
        <th>외부 LB 사용시 처리되는 기본 용량</th>
    </tr> 
    <tr>
        <th>LoadBalancer</th>
        <th>Gslb service provider exclude (gslb.service.provider.exclude)</th>
        <th>GSLB 서비스 제공자 제외 목록</th>
    </tr> 

</table>

* Hypervisor
    * 하이퍼바이저 유형별 특성 및 호스트 관리 관련 설정 항목입니다.

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Hypervisor</th>
        <th>Add host on service restart kvm (add.host.on.service.restart.kvm)</th>
        <th>KVM 호스트 에이전트 재시작후 호스트를 관리 서버에 자동으로 재등록합니다.</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Execute in sequence hypervisor commands (execute.in.sequence.hypervisor.commands)</th>
        <th>하이퍼바이저 명령들을 순차실행합니다. 비활성화시 병렬실행합니다.</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Global allow expose host hostname (global.allow.expose.host.hostname)</th>
        <th>API 응답이나 UI 에서 호스트명을 노출합니다.</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host (host)</th>
        <th>관리 서버 주소</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host allocators exclude (host.allocators.exclude)</th>
        <th>가상머신 할당시 제외할 알고리즘</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host allocators order (host.allocators.order)</th>
        <th>가상머신 할당시 사용되는 알고리즘 순서</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host capacityType to order clusters (host.capacityType.to.order.clusters)</th>
        <th>클러스터 정렬시 기준이 되는 호스트 자원(CPU or RAM)</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host maintenance local storage strategy (host.maintenance.local.storage.strategy)</th>
        <th>호스트 유지보수 모드 진입시 로컬스토리지에서 운영 중인 가상머신 처리 방침입니다. Migration -> 가상머신을 다른 호스트로 옮길 수 있으나 로컬 스토리지 디스크도 마이그레이션 필요, Skip -> 유지보수 모드 진입은 가능하지만 로컬 스토리지 가상머신은 유지되므로 데이터 손상 위험, Error -> 로컬 스토리지 가상머신이 있는 한 유지보수 모드 진입 불가</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host reservation release period (host.reservation.release.period)</th>
        <th>가상머신 배치시에 예약한 호스트 자원이 특정 상황(가상머신 생성 실패, 작업 취소 등)으로 인해 해제하는 주기입니다.(단위 밀리초)</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host retry (host.retry)</th>
        <th>관리 서버가 호스트 연결 실패시 재시도 횟수</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host stats interval (host.stats.interval)</th>
        <th>관리 서버가 수집하는 호스트 통계 주기(단위 밀리초)</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Host tag rule execution timeout (host.tag.rule.execution.timeout)</th>
        <th>호스트 태그 기반 가상머신 배치가 실패하기까지 시간입니다. 이 시간이 지나면 작업을 실패 처리 하거나 다른 호스트 선택 로직으로 넘어갑니다.</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Hypervisor custom display name (hypervisor.custom.display.name)</th>
        <th>하이퍼바이저명(KVM, XenServer, VMware)을 변경하여 표시합니다.</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Hypervisor gurus exclude (hypervisor.gurus.exclude)</th>
        <th>하이퍼바이저 제공자 제외 목록</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Hypervisor list (hypervisor.list)</th>
        <th>하이퍼바이저 제공자 목록</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Implicit host tags (implicit.host.tags)</th>
        <th>모든 호스트에 기본으로 붙이는 태그입니다.</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Monitoring wall portal host uri (monitoring.wall.portal.host.uri)</th>
        <th>외부 모니터링 서비스 Wall 접근 페이지</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Resource limit host tags (resource.limit.host.tags)</th>
        <th>자원을 제한할 호스트 태그</th>
    </tr> 
    <tr>
        <th>Hypervisor</th>
        <th>Set host down to maintenance (set.host.down.to.maintenance)</th>
        <th>호스트가 Down 상태일 때, 유지보수 모드로 자동으로 진입합니다.</th>
    </tr> 

</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>KVM</th>
        <th>Enable kvm host auto enable disable (enable.kvm.host.auto.enable.disable)</th>
        <th>호스트 헬스 체크 결과에 따라 KVM 호스트를 자동으로 연결/비연결 합니다.</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm auto convergence (kvm.auto.convergence)</th>
        <th>HA 활동성 확인시 실패 비율이 임계치를 넘어가면 호스트를 비정상으로 간주합니다.</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha activity check interval (kvm.ha.activity.check.interval)</th>
        <th>HA 활동성을 체크하는 주기(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha activity check max attempts (kvm.ha.activity.check.max.attempts)</th>
        <th>HA 활동성 확인 시도 횟수</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha activity check timeout (kvm.ha.activity.check.timeout)</th>
        <th>HA 활동성 확인시 각 확인 요청에 대한 응답을 기다리는 시간입니다.</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha fence on storage heartbeat failure (kvm.ha.fence.on.storage.heartbeat.failure)</th>
        <th>스토리지 하트비트가 실패하면 호스트를 펜싱 처리합니다.</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha fence timeout (kvm.ha.fence.timeout)</th>
        <th>펜싱 처리 대기시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha health check timeout (kvm.ha.health.check.timeout)</th>
        <th>HA 헬스체크 대기시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha on storage heartbeat (kvm.ha.on.storage.heartbeat)</th>
        <th>스토리지 하트비트에 기반한 HA</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha recover failure threshold (kvm.ha.recover.failure.threshold)</th>
        <th>HA 시 다른 호스트로 가상머신 복구를 시도하는 횟수</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha recover timeout (kvm.ha.recover.timeout)</th>
        <th>HA 시 다른 호스트로 가상머신 복구 작업 시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ha recover wait period (kvm.ha.recover.wait.period)</th>
        <th>HA 시 다른 호스트로 가상머신 복구를 위한 자원 대기 시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm rolling maintenance ping interval (kvm.rolling.maintenance.ping.interval)</th>
        <th>롤링 유지보수 모드시 관리 서버와 호스트 간 핑 확인 주기</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm rolling maintenance stage timeout (kvm.rolling.maintenance.stage.timeout)</th>
        <th>롤링 유지보수 모드시 각 단계가 완료되는 시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm rolling maintenance wait maintenance timeout (kvm.rolling.maintenance.wait.maintenance.timeout)</th>
        <th>롤링 유지보수 모드 진입시 호스트가 유지보수 모드로 진입하는 최대 시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm snapshot enabled (kvm.snapshot.enabled)</th>
        <th>KVM 호스트에서 스냅샷을 사용합니다.</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ssh port (kvm.ssh.port)</th>
        <th>KVM 호스트 에이전트 포트</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm ssh to agent (kvm.ssh.to.agent)</th>
        <th>관리 서버가 ssh 포트를 통해 호스트 에이전트에 접근합니다.</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm storage offline migration wait (kvm.storage.offline.migration.wait)</th>
        <th>종료된 가상머신 디스크를 다른 스토리지로 마이그레이션할 때 최대 대기 시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm storage online migration wait (kvm.storage.online.migration.wait)</th>
        <th>운영 중인 가상머신 디스크를 다른 스토리지로 마이그레이션할 때 최대 대기 시간(단위 초)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm storage pool io policy (kvm.storage.pool.io.policy)</th>
        <th>KVM 호스트가 스토리지 풀에 접근할 때 사용하는 정책입니다. 특정 스토리지와 연결된 가상머신 세팅이 있을 경우 덮어씌워 집니다. -threads, native, io_uring</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Kvm vmstoragesnapshot enabled (kvm.vmstoragesnapshot.enabled)</th>
        <th>게스트 에이전트가 설치된 가상머신에 한해 스토리지스냅샷을 활성화합니다.</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Remote kvm instance disks copy timeout (remote.kvm.instance.disks.copy.timeout)</th>
        <th>외부 호스트에서 인스턴스를 가져오는 동안 KVM 호스트가 디스크를 준비하고 복사하는 최대 시간(단위 분)</th>
    </tr> 
    <tr>
        <th>KVM</th>
        <th>Threads on kvm host to import vmware vm files (threads.on.kvm.host.to.import.vmware.vm.files)</th>
        <th>ovftool을 이용해 KVM 호스트에서 VMware 가상머신을 가져오는 스레드. -1/1은 스레드 비활성화, 0은 가상머신 디스크당 스레드 1(싱글 디스크에는 작동하지 않음), 1보다 큰값은 수동 설정, 최대값은 10</th>
    </tr> 

</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>VMware</th>
        <th>Convert vmware instance to kvm timeout (convert.vmware.instance.to.kvm.timeout)</th>
        <th>VMware 가상머신을 KVM 호스트로 가져올 때 최대 작업 시간(단위 시간)</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Threads on ms to import vmware vm files (threads.on.ms.to.import.vmware.vm.files)</th>
        <th>ovftool을 이용해 KVM 호스트에서 VMware 가상머신을 가져오는 스레드. -1/1은 스레드 비활성화, 0은 가상머신 디스크당 스레드 1(싱글 디스크에는 작동하지 않음), 1보다 큰값은 수동 설정, 최대값은 10</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware additional vnc portrange size (vmware.additional.vnc.portrange.size)</th>
        <th>VMware에 있는 가상머신 콘솔에 접근할 때 사용하는 포트의 갯수</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware additional vnc portrange start (vmware.additional.vnc.portrange.start)</th>
        <th>VMware에 있는 가상머신 콘솔에 접근할 때 사용하는 포트의 시작 번호</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware allow parallel command execution (vmware.allow.parallel.command.execution)</th>
        <th>VMware 환경에서 병렬 명령 실행 허용</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware clean old worker vms (vmware.clean.old.worker.vms)</th>
        <th>특정 작업(VM 가져오기, 디스크 변환, 마이그레이션 등)을 수행한 임시 가상머신을 삭제합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware cleanup port groups (vmware.cleanup.port.groups)</th>
        <th>가상머신 네트워크를 구성할 때 생성한 임시 포트그룹을 삭제합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware create full clone (vmware.create.full.clone)</th>
        <th>VMware 가상머신 복제시 전체 복사하여 독립적인 가상머신을 만듭니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware full clone template cleanup period (vmware.full.clone.template.cleanup.period)</th>
        <th>가상머신 전체 복사시 생성한 임시 템플릿을 삭제하는 주기입니다. 삭제 전까지는 계속해서 복제 가상머신을 생성할 수 있습니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware hung wokervm timeout (vmware.hung.wokervm.timeout)</th>
        <th>VMware 환경에서 특정 작업(VM 가져오기, 디스크 변환, 마이그레이션 등)을 수행한 임시 가상머신에 행이 걸렸을 때, 최대 대기 시간입니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware management portgroup (vmware.management.portgroup)</th>
        <th>관리 서버와 ESXi 호스트간에 사용할 네트워크명. 실제로 VMware 호스트에 존재하는 네트워크명이어야 합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware nested virtualization (vmware.nested.virtualization)</th>
        <th>중첩 가상화를 지원합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware nested virtualization perVM (vmware.nested.virtualization.perVM)</th>
        <th>VMware 가상머신 단위로 중첩 가상화를 지원합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware nic hotplug wait timeout (vmware.nic.hotplug.wait.timeout)</th>
        <th>VMware 가상머신에 네트워크 추가/제거시 기다리는 시간입니다.(단위 밀리초)</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware package ova timeout (vmware.package.ova.timeout)</th>
        <th>VMware가 가상머신을 ova로 추출할 때 최대 대기 시간</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware recycle hung wokervm (vmware.recycle.hung.wokervm)</th>
        <th>VMware 환경에서 특정 작업(VM 가져오기, 디스크 변환, 마이그레이션 등)을 수행한 임시 가상머신이 행 걸린 상태일 때, 이를 재활용합니다. 비활성화시 폐기하고 새로 생성합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware reserve cpu (vmware.reserve.cpu)</th>
        <th>하나의 가상머신 배포시 할당된 CPU 자원을 예약하여 다른 가상머신이 사용할 수 없게 합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware reserve mem (vmware.reserve.mem)</th>
        <th>하나의 가상머신 배포시 할당된 RAM 자원을 예약하여 다른 가상머신이 사용할 수 없게 합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware root disk controller (vmware.root.disk.controller)</th>
        <th>VMware 가상머신 배포시 사용하는 루트 디스크 컨트롤러입니다. ide/scsi/lsilogic/pvscsi/sata</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware search exclude folders (vmware.search.exclude.folders)</th>
        <th>관리 서버가 VMware 검색시 제외할 폴더</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware service console (vmware.service.console)</th>
        <th>ESXi 호스트의 서비스 콘솔 네트워크</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware stats time window (vmware.stats.time.window)</th>
        <th>관리 서버가 VMware의 통계를 수집하는 주기(단위 초). 20 이하일 땐 기본값인 300초가 사용됩니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware systemvm nic device type (vmware.systemvm.nic.device.type)</th>
        <th>VMware 환경에 배포하는 시스템VM 의 NIC 유형을 지정합니다. E1000/PCNet32/Vmxnet2/Vmxnet3</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware use dvswitch (vmware.use.dvswitch)</th>
        <th>VMware에서 제공하는 중앙 관리식 분산 스위치인 Distributed vSwitch 를 연결합니다. 비활성화하면 호스트단위 가상 스위치인 Standard vSwitch를 사용합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware use nexus vswitch (vmware.use.nexus.vswitch)</th>
        <th>VMware 환경에서 네트워크를 구성할 때 Cisco Nexus를 사용합니다. 비활성화하면 Standard vSwitch를 사용합니다.</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware uservm nic device type (vmware.uservm.nic.device.type)</th>
        <th>가상머신 배포시 사용하는 NIC 유형을 정합니다. E1000/E1000e/Vmxnet2/Vmxnet3</th>
    </tr> 
    <tr>
        <th>VMware</th>
        <th>Vmware vcenter session timeout (vmware.vcenter.session.timeout)</th>
        <th>관리 서버가 vCenter와 연결하는 세션 최대 연결 시간입니다. 지정 시간이 만료되면 세션은 종료되고, 필요시 새로운 세션이 만들어 집니다.</th>
    </tr> 

</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>XenServer</th>
        <th>Xapiwait (xapiwait)</th>
        <th>XenServer/XCP 환경에서 관리 서버가 응답을 기다리는 최대 시간입니다.</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xen heartbeat timeout (xen.heartbeat.timeout)</th>
        <th>XenServer/XCP 환경에서 관리 서버가 호스트의 하트비트를 기다리는 최대 시간입니다. 지정한 시간이 지나도 응답이 없을 경우 HA가 시작될 수 있습니다.</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xen vm vcpu max (xen.vm.vcpu.max)</th>
        <th>XenServer/XCP 환경에서 가상머신에 할당가능한 최대 vCPU 갯수</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xenserver bond storage nics (xenserver.bond.storage.nics)</th>
        <th>XenServer/XCP 환경의 스토리지 NIC 있을 경우 본딩합니다. NIC는 XenServer에 실재 있어야 합니다.</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xenserver heartbeat interval (xenserver.heartbeat.interval)</th>
        <th>관리 서버가 XenServer 호스트에 보내는 하트비트 주기</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xenserver heartbeat timeout (xenserver.heartbeat.timeout)</th>
        <th>관리 서버가 XenServer 호스트에 보낸 하트비트 응답 대기 시간</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xenserver hotfix enabled (xenserver.hotfix.enabled)</th>
        <th>관리 서버가 XenServer에 필요한 Hotfix를 자동으로 발견하고 적용합니다.</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xenserver nics max (xenserver.nics.max)</th>
        <th>XenServer/XCP 환경 가상머신에 부여 가능한 NIC 갯수</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xenserver pvdriver version (xenserver.pvdriver.version)</th>
        <th>XenServer/XCP 가상머신에 사용된 Paravirtual Driver 의 최소 버전을 지정합니다. 지정한 버전보다 낮을 경우 업데이트가 필요할 수 있습니다.</th>
    </tr> 
    <tr>
        <th>XenServer</th>
        <th>Xenserver setup multipath (xenserver.setup.multipath)</th>
        <th>관리 서버가 XenServer/XCP 의 스토리지 네트워크 멀티패스를 자동으로 구성합니다.</th>
    </tr> 

</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>OVM</th>
        <th>Ovm3 heartbeat interval (ovm3.heartbeat.interval)</th>
        <th>관리 서버와 OVM3 호스트와의 하트비트 주기</th>
    </tr> 
    <tr>
        <th>OVM</th>
        <th>Ovm3 heartbeat timeout (ovm3.heartbeat.timeout)</th>
        <th>관리 서버 보낸 OVM3 호스트 하트비트 응답 대기 시간</th>
    </tr> 
    
</table>

<table>
    <tr>
        <th>분류</th>
        <th>옵션명</th>
        <th>설명</th>
    </tr>
    <tr>
        <th>Baremetal</th>
        <th>Baremetal internal storage server ip (baremetal.internal.storage.server.ip)</th>
        <th>베어메탈 환경에서 OS 이미지, 커널, ISO, PXE 부팅 파일 등을 저장하고 제공하는 내부 스토리지 서버의 주소입니다.</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>Baremetal ipmi fail retry (baremetal.ipmi.fail.retry)</th>
        <th>베어메탈 호스트의 IPMI를 통한 상태 확인 실패시 재시도 횟수</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>Baremetal ipmi lan interface (baremetal.ipmi.lan.interface)</th>
        <th>IPMI 의 LAN 인터페이스 지원 모드를 정합니다. lan(기본 인터페이스)/lanplus(보안이 강화된 인터페이스)</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>Baremetal provision done notification enabled (baremetal.provision.done.notification.enabled)</th>
        <th>베어메탈 프로비전이 완료됐을 때 알립니다.</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>Baremetal provision done notification port (baremetal.provision.done.notification.port)</th>
        <th>베어메탈 프로비전이 완료됐을 때 알리는 포트 번호</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>Baremetal provision done notification timeout (baremetal.provision.done.notification.timeout)</th>
        <th>베어메탈 프로비전이 완료될 때까지 기다리는 시간입니다. 정해진 시간이 지나면 프로비전 실패로 간주합니다.(단위 초)</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>Enable baremetal securitygroup agent echo (enable.baremetal.securitygroup.agent.echo)</th>
        <th>프로비전 프로세스 시작후, 보안그룹 에이전트 Echo 요청(ICMP ping)으로 연결을 확인합니다.</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>External baremetal resource classname (external.baremetal.resource.classname)</th>
        <th>외부 베어메탈 자원을 관리할 때 사용할 Java Class 입니다. 예)com.cloud.baremetal.ExternalBaremetalResource</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>External baremetal system url (external.baremetal.system.url)</th>
        <th>외부 베어메탈 자원의 관리 시스템 URL</th>
    </tr> 
    <tr>
        <th>Baremetal</th>
        <th>Timeout baremetal securitygroup agent echo (timeout.baremetal.securitygroup.agent.echo)</th>
        <th>프로비전 프로세스 시작후, 보안그룹 에이전트 Echo 요청(ICMP ping)으로 연결을 확인할 때 최대 대기 시간. 지정한 시간이 초과될 경우, 프로비전 실패로 간주합니다.</th>
    </tr> 
    
</table>

* Management Server
    * 관리 서버의 동작 방식과 관련된 설정 항목입니다.

* System VMs
    * 시스템 VM(예: 가상 라우터, 콘솔 프록시 등) 관련 설정 항목입니다.

* Infrastructure
    * 인프라 구성 및 운영 환경 설정 항목입니다.

* Miscellaneous
    * 기타 분류되지 않은 일반적인 설정 항목입니다.
