# 사용자 인터페이스
Mold는 관리자와 최종 사용자가 모두 사용할 수 있는 웹 기반 UI를 제공합니다. 로그인에 사용된 자격 증명에 따라 적절한 버전의 UI가 표시됩니다. UI는 Chrome, Firefox, Edge 및 Safari를 포함한 모든 최신 인기 브라우저에서 사용할 수 있습니다. UI는 API 자동 검색을 사용하여 로그인 한 사용자에게 허용 된 메뉴 및 기능을 제공합니다.

접속하는 URL은 다음과 같습니다.

 `http://ccvmIP:8080`

![mold-login-webui](../../assets/images/mold_login_webUI.png)

사용자 명 : 계정의 사용자 ID 입니다. 최초 기본 사용자 이름은 admin 입니다

암호 : 사용자 ID에 대한 암호. 최초 기본 사용자에 대한 암호는 password 입니다
!!! info
    초기 로그인 후 Zone 구성 시에 admin 계정에 대한 비밀번호 변경을 해야 합니다

도메인 : 계정이 소속된 도메인 전체 경로를 입력합니다. 
!!! tip
    예를 들어 ablecloud라는 도메인이 있고 그 하위에 dev1, dev2와 같이 여러 수준의 도메인이 만들어 져있다고 할 경우 ablecloud라는 도메인의 사용자는 도메인 항목에 ablecloud 라고 입력하고 dev1 도메인 사용자는 ablecloud/dev1 이라고 입력해야 합니다
    
    만일, 루트 사용자인 경우는 입력하지 않아도 됩니다.



