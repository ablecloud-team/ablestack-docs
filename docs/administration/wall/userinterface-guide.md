# 사용자 인터페이스

## UI 로그인
Wall은 관리자와 최종 사용자가 모두 사용할 수 있는 웹 기반 UI를 제공합니다. 관리자는 Wall에 로그인하여 ABLESTACK 모니터링에 필요한 다양한 대시보드를 확인할 수 있으며 장애 이메일 알림서비스를 통해 ABLESTACK 장애상황을 조기에 대처할 수 있습니다. 최종 사용자는 Mold UI를 통해 자신이 소유한 가상머신의 모니터링 정보를 확인할 수 있습니다.

관리자 접속하는 URL은 다음과 같습니다.

 `http://ccvm-mngt-ip:3000/login`

![wall-login-webui](../../assets/images/wall-login-webui.png)

이메일 또는 사용자 이름 : 계정의 사용자의 이메일 또는 사용자 이름입니다. 최초 기본 사용자 이름은 admin입니다.
암호 : 사용자에 대한 암호. 최초 기본 사용자에 대한 암호는 admin입니다.

최초 로그인 성공화면 입니다.
![wall-passwd-reset](../../assets/images/wall-passwd-reset.png)

!!! info
    초기 로그인 후 admin 계정에 대한 비밀번호 변경을 해야 합니다.


## 관리자 계정 Wall UI 개요
관리자 계정으로 로그인하면 메인 페이지인 "1. 종합 대시보드" 화면이 나타납니다.
![wall-admin-page-info](../../assets/images/wall-admin-page-info.png)

ABLESTACK Wall 메뉴에 대한 간략한 설명은 다음과 같습니다. 

* 대시보드 검색 : 최근 본 대시보드, Wall 대시보드, 알람 대시보드를 볼 수 있습니다. 
* 홈 : Wall의 기본 시작 페이지로, 대시보드 목록과 즐겨찾기한 대시보드를 확인할 수 있습니다.
* 북마크 : 자주 사용하는 대시보드 또는 페이지를 북마크하여 빠르게 접근할 수 있습니다.
* 즐겨찾기 : 특정 대시보드를 즐겨찾기로 설정하여 빠르게 접근할 수 있는 기능입니다.
* 탐색 : 데이터 소스를 쿼리로 조회할 수 있습니다. 
* 경고 : 경고 규칙 및 알림 채널을 설정할 수 있습니다. 
* 연결 : 다양한 데이터 소스, 플러그인, 애플리케이션과 Grafana를 연결할 수 있는 설정 메뉴입니다. 
* 더 많은 앱 : Wall의 확장 기능을 제공하는 다양한 앱 및 플러그인을 설치하고 관리할 수 있습니다.
* 관리 : 사용자 관리, 권한 설정, 데이터 소스 및 플러그인 관리를 수행하고 조직 설정, 인증 설정 등의 고급 관리 기능을 포함하고 있습니다.

## 관리자 계정 Mold UI에서 Wall UI 접속 방법
admin 권한의 게정으로 Mold UI로 로그인 하고 ![wall-moldadmin-logon-button](../../assets/images/wall-moldadmin-logon-button.png) 버튼 클릭하면 아래 모달창이 나타납니다.

![wall-mold-logon-button-modal](../../assets/images/wall-mold-logon-button-modal.png)

"Monitoring Dashboard" 버튼을 클릭하여 Wall UI 로그인 페이지로 접근 가능 합니다.

## 최종 사용자 계정 Mold UI에서 Wall UI 접속 방법
최종 사용자 권한의 게정으로 Mold UI로 로그인 하고 (컴퓨트 > 가상머신) 메뉴에서 가상머신을 선택합니다.  
선택 후 ![wall-enduser-monitoring-button](../../assets/images/wall-enduser-monitoring-button.png) 버튼을 클릭하면 해당 가상머신의 모니터링을 확인할 수 있는 Wall UI 대시보드 페이지로 접근 합니다.

![wall-enduser-main-page](../../assets/images/wall-enduser-main-page.png)

!!! info
    최종 사용자는 별도의 로그인 필요 없이 접근 가능합니다.