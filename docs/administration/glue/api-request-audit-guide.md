!!! danger
    이 문서는 기술지원 용도의 문서입니다. 기술지원 엔지니어가 아닌 사용자가 조작할 때 시스템에 문제가 발생할 수 있습니다.
# API 요청 감사
REST API는 PUT, POST 및 DELETE 요청을 Ceph 감사 로그에 기록 할 수 있습니다. 이 기능은 기본적으로 비활성화 되어 있지만 다음 명령을 사용하여 활성화 할 수 있습니다.
```
ceph dashboard set-audit-api-enabled <true|false\>
```
활성화 된 경우 각 요청마다 다음 매개 변수가 기록됩니다.

- from - 출처, 예: https://[:: 1]:44410
- path - REST API 경로, 예: /api/auth
- method - 예: PUT, POST, DELETE 등
- user - 사용자의 이름, 그렇지 않으면 '없음'

페이로드 요청(인수 및 해당 값)의 로깅은 기본적으로 활성화됩니다. 다음 명령어를 이용하여 기능을 비활성화 할 수 있습니다.
```
ceph dashboard set-audit-api-log-payload <true|false\>
```
로그 내용은 다음과 같습니다.
```
2021-04-19 13:52:01.302514 mgr.x [INF] [DASHBOARD] from='https://[::ffff:127.0.0.1]:37022' path='/api/rgw/user/ablecloud' method='PUT' user='admin' params='{"max_buckets": "1000", "display_name": "Ablecloud", "uid": "ablecloud", "suspended": "0", "email": "ablecloud@ablecloud.io"}'
```
