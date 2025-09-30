pacemaker를 설치하고 고가용성 클러스터를 구성합니다. 

###  방화벽 해제
==== [VM1, VM2 실행]

```
firewall-cmd --permanent --zone=public --add-port=22/tcp
firewall-cmd --permanent --zone=public --add-service=high-availability
firewall-cmd --add-service=high-availability
```

### pacemaker 패키지 설치
==== [VM1, VM2 실행]
```
dnf -y upgrade
dnf -y config-manager --set-enabled crb
dnf -y install epel-release
dnf -y install https://rpms.remirepo.net/enterprise/remi-release-9.rpm
dnf --enablerepo=highavailability -y install pacemaker pcs fence-agents-all
```

### 서비스 시작 및 등록
```
systemctl start pcsd
systemctl enable pcsd
systemctl enable corosync
systemctl enable pacemaker
```

### 클러스터 계정 존재여부 확인
```
cat /etc/passwd |grep hacluster
```

### hosts 파일 변경
```
vi /etc/hosts
```
```
####Pacemaker Hearbeat IP####
10.10.254.100 lilo-ha1
10.10.254.101 lilo-ha2
```

```
systemctl restart NetworkManager
```

### Pacemaker 클러스터 구성 및 시작
==== [VM1 실행]
```
pcs host auth lilo-ha1 lilo-ha2 -u hacluster -p 비밀번호
pcs cluster setup hacluster --start lilo-ha1 lilo-ha2
```

==== [VM1, VM2 실행]
```
systemctl start pacemaker
```
