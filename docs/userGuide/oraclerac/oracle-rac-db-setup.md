Oracle 데이터베이스 소프트웨어 설치 및 데이터베이스를 구성하는 가이드입니다.

!!! info
    가이드에 사용되는 입력값은 예시입니다. 필요시 환경에 맞게 변경 가능합니다.

## 데이터베이스 소프트웨어 구성
Oracle RAC 데이터베이스 엔진 소프트웨어를 설치합니다.

```shell title="Oracle 설치 폴더 생성 및 권한설정 ( 노드 : 전체 / 계정 : root )"
mkdir -p /u02/app/oracle
mkdir -p /u02/app/oraInventory
chown -R oracle:dba /u02/app/oracle
chown -R oracle:dba /u02/app/oraInventory
chmod -R 775 /u02/app
```

```shell title="oracle 계정 bash_profile 수정 ( 노드 : node1 / 계정 : oracle )"
su – oracle
vi .bash_profile

(추가)
export LANG=C
export ORACLE_BASE=/u02/app/oracle
export ORACLE_HOME=/u02/app/oracle/product/19.0.0/dbhome_1
export ORACLE_SID=ORA191
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export NLS_LANG=AMERICAN_AMERICA.AL32UTF8
export PATH=$ORACLE_HOME/bin:$PATH

alias oh='cd $ORACLE_HOME'
```

```shell title="oracle 계정 bash_profile 수정 ( 노드 : node2 / 계정 : oracle )"
su – oracle
vi .bash_profile

(추가)
export LANG=C
export ORACLE_BASE=/u02/app/oracle
export ORACLE_HOME=/u02/app/oracle/product/19.0.0/dbhome_1
export ORACLE_SID=ORA192
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export NLS_LANG=AMERICAN_AMERICA.AL32UTF8
export PATH=$ORACLE_HOME/bin:$PATH

alias oh='cd $ORACLE_HOME'
```

```shell title="oracle 설치파일 압축 풀기 ( 노드 : node1 / 계정 : oracle )"
mkdir -p /u02/app/oracle/product/19.0.0/dbhome_1
cd /u02/app/oracle/product/19.0.0/dbhome_1
unzip -q /home/STAGE/LINUX.X64_193000_db_home.zip
(1번노드에서만 풀면 됨 > 설치시 다른노드에 자동 복사함)
```

```shell title="oracle 설치 ui 구동 ( 노드 : node1 / 계정 : oracle )"
> 윈도우 x-trem으로 접속하여 실행 (mac os 에서는 설치 UI 화면 깨짐 / windows MobaXtrem 사용)
su - oracle

cd /u02/app/oracle/product/19.0.0/dbhome_1
./runInstaller
```

![db-1](../../../../assets/images/oraclerac/oracle-rac-db-setup-1.png){:class="imgCenter"}

- Set Up Software Only 선택
- Next 버튼 클릭

![db-2](../../../../assets/images/oraclerac/oracle-rac-db-setup-2.png){:class="imgCenter"}

- Oracle Real Application Clusters database installation 선택
- Next 버튼 클릭

![db-3](../../../../assets/images/oraclerac/oracle-rac-db-setup-3.png){:class="imgCenter"}

- SSH connectivity 버튼 클릭
- OS Password : oracle 계정 비밀번호 입력
- Setup 버튼 클릭
- Next 버튼 클릭

![db-4](../../../../assets/images/oraclerac/oracle-rac-db-setup-4.png){:class="imgCenter"}

- Enterprise Edition 선택
- Next 버튼 클릭

![db-5](../../../../assets/images/oraclerac/oracle-rac-db-setup-5.png){:class="imgCenter"}

- Next 버튼 클릭

![db-6](../../../../assets/images/oraclerac/oracle-rac-db-setup-6.png){:class="imgCenter"}

- group 을 dba로 선택
- Next 버튼 클릭

![db-7](../../../../assets/images/oraclerac/oracle-rac-db-setup-7.png){:class="imgCenter"}

- Automatically run configuration scripts 선택
- Password 입력
- Next 버튼 클릭

![db-8](../../../../assets/images/oraclerac/oracle-rac-db-setup-8.png){:class="imgCenter"}

- 설치 전 체크 테스트 화면

![db-9](../../../../assets/images/oraclerac/oracle-rac-db-setup-9.png){:class="imgCenter"}

- Ignore 선택
- Next 버튼 클릭
- Yes 버튼 클릭

![db-10](../../../../assets/images/oraclerac/oracle-rac-db-setup-10.png){:class="imgCenter"}

- Install 버튼 클릭

![db-11](../../../../assets/images/oraclerac/oracle-rac-db-setup-11.png){:class="imgCenter"}

- Yes 버튼 클릭

![db-12](../../../../assets/images/oraclerac/oracle-rac-db-setup-12.png){:class="imgCenter"}

- Close 버튼 클릭

```shell title="oracle 데이터베이스 구성 ui 구동 ( 노드 : node1 / 계정 : oracle )"
> 윈도우 x-trem으로 접속하여 실행 (mac os 에서는 설치 UI 화면 깨짐 / windows MobaXtrem 사용)
su - oracle

dbca
```

![db-13](../../../../assets/images/oraclerac/oracle-rac-db-setup-13.png){:class="imgCenter"}

- Create a databases 선택
- Next 버튼 클릭

![db-14](../../../../assets/images/oraclerac/oracle-rac-db-setup-14.png){:class="imgCenter"}

- Advanced configuration 선택
- Next 버튼 클릭

![db-15](../../../../assets/images/oraclerac/oracle-rac-db-setup-15.png){:class="imgCenter"}

- General Purpose or Transaction Processiong 선택
- Next 버튼 클릭

![db-16](../../../../assets/images/oraclerac/oracle-rac-db-setup-16.png){:class="imgCenter"}

- Next 버튼 클릭

![db-17](../../../../assets/images/oraclerac/oracle-rac-db-setup-17.png){:class="imgCenter"}

- Create as Container database 해제
- Next 버튼 클릭

![db-18](../../../../assets/images/oraclerac/oracle-rac-db-setup-18.png){:class="imgCenter"}

- Next 버튼 클릭

![db-19](../../../../assets/images/oraclerac/oracle-rac-db-setup-19.png){:class="imgCenter"}

- Next 버튼 클릭

![db-20](../../../../assets/images/oraclerac/oracle-rac-db-setup-20.png){:class="imgCenter"}

- Next 버튼 클릭

![db-21](../../../../assets/images/oraclerac/oracle-rac-db-setup-21.png){:class="imgCenter"}

- Sample schemas 탭 클릭
- Add sample schemas to the database 선택
- Next 버튼 클릭

![db-22](../../../../assets/images/oraclerac/oracle-rac-db-setup-22.png){:class="imgCenter"}

- Run Cluster Verification Utility (CVU) checks periodically 해제
- Next 버튼 클릭

![db-23](../../../../assets/images/oraclerac/oracle-rac-db-setup-23.png){:class="imgCenter"}
오라클 관리자 계정 비밀번호 입력

- Use the same administrative passwrod for all accounts 선택
- 비밀번호 입력
- Next 버튼 클릭

![db-24](../../../../assets/images/oraclerac/oracle-rac-db-setup-24.png){:class="imgCenter"}

- Next 버튼 클릭

![db-25](../../../../assets/images/oraclerac/oracle-rac-db-setup-25.png){:class="imgCenter"}

- 설치 전 체크 테스트 화면

![db-26](../../../../assets/images/oraclerac/oracle-rac-db-setup-26.png){:class="imgCenter"}

- Ignore 선택
- Next 버튼 클릭
- Yes 버튼 클릭

![db-27](../../../../assets/images/oraclerac/oracle-rac-db-setup-27.png){:class="imgCenter"}

- Finish 선택

![db-28](../../../../assets/images/oraclerac/oracle-rac-db-setup-28.png){:class="imgCenter"}

- 설치 진행 화면

![db-29](../../../../assets/images/oraclerac/oracle-rac-db-setup-29.png){:class="imgCenter"}

- Close 버튼 클릭

Oracle 데이터베이스 구성 완료

```shell title="Oracle 데이터베이스 구성 확인 ( 노드 : node1 / 계정 : grid )"
crsctl stat res -t
```

![db-30](../../../../assets/images/oraclerac/oracle-rac-db-setup-30.png){:class="imgCenter"}

- ora19.db에 항목에 ol7rac1, ol7rac2 노드의 상태가 ONLINE인지 확인
- 설치 완료

## RAC 테스트 구성
Oracle RAC 데이터베이스 구성후 테스트는 1번 노드와 2번 노드에서 각각 insert 쿼리를 실행하고 양방향 저장 및 조회가 정상적으로 가능한지 확인

![db-31](../../../../assets/images/oraclerac/oracle-rac-db-setup-31.png){:class="imgCenter"}

1. 1번 노드에서 테스트 테이블 member_info 생성
2. 1번 노드에서 테이블 데이터 조회, 데이터 없음 확인
3. 1번 노드에서 insert 데이터 kim
4. 1번 노드에서 데이터 조회, 입력된 kim 데이터 확인
5. 2번 노드에서 데이터 조회, 입력된 kim 데이터 확인
6. 2번 노드에서 insert 데이터 lee
7. 2번 노드에서 데이터 조회, 입력된 kim, lee 데이터 확인
8. 1번 노드에서 데이터 조회, 입력된 kim, lee 데이터 확인

Oracle RAC 구성 완료














