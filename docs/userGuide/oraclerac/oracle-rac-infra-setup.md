ABLESTACK Mold 가상화 환경에서 Oracle RAC를 구성하기위해 ISO 다운로드, 네트워크 생성, 오퍼링 생성, 템플릿 생성, 가상머신 생성, 공유 디스크 연결 작업 가이드입니다.

!!! info
    가이드에 사용되는 입력값은 예시입니다. 필요시 환경에 맞게 변경 가능합니다.

## Oracle Linux ISO 등록
Oracle RAC를 구성하는 운영체제로 Red Hat Enterprise Linux 계열과 Oracle Linux을 사용할 수 있으며 해당 가이드에서는 Oracle Linux 7.9를 활용하여 구성합니다.

![infra-setup-1](../../../../assets/images/oraclerac/oracle-rac-infta-setup-1.png){:class="imgCenter"}

- https://yum.oracle.com/oracle-linux-isos.html 사이트에 접속
- 링크 주소 복사하여 OracleLinux 7.9  다운로드 링크 (https://yum.oracle.com/ISOS/OracleLinux/OL7/u9/x86_64/OracleLinux-R7-U9-Server-x86_64-dvd.iso) 복사
- Mold에  접속하여 OracleLinux ISO 등록 작업 진행

!!! info
    Oracle linux download 사이트 https://yum.oracle.com/oracle-linux-isos.html

## Oracle Linux ISO 등록
ABLESTACK Mold 화면에서 **이미지 > ISO** 화면에서 **ISO 등록 버튼**을 클릭하여 ISO 등록 화면으로 이동합니다.

![infra-setup-2](../../../../assets/images/oraclerac/oracle-rac-infta-setup-2.png){:class="imgCenter"}

- URL : https://yum.oracle.com/ISOS/OracleLinux/OL7/u9/x86_64/OracleLinux-R7-U9-Server-x86_64-dvd.iso
- 이름 : OracleLinux-R7-U9-Server-x86_64-dvd.iso
- 설명 : OracleLinux-R7-U9-Server-x86_64-dvd.iso
- 부팅 가능 : 선택
- OS 유형 : Oracle Linux 7 선택
- 추출 가능 : 선택
- 공개 : 선택
- 추천 : 선택
- 확인 버튼을 클릭하여 ISO 생성

![infra-setup-3](../../../../assets/images/oraclerac/oracle-rac-infta-setup-3.png){:class="imgCenter"}

- ISO 목록에 OracleLinux-R7-U9-Server-x86_64-dvd.iso의 상태가 Ready인지 확인
- Ready 상태가 되면  ISO 사용가능

## RAC용 네트워크 추가
ABLESTACK Mold 화면에서 **네트워크 > 가상머신용 네트워크** 화면에서 **네트워크 추가 버튼**을 클릭하여 네트워크 등록 화면으로 이동합니다.

### public 용 네트워크 추가
![infra-setup-4](../../../../assets/images/oraclerac/oracle-rac-infta-setup-4.png){:class="imgCenter"}

- 이름 : rac-public-net
- 설명 : rac-public-net
- Zone : zone 선택
- 네트워크 오퍼링 : 기본 격리 네트워크 (with SourceNat)
- 게이트웨이 : 192.168.0.1
- 넷마스크 : 255.255.255.0
- 확인 버튼을 클릭하여 private 용 네트워크 생성

### private 용 네트워크 추가
![infra-setup-5](../../../../assets/images/oraclerac/oracle-rac-infta-setup-5.png){:class="imgCenter"}

- 이름 : rac-private-net
- 설명 : rac-private-net
- Zone : zone 선택
- 네트워크 오퍼링 : 기본 격리 네트워크 (with SourceNat)
- 확인 버튼을 클릭하여 private 용 네트워크 생성

![infra-setup-6](../../../../assets/images/oraclerac/oracle-rac-infta-setup-6.png){:class="imgCenter"}

- rac-public-net과 rac-private-net이 정상적으로 생성되었는지 확인


## 디스크 오퍼링 생성
ABLESTACK Mold 화면에서 **서비스 오퍼링 > 디스크 오퍼링** 화면에서 **디스크 오퍼링 추가 버튼**을 클릭하여 디스크 오퍼링 추가 화면으로 이동합니다.

### root용 디스크 오퍼링 생성
![infra-setup-7](../../../../assets/images/oraclerac/oracle-rac-infta-setup-7.png){:class="imgCenter"}

- 이름 : 100GB-WB
- 설명 : 100GB-WB
- 사용자지정 디스크 크기 : 해제
- 디스크 크기(GB 단위) : 100
- Write-cache 유형 : Write-back 디스크 캐싱 선택
- 스토리지 태그 : ps 선택
- 공개 : 선택
- 확인 버튼을 클릭하여 디스크 오퍼링 생성

### 공유 스토리지용 공유 디스크 오퍼링 생성
![infra-setup-8](../../../../assets/images/oraclerac/oracle-rac-infta-setup-8.png){:class="imgCenter"}

- 이름 : 100GB-shareable
- 설명 : 100GB-shareable
- 사용자지정 디스크 크기 : 해제
- 디스크 크기(GB 단위) : 100
- 공유 볼륨 : 선택
- 스토리지 태그 : ps 선택
- 공개 : 선택
- 확인 버튼을 클릭하여 공유디스크 용 디스크 오퍼링 생성

![infra-setup-9](../../../../assets/images/oraclerac/oracle-rac-infta-setup-9.png){:class="imgCenter"}

- 100GB-WB와 100GB-shareable 디스크 오퍼링이 정상적으로 생성되었는지 확인

## 컴퓨트 오퍼링 생성
ABLESTACK Mold 화면에서 **서비스 오퍼링 > 컴퓨트 오퍼링** 화면에서 **컴퓨트 오퍼링 추가 버튼**을 클릭하여 컴퓨트 오퍼링 추가 화면으로 이동합니다.

![infra-setup-10-1](../../../../assets/images/oraclerac/oracle-rac-infta-setup-10-1.png){:class="imgCenter"}
![infra-setup-10-2](../../../../assets/images/oraclerac/oracle-rac-infta-setup-10-2.png){:class="imgCenter"}

- 이름 : 4C-16GB-100GB-WB-HA
- 설명 : 4C-16GB-100GB-WB-HA
- CPU 코어 : 4
- CPU(MHz) : 2000
- 메모리 (MB) : 16384
- Write-cache 유형 : Write-back 디스크 캐싱 선택
- 루트 디스크 크기(GB) : 100
- 스토리지 태그 : ps 선택
- 확인 버튼을 클릭하여 컴퓨트 오퍼링 생성

![infra-setup-11](../../../../assets/images/oraclerac/oracle-rac-infta-setup-11.png){:class="imgCenter"}

- 4C-16GB-100GB-WB-HA 디스크 오퍼링이 정상적으로 생성되었는지 확인

## 템플릿용 가상머신 생성
ABLESTACK Mold 화면에서 **컴퓨트 > 가상머신** 화면에서 **가상머신 추가 버튼**을 클릭하여 가상머신 생성 화면으로 이동합니다.

![infra-setup-12-1](../../../../assets/images/oraclerac/oracle-rac-infta-setup-12-1.png){:class="imgCenter"}

- Zone : zone 입력
- 템플릿/ISO : ISO 탭에 OracleLinux-R7-U9-Server-x86_64-dvd.iso 선택

![infra-setup-12-2](../../../../assets/images/oraclerac/oracle-rac-infta-setup-12-2.png){:class="imgCenter"}

- 컴퓨트 오퍼링 : 4C-16GB-100GB-WB-HA 선택
- 디스크 크기 : 100GB-WB 선택
- 네트워크 : rac-private-net 선택

![infra-setup-12-3](../../../../assets/images/oraclerac/oracle-rac-infta-setup-12-3.png){:class="imgCenter"}

- 기본 네트워크 : rac-private-net 선택

![infra-setup-12-4](../../../../assets/images/oraclerac/oracle-rac-infta-setup-12-4.png){:class="imgCenter"}

![infra-setup-12-5](../../../../assets/images/oraclerac/oracle-rac-infta-setup-12-5.png){:class="imgCenter"}

- 이름(옵션) : template-vm
- VM 시작 버튼을 클릭하여 템플릿용 가상 머신 생성

![infra-setup-13](../../../../assets/images/oraclerac/oracle-rac-infta-setup-13.png){:class="imgCenter"}

- 가상머신 목록에 template-vm 상태가 실행 중으로 뜨는지 확인
- 콘솔보기 클릭하여 템플릿용 가상머신 콘솔 화면으로 이동하여 OS 설치를 진행

## 템플릿용 가상머신 OS 설치
생성한 템플릿용 가상머신에 접속하여 운영체제 설치를 진행합니다. ABLESTACK Mold 화면에서 **컴퓨트 > 가상머신** 화면에서 **콘솔보기 버튼**을 클릭하여 가상머신 콘솔 화면으로 이동합니다.

![infra-setup-14](../../../../assets/images/oraclerac/oracle-rac-infta-setup-14.png){:class="imgCenter"}

- Install Oracle Linux 7.9 선택

![infra-setup-15](../../../../assets/images/oraclerac/oracle-rac-infta-setup-15.png){:class="imgCenter"}

- English (United States) 선택 후 Continue 버튼 클릭

![infra-setup-16](../../../../assets/images/oraclerac/oracle-rac-infta-setup-16.png){:class="imgCenter"}

- INSTALLATION SUMMARY > DATA & TIME 클릭

![infra-setup-17](../../../../assets/images/oraclerac/oracle-rac-infta-setup-17.png){:class="imgCenter"}

- Region : Asia 선택
- City : Seoul 선택
- Done 버튼을 클릭하여 적용

![infra-setup-18](../../../../assets/images/oraclerac/oracle-rac-infta-setup-18.png){:class="imgCenter"}

- INSTALLATION SUMMARY > SOFTWARE SELECTION 클릭
- Server with GUI 선택
- Done 버튼을 클릭하여 적용

![infra-setup-19](../../../../assets/images/oraclerac/oracle-rac-infta-setup-19.png){:class="imgCenter"}

- INSTALLATION SUMMARY > INSTALLATION DESTINATION 클릭
- Local Standard Disk에 OS 설치할 디스크 선택
- Other Storage Options에 I wall configure partitioning 선택
- Done 버튼을 클릭하여 다음으로 진행

![infra-setup-20](../../../../assets/images/oraclerac/oracle-rac-infta-setup-20.png){:class="imgCenter"}

- Click here to create them automatically 클릭

![infra-setup-21](../../../../assets/images/oraclerac/oracle-rac-infta-setup-21.png){:class="imgCenter"}

- swap 16GiB 할당 
- 나머지 용량을 / 에 할당
- Done 버튼을 클릭

![infra-setup-22](../../../../assets/images/oraclerac/oracle-rac-infta-setup-22.png){:class="imgCenter"}

- Accept Changes 버튼을 클릭하여 파티션 적용

![infra-setup-23](../../../../assets/images/oraclerac/oracle-rac-infta-setup-23.png){:class="imgCenter"}

- Begin Installation 버튼을 클릭하여 설치 진행

![infra-setup-24](../../../../assets/images/oraclerac/oracle-rac-infta-setup-24.png){:class="imgCenter"}

- Root Password에 사용할 암호 입력
- Confirm에 비밀번호 재입력
- Done 버튼을 클릭하여 Root 계정 비밀번호 설정

![infra-setup-25](../../../../assets/images/oraclerac/oracle-rac-infta-setup-25.png){:class="imgCenter"}

- Reboot 화면이 뜨면 설치 완료

## Oracle RAC 가상머신 템플릿 생성
ABLESTACK Mold 화면에서 **컴퓨트 > 가상머신** 목록 화면으로 이동합니다.

![infra-setup-26](../../../../assets/images/oraclerac/oracle-rac-infta-setup-26.png){:class="imgCenter"}

- template-vm 선택 후 가상머신 정지 버튼 클릭
- 확인 버튼을 클릭하여 가상머신 정지

![infra-setup-27](../../../../assets/images/oraclerac/oracle-rac-infta-setup-27.png){:class="imgCenter"}

- 가상머신 목록에서 template-vm 클릭하여 상세조회 화면으로 이동
- 볼륨 탭 선택
- 유형이 ROOT인 볼륨을 선택하여 볼륨 상세조회 화면으로 이동


![infra-setup-28](../../../../assets/images/oraclerac/oracle-rac-infta-setup-28.png){:class="imgCenter"}

- 볼륨으로 템플릿 생성 버튼 클릭
- 이름 : OracleLinux-R7-U9-Server-x86_64
- 설명 : OracleLinux-R7-U9-Server-x86_64
- OS 유형 : Oracle Linux7
- 공개 : 선택
- 추천 : 선택
- 동적으로 확장 가능 : 선택
- 확인 버튼 클릭하여 템플릿 생성

![infra-setup-29](../../../../assets/images/oraclerac/oracle-rac-infta-setup-29.png){:class="imgCenter"}

- 이미지 > 템플릿 목록 화면에 OracleLinux-R7-U9-Server-x86_64의 상태가 Ready인지 확인
- 정상적으로 템플릿 등록 완료

## RAC 가상머신 생성
Oracle RAC 가상머신 템플릿을 이용해 RAC Node 가상머신을 생성하는 것을 권장합니다. 위 Oracle RAC 가상머신 템플릿 생성 절차에 템플릿을 등록 후 가상머신을 생성해야합니다.

!!! note "Oracle RAC 구성에 필요한 노드 개수"
    2대 이상의 노드가 필요하며, 해당 가이드에서는 2대로 구성합니다.

가상머신을 추가하기 위해 **컴퓨트 > 가상머신** 화면으로 이동하여 **가상머신 추가** 버튼을 클릭합니다. "새 가상머신" 마법사 페이지가 표시됩니다. 해당 페이지에서는 "템플릿을 이용한 VM 생성" 문서를 참고하여 가상머신을 생성합니다.

!!! info "템플릿을 이용한 VM 생성"
    템플릿을 이용한 가상머신 추가를 위해 [템플릿을 이용한 VM 생성](../../../vms/    windows-guide-add-and-use-vm#vm) 문서를 참고하십시오.

- RAC node1 가상머신

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **OracleLinux-R7-U9-Server-x86_64**
    - 컴퓨트 오퍼링 : **4C-16GB-100GB-WB-HA**
    - 네트워크1 : **rac-public-net**
        - IP: 192.168.0.110
    - 네트워크2 : **rac-private-net**
        - IP: 10.1.1.110
    - 이름 : **ol7rac1**

- RAC node2 가상머신

    - 배포 인프라 선택 : **Zone**
    - 템플릿/ISO : **OracleLinux-R7-U9-Server-x86_64**
    - 컴퓨트 오퍼링 : **4C-16GB-100GB-WB-HA**
    - 네트워크1 : **rac-public-net**
        - IP: 192.168.0.120
    - 네트워크2 : **rac-private-net**
        - IP: 10.1.1.120
    - 이름 : **ol7rac2**


![infra-setup-30](../../../../assets/images/oraclerac/oracle-rac-infta-setup-30.png){:class="imgCenter"}

- 컴퓨트 > 가상머신 목록 화면에서 ol7rac1, ol7rac2 가상머신의 상태가 실행중 인지 확인
- 정상적으로 생성되었다면 데이터베이스 데이터 디스크로 사용할 볼륨을 생성하여 공유작업 진행

## Oracle RAC 가상머신 노드 공유디스크 생성 및 연결
ABLESTACK Mold 화면에서 **스토리지 > 볼륨** 화면에서 **볼륨 생성 버튼**을 클릭하여 볼륨 생성 화면으로 이동합니다.

![infra-setup-31](../../../../assets/images/oraclerac/oracle-rac-infta-setup-31.png){:class="imgCenter"}

- 이름 : DATA-DISK
- Zone : zone
- 디스크 오퍼링 : 100GB-shareable
- 확인 버튼을 클릭하여 ol7rac1 가상머신이 사용할 볼륨 생성

![infra-setup-32](../../../../assets/images/oraclerac/oracle-rac-infta-setup-32.png){:class="imgCenter"}

- 이름 : DATA-DISK2
- Zone : zone
- 디스크 오퍼링 : 100GB-shareable
- 확인 버튼을 클릭하여 ol7rac2 가상머신이 사용할 볼륨 생성

![infra-setup-33](../../../../assets/images/oraclerac/oracle-rac-infta-setup-33.png){:class="imgCenter"}

- 볼륨 목록에서 DATA-DISK 디스크 연결 버튼 클릭
- VM ID : ol7rac1
- 확인 버튼을 클릭하여 해당 디스크를 ol7rac1에 연결 (데이터 경로는 가상머신에 연결할 됨 생성됨)

![infra-setup-34](../../../../assets/images/oraclerac/oracle-rac-infta-setup-34.png){:class="imgCenter"}

- 스토리지 > 볼륨 목록에서 공유할 DATA-DISK를 클릭하여 상세화면으로 이동
- 경로 항목에 생성된 볼륨을 (ce6c7e06-24ef-437a-b45a-6ce01b88c28e) 확인 및 복사

![infra-setup-35](../../../../assets/images/oraclerac/oracle-rac-infta-setup-35.png){:class="imgCenter"}

- ol7rac2 노드에 연결할 공유 디스크 DATA-DISK2 편집 버튼 클릭
- 경로를 활성화 후 DATA-DISK1에서 생성한 디스크 경로 ce6c7e06-24ef-437a-b45a-6ce01b88c28e를 DATA-DISK2의 경로에 동일하게 입력
- 확인 버튼을 클릭하여 DATA-DISK1과 디스크를 공유하는 DATA-DISK2 생성 완료

![infra-setup-36](../../../../assets/images/oraclerac/oracle-rac-infta-setup-36.png){:class="imgCenter"}

- 볼륨 목록에서 DATA-DISK2 디스크 연결 버튼 클릭
- VM ID : ol7rac2
- 확인 버튼을 클릭하여 해당 디스크를 ol7rac2에 연결

![infra-setup-37](../../../../assets/images/oraclerac/oracle-rac-infta-setup-37.png){:class="imgCenter"}

- 볼륨 목록에서 DATA-DISK, DATA-DISK2의 상태 및 VM이 정상적으로 연결되었는지 확인

!!! note "가상 인프라 구성 완료"
    RAC 구성하기 위한 가상 인프라 작업이 완료 되었으며, 다음 작업으로 ASM 공유스토리지 생성 및 Grid Infrastructure 구성 작업을 진행합니다.