두 가상머신에 Shared Volume을 LVM으로 구성한 후 Mysql-server를 각각 설치하고 DB의 데이터 경로를 Shared Volumed 경로로 변경합니다.  

lvm, file system, mysql을 pcs resource로 등록하고 그룹화하여 한 Node에서만 실행되고 이동되도록 구성합니다.

* resource group은 등록 순서에 따라 실행됩니다.

#### LVM-activate resource 에이전트 등록
예) # pcs resource create <resource name> LVM-activate vgname=<vgname> vg_access_mode=system_id --group <groupname>
```
pcs resource create cluster-vg ocf:heartbeat:LVM-activate vgname=able activation_mode=exclusive vg_access_mode=system_id --group test-grp
```

#### Filesystem resource 에이전트 등록
예) # pcs resource create <resource name> Filesystem device="/dev/<vgname>/<lvname>" directory="<directory name>" fstype="xfs" --group <groupname>
```
pcs resource create cluster-fs ocf:heartbeat:Filesystem device=/dev/able/lv_data directory=/mnt/share/ fstype=xfs --group test-grp
```

#### VIP resource 등록
```
pcs resource create vip ipaddr2 ip=10.10.254.199 cidr_netmask=16 op monitor interval=10 --group test-grp
pcs resource meta vip migration-threshold=1
pcs resource meta vip resource-stickiness=50
```

#### Mysql resource 에이전트 등록
* mysql은 systemctl service로 실행되는 것이 아닌, pcs agent에 의해 실행됩니다.
```
pcs resource create mysql ocf:heartbeat:mysql binary="/usr/sbin/mysqld" config="/etc/my.cnf.d/mysql-server.cnf" datadir="/mnt/share/mysql" pid="/run/mysql/mysqld.pid" socket="/mnt/share/mysql/mysql.sock" op start timeout=60s op stop timeout=60s op monitor interval=20s timeout=30s --group test-grp
```


## 구성 완료된 pcs 상태 확인
![image](https://github.com/ablecloud-team/ablestack-cloud/assets/34114265/d0c5a9de-f3a5-4d2b-aea9-75b47ddf4354)
![image](https://github.com/ablecloud-team/ablestack-cloud/assets/34114265/bfc7ca5c-ee3f-4d7c-8018-f31508ab18ad)