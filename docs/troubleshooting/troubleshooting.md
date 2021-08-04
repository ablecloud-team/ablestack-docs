# 문제유형

### Mold 대시보드 2차스토리지 용량이 0/0 으로 표기되고 연결이 안되는 현상

![Mold 대시보드 2차스토리지 오류](../assets/images/mold_secondarystorage_error.png){ align=center }

[에러 확인 방법]
 
 ssvm에 접속해서
 
 (접속하는 방법은 웹에서 웹콘솔로 접속하거나 ssvm 이 있는 호스트에 접속해서 virsh console s-oo-oo 로 접속) 

tail -f /var/log/cloud.log 를 확인하여 다음과 같은 에러메시지가 나온다면

에러메시지
!!! error
    Unable to start agent: Resource class not found: com.cloud.storage.resource.PremiumSecondaryStorageResource due to: java.lang.ClassNotFoundException: com.cloud.storage.resource.PremiumSecondaryStorageResource 

[조치방법]

/var/cache/cloud/cmdline  파일을 vi 편집기로 연 후에

!!! info "원본 cmdline 파일 내용"
    template=domP type=secstorage host=10.10.1.10 port=8250 name=s-4-VM zone=1 pod=11
    guid=s-4-VM workers=5 <span style="color:red">resource=com.cloud.storage.resource.PremiumSecondaryStoraa
    geResource</span> instance=SecStorage sslcopy=false role=templateProcessor mtu=1500 ethh
    2ip=10.10.1.22 eth2mask=255.255.0.0 gateway=10.10.0.1 public.network.device=eth22
    eth0ip=169.254.154.163 eth0mask=255.255.0.0 eth1ip=10.10.1.14 eth1mask=255.255..
    0.0 mgmtcidr=10.10.0.0/16 localgw=10.10.0.1 private.network.device=eth1 internall
    dns1=10.10.0.1 dns1=8.8.8.8 nfsVersion=nulll

resource 태그값을 수정
<span style="color:red">resource=com.cloud.storage.resource.PremiumSecondaryStorageResource</span>

-> <span style="color:blue">resource=org.apache.cloudstack.storage.resource.NfsSecondaryStorageResource</span>

!!! info "수정된 cmdline 파일 내용"
    template=domP type=secstorage host=10.10.1.10 port=8250 name=s-4-VM zone=1 pod=11
    guid=s-4-VM workers=5 <span style="color:blue">resource=org.apache.cloudstack.storage.resource.NfsSecondaryStorageResource</span> instance=SecStorage sslcopy=false role=templateProcessor mtu=1500 ethh
    2ip=10.10.1.22 eth2mask=255.255.0.0 gateway=10.10.0.1 public.network.device=eth22
    eth0ip=169.254.154.163 eth0mask=255.255.0.0 eth1ip=10.10.1.14 eth1mask=255.255..
    0.0 mgmtcidr=10.10.0.0/16 localgw=10.10.0.1 private.network.device=eth1 internall
    dns1=10.10.0.1 dns1=8.8.8.8 nfsVersion=nulll

혹은 다음의 스크립트 실행 - 해당부분을 바꿔주는 스크립트
``` shell
sed -i 's$resource=com.cloud.storage.resource.PremiumSecondaryStorageResource$resource=org.apache.cloudstack.storage.resource.NfsSecondaryStorageResource$' /var/cache/cloud/cmdline
```

수정한 후에 에이전트 재실행

``` shell
 systemctl restart cloud
```

### 디스크 장애(불량)으로 교체하는 방법

[에러 확인 방법]
SCVM에 접속하여 다음의 명령어