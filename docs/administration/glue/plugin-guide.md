# 플러그인
플러그인은 모듈 방식으로 느슨하게 결합 된 방식으로, Glue 대시보드의 기능을 확장합니다.

## 기능 토글
이 플러그인은 요청 형식의 Glue 대시보드에서 일부 기능을 활성화 또는 비활성화 할 수 있습니다.
기능이 비활성화 되면 아래와 같습니다.
```
프런트 엔드 요소(웹 페이지, 메뉴 항목, 차트 등)가 숨겨집니다.
연관된 REST API 엔드 포인트는 추가 요청을 거부합니다(404, 찾을 수 없음 오류).
```
이 플러그인의 주요 목적은 대시보드에 의해 노출 된 워크 플로우의 임시 사용자 정의를 허용하는 것입니다. 또한 최소한의 구성 부담과 서비스 영향없이 실험적 기능을 동적으로 활성화 할 수 있습니다.
활성화 / 비활성화 할 수있는 기능 목록은 다음과 같습니다.
```
블록(RBD)
    이미지 관리 : rbd
    미러링 : mirroring
    iSCSI : iscsi
파일 시스템 (Cephfs) :cephfs
객체(RGW) : rgw(데몬, 사용자 및 버킷 관리 포함)
NFS : nfs-ganesha 내보내기
```
기본적으로 모든 기능이 활성화됩니다.
다음의 명령어를 이용하면 기능 목록 및 현재 상태를 검색할 수 있습니다.
```
$ ceph dashboard feature status
  Feature 'cephfs': 'enabled'
  Feature 'iscsi': 'enabled'
  Feature 'mirroring': 'enabled'
  Feature 'rbd': 'enabled'
  Feature 'rgw': 'enabled'
  Feature 'nfs': 'enabled'
```
하나 또는 여러 기능을 활성화 또는 비활성화 할 수 있습니다. 다음의 명령어는 iscsi, mirroring 기능을 비활성화 하는 예시입니다.
```
$ ceph dashboard feature disable iscsi mirroring
  Feature 'iscsi': disabled
  Feature 'mirroring': disabled
```
기능 상태가 변경된 후 API REST 엔드 포인트는 해당 변경에 즉시 응답하지만, 프런트 엔드 UI 요소의 경우에는 이를 반영하는 데 최대 20초가 걸릴 수 있습니다.

## 디버그
이 플러그인을 사용하면 디버그 모드에 따라 대시 보드의 동작을 사용자 지정할 수 있습니다. 다음 명령으로 현재 상태를 확인, 활성화 또는 비활성화 할 수 있습니다.
```
$ ceph dashboard debug status
  Debug: 'disabled'
$ ceph dashboard debug enable
  Debug: 'enabled'
$ ceph dashboard debug disable
  Debug: 'disabled'
```