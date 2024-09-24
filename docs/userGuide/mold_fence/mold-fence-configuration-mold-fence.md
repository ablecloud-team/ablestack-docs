Mold 가상머신을 fencing 처리하기 위한 mold fence agent를 설치하고 이를 동작시키기 위한 PCS STONITH(Shoot The Other Node In The Head)를 생성합니다.

### Mold Fence Agent 설치

==== [VM1, VM2 실행]
```
wget -P /root/ https://images.ablecloud.io/fence-mold-1.0-1.el9.x86_64.rpm
rpm -Uvh /root/fence-mold-1.0-1.el9.x86_64.rpm --force
```

### PCS Resource 등록
fencing 처리를 위한 stonith resource 구성

#### 각 노드에 fencing 처리를 위한 stonith를 생성하고 구성.
==== [VM1 실행]
```
   -z, --zone=[zone]                          					Zone, e.g. zone1
   -ap, --api-protocol=[api-protocol] 				Api protocol, e.g. http
   -a, --api_key=[key]                        					API Key
   -s, --secret_key=[key]                    					Secret Key
   -vi, --vm_id=[option]                       				VM-ID
   -mip, --m_ip=[mip]                          				MOLD Ip Address
   -mpt, --m_port=[mport]                 					MOLD Port
   -mtt, --m_total_timeout=[mtotaltineout]   	Total Timeout to check MOLD Status(seconds)
   -mit, --m_interval=[mport]                  			Interval to check MOLD Status

```
	* stonith에 대한 추가 명령어 정보는 `fence_mold -h` 를 입력하여 확인할 수 있습니다.

1) stonith 생성 예제
   VM1을 fence하는 fence-node1와 VM2을 fence하는 fence-node2를 생성합니다.
```
pcs stonith create fence-node1 fence_mold \
api_protocol="http" \
m_ip="10.10.1.10" \
m_port="8080" \
api_key="ew68uZifMjNXd6PbRUGtvVA98TnohwDc6R73-kq_tvI" \
secret_key="xrWdgQNJMoAzhtnJYl7-fGApjLxhz4GHqnuMrSbVn2E" \
vm_id="0d859221-87a6-428b-9516-f9727e22ec20" \
delay="15" \
m_total_timeout="600" \
m_interval="10" \
pcmk_host_list="lilo-ha1" \
pcmk_reboot_action="off"
```

```
pcs stonith create fence-node2 fence_mold \
api_protocol="http" \
m_ip="10.10.1.10" \
m_port="8080" \
api_key="ew68uZifMjNXd6PbRUGtvVA98TnohwDc6R73-kq_tvI" \
secret_key="xrWdgQNJMoAzhtnJYl7-fGApjLxhz4GHqnuMrSbVn2E" \
vm_id="fb42b9ff-43c2-49b2-9641-1ca2c67e43f9" \
m_total_timeout="30" \
m_interval="6" \
pcmk_host_list="lilo-ha2" \
pcmk_reboot_action="off"
```

* stonith 업데이트 방법
  설정 요소 변경에 따른 업데이트 명령어는 다음과 같습니다.
  예) # pcs stonith update my-stonith attribute1=value1 attribute2=value2
  ```
  pcs stonith update fence-node1 api_key="3568uZifMjNXd6PSDFEsfdtvVA98TnohwDc6R73-kq_tvI" m_port="8443"
  ```


2) stonith 정책 설정
   서로 다른 노드에서 실행되도록 설정
```
pcs constraint location fence-node1 avoids lilo-ha1
pcs constraint location fence-node2 avoids lilo-ha2
```
기본 stonith 액션을 power off로 변경
```
pcs property set stonith-action=off
```