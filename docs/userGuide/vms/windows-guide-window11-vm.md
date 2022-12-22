## Windows 11 가상머신 생성

![Windows 11 가상머신 생성](../../assets/images/windows11-guide-vm1.png){ align=center }  

1. **배포 인프라 선택** : Mold 에서 구성된 **Zone** 을 선택 합니다.  

    !!! info
        - Pod, 클러스터, 호스트는 옵션 입력창 입니다. 별도의 값을 입력 하지 않아도 가상머신 생성하는데 문제가 되지 않습니다.
        - 특정 Pod, 클러스터, 호스트를 선택 하지 않을 경우 임의의 Pod, 클러스터, 호스트에 가상머신이 생성됩니다.

2. **템플릿/ISO** : ISO 탭 선택 후 마스터 템플릿으로 설치할 ISO 를 선택 하고, Zone 에서 구성된 **하이퍼바이저** 를 선택 합니다.

    ![windows11-guide-vm2](../../assets/images/windows11-guide-vm2.png){ align=center }

3. **컴퓨트 오퍼링** : 가상머신의 오퍼링을 선택 합니다.  

    !!! info
        - 현재 선택한 가상머신의 오퍼링은 Works 에서 생성되는 데스크탑 가상머신의 오퍼링과 연관이 없습니다.
        - Windows 관련하여 최소한의 CPU 와 Memory 만 할당 후에 생성해도 상관없습니다.

4. **디스크 크기** : 가상머신에 할당할 디스크 크기를 선택 합니다. windows11에 사용할 수 있는 디스크 오퍼링 크기는 **100GB** 이상만 생성이 가능합니다. 


    ![windows11-guide-vm3](../../assets/images/windows11-guide-vm3.png){ align=center }

5. **네트워크** : 가상머신을 생성할 네트워크를 선택 합니다.  

6. **SSH 키 쌍** : Windows 와는 상관없는 옵션으로 **설정 안함** 을 선택 합니다.  

    ![windows11-guide-vm4](../../assets/images/windows11-guide-vm4.png){ align=center }

7. **확장 모드** :  확장 모드 설정에서 부팅 유형을 **UEFI 유형** 으로 설정해주시고, 부팅 모드는 **SECURE 모드** , **TPM 설정을 2.0** 으로 맞추고 생성합니다.

    ![windows11-guide-vm5](../../assets/images/windows11-guide-vm5.png){ align=center }

8. **상세** : 이름, 그룹, 키보드 언어의 입력값을 입력하고, 가상머신 시작 라디오 버튼을 확인합니다.  

    !!! info
        - **이름** : 이름은 옵션입니다. 입력 값이 없는경우 Mold 에서 임이의 이름 으로 생성이 됩니다.
        - **그룹** : 그룹은 옵셥입니다. 가상머신 그룹에서 생성된 그룹명을 입력합니다. 
        - **키보드 언어** : 키보드 언어는 옵션입니다. 키보드 언어를 변경할 경우 값을 입력합니다.
        - **가상머신 시작** : 가상머신 시작을 선택하고 가상머신을 생성하면 생성과 동시가 가상머신이 시작됩니다.

9. **VM 시작** : 가상머신 생성과 관련된 선택 값 및 입력 값을 확인 후에 **VM 시작** 버튼을 클릭 합니다.  

## Windows 11 OS 설치 (1/2)

1. Mold 에서 생성된 Master Template 용 가상머신 상세 정보화면에서 **콘솔 보기** 버튼을 클릭하여, 해당 가상머신의 콘솔 화면으로 이동합니다.

    ![windows11-guide-vm6](../../assets/images/windows11-guide-vm6.png){ align=center }

    ![windows11-guide-vm7](../../assets/images/windows11-guide-vm7.png){ align=center }

    ![windows11-guide-vm8](../../assets/images/windows11-guide-vm8.png){ align=center }

    ![windows11-guide-vm9](../../assets/images/windows11-guide-vm9.png){ align=center }

    ![windows11-guide-vm10](../../assets/images/windows11-guide-vm10.png){ align=center }

    1. **설치할 언어** : Windows 11 OS 설치 언어를 선택 합니다.
    2. **시간 및 통화 형식** : Windows 11 OS 시간 설정 및 통화 형식을 선택 합니다.
    3. **키보드 또는 입력 방법** : Windows 11 OS 키보드 또는 입력 방법을 선택 합니다.
    4. **키보드 종류** : Windows 11 OS 키보드 종류를 선택 합니다.
    5. 선택 사항을 확인 후에 **다음** 버튼을 클릭 합니다.
    !!! info
        OS 설정 사항을 잘못 선택 할 경우 OS 설치가 완료 후에 변경 가능하나 초기 선택을 신중하게 선택하셔야 합니다.

2. Windows 11 설치 진행

    ![windows11-guide-vm11](../../assets/images/windows11-guide-vm11.png){ align=center }

    1. **지금 설치** 버튼을 클릭 하여 Windows 11 OS 설치를 진행 합니다.
   
    ![windows11-guide-vm12](../../assets/images/windows11-guide-vm12.png){ align=center }


3. Windows 11 관련 통지 및 사용 조건

    ![windows11-guide-vm13](../../assets/images/windows11-guide-vm13.png){ align=center }

    1. MICROSOFT 소프트웨어 사용권 계약서 내용 확인후 **동의함** 선택을 체크 한 후에 **다음** 버튼을 클릭 합니다.

4. Windows 11 설치 유형

    ![windows11-guide-vm14](../../assets/images/windows11-guide-vm14.png){ align=center }

    Windows 11 설치 유형을 선택 하는 화면 입니다.
    **사용자 지정: Windows만 설치(고급)** 을 선택 하여 다음 화면으로 이동합니다.

5. Windows 를 설치할 위치를 지정하세요.

    ![windows11-guide-vm15](../../assets/images/windows11-guide-vm15.png){ align=center }

    !!! info
        ABLECLOUD 의 Mold 에서 Windows 계열의 OS 를 설치할 경우 디스크 정보가 정상적으로 보이지 않습니다.  
        그 이유는 디스크와 관련된 Agent 가 정상적으로 설치가 안되여서 디스크 정보를 정상적으로 읽을 수 없는 상황입니다.
        디스크 Agent 소프트웨어를 설치하면 정상적으로 디스크 정보를 확인 할 수 있으며, Windows OS 를 정상적으로 설치 진행이 가능합니다.

## VirtIOStor 설치 진행
!!! info
    Virt IO Stor 설치 진행에 대하여 설명하는 부분 입니다. Windows OS 종류와 상관없이 동일한 절차로 진행이 되며, OS 버전 선택 부분을 제외한 나머지 부분은 동일합니다.
    현재 부분에서는 디스크와 관련된 Agent 만 설치 진행되며 디바이스 관련 Agent 는 OS 설치 완료 후 진행 됩니다.
    **virtio-win-0.1.221.iso** 버전을 사용해야합니다.

1. Windows 설치용 ISO 연결 해제

    ![windows11-guide-vm16](../../assets/images/windows11-guide-vm16.png){ align=center }

    1. Windows 11 설치 중인 가상머신에서 **ISO 분리** 버튼을 클릭합니다.
    2. ISO 분리 확인 창에서 **확인** 버튼을 클릭하여 ISO 를 분리 합니다.
   
2. VirtIO-win ISO 연결
    ![windows11-guide-vm17](../../assets/images/windows11-guide-vm17.png){ align=center }
    ![windows11-guide-vm18](../../assets/images/windows11-guide-vm18.png){ align=center }
     
    1. Windows 11 설치 중인 가상머신에서 **ISO 연결** 버튼을 클릭합니다.
    
    2. 선택 박스에서 **virtio-win-0.1.221** ISO 선택 하고 **확인** 버튼을 클릭 합니다.
   
    !!! info
        virt-io 설치용 ISO 명은 상황에 따라 다를수가 있습니다. 위에 명시된 이름은 참고용 입니다.

    ![windows11-guide-vm19](../../assets/images/windows11-guide-vm19.png){ align=center }
    3. **드라이버 로드** 버튼을 클릭 합니다.
       
    ![windows11-guide-vm20](../../assets/images/windows11-guide-vm20.png){ align=center }
    4. **찾아보기** 버튼을 클릭 합니다.
   
    ![windows11-guide-vm21](../../assets/images/windows11-guide-vm21.png){ align=center }
    5. **CD 드라이브 (D:): virtio-win-0.1.221** 을 선택 합니다.

    ![windows11-guide-vm22](../../assets/images/windows11-guide-vm22.png){ align=center }
    6. **viostor > w11 > amd64** 위치로 이동한 후 **확인** 버튼을 클릭 합니다.

    !!! info
        폴더별 설명  
        - **viostor** : 디스크와 관련된 Agent 설치 폴더 입니다.  
        - **w11** : Windows OS 버전별로 나누어져 있는 폴더 입니다. 설치 OS 버전에 맞는 폴더를 선택 하시면 됩니다.  
        - **amd64** : CPU 타입별로 나누어져 있는 폴더 입니다. 설치중인 서버의 CPU 타입에 맞는 폴더를 선택 하시면 됩니다.  

    ![windows11-guide-vm23](../../assets/images/windows11-guide-vm23.png){ align=center }


    7. **Red Hat VirtIO SCSI controller** 를 선택 한 후에 **다음** 버튼을 클릭 합니다.

    8. VirtIOStor 설치가 마무리 되면 **virtio-win-0.1.221** ISO 를 분리하고 Windows 설치 ISO 를 다시 연결 한 후 Windows 11 OS 설치를 이어서 진행 합니다.

## Windows 11 OS 설치 (2/2)

1. Windows 를 설치할 위치를 지정하세요.

    ![windows11-guide-vm24](../../assets/images/windows11-guide-vm24.png){ align=center }
    1. **드라이버 로드** 가 됐는지 확인해줍니다.

    ![windows11-guide-vm25](../../assets/images/windows11-guide-vm25.png){ align=center }
    2. ISO를 분리해줍니다.

    ![windows11-guide-vm26](../../assets/images/windows11-guide-vm26.png){ align=center }

    ![windows11-guide-vm27](../../assets/images/windows11-guide-vm27.png){ align=center }
    3. **Windows 11.ISO** 를 연결해 줍니다.

    ![windows11-guide-vm28](../../assets/images/windows11-guide-vm28.png){ align=center }
    4. **새로고침** 버튼을 눌러줍니다.

    ![windows11-guide-vm29](../../assets/images/windows11-guide-vm29.png){ align=center }
    
    ![windows11-guide-vm30](../../assets/images/windows11-guide-vm30.png){ align=center }
    5. Windows OS 설치 마무리 후 재부팅을 진행 합니다.  

## Windows 11 OS 설치 후 설정

Windows 11 OS 설치 완료 설정 Windows 설정 진행 절차 입니다.  

![windows11-guide-vm31](../../assets/images/windows11-guide-vm31.png){ align=center }
1. **한국** 을 선택 후 **예** 버튼을 클릭 합니다.

![windows11-guide-vm32](../../assets/images/windows11-guide-vm32.png){ align=center }
2. **자판배열** 확인 후 **예** 버튼을 클릭 합니다.

![windows11-guide-vm33](../../assets/images/windows11-guide-vm33.png){ align=center }
3. **건너뛰기** 버튼을 클릭 합니다.

![windows11-guide-vm34](../../assets/images/windows11-guide-vm34.png){ align=center }
4. **제한된 설치로 계속** 버튼을 클릭 합니다.

![windows11-guide-vm35](../../assets/images/windows11-guide-vm35.png){ align=center }
5. **PC 이름** 을 입력 합니다.

!!! info
    Works 에서 데스크탑 가상머신 생성시 PC 이름은 재설정 됩니다.

![windows11-guide-vm36](../../assets/images/windows11-guide-vm36.png){ align=center }
6. **비밀번호** 를 설정한 후에 **다음** 버튼을 클릭 합니다.

![windows11-guide-vm37](../../assets/images/windows11-guide-vm37.png){ align=center }
7. **비밀번호** 를 한번더 입력 후 **다음** 버튼을 클릭 합니다.

![windows11-guide-vm38](../../assets/images/windows11-guide-vm38.png){ align=center }
8. **보안 질문 작성** 3단계를 진행 합니다.

![windows11-guide-vm39](../../assets/images/windows11-guide-vm39.png){ align=center }
![windows11-guide-vm40](../../assets/images/windows11-guide-vm40.png){ align=center }
![windows11-guide-vm41](../../assets/images/windows11-guide-vm41.png){ align=center }
![windows11-guide-vm42](../../assets/images/windows11-guide-vm42.png){ align=center }
![windows11-guide-vm43](../../assets/images/windows11-guide-vm43.png){ align=center }
![windows11-guide-vm44](../../assets/images/windows11-guide-vm44.png){ align=center }
9. **기타 설정** 진행을 진행 합니다.

![windows11-guide-vm45](../../assets/images/windows11-guide-vm45.png){ align=center }
![windows11-guide-vm46](../../assets/images/windows11-guide-vm46.png){ align=center }
![windows11-guide-vm47](../../assets/images/windows11-guide-vm47.png){ align=center }
10. **Windows 11 설정** 완료.

## Windows 10 디바이스 설정을 위한 Agent 설치

Windows 11 OS 설치 완료 후 디바이스의 설정을 위해 Agent 설치를 진행합니다.

![windows11-guide-vm48](../../assets/images/windows11-guide-vm48.png){ align=center }

![windows11-guide-vm49](../../assets/images/windows11-guide-vm49.png){ align=center }
1. Windows 11 설치 ISO 분리 후 **virtio-win-0.1.221** ISO 연결

![windows11-guide-vm50](../../assets/images/windows11-guide-vm50.png){ align=center }
![windows11-guide-vm51](../../assets/images/windows11-guide-vm51.png){ align=center }
![windows11-guide-vm52](../../assets/images/windows11-guide-vm52.png){ align=center }
2. **D:** 드라이브 폴더로 이동 후 **virtio-win-guest-tools** 실행 파일을 실행 합니다.

![windows11-guide-vm53](../../assets/images/windows11-guide-vm53.png){ align=center }
3. **Install** 버튼을 클릭 합니다.

![windows11-guide-vm54](../../assets/images/windows11-guide-vm54.png){ align=center }
![windows11-guide-vm55](../../assets/images/windows11-guide-vm55.png){ align=center }
4. **Next** 버튼을 클릭한 뒤 Virtio-win-driver-installer 라이센스 정보 확인 후 **I accept the terms in the License Agreement** 체크 후 **Next** 버튼을 클릭 합니다.

![windows11-guide-vm56](../../assets/images/windows11-guide-vm56.png){ align=center }
5. 설치 리스트를 확인 후에 **Next** 버튼을 클릭 합니다.

![windows11-guide-vm57](../../assets/images/windows11-guide-vm57.png){ align=center }
![windows11-guide-vm58](../../assets/images/windows11-guide-vm58.png){ align=center }
![windows11-guide-vm59](../../assets/images/windows11-guide-vm59.png){ align=center }
![windows11-guide-vm60](../../assets/images/windows11-guide-vm60.png){ align=center }
6. **Install** 버튼을 클릭하여 설치 합니다.

![windows11-guide-vm61](../../assets/images/windows11-guide-vm61.png){ align=center }
![windows11-guide-vm62](../../assets/images/windows11-guide-vm62.png){ align=center }
7. **Virtio 설치** 완료 및 **제어판 > 하드웨어 및 소리 > 장치관리자** 에서 설치 결과를 확인 합니다.