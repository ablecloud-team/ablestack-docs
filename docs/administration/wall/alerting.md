
# 경고
경고를 통해 시스템 문제가 발생한 직후 문제에 대해 알 수 있습니다. 강력하고 실행 가능한 경고를 통해 문제를 신속하게 식별하고 해결하여 서비스 중단을 최소화할 수 있습니다.

![wall-dashboard-dashboard-alerting-meun](../../assets/images/wall-dashboard-dashboard-alerting-meun.png)

메뉴 구조는 경고 규칙을 확인할 수 있는 "경고 규칙", 경고 알림을 보낼 대상(연락처)을 설정하는 "콘택트 포인트", 경고 알림 서비스를 설정할 수 있는 "알림 채널" 기능으로 구성되어 있습니다.

## 경고 규칙

![wall-dashboard-dashboard-alerting-alert-rule](../../assets/images/wall-dashboard-dashboard-alerting-alert-rule.png)

경고 규칙은 Wall에서 메뉴는 경고 조건을 설정하고 특정 임계값을 초과할 때 알림을 트리거하는 기능을 제공합니다.

**States 유형**
    - Normal : 정상 상태인 알람 조회
    - Not OK : 비정상 상태인 알람 조회
    - Alerting(firing) : 경고 상태인 알람 조회
    - No data : 데이터가 조회되지 않는 알람 조회
    - Paused : 일시중지된 알람 조회
    - Pending : 보류 중인 알람 조회 (지속적으로 조건을 충족하면 Alerting으로 변경됨)
    - Error : 쿼리 실행 중 오류 발생

## 콘택트 포인트

![wall-dashboard-dashboard-alerting-alert-channel](../../assets/images/wall-dashboard-dashboard-alerting-alert-channel.png)

콘택트 포인트 메뉴는 경고 규칙에서 발생한 경고(Alerting 상태)를 특정 대상(Slack, Email, Webhook 등)으로 알리는 역할을 합니다.
즉, Alert Rule이 트리거되었을 때 알림이 전송될 곳을 설정하는 메뉴입니다.

* 콘택트 포인트 생성 버튼 : 새로운 콘택트 포인트를 추가 등록할 수 있습니다.
* 모두 내보내기 버튼 : JSON 형식으로 콘택트 포인트를 내보내기할 수 있습니다.

!!! info
    Wall의 기본 알람 채널은 Email 방식입니다.

### 콘택트 포인트 생성

![wall-dashboard-dashboard-alerting-alert-new-channel](../../assets/images/wall-dashboard-dashboard-alerting-alert-new-channel.png)

새 콘택트 포인트를 등록하는 화면입니다.

1) 이름 : 콘택트 포인트 이름
2) 통합 : 알림을 받을 서비스 선택 (Slack, Email, Webhook 등)
3) Addresses : 수신 받을 이메일 ( ; 로 구분하여 다수의 이메일 입력 가능)
4) 추가 이메일 설정 : 선택적으로 설정할 수 있는 옵션 정보이며 알림에 포함할 정보 메시지를 설정합니다.
5) 알림 설정 : 알림에 포함할 정보를 선택
