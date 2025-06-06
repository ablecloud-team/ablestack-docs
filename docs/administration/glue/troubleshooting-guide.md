!!! danger
    이 문서는 기술지원 용도의 문서입니다. 기술지원 엔지니어가 아닌 사용자가 조작할 때 시스템에 문제가 발생할 수 있습니다.
# 문제해결
## 대시보드 찾기
Glue 대시보드는 다음의 명령어를 이용하여 위치를 검색할 수 있습니다.
```
ceph mgr services | jq .dashboard
```
!!! tip
    많은 Ceph 도구는 결과를 JSON 형식으로 반환합니다.
    
    JSON 데이터 작업을 용이하게 하려면 jq 유틸리티를 설치하는 것이 좋습니다.

## 대시보드 접근
Glue 대시보드에 접근할 수 없는 경우 아래의 절차를 따라 문제 해결을 시도합니다.

문제를 해결하려면:

1. Glue 대시보드 모듈이 활성화 되었는지 확인합니다.
```
ceph mgr module ls | jq .enabled_modules
```
    명령의 반환 값에 Glue 대시보드 모듈이 나열되어 있는지 확인합니다. 위 명령어의 결과는 아래와 같습니다.
    ```
    [
      "dashboard",
      "iostat",
      "restful"
    ]
    ```

2. 목록에 없으면 다음 명령어를 이용하여 모듈을 활성화 합니다.
```
ceph mgr module enable dashboard
```

3. Glue 대시보드 또는 ceph-mgr 로그 파일에서 오류를 확인합니다.
    ceph-mgr 로그 메시지가 파일에 기록되었는지 확인합니다. 다음의 명령어를 이용합니다.
    ```
    ceph config get mgr log_to_file
    ```
    로그 파일의 위치를 가져옵니다. (기본 위치는 /var/log/ceph/<cluster-name\>-<daemon-name\>.log 입니다.)
    ```
    ceph config get mgr log_file
    ```

4. SSL/TLS 지원이 올바르게 구성되었는지 확인합니다.
    SSL/TLS 지원이 활성화 되어 있는지 확인하려면 다음 명령어를 이용합니다.
    ```
    ceph config get mgr mgr/dashboard/ssl
    ```
    위 명령어가 ture 값을 반환하면, 다음의 명령어를 이용하여 인증서가 있는지 확인합니다.
    ```
    ceph config-key get mgr/dashboard/crt
    ```
    ```
    ceph config-key get mgr/dashboard/key
    ```
    위 명령어가 ture 값을 반환하지 않으면, 다음의 명령어를 이용하여 자체 서명된 인증서를 생성하거나 SSL/TLS 지원에 설명된 지침을 참고하시기 바랍니다.
    ```
    ceph dashboard create-self-signed-cert
    ```
## 대시보드 로그인 문제
Glue 대시보드에 로그인 할 수없고 다음 오류가 표시되는 경우 아래 절차를 확인하시기 바랍니다.

<center>
![glue-troubleshooting](../../assets/images/glue-troubleshooting.png)
</center>

1. 사용자 자격 증명이 올바른지 확인합니다.

    Glue 대시보드에 로그인하려고 할 때 위의 알림 메시지가 표시되는 경우 잘못된 자격 증명을 사용하고있을 가능성이 있습니다. 사용자 이름과 암호를 다시 확인하고 키보드의 Caps Lock이 실수로 활성화되지 않았는지 확인하시기 바랍니다.

2. 사용자 자격 증명이 정확하지만 동일한 오류가 발생하는 경우 사용자 계정이 있는지 확인합니다.
    ```
    ceph dashboard ac-user-show <username>
    ```
    이 명령은 사용자 데이터를 반환합니다. 사용자가 존재하지 않으면 다음과 같은 값을 반환합니다.
    ```
    Error ENOENT: User <username> does not exist
    ```
3. 사용자가 활성화 되어 있는지 확인합니다.
    ```
    ceph dashboard ac-user-show <username> | jq .enabled
    ```
    만약 사용자가 활성화 되어 있지 않은 경우 다음의 명령어를 입력합니다.
    ```
    ceph dashboard ac-user-enable <username>
    ```

    자세한 내용은 [사용자 및 역할 관리](../account&role-guide)를 참조하세요.

## 대시보드 기능이 동작하지 않음
백엔드에서 오류가 발생하면 일반적으로 프런트 엔드에서 오류 알림을 받게됩니다. 디버그하려면 다음 시나리오를 실행하십시오.

1. Glue 대시보드 및 ceph-mgr 로그 파일에서 오류를 확인합니다. 500 내부 서버 오류와 같은 키워드를 검색 한 다음 추적하여 찾을 수 있습니다. traceback의 끝에는 발생한 오류에 대한 자세한 정보가 포함되어 있습니다.
2. 웹 브라우저의 Javascript 콘솔에서 오류를 확인하십시오.

## 대시보드 로그
### 대시보드 디버그 플래그
이 플래그를 사용하면 오류 추적이 백엔드 응답에 포함됩니다.
Glue 대시보드에서 이 플래그를 활성화하려면 클러스터에서 관리자 모듈로 이동합니다. 대시 보드 모듈을 선택하고 편집 버튼을 클릭합니다. 디버그 확인란을 클릭하고 업데이트합니다.

다음 명령어를 이용하면 CLI를 통해 디버그 모드를 활성화 할 수 있습니다.
```
ceph dashboard debug enable
```

### 대시보드 모듈의 로깅 수준 설정
로깅 수준을 debug로 설정하면 로그가 더 자세하고 디버깅에 도움이됩니다.

관리자 데몬의 로깅 수준을 높이는 명령어는 다음과 같습니다.
```
ceph tell mgr config set debug_mgr 20
```
Glue 대시보드의 로깅 수준을 높이는 명령어는 방법은 다음과 같습니다.

- 대시보드를 이용하는 방법

    클러스터에서 관리자 모듈로 이동합니다. 대시보드 모듈을 선택하고 편집 버튼을 클릭합니다. log_level 구성을 수정합니다.

- CLI를 이용하는 방법
    ```
    ceph config set mgr mgr/dashboard/log_level debug
    ```
!!! warning
    로그 수준이 높으면 로그 볼륨이 매우 높아져 시스템에 영향을 미칠 수 있습니다.
    
로깅 증가를 초기화 할 수 있는 명령어는 다음과 같습니다.
```
ceph config log

...
--- 11 --- 2020-11-07 11:11:11.960659 --- mgr.x/dashboard/log_level = debug ---
...
```
```
ceph config reset 11
```
