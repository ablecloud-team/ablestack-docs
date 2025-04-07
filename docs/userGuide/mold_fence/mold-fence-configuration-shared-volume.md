두 가상머신에 Shared Volume을 LVM으로 구성한 후 Mysql-server를 각각 설치하고 DB의 데이터 경로를 Shared Volumed 경로로 변경합니다.  

==== [VM1, VM2 실행]
- Mold에서 Shared Disk를 구성합니다.
- 볼륨 파티션, 포멧, 마운트를 합니다.
```
fdisk /dev/sdb
  => n, 엔터, 엔터, 엔터, 엔터, 엔터, t, 8e, w

pvcreate /dev/sdb1
pvdisplay

vgcreate able /dev/sdb1
vgdisplay

lvcreate -l 100%FREE -n lv_data able
lvdisplay

mkfs.xfs -f /dev/able/lv_data
```

#### lvm.conf 설정
==== [VM1, VM2 실행]

LVM-activate를 등록할 때 해당 system_id를 사용하기 때문에 /etc/lvm/lvm.conf 구성 파일에서 system_id_source 구성 옵션을 uname 으로 설정합니다.
```
vi /etc/lvm/lvm.conf 
```
system-id 확인
```
vgs -o+systemid
```


### Mysql 설치 및 구성
==== [VM1, VM2 실행]
#### Mysql를 설치합니다.
* Mysql pcs resource에 의해 mysql이 제어되므로 mysql 서비스는 enable 하지 않습니다.
```
dnf install -y mysql-server
```

#### mysql을 구성합니다.
```
mysqld --initialize --datadir=/mnt/share/mysql
semanage fcontext -a -t mysqld_db_t "/mnt/share/mysql(/.*)?"
restorecon -R -v /mnt/share/mysql
chown -R mysql:mysql /mnt/share/mysql
chmod -R 750 /mnt/share/mysql
systemctl restart mysqld
```
```
mysql -uroot -p
ALTER USER 'root'@'localhost' IDENTIFIED BY '비밀번호';
FLUSH PRIVILEGES;
```

데이터 폴더를 변경합니다.
```
vi /etc/my.cnf.d/mysql-server.cnf
```
```
[mysqld]
datadir=/mnt/share/mysql
socket=/mnt/share/mysql/mysql.sock

[client]
socket=/mnt/share/mysql/mysql.sock
```
