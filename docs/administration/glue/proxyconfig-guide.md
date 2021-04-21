!!! danger
    이 문서는 관리자용 문서입니다. 관리자가 아닌 사용자가 동작시 문제가 발생할수도 있습니다.
# 프록시 설정
여러 ceph-mgr 인스턴스가 있는 Ceph 클러스터에서는 현재 활성 ceph-mgr 데몬에서 실행중인 대시보드만 수신 요청을 처리합니다.
대기 ceph-mgr 인스턴스에서 대시보드의 TCP 포트에 대한 연결은 활성 관리자의 대시보드 URL에 대한 HTTP 리다이렉션(303)을 수신합니다.
이렇게하면 ceph-mgr 대시보드에 접근하기 위해 브라우저에서 인스턴스를 가리킬 수 있습니다.

대시보드에 연결하기 위한 고정 URL을 설정하거나 관리자 노드에 대한 직접 연결을 허용하지 않으려는 경우, 수신 요청을 활성 ceph-mgr 인스턴스로 자동 전달하는 프록시를 설정할 수 있습니다.
## URL 접두사 구성 
역방향 프록시를 통해 대시보드에 액세스하는 경우 URL 접두사로 서비스를 제공 할 수 있습니다. 접두사가 포함 된 하이퍼링크를 사용하여 대시보드를 가져 오려면 url_prefix을 설정합니다.
???+example "PREFIX 설정"
    ceph config set mgr mgr/dashboard/url_prefix $PREFIX

!!! info "http://\$IP:\$PORT/\$PREFIX/ 를 통해 대시보드에 접근할 수 있습니다."

## 리다이렉션 비활성화
대시보드가 HAProxy와 같은 로드 밸런싱 프록시 뒤에 있는 경우 내부(확인할 수 없는) URL이 프런트 엔드 클라이언트에 게시되는 상황을 방지하기 위해 리다이렉션을 비활성화 할 수 있습니다. 다음 명령을 사용하여 대시 보드가 활성 대시 보드로 리다이렉션하는 대신 HTTP 오류 (기본적으로 500)로 응답하도록 합니다.
???+ example "리다이렉션 비활성화"
    ceph config set mgr mgr/dashboard/standby_behaviour "error"

설정을 기본 리다이렉션으로 재설정하려면 다음의 명령을 이용합니다.
???+ example "리다이렉션 활성화"
    ceph config set mgr mgr/dashboard/standby_behaviour "redirect"

## 오류 상태 코드 설정
리디렉션이 비활성화 된 경우 대기 대시보드의 HTTP 상태 코드를 사용자가 지정할 수 있습니다. 다음의 명령을 실행해야 합니다.
???+ example "상태 코드 사용자 지정"
    ceph config set mgr mgr/dashboard/standby_error_status_code 503

## HAProxy 예제 구성
아래에서 HAProxy를 사용하는 SSL/TLS 패스스루 구성 예제를 확인할 수 있습니다.

이 구성은 다음 조건에서 작동합니다. 대시보드가 장애 조치되면 프런트 엔드 클라이언트가 HTTP 리디렉션 (303) 응답을 수신하고 확인할 수 없는 호스트로 리다이렉션됩니다. 이는 두 HAProxy 상태 확인간에 장애 조치가 발생할 때 발생합니다. 이 상황에서 이전 활성 대시보드 노드는 새 활성 노드를 가리키는 303으로 응답합니다. 이러한 상황을 방지하려면 대기 노드에서 리다이렉션을 비활성화하는 것을 고려해야합니다.
```
defaults
  log global
  option log-health-checks
  timeout connect 5s
  timeout client 50s
  timeout server 450s

frontend dashboard_front
  mode http
  bind *:80
  option httplog
  redirect scheme https code 301 if !{ ssl_fc }

frontend dashboard_front_ssl
  mode tcp
  bind *:443
  option tcplog
  default_backend dashboard_back_ssl

backend dashboard_back_ssl
  mode tcp
  option httpchk GET /
  http-check expect status 200
  server x <HOST>:<PORT> ssl check verify none
  server y <HOST>:<PORT> ssl check verify none
  server z <HOST>:<PORT> ssl check verify none
```