# 가상머신 관리
Mold는 클라우드에서 실행되는 모든 가상머신(VM)의 생명주기(lifecycle) 완벽하게 관리할 수 있는 권한을 제공합니다. Mold는 최종 사용자와 관리자를 위한 여러 관리 작업을 제공합니다. VM은 중지, 시작, 재부팅 및 삭제될 수 있습니다.

사용자 VM에는 이름과 그룹이 있습니다. 각 VM은 서로 다른 컨텍스트에서 사용할 수 있도록 다음의 세 가지 이름을 가질 수 있으며 다음 이름 중 내부명을 제외한 두 개만 사용자가 제어할 수 있습니다.

- 인스턴스 이름(ID) – Mold에서 생성하고 사용자가 수정할 수 없는 고유하고 변경할 수 없는 ID입니다. 이 이름은 IETF RFC 1123의 요구 사항을 따릅니다.
- 표시명(Display Name) – Mold 웹 UI에 표시되는 이름입니다. 사용자가 설정할 수 있습니다. 기본값은 인스턴스 이름입니다.
- 이름(Name) – DHCP 서버가 VM에 할당하는 호스트 이름입니다. 사용자가 설정할 수 있습니다. 기본값은 인스턴스 이름입니다.

!!! note
    사용자 VM의 표시 이름을 내부 이름에 추가할 수 있습니다. 자세한 내용은 "사용자 VM의 내부 이름에 표시 이름 추가"를 참조하십시오

사용자 VM은 고가용성(HA)으로 구성할 수 있습니다. HA가 활성화된 VM은 시스템에서 모니터링됩니다. 시스템이 VM이 다운되었음을 감지하면 다른 호스트에서 VM을 다시 시작하려고 시도합니다. 자세한 내용은 [HA 지원 가상머신](ha-mngt-guide.md)를  참조하십시오.

는 사용자가 종료한 사용자 VM (예 : Linux의 "shutdown"명령 사용)과 예기치 않게 종료된 VM을 구별할 수 없습니다. HA가 활성화된 VM이 VM 내부에서 종료되면 Mold를 다시 시작합니다. HA이 활성화된 VM을 종료하려면 Mold에서 종료하거나 HA를 비활성화 시켜야 합니다.

!!! info
    Mold 관리자는 각 클러스터의 총 VM 인스턴스 수를 모니터링하고 총계가 하이퍼바이저가 처리할 수 있는 최대 값에 가까워지면 클러스터에 대한 할당을 제한하거나 재구성해야 합니다. 하나 이상의 호스트가 장애가 발생할 가능성을 고려하여 여유를 두어야 합니다. 이 경우 VM이 자동으로 재배치되므로 다른 호스트에서 VM로드가 증가합니다. 선택한 하이퍼바이저의 설명서를 참조하여 호스트당 허용되는 최대 VM 수를 찾은 다음 자원할당을 기본 제한으로 설정합니다. 클러스터의 VM 활동을 모니터링하여 호스트 장애를 허용하는 안전한 수준 이하로 총 VM 수를 유지합니다. 예를 들어 클러스터에 N 개의 호스트가 있고 클러스터에 의한 호스트가 주어진 시간에 다운되도록 허용하려는 경우 클러스터에서 허용할 수 있는 총 VM 인스턴스 수는 최대 (N-1 ) * (호스트당 제한). 클러스터가 이 VM 수에 도달하면 자원증설 혹은 재배치를 고려해야 합니다.

## VM lifecycle 관리
사용자 VM은 다음과 같은 작업이 완료된 혹은 작업중인 상태가 표시됩니다. 

- 작업이 완료된 상태
    - Created : 생성완료
    - Running : 실행 중
    - Stopped : 정지된 상태
    - Destroyed : 삭제
    - Expunged : 소거
- 작업중인 상태
    - Creating : 생성 중
    - Starting : 시작 중
    - Stopping : 정지 중
    - Destoring : 삭제 중
    - Expunging : 소거 중

<H3>VM 생성</H3>
가상머신은 일반적으로 템플릿에서 생성됩니다. 사용자는 빈 가상머신을 생성할 수도 있습니다. 빈 가상머신은 OS 템플릿이 없는 가상머신입니다. 사용자는 ISO 파일을 첨부하고 OS를 설치할 수 있습니다.
!!! note
    VM을 시작하지 않고도 만들 수 있습니다. VM 배포의 일부로 VM을 시작해야 하는지 여부를 결정할 수 있습니다. deployVm API의 요청 매개 변수인 startVM이 이 기능을 제공합니다. 자세한 내용은 개발자 안내서를 참조하십시오.

템플릿에서 VM을 만들려면 :

1. 관리자 또는 사용자로 Mold UI에 로그인하십시오.
2. 왼쪽 탐색 모음에서 컴퓨트를 클릭합니다.
3. 가상머신을 선택 클릭합니다.
4. 가상머신 추가를 클릭합니다.
5. Zone을 선택하십시오. 관리자는 Pod, 클러스터 또는 호스트를 선택할 수 있는 옵션이 있습니다.
6. 템플릿을 선택한 다음 마법사의 단계를 따릅니다. 템플릿이 이 목록에 포함된 방법에 대한 자세한 내용은 템플릿 작업을 참조하십시오.
7. 보유한 하드웨어가 선택한 서비스 제공을 시작할 수 있는지 확인하십시오.
!!! note
    VMware 전용 : 선택한 템플릿에 OVF 속성, 다른 배포 옵션 또는 구성, 여러 NIC 또는 최종 사용자 라이센스 계약이 포함된 경우 마법사에 이러한 속성이 표시됩니다. "가상 어플라이언스 지원"을 참조하십시오.
8. VM 시작 클릭하면 VM이 생성되고 시작됩니다.
!!! note
    보안상의 이유로 VM의 내부 이름은 루트 관리자에게만 표시됩니다.

ISO에서 VM을 만들려면 :
!!! note
    XenServer
    XenServer에서 실행되는 Windows VM에는 템플릿에 제공되거나 VM이 생성된 후 추가될 수 있는 PV 드라이버가 필요합니다. PV 드라이버는 추가 볼륨 및 ISO 이미지 마운트, 라이브 마이그레이션 및 정상 종료와 같은 필수 관리 기능에 필요합니다.

1. 관리자 또는 사용자로 Mold UI에 로그인하십시오.
2. 왼쪽 탐색 모음에서 컴퓨트를 클릭합니다.
3. 가상머신을 선택 클릭합니다.
5. 가상머신 추가를 클릭합니다.
6. Zone을 선택하십시오. 관리자는 Pod, 클러스터 또는 호스트를 선택할 수 있는 옵션이 있습니다.
7. ISO 부팅을 선택하고 마법사의 단계를 따릅니다.
8. VM 시작 클릭하면 VM이 생성되고 시작됩니다.

<H4>필요한 도구 및 드라이버 설치</H4>
각 VM에 다음이 설치되어 있는지 확인하십시오.

* XenServer의 경우 각 VM에 PV 드라이버와 Xen 도구를 설치합니다. 이렇게 하면 실시간 마이그레이션과 게스트를 완전히 종료할 수 있습니다. 동적 CPU 및 RAM 확장이 작동하려면 Xen 도구가 필요합니다.
* vSphere의 경우 각 VM에 VMware Tools를 설치합니다. 이렇게 하면 콘솔보기가 제대로 작동합니다. 동적 CPU 및 RAM 확장이 작동하려면 VMware Tools가 필요합니다.

Xen 도구 또는 VMware Tools가 설치되어 있는지 확인하려면 다음 기술 중 하나를 사용하십시오.

* 이미 도구가 설치된 템플릿에서 각 VM을 만듭니다. 또는,
* 새 템플릿을 등록할 때 관리자 또는 사용자는 템플릿에 도구가 설치되어 있는지 여부를 나타낼 수 있습니다. 이 작업은 UI 또는 updateTemplate API를 사용하여 수행할 수 있습니다. 또는,
* 사용자가 Xen 도구 또는 VMware Tools가 없는 템플릿을 사용하여 가상머신을 배포하고 나중에 VM에 도구를 설치하는 경우 사용자는 updateVirtualMachine API를 사용하여 Mold에 알릴 수 있습니다. 도구를 설치하고 가상머신을 업데이트한 후 VM을 중지하고 시작합니다.


<H3>VM 접속</H3>
모든 사용자는 자신의 가상머신에 액세스할 수 있습니다. 관리자는 클라우드에서 실행되는 모든 VM에 액세스할 수 있습니다.

Mold UI를 통해 VM에 액세스하려면 :

1. 사용자 또는 관리자로 Mold UI에 로그인합니다.
2. 왼쪽 탐색 모음에서 컴퓨트를 클릭합니다.
3. 가상머신을 선택 클릭합니다.
4. 실행 중인 가상머신의 이름을 클릭합니다.
5. 콘솔보기 버튼을 클릭합니다.

네트워크를 통해 직접 VM에 액세스하려면 :

1. VM에는 들어오는 트래픽에 대해 일부 포트가 열려 있어야 합니다. 예를 들어 기본 zone에서 들어오는 트래픽을 허용하는 보안 그룹에 새 VM을 할당할 수 있습니다. 이는 VM을 만들 때 선택한 보안 그룹에 따라 다릅니다. 다른 경우에는 포트 전달 정책을 설정하여 포트를 열 수 있습니다. “IP 전달 및 방화벽"을 참조하십시오.
2. 포트가 열려 있지만 ssh를 사용하여 VM에 액세스할 수 없는 경우 VM에서 ssh가 아직 활성화되지 않았을 수 있습니다. 이는 VM을 만들 때 선택한 템플릿에서 ssh가 활성화되어 있는지 여부에 따라 다릅니다. Mold UI를 통해 VM에 액세스하고 VM의 운영 체제에 대한 명령을 사용하여 머신에서 ssh를 활성화합니다.
3. 네트워크에 외부 방화벽 장치가 있는 경우 액세스를 허용하는 방화벽 규칙을 만들어야 합니다. “IP 전달 및 방화벽"을 참조하십시오.

<H3>VM 시작/중지</H3>
VM 인스턴스가 생성되면 필요에 따라 중지, 다시 시작 또는 삭제할 수 있습니다. Mold UI에서 컴퓨트 > 가상머신을 클릭하고 VM을 선택한 다음 가상머신 정지, 가상머신 시작, 가상머신 재시작 및 가상머신 파기 버튼을 사용합니다.

중지는 물리적 서버에서 소프트 전원 스위치를 누르는 것과 유사한 ACPI '중지' 명령을 통해 운영체제를 정상적으로 종료하려고 시도합니다. 운영체제를 중지할 수 없는 경우 강제로 종료됩니다. 이것은 물리적 시스템에서 전원 코드를 뽑는 것과 동일한 효과가 있습니다.

재부팅은 중지 후 시작으로 간주되어서는 안 됩니다. Mold에서 시작 명령은 가상머신을 Mold의 데이터베이스에 저장된 매개 변수로 재구성합니다. 재부팅 프로세스는 이를 수행하지 않습니다.

VM을 시작할 때 관리자는 Pod, 클러스터 또는 호스트를 지정할 수 있는 옵션이 있습니다.

<H3>VM 삭제</H3>
사용자는 자신의 가상머신을 삭제할 수 있습니다. 실행 중인 가상머신은 삭제되기 전에 중지됩니다. 관리자는 모든 가상머신을 삭제할 수 있습니다.

가상머신을 삭제하려면 :

1. 사용자 또는 관리자로 Mold UI에 로그인합니다.
2. 왼쪽 탐색 모음에서 컴퓨트를 클릭합니다.
3. 가상머신을 선택 클릭합니다.
4. 인스턴스 파기 버튼을 클릭합니다.
5. 선택적으로 추가된 볼륨의 정리 및 삭제를 모두 활성화할 수 있습니다.

가상머신이 삭제 되면 최종 사용자는 더 이상 볼 수 없지만, 루트 관리자는 볼 수 있고 복구할 수 있습니다. 이 상태에서는 여전히 논리적 리소스를 사용합니다. 전역 설정은 제거되는 VM에서 제거되는 물리적 디스크까지의 최대 시간을 제어합니다. VM과 루트 디스크가 삭제 되면 VM이 영구 삭제되었다고 합니다.

가상머신이 영구 삭제 되면 복구할 수 없습니다. 가상머신에서 사용하는 모든 리소스는 시스템에서 회수됩니다. 여기에는 가상머신의 IP 주소가 포함됩니다.

## VM 관리
<H3>VM 이름, OS 또는 그룹 변경</H3>
VM이 생성된 후 표시 이름, 운영 체제 및 VM이 속한 그룹을 수정할 수 있습니다.

Mold UI를 통해 VM에 액세스하려면 :

1. 사용자 또는 관리자로 Mold UI에 로그인합니다.
2. 왼쪽 탐색에서 가상머신을 클릭합니다.
3. 수정하려는 가상머신을 선택합니다.
4. 가상머신 정지 버튼을 클릭하여 VM을 중지합니다.
5. 가상머신 편집을 클릭하십시오.
6. 다음을 원하는 대로 변경합니다.
7. 이름 : VM의 이름을 변경하려면 새 이름을 입력합니다.
8. 표시 이름 : VM의 이름을 변경하려면 새 표시 이름을 입력합니다.
9. OS 유형 : 원하는 운영 체제를 선택합니다.
10. 동적으로 확장 가능 : VM에 VM CPU/메모리의 동적 확장을 지원하기 위한 XS/VMWare 도구가 포함된 경우 true
11. HA 활성화 됨 : 가상 머신에 고가용성이 활성화된 경우 true, 그렇지 않으면 false
12. 그룹 : VM의 그룹 이름을 입력합니다.
10. 확인을 클릭하십시오.

<H3>게스트 VM의 내부 이름에 표시 이름 추가</H3>
모든 게스트 VM에는 내부 이름이 있습니다. 호스트는 내부 이름을 사용하여 게스트 VM을 식별합니다. Mold는 게스트 VM에 표시 이름을 제공하는 옵션을 제공합니다. vCenter가 게스트 VM을 식별하는 데 사용할 수 있도록 이 표시 이름을 내부 이름으로 설정할 수 있습니다. 이제 이 기능을 수행하기 위해 새 전역 매개 변수 vm.instancename.flag가 추가되었습니다.

내부 이름의 기본 형식은 `i-<user_id>-<vm_id>-<instance.name>` 이며 여기서 instance.name은 전역 매개 변수입니다. 그러나 vm.instancename.flag가 true로 설정되고 게스트 VM을 만드는 동안 표시 이름이 제공되면 표시 이름이 호스트에 있는 게스트 VM의 내부 이름에 추가됩니다. 이것은 내부 이름 형식을 `i-<user_id>-<vm_id>-<displayName>`으로 만듭니다. vm.instancename.flag의 기본값은 false로 설정됩니다. 이 기능은 대규모 데이터 센터 배포에서 인스턴스 이름과 내부 이름 간의 상관 관계를 보다 쉽게 ​​만들기 위한 것 입니다.

다음 표에서는 다양한 시나리오에서 VM 이름이 표시되는 방식을 설명합니다.

|<center>사용자 제공 표시 이름</center>|<center>vm.instancename.flag</center>|<center>VM의 호스트 이름</center>|<center>vCenter의 이름</center>|<center>내부 이름</center>|
|:---|:---|:---|:---|:---|
|Yes|True|Display name|`i-<user_id>-<vm_id>-displayName`|`i-<user_id>-<vm_id>-displayName`|
|No|True|UUID|`i-<user_id>-<vm_id>-<instance.name>`|`i-<user_id>-<vm_id>-<instance.name>`|
|Yes|False|Display name|`i-<user_id>-<vm_id>-<instance.name>`|`i-<user_id>-<vm_id>-<instance.name>|`
|No|False|UUID|`i-<user_id>-<vm_id>-<instance.name>`|`i-<user_id>-<vm_id>-<instance.name>`|

<H3>VM 서비스 오퍼링 변경</H3>
가상 머신에서 사용할 수 있는 컴퓨팅 리소스 수준을 업그레이드하거나 다운 그레이드하려면 VM의 컴퓨팅 제품을 변경할 수 있습니다.

1. 사용자 또는 관리자로 Mold UI에 로그인합니다.
2. 왼쪽 탐색에서 가상머신을 클릭합니다.
3. 작업하려는 가상머신을 선택합니다.
4. (동적 VM 확장을 사용하도록 설정한 경우 이 단계를 건너뜁니다. VM 실행을 위한 CPU 및 메모리 확장을 참조하세요) 가상머신 정지 버튼을 클릭하여 VM을 중지합니다.
5. VM 확장 버튼을 클릭합니다.
6. 서비스 변경 대화 상자가 표시됩니다.
7. 선택한 VM에 변경할 오퍼링을 선택하십시오.
8. 확인을 클릭하십시오.

<H4>실행 중인 가상머신 CPU 및 메모리 확장</H4>
(VMware 및 XenServer에서 지원됨)

VM을 처음 배포할 때 항상 CPU 및 RAM 요구 사항을 정확하게 예측할 수 있는 것은 아닙니다. VM 수명 동안 언제든지 이러한 리소스를 늘려야 할 수 있습니다. CPU 및 RAM 수준을 동적으로 수정하여 가동 중지 시간 없이 실행 중인 VM에 대해 이러한 리소스를 확장할 수 있습니다.

동적 CPU 및 RAM 확장은 다음과 같은 경우에 사용할 수 있습니다.

VMware 및 XenServer를 실행하는 호스트의 사용자 VM.
VMware의 시스템 VM.
가상 머신에 VMware Tools 또는 XenServer Tools를 설치해야 합니다.
새로 요청된 CPU 및 RAM 값은 하이퍼바이저 및 VM 운영 체제에서 허용하는 제약 조건 내에 있어야 합니다.

<H4>기존 VM 업데이트</H4>
Mold 버전을 업그레이드 하고 이전 버전으로 생성된 기존 VM에 동적 확장 기능이 포함되도록 하려면 다음 단계를 사용하여 VM을 업데이트합니다.

zone 수준 설정 enable.dynamic.scale.vm이 true로 설정되어 있는지 확인합니다. Mold UI의 왼쪽 탐색 모음에서 인프라스트럭쳐를 클릭한 다음 Zone을 클릭하고 원하는 Zone을 클릭한 다음 설정 탭을 클릭합니다.
Xen 도구 (XenServer 호스트용) 또는 VMware Tools (VMware 호스트용)가 아직 설치되지 않은 경우 각 VM에 설치합니다.
가상머신을 중지합니다.
가상머신 편집 버튼을 클릭합니다.
동적 확장 가능 확인란을 클릭합니다.
확인을 클릭하십시오.
VM을 다시 시작하십시오.

<H4>동적 CPU 및 RAM 확장 구성</H4>
이 기능을 구성하려면 다음과 같은 새 글로벌 설정 변수를 사용하십시오.

enable.dynamic.scale.vm : 기능을 활성화하려면 True로 설정합니다. 기본적으로 이 기능은 꺼져 있습니다.
scale.retry : 확장 작업을 시도하는 횟수입니다. 기본값은 2입니다.

<H4>CPU 및 RAM을 동적으로 확장하는 방법</H4>
가상 머신의 CPU 또는 RAM 용량을 수정하려면 VM의 컴퓨트 오퍼링을 원하는 CPU 및 RAM 값이 있는 새 컴퓨트 오퍼링으로 변경해야 합니다. 위의 "VM에 대한 서비스 제공 변경" 에서 설명한 것과 동일한 단계를 사용할 수 있지만 가상 머신을 중지하는 단계는 건너뜁니다. 물론 먼저 새 컴퓨트 오퍼링을 만들어야 할 수도 있습니다.

동적 조정 요청을 제출하면 가능한 경우 현재 호스트에서 리소스가 확장됩니다. 호스트에 리소스가 충분하지 않은 경우 VM은 동일한 클러스터의 다른 호스트로 라이브 마이그레이션 됩니다. 요청된 CPU 및 RAM 수준을 충족할 수 있는 호스트가 클러스터에 없으면 확장 작업이 실패합니다. VM은 이전과 같이 계속 실행됩니다.

<H4>한계</H4>
XenServer에서 시스템 VM에 대해 동적 확장을 수행할 수 없습니다.
Mold는 새 CPU 및 RAM 레벨이 VM에서 실행 중인 OS와 호환되는지 확인하지 않습니다.
VMware에서 Linux VM의 메모리 또는 CPU를 확장할 때 위에서 언급한 다른 단계 외에도 스크립트를 실행해야 할 수 있습니다. 자세한 내용은 VMware 기술 자료에서 Linux의 핫 추가 메모리 (1012764)를 참조하십시오.
(VMware) 현재 호스트에서 리소스를 사용할 수 없는 경우 Mold와 vCenter가 사용 가능한 용량을 다르게 계산하는 알려진 문제로 인해 VMware에서 확장이 실패합니다. 자세한 내용은 https://issues.apache.org/jira/browse/CLOUDSTACK-1809를 참조 하십시오.
Linux 64 비트 및 Windows 7 32 비트 운영 체제를 실행하는 VM에서 VM에 처음에 3GB 미만의 RAM이 할당된 경우 최대 3GB까지 동적으로 확장할 수 있지만 그 이상은 아닙니다. 이는 이러한 운영 체제의 알려진 문제로 인해 3GB 미만에서 3GB 이상으로 동적으로 확장하려고 하면 작동이 중지됩니다.


<H3>재부팅 시 가상 머신 루트 볼륨 재설정</H3>
안전한 환경을 위해 그리고 VM 상태가 재부팅 후에도 유지되지 않도록 하려면 루트 디스크를 재설정할 수 있습니다. 자세한 내용은 “재부팅 시 VM을 새 루트 디스크로 재설정"을 참조하십시오.

<H3>다른 호스트로 VM 이전 (수동 라이브 마이그레이션)</H3>
Mold 관리자는 사용자에 대한 서비스를 중단하거나 유지 관리 모드로 전환하지 않고도 실행 중인 VM을 한 호스트에서 다른 호스트로 이동할 수 있습니다. 이를 수동 라이브 마이그레이션이라고하며 다음 조건에서 수행할 수 있습니다.

* 루트 관리자가 로그인되어 있어야 합니다. 도메인 관리자 및 사용자는 VM의 수동 라이브 마이그레이션을 수행할 수 없습니다.
* VM이 실행 중입니다. 중지된 VM은 라이브 마이그레이션 할 수 없습니다.
* 대상 호스트에는 사용 가능한 용량이 충분해야 합니다. 그렇지 않은 경우 VM은 메모리를 사용할 수 있을 때까지 "마이그레이션 중"상태로 유지됩니다.
* (KVM) VM은 로컬 디스크 스토리지를 사용하지 않아야 합니다. (XenServer 및 VMware에서 로컬 디스크를 사용한 VM 라이브 마이그레이션은 XenMotion 및 vMotion에 대한 Mold 지원을 통해 활성화됩니다)
* (KVM) 대상 호스트는 원래 호스트와 동일한 클러스터에 있어야 합니다. (XenServer 및 VMware에서 한 클러스터에서 다른 클러스터로의 VM 라이브 마이그레이션은 XenMotion 및 vMotion에 대한 Mold 지원을 통해 활성화됩니다)

가상 머신을 수동으로 라이브 마이그레이션 하려면

1. 사용자 또는 관리자로 Mold UI에 로그인합니다.
2. 왼쪽 탐색에서 가상머신을 클릭합니다.
3. 마이그레이션 할 가상머신을 선택합니다.
4. 다른 호스트에게 가상머신 마이그레이션 버튼을 클릭합니다.
5. 적합한 호스트 목록에서 VM을 이동할 호스트를 선택합니다.

    !!! note
        VM의 스토리지를 VM과 함께 마이그레이션 해야 하는 경우 호스트 목록에 표시됩니다. Mold가 스토리지 마이그레이션을 처리합니다.

6. 확인을 클릭하십시오.
!!! note
    ```
    (KVM) If the VM's storage has to be migrated along with the VM, from a mounted NFS storage pool to a cluster-wide mounted NFS storage pool, then the 'migrateVirtualMachineWithVolume' API has to be used. There is no UI integration for this feature.

    (CloudMonkey) > migrate virtualmachinewithvolume virtualmachineid=<virtual machine uuid> hostid=<destination host uuid> migrateto[i].volume=<virtual machine volume number i uuid> migrateto[i].pool=<destination storage pool uuid for volume number i>

    where i in [0,..,N] and N = number of volumes of the virtual machine
    ```
<H3>호스트에 VM 할당</H3>
어느 시점에서든 각 가상 머신 인스턴스는 단일 호스트에서 실행됩니다. Mold는 VM을 배치할 호스트를 어떻게 결정합니까? 여러 가지 방법이 있습니다.

* 자동 기본 호스트 할당. Mold는 각 가상 머신을 실행하는 데 가장 적합한 호스트를 자동으로 선택할 수 있습니다.
* 인스턴스 유형 기본 설정. Mold 관리자는 특정 호스트가 특정 유형의 게스트 인스턴스에 대한 기본 설정을 갖도록 지정할 수 있습니다. 예를 들어 관리자는 호스트가 Windows 게스트를 실행하기 위한 기본 설정이 있어야 한다고 말할 수 있습니다. 기본 호스트 할당자는 먼저 해당 호스트에 해당 OS 유형의 게스트를 배치하려고 시도합니다. 그러한 호스트를 사용할 수 없는 경우 할당자는 충분한 물리적 용량이 있는 곳에 인스턴스를 배치합니다.
* 수직 및 수평 할당. 수직 할당은 두 번째 호스트에 게스트를 할당하기 전에 주어진 호스트의 모든 리소스를 소비합니다. 이것은 클라우드의 전력 소비를 줄입니다. 수평 할당은 라운드 로빈 방식으로 각 호스트에 게스트를 배치합니다. 이는 경우에 따라 게스트에게 더 나은 성능을 제공할 수 있습니다.
* 관리자 사용자 환경 설정. 관리자는 VM을 실행할 Zone, Cluster 또는 호스트를 지정할 수 있습니다. 그러면 Mold는 주어진 인프라 내에서 호스트를 선택합니다.
최종 사용자 기본 설정. 사용자는 특정 VM 인스턴스를 실행할 호스트를 정확히 제어할 수 없지만, VM의 zone을 지정할 수 있습니다. 그러면 Mold는 해당 zone의 호스트 중 하나에만 VM을 할당하도록 제한됩니다.
* 호스트 태그. 관리자는 호스트에 태그를 할당할 수 있습니다. 이러한 태그는 VM이 ​​사용해야 하는 호스트를 지정하는 데 사용할 수 있습니다. Mold 관리자는 호스트 태그를 정의할지 여부를 결정한 다음 해당 태그를 사용하여 서비스 오퍼링을 생성하여 사용자에게 제공합니다.
* 동질 그룹. Affinity 그룹을 정의하고 여기에 VM을 할당함으로써 사용자 또는 관리자는 별도의 호스트에서 실행해야 하는 VM에 영향을 줄 수 있지만 지정할 수는 없습니다. 이 기능은 사용자가 특정 VM이 동일한 호스트에 있지 않도록 지정할 수 있도록 하는 것입니다.
* Mold는 또한 새 할당자를 추가하기 위한 플러그형 인터페이스를 제공합니다. 이러한 사용자 지정 할당자는 관리자가 원하는 모든 정책을 제공할 수 있습니다.

<H4>Affinity 그룹</H4>
Affinity 그룹을 정의하고 여기에 VM을 할당함으로써 사용자 또는 관리자는 별도의 호스트에서 실행해야 하는 VM에 영향을 줄 수 있지만 지정할 수는 없습니다. 이 기능은 사용자가 "host anti Affinity" 유형이 동일한 VM이 동일한 호스트에 있지 않도록 지정할 수 있도록 하기 위한 것입니다. 이는 내결함성을 높이는 역할을 합니다. 호스트가 실패하면 동일한 서비스를 제공하는 다른 VM (예 : 사용자의 웹 사이트 호스팅)이 여전히 다른 호스트에서 실행되고 있습니다.

Affinity 그룹의 범위는 사용자 계정 당입니다.

<H4>새 Affinity 그룹 생성</H4>
Affinity 그룹을 추가하려면 다음을 수행하십시오.

1. 관리자 또는 사용자로 Mold UI에 로그인하십시오.
2. 왼쪽 탐색 모음에서 컴퓨트를 클릭합니다.
2. Affinity 그룹을 클릭합니다.
3. Affinity 그룹 추가를 클릭하십시오. 대화 상자에서 다음 필드를 채웁니다.
    * 이름. 그룹에 이름을 지정하십시오.
    * 기술. 그룹의 목적에 대해 자세히 설명하기 위해 원하는 텍스트입니다.
    * 유형. Mold 함께 제공되는 유일하게 지원되는 유형은 Host Anti-Affinity입니다. 이는 이 그룹의 VM이 서로 동일한 호스트에 배치되지 않아야 함을 나타냅니다. 이 목록에 다른 유형이 표시되면 Mold 설치가 사용자 지정된 Affinity 그룹 플러그인으로 확장되었음을 의미합니다.

<H4>Affinity 그룹에 새 VM 할당</H4>
Affinity 그룹에 새 VM을 할당하려면 :

“VM 만들기"에 설명 된 대로 평소와 같이 VM을 만듭니다. 인스턴스 추가 마법사에는 Affinity 그룹을 선택할 수 있는 새 Affinity 탭이 있습니다.

<H4>기존 VM에 대한 Affinity 그룹 변경</H4>
Affinity 그룹에 기존 VM을 할당하려면 :

1. 관리자 또는 사용자로 Mold UI에 로그인하십시오.
2. 왼쪽 탐색에서 가상머신을 클릭합니다.
3. 수정하려는 가상머신을 선택합니다.
4. 작업할 VM의 이름을 클릭합니다.
5. 중지 버튼을 클릭하여 VM을 중지합니다.
6. Affinity 변경 버튼을 클릭합니다.

<H4>Affinity 그룹의 구성원 보기</H4>
현재 특정 Affinity 그룹에 할당된 VM을 확인하려면 :

1. 왼쪽 탐색 모음에서 컴퓨트 클릭합니다.
2. Affinity 그룹을 클릭합니다.
3. 삭제할 Affinity 그룹의 이름을 클릭하십시오.
4. 가상머신 보기를 클릭합니다. 그룹의 구성원이 나열됩니다.
5. 여기에서 목록의 VM 이름을 클릭하여 모든 세부 정보 및 제어에 액세스할 수 있습니다.

<H4>Affinity 그룹 삭제</H4>
Affinity 그룹을 삭제하려면 다음을 수행하십시오.

1. 왼쪽 탐색 모음에서 컴퓨트 클릭합니다.
2. Affinity 그룹을 클릭합니다.
3. 삭제할 그룹의 이름을 클릭하십시오.
4. Affinity 그룹 삭제 버튼을 클릭합니다.
5. 확인을 클릭합니다.

Affinity 그룹의 구성원인 모든 VM은 그룹에서 연결 해제됩니다. 이전 그룹 구성원은 현재 호스트에서 계속 정상적으로 실행되지만 VM이 다시 시작되면 더 이상 이전 선호도 그룹의 호스트 할당 규칙을 따르지 않습니다.

<H3>VM의 기본 이미지 변경</H3>
모든 VM은 Mold에 생성 및 저장된 템플릿 또는 ISO인 기본 이미지에서 생성됩니다. 클라우드 관리자와 최종 사용자는 모두 템플릿, ISO 및 VM을 만들고 수정할 수 있습니다.

Mold에서 기존 VM의 기본 이미지를 한 템플릿에서 다른 템플릿으로 또는 한 ISO에서 다른 ISO로 변경할 수 있습니다. (ISO에서 템플릿으로 또는 템플릿에서 ISO로 변경할 수 없습니다.)

예를 들어 특정 운영 체제를 기반으로 하는 템플릿이 있고 OS 공급 업체가 소프트웨어 패치를 릴리스한다고 가정합니다. 관리자 또는 사용자는 당연히 패치를 적용한 다음 기존 VM에서 패치를 사용하기를 원합니다. 소프트웨어 업데이트 관련 여부와 관계없이 VM을 현재 템플릿에서 원하는 다른 템플릿으로 간단히 전환할 수도 있습니다.

VM의 기본 이미지를 변경하려면 restoreVirtualMachine API 명령을 호출하고 가상 머신 ID와 새 템플릿 ID를 전달합니다. 템플릿 ID 매개 변수는 VM이 ​​이미 사용 중인 기본 이미지 유형에 따라 템플릿 또는 ISO를 참조할 수 있습니다 (이전 이미지 유형과 일치해야 함). 이 호출이 발생하면 VM의 루트 디스크가 먼저 파괴된 다음 템플릿 ID 매개 변수에 지정된 소스에서 새 루트 디스크가 생성됩니다. 새 루트 디스크가 VM에 연결되고 이제 VM이 새 템플릿을 기반으로 합니다.

restoreVirtualMachine 호출에서 템플릿 ID 매개 변수를 생략할 수도 있습니다. 이 경우 VM의 루트 디스크가 삭제되고 다시 생성되지만 VM에서 이미 사용 중인 동일한 템플릿 또는 ISO에서 생성됩니다.

<H3>VM 고급 설정</H3>
각 사용자 VM에는 이와 관련된 일련의 "세부 정보"가 있습니다 (listVirtualMachine API 호출을 통해 표시됨). 이러한 "세부 정보"는 GUI에서 VM의 "설정"탭에 표시됩니다

설정 탭은 항상 표시/표시되지만 VM이 중지됨 상태인 경우에만 설정을 변경할 수 있습니다. 일부 VM 세부 정보/설정은 "user.vm.blacklisted.details" 글로벌 설정을 통해 숨길 수 있습니다 (기본적으로 숨겨진 목록 아래에서 찾을 수 있음).

!!! note
    ROOT 디스크 컨트롤러, NIC 어댑터 유형 및 데이터 디스크 컨트롤러에 대한 VMware VM 설정은 템플릿에서 상속된 값으로 자동으로 채워집니다.

새 설정을 추가하거나 기존 설정을 수정할 때 설정 이름과 가능한 값 (부울 또는 숫자 값 제외)이 드롭 다운 목록에 표시/제공됩니다.

* rootdisksize
* cpuOvercommitRatio
* memoryOvercommitRatio
* Message.ReservedCapacityFreed.Flag

## 가상 머신 스냅샷
(VMware, XenServer 및 KVM에서 지원됨 (NFS 만 해당))

개별 VM 볼륨의 스냅샷을 생성하는 기존 Mold 기능 외에도 VM 스냅샷을 생성하여 모든 VM의 데이터 볼륨과 CPU/메모리 상태 (선택 사항)를 보존할 수 있습니다. 이는 VM의 빠른 복원에 유용합니다. 예를 들어 VM의 스냅샷을 만든 다음 소프트웨어 업그레이드와 같은 변경 작업을 수행할 수 있습니다. 문제가 발생하면 이전에 저장된 VM 스냅샷을 사용하여 VM을 이전 상태로 복원하기 만 하면됩니다.

스냅샷은 하이퍼바이저의 기본 스냅샷 기능을 사용하여 생성됩니다. VM 스냅샷에는 데이터 볼륨뿐 아니라 선택적으로 VM이 실행 중인지 꺼져 있는지 (CPU 상태) 및 메모리 내용도 포함됩니다. 스냅샷은 Mold의 기본 스토리지에 저장됩니다.

VM 스냅샷은 상위/하위 관계를 가질 수 있습니다. 동일한 VM의 연속적인 각 스냅샷은 이전에 나온 스냅샷의 하위입니다. 동일한 VM의 추가 스냅샷을 만들 때마다 VM의 현재 상태와 가장 최근의 이전 스냅샷에 저장된 상태 간의 차이만 저장됩니다. 이전 스냅샷은 상위가 되고 새 스냅샷은 하위입니다. 이러한 상위/하위 스냅샷의 긴 체인을 생성할 수 있으며 이는 VM의 현재 상태에서 원래 상태로 돌아가는 "재실행" 레코드에 해당합니다.

VM 스냅샷이 생성되면 Mold의 다른 많은 리소스와 마찬가지로 키/값 쌍으로 태그를 지정할 수 있습니다.

KVM은 NFS 공유 스토리지를 사용할 때 VM 스냅샷을 지원합니다. 원시 블록 스토리지가 사용되는 경우 (예 : Ceph), RAM 메모리 콘텐츠를 어디에도 쓸 수 없기 때문에 VM 스냅샷이 불가능합니다.

VMware의 VM 스냅샷에 대한 자세한 정보가 필요한 경우 VMware 문서 및 VMware Knowledge Base, 특히 가상 머신 스냅샷 이해를 확인하십시오.

<H3>가상 머신 스냅샷</H3>
VM 스냅샷에 대한 제한

* VM에 저장된 스냅샷이 있는 경우 새 볼륨을 VM에 연결하거나 기존 볼륨을 삭제할 수 없습니다. VM의 볼륨을 변경하면 이전 볼륨 구조로 생성된 VM 스냅샷을 복원할 수 없게 됩니다. 이러한 VM에 볼륨을 연결하려면 먼저 해당 스냅샷을 삭제하십시오.
* 데이터 볼륨과 메모리를 모두 포함하는 VM 스냅샷은 VM의 서비스 제공을 변경하면 보관할 수 없습니다. 이 유형의 기존 VM 스냅샷은 모두 삭제됩니다.
* 볼륨 스냅샷을 만드는 동시에 VM 스냅샷을 만들 수 없습니다.
* Mold에 관리하는 호스트에서 VM 스냅샷을 생성하려면 Mold만 사용해야 합니다. 하이퍼바이저에서 직접 만든 스냅샷은 Mold에서 추적되지 않습니다.

<H3>VM 스냅샷 구성</H3>
클라우드 관리자는 글로벌 설정 변수를 사용하여 VM 스냅샷의 동작을 제어할 수 있습니다. 이러한 변수를 설정하려면 Mold UI의 글로벌 설정 영역으로 이동하십시오.

|<center>구성</center>|<center>설명 유형</center>|
|:---|:---|
|vmsnapshots.max|클라우드의 특정 가상 머신에 대해 저장할 수 있는 최대 VM 스냅샷 수입니다. 클라우드에서 가능한 총 VM 스냅샷 수는 (VM 수) * vmsnapshots.max입니다. VM의 스냅샷 수가 최대 값에 도달하면 이전 스냅샷이 스냅샷 정리 작업에 의해 제거됩니다.|
|vmsnapshot.create.wait|실패를 선언하고 오류를 발생하기 전에 스냅샷 작업이 성공하기를 기다리는 시간 (초)입니다.|

<H3>VM 스냅샷 구성</H3>
Mold UI를 사용하여 VM 스냅샷을 생성하려면 :

1. 사용자 또는 관리자로 Mold UI에 로그인하십시오.
2. 컴퓨트를 클릭하십시오.
3. 가상머신을 클릭합니다.
4. 스냅샷을 생성할 VM의 이름을 클릭합니다.
5. VM 볼륨 스냅샷 생성 버튼을 클릭합니다.

    !!! note
        스냅샷이 이미 진행 중인 경우 이 버튼을 클릭해도 아무 효과가 없습니다.

6. 이름과 설명을 제공하십시오. VM 스냅샷 목록에 표시됩니다.
7. (실행 중인 VM에만 해당) VM의 메모리를 스냅샷에 포함하려면 메모리 확인란을 클릭합니다. 이렇게 하면 가상 머신의 CPU 및 메모리 상태가 저장됩니다. 이 상자를 선택하지 않으면 VM 디스크의 현재 상태만 저장됩니다. 이 확인란을 선택하면 스냅샷이 더 오래 걸립니다.
8. VM 중지 : 스냅샷을 생성하기 전에 VM의 파일 시스템을 중지하려면 확인란을 선택합니다. 에서 제공하는 기본 스토리지와 함께 사용하는 경우 XenServer에서 지원되지 않습니다.
9. 이 옵션을 Mold에서 제공하는 기본 스토리지와 함께 사용하면 기본 하이퍼바이저에서 중지 작업이 수행됩니다 (VMware가 지원됨). 다른 기본 스토리지 공급 업체의 플러그인과 함께 사용하는 경우 공급 업체의 구현에 따라 정지 작업이 제공됩니다.
10. 확인을 클릭하십시오.

스냅샷을 삭제하거나 특정 스냅샷에 저장된 상태로 VM을 복원하려면 :

1. 사용자 또는 관리자로 Mold UI에 로그인하십시오.
2. 컴퓨트를 클릭하십시오.
3. VM 스냅샷을 클릭합니다.
4. 스냅샷 목록에서 작업할 스냅샷의 이름을 클릭합니다.
5. 수행하려는 작업에 따라 :
    스냅샷을 삭제하려면 삭제 버튼을 클릭합니다.
    스냅샷으로 되돌리려면 되돌리기 버튼을 클릭합니다.

!!! note
    VM이 파괴되면 VM 스냅샷이 자동으로 삭제됩니다. 이 경우 스냅샷을 수동으로 삭제할 필요가 없습니다.

## 가상 어플라이언스 지원
<H3>가상 어플라이언스 정보</H3>
Mold를 사용하면 vCenter를 통해 직접 만든 것과 같은 가상 어플라이언스를 VMware에 배포할 수 있습니다. VMware용 가상 어플라이언스 공급 업체는 종종 OVA 형식으로 어플라이언스의 '템플릿'을 생성합니다. OVA 파일에는 디스크 이미지, 가상 어플라이언스의 구성 데이터 및 때때로 승인되어야 하는 EULA가 포함됩니다.

<H3>배포 옵션 (구성)</H3>
VMware 템플릿은 OVF 설명자 파일에서 다양한 배포 옵션을 제공할 수 있습니다. Mold는 템플릿이 등록될 때 다양한 배포 옵션을 가져와서 컴퓨트 오퍼링 섹션의 가상 머신 배포 마법사에서 사용자에게 표시합니다.

사용자가 배포 옵션을 선택하면 Mold는 CPU 및 메모리에 대한 배포 옵션 하드웨어 요구 사항과 일치하거나 초과하는 컴퓨팅 제품을 나열합니다.

!!! note
    모든 사용자 지정 제한되지 않은 컴퓨팅 제품이 표시되지만 선택한 배포 옵션에서 CPU 및 메모리에 대한 최대 또는 최소 요구 사항이 지원되는 제한된 사용자 지정 제품만 표시됩니다.

'컴퓨트 오퍼링'섹션은 다음과 같습니다.
<center>![mold_compute_offering_section](../../assets/images/mold_compute_offering_section.png)</center>

고급 배포 설정
가상 어플라이언스에 대한 부팅 유형 (BIOS, UEFI) 및 부팅 모드를 선택할 수 없습니다. 가상 어플라이언스에서 사용하는 부팅 모드 및 유형은 템플릿에 정의되어 있습니다.

<H3>고급 배포 설정</H3>
가상 어플라이언스에 대한 부팅 유형 (BIOS, UEFI) 및 부팅 모드를 선택할 수 없습니다. 가상 어플라이언스에서 사용하는 부팅 모드 및 유형은 템플릿에 정의되어 있습니다.

## 가상 머신 관리 해제
<H3>관리되지 않는 가상 머신 정보</H3>
Mold에는 관리되지 않는 가상 머신의 개념이 있습니다. 이들은 Mold 관리 호스트에 있지만 Mold의 데이터베이스에 없는 가상머신이므로 Mold는 어떤 식으로든 제어(관리)할 수 없습니다. 

Mold는 listUnmanagedInstances API 명령을 통해 이러한 VM을 나열한 다음 importUnmanagedInstance API를 통해 관리되지 않는 VM을 가져와 (수집이라고도 함) Mold 관리 게스트 인스턴스가 되도록 할 수 있습니다.

Mold 관리자는 게스트 가상 머신을 관리 취소할 수 있습니다.

!!! note
    현재 vSphere 클러스터에서만 사용할 수 있습니다.

<H3>API를 통해 가상 머신 관리 해제</H3>
관리자는 Mold에서 게스트 가상 머신을 관리 취소할 수 있습니다. 관리가 해제되면 Mold는 더 이상 가상 머신에서 프로비저닝 및 오케스트레이션 관련 작업을 모니터링, 제어 또는 관리할 수 ​​없습니다.

게스트 가상 머신의 관리를 해제하려면 관리자가 unmanageVirtualMachine API를 호출하여 관리 해제할 가상 머신의 ID를 전달해야 합니다. API에는 다음과 같은 전제 조건이 있습니다.

* 가상 머신을 폐기해서는 안됩니다.
* 가상 머신 상태는 '실행중'또는 '중지됨'이어야합니다.
* 가상 머신은 VMware 가상 머신이어야합니다.

API 실행은 다음 사전 검사를 수행하며 충족되지 않으면 실패합니다.

* 가상 머신 볼륨과 연결된 볼륨 스냅샷이 없습니다.
* 가상 머신에 연결된 ISO가 없습니다.

!!! note
    현재 vSphere 클러스터에서만 사용할 수 있습니다.

<H3>관리되지 않는 가상 머신 NIC 보존</H3>
zone 설정 : unmanage.vm.preserve.nics를 사용하여 가상 머신 NIC 및 MAC 주소를 관리 해제한 후 보존할 수 있습니다. true로 설정하면 가상 머신 NIC (및 해당 MAC 주소)가 관리 취소 시 보존됩니다. 그렇지 않으면 NIC가 제거되고 MAC 주소가 다시 할당될 수 있습니다.

## 가상 머신 작업 관리 해제
* 가상 머신 NIC를 정리하고 가상 라우터의 IP 주소 및 DHCP 항목과 같은 사용된 네트워크 리소스를 할당 해제합니다.
    * 'unmanage.vm.preserve.nics'='false'이면 NIC가 할당 해제되고 Mold에서 제거됩니다.
    * 'unmanage.vm.preserve.nics'='true'이면 NIC가 할당된 상태로 유지되고 데이터베이스에서 제거되지 않습니다. NIC의 MAC 주소는 그대로 유지되므로 새 NIC에 할당할 수 없습니다.

* Mold 데이터베이스에서 가상 머신 볼륨 정리
* Mold 데이터베이스 (있는 경우)에서 가상 머신 스냅 샷 정리
* VM에 연결된 모든 관리 볼륨에 대한 호스트 액세스 권한 취소 (관리 스토리지에만 적용 가능)
* 다음에서 가상 머신을 정리합니다.
    * 보안 그룹에서 가상 머신 제거 (있는 경우)
    * 가상머신 그룹에서 가상 머신 제거 (있는 경우)
    * 가상 머신에 대한 방화벽 규칙 제거 (있는 경우)
    * 가상 머신에 대한 포트 전달 규칙 제거 (있는 경우)
    * 가상 머신에 대한 로드 밸런싱 규칙 제거 (있는 경우)
    * 정적 NAT 비활성화 (가상 머신이 할당된 경우)
    * 선호도 그룹 (있는 경우)에서 가상 머신 제거

* Mold 데이터베이스에서 VM 세부 정보 제거
* 볼륨 및 가상 머신에 대한 계정 리소스 수 줄이기
* 사용 이벤트 생성 :
    * 파괴된 볼륨의 경우, 유형 : 'VOLUME.DELETE'
    * 삭제된 가상 머신 스냅 샷의 경우 (있는 경우), 유형 : 'VMSNAPSHOT.DELETE'및 'VMSNAPSHOT.OFF_PRIMARY'
    * 파괴된 가상 머신 NIC의 경우 : 'NETWORK.OFFERING.REMOVE'유형 사용
    * 관리되지 않는 가상 머신의 경우 : 중지 및 폐기된 사용 이벤트 (가상 머신을 정리할 때 생성된 사용 이벤트와 유사), 유형 : 'VM.STOP'및 'VM.DESTROY'(VM이 이미 중지된 상태가 아닌 경우) 관리되지 않으며 이 경우 'VM.DESTROY'만 생성됩니다.

## 가상 머신 가져오기
VM을 가져올 수 있는 기능을 통해 클라우드 운영자(퍼블릭 및 프라이빗 모두)는 최소한의 디스크 IO로 간단하고 빠르게 새 테넌트를 온 보딩할 수 있습니다. 그러나 원격 사이트의 재해 복구 시나리오 (스토리지가 복제된 경우) 및 백업된 VM의 재현에도 사용할 수 있습니다.

VM 가져오기에서 가장 복잡한 부분은 관리되지 않는 VM의 네트워크를 Mold 네트워크에 매핑하는 것입니다. 운영자가 수십 또는 수백 개의 VM을 가져올 수 있으므로 이 기능에 대한 UI는 아직 생성되지 않았습니다.

'대상' 네트워크 VLAN 및 요청된 서비스 제공이 기존 VM과 일치하면 인스턴스가 실행되는 동안 가져올 수 있습니다. VLAN 또는 서비스 오퍼링이 일치하지 않으면 가져올 인스턴스를 중지해야합니다. 가상머신이 Mold에 추가되면 Mold를 통해 시작하면 Mold DB에 설정된 설정에 따라 인스턴스 설정이 변경됩니다.

인스턴스를 가져오려면 클라우드 제공자가 다음을 수행한다고 가정합니다.

* 가져올 인스턴스가 있는 기존 네트워크를 모두 나열합니다.
* Mold에서 해당 네트워크 생성
* listUnmanagedInstances API를 사용하여 가져올 인스턴스의 CSV를 만듭니다.
* 필요한 경우 각 VM이 연결되는 계정, 각 VM이 연결될 네트워크, 각 인스턴스에 필요한 컴퓨트 오퍼링 및 각 디스크에 대한 디스크 오퍼링과 같은 메타 데이터를 CSV에 추가합니다.
* CSV를 반복하는 스크립트를 만들고 CSV에서 읽는 각 인스턴스에 해당하는 매개 변수와 함께 importUnmanagedInstance API 명령을 보냅니다.

<H3>listUnmanagedInstances API</H3>
<H4>비 관리 형 인스턴스를 나열하기 위한 사전 요구 사항 (vSphere)</H4>
Mold에 호스트/클러스터의 Mold에서 관리하지 않는 인스턴스를 나열하려면 vSphere 클러스터의 호스트가 Mold에 추가되어 있어야 합니다. Mold에 호스트를 추가하기 위한 표준 전제 조건이 적용됩니다.

<H4>API</H4>
이 API는 지정된 클러스터의 모든 관리되지 않는 VM을 나열합니다. 선택적으로 기존 관리되지 않는 VM의 vSphere 이름을 지정하여 VM 세부 정보를 검색할 수 있습니다. API는 모든 Mold 관리 VM을 필터링하고 vCenter에서 VM으로 표시되는 템플릿도 필터링합니다.

요청 매개 변수 :

```
- clusterid (클러스터의 Mold UUID)
- name (vSphere 인스턴스 이름)
```

응답 :
```
- clusterid
- hostid
- name 
- osdisplayname 
- memory 
- powerstate
- cpuCoresPerSocket 
- cpunumber 
- cpuspeed 
- disk 
   - id 
   - capacity (바이트)
   - controller 
   - controllerunit 
   - imagepath
   - position
- NIC 
   - id 
   - macaddress
   - networkname
   - vlanid 
   - pcislot 
   - adaptertype (가능한 경우)
   - ipaddress (VMware 도구가 인스턴스에서 실행 중인 경우에만 반환됩니다.)
```

<H3>importUnmanagedInstance API</H3>
요청 매개 변수 :
```
- 클러스터 ID (클러스터의 Mold UUID)
- 이름 (vSphere 인스턴스 이름)
- 표시 이름 
- 호스트 이름 
- 계정 (가상 머신에 대한 옵션 계정 이름이 domainid 매개 변수와 함께 사용할 수 있어야 합니다)
- domainid (가상 머신에 대한 옵션 도메인 ID는 계정 매개 변수와 함께 사용해야 합니다.)
- projectid 
- templateId
- serviceofferingid
- nicnetworklist (NIC ID 용 맵 및 해당 네트워크 UUID)
- nicipaddresslist (NIC ID에 대한지도 및 해당 IP 주소)
- datadiskofferinglist (지도 데이터 디스크 ID 및 해당 디스크를 제공하는 UUID에 대한)
- 세부 정보 (VM 세부 정보 맵)
- migrateallowed (호스트/스토리지 풀에 태그 충돌을 제공할 경우 VM과 볼륨이 다른 호스트/저장 zone 풀로 마이그레이션 할 수 있습니다)
- 강제 (true인 경우 일부 NIC의 MAC 주소가 이미 존재하더라도 VM을 가져옴)
```

!!! note
    강제 매개 변수는 기본적으로 이전에 Mold에 의해 할당된 MAC 주소를 포함하는 NIC가 있는 VM을 가져 방지하여 false입니다. true로 설정되면 Mold 데이터베이스에 이미 존재하는 MAC 주소가 있는 NIC에는 기존 MAC 주소가 NIC에 재 할당됩니다.

응답 :
    ```
    Same response as that of deployVirtualMachine API.
    ```
<H4>비 관리형 인스턴스를 가져오기 위한 사전 요구 사항 (vSphere)</H4>
관리되지 않는 인스턴스를 Mold로 가져오기 위한 몇 가지 전제 조건이 있습니다. 대체로 Mold에서 인스턴스를 연결하려는 네트워크는 Mold에 이미 존재해야하며 관리되지 않는 인스턴스가 있는 스토리지(가져오기 전) 및 가져온 후 가상머신이 데이터를 이관할 스토리지가 있어야 합니다.

VM은 격리, 공유 또는 L2 네트워크로 가져올 수 있습니다. VM을 가져온 다음 migrateallowed API 매개 변수를 사용하여 서비스 제공에 따라 스토리지로 자동 마이그레이션 할 수도 있습니다.

<H4>더미 템플릿</H4>
Mold의 모든 게스트 인스턴스가 템플릿 또는 ISO에서 생성된다는 가정은 Mold에 하드 코딩됩니다. 이 소스 템플릿은 Mold로 가져온 인스턴스에 대해 존재하지 않으며 Mold 데이터베이스에 더미 템플릿이 생성되었습니다. 인스턴스를 가져올 때 템플릿 ID가 제공되지 않으면 내장된 더미 템플릿 ID가 사용됩니다. 이 템플릿은 더미 템플릿이므로 실제 템플릿 ID를 지정하지 않으면 원래 템플릿으로 '되돌릴' 수 없습니다.

<H4>오퍼링 및 자동 매핑</H4>
인스턴스를 가져올 때 Mold는 vNIC (가상 네트워크 인터페이스)를 Mold 네트워크에 연결해야 합니다. vNIC는 두 가지 방법 중 하나로 네트워크와 연결됩니다.

1. 자동 (L2 및 공유 네트워크에서 사용 가능)
2. VM에 둘 이상의 NIC가 있는 경우 맵으로 네트워크 (ID)에 vNIC 수동 할당

기업에서 대부분의 네트워크는 Active Directory 또는 InfoBlox와 같은 IPAM 시스템에서 처리하는 IP 주소 지정을 사용하여 계층 2 네트워크로 작동합니다. 따라서 Mold의 L2 네트워크는 VM의 유사 마이그레이션/온 보딩을 위한 자연스러운 선택입니다.

인스턴스를 공유 또는 L2 네트워크로 가져올 때 Mold는 인스턴스의 NIC가 이미 켜져 있는 것과 동일한 VLAN이 있는 Mold 네트워크를 자동으로 찾습니다. 'nicnetworklist' 매개 변수에 network_id를 제공하여 재정의 할 수 있습니다.

!!! note
    여기에는 L2 네트워크의 PVLAN이 포함됩니다.

NIC에 특정 IP 주소를 할당하기 위해 'nicipaddresslist' 매개 변수가 사용됩니다. 이 매개 변수는 L2 네트워크에 사용해서는 안 되며 공유 네트워크에 대해서는 선택 사항입니다. 가져올 때 Mold에 인스턴스의 기존 IP를 할당하도록 요청하려면 auto 값을 사용할 수 있습니다.

```
nicipaddresslist[0].nic=NIC_ID nicipaddresslist[0].ip4Address=auto
```

IP 주소를 자동 할당하려면 VMware 도구가 게스트 인스턴스에 있어야 하며 (IP가 vCenter에 보고되도록) 관리되지 않는 VM이 ​​해당 NIC와 연결된 두 개 이상의 IP 주소를 보고하는 경우 지원되지 않습니다 (Mold에서 기본 주소). NIC당 IP 주소가 2 개 이상인 인스턴스의 경우 가져오기 API를 통해 첫 번째 IP 주소를 전달한 다음 'addIpToNic'API를 통해 보조 주소를 추가합니다.

<H4>맞춤형 vs 고정 오퍼링</H4>
Mold의 모든 게스트 인스턴스에는 연결된 컴퓨팅 제품이 있어야 합니다. 가져오기 API는 '고정'(즉, 오퍼링에 하드 코딩된 2GB RAM이있는 2 개의 vCPU) 및 '커스텀'(사용자가 vCPU 및 메모리 수를 선택할 수 있음) 오퍼링 사용을 지원합니다. 커스텀 오퍼링을 선택하면 Mold는 가져오기 전에 VM과 동일하게 vCPU 수, CPU 속도 및 RAM 양을 자동으로 설정합니다. 사용자 정의 오퍼링을 사용할 때 가져올 인스턴스는 계속 실행될 수 있습니다. 컴퓨트 오퍼링이 '고정' 이고 기존 인스턴스의 vCPU 및 RAM과 일치하면 인스턴스를 가져 오는 동안 계속 실행될 수 있습니다. 그렇지 않으면 인스턴스를 먼저 중지해야 하며 시작 시 새 값으로 재구성됩니다.

VM을 가져올 때 호환성을 극대화하기 위해 Mold에서 사용자 지정 제한 유형의 컴퓨팅 제품이 권장되는 제품 유형입니다. 가져온 VM에 할당된 메모리 양과 CPU 수가 기존 VM과 자동으로 일치하는 반면, CPU 속도는 오퍼링을 생성할 때 관리자가 합리적인 값으로 설정합니다.

!!! note
    Custom Unconstrained 유형의 컴퓨트 오퍼링을 사용하려면 vSphere에서 관리되지 않는 VM에 대해 CPU 예약이 설정되지 않은 경우 세부 매개 변수를 사용하여 CPU 속도를 전달해야 합니다. 후자의 경우 CPU 속도는 details[0].cpuSpeed​​=SOME_VALUE로 전달할 수 있습니다.

<H4>디스크 제품</H4>
데이터 디스크가 연결된 VM을 가져오려면 datadiskofferinglist 매개 변수를 통해 디스크 ID 및 해당 디스크 오퍼링 ID의 맵을 전달해야 합니다.

예를 들면 :
```
datadiskofferinglist[0].disk=<DISK_ID> datadiskofferinglist[0].diskOffering=<DISK_OFFERING_ID>
```

!!! note
    선택한 디스크 오퍼링의 크기가 실제 디스크 크기보다 큰 경우 Mold는 가져올 때 디스크 크기 조정을 수행하지 않습니다. 디스크는 원래 크기로 유지되지만 Mold는 오퍼링에 따라 기록을 갖게됩니다.

<H4>호스트 및 스토리지 태그</H4>
migrateallowed 매개 변수가 true로 설정되어 있는 컴퓨팅/디스크 제품의 호스트 또는 저장 태그는 현재 호스트 스토리지 풀과 호환되지 않는 경우, Mold는 적절한 호스트 및 스토리지 풀에 VM과 볼륨을 마이그레이션합니다.

migrateallowed는 거짓과 충돌이 발생, 해당 오류가 반환됩니다.

마이그레이션은 실행 중인 VM과 중지된 VM 모두에 대해 지원됩니다. 가져온 VM을 실행하기 위해 라이브 마이그레이션이 지원됩니다. 중지된 VM을 가져 오면 Mold는 다시 시작될 때 VM을 적절한 호스트로 마이그레이션합니다.

볼륨의 경우 실행 중인 VM의 볼륨에 대해 라이브 마이그레이션이 수행됩니다. 기존 Mold 동작에 따라 중지된 가져온 VM은 VM이 다시 시작될 때까지 루트 볼륨이 마이그레이션될 때 vCenter에 나타나지 않을 수 있습니다.

<H4>등록된 운영 체제</H4>
Import API는 관리되지 않는 VM의 운영 체제 유형을 인식하고 Mold에서 사용 가능한 게스트 운영 체제 목록의 운영 체제 유형에 매핑하려고 합니다. 운영 체제 유형을 매핑할 수 없는 경우 API는 오류를 반환하고 성공적인 가져오기를 위해 templateid 매개 변수 (값 = 적절한 운영 체제가 있는 템플릿의 ID)가 필요합니다. 가져오기 API 호출에서 templateid가 정의되면 가져온 VM의 게스트 운영체제 세부 정보가 VM 다시 시작 후 지정된 템플릿의 운영 체제 세부 정보로 설정됩니다.

<H4>importUnmanagedInstance API에 대한 기타 참고 사항</H4>

* API는 hostname 매개 변수가 명시적으로 전달되지 않은 경우 VM 의 호스트 이름에 이름을 사용합니다. 호스트 이름은 63자를 초과할 수 없습니다. ASCII 문자 az, AZ, 숫자 0-9, 하이픈만 허용됩니다. 문자로 시작하고 문자 또는 숫자로 끝나야 합니다.
* VM의 NIC 어댑터 및 디스크 컨트롤러는 템플릿 구성에 관계 없이 가져오기 전과 동일하게 유지됩니다.
* 가져 오는 동안 VM 운영 체제가 자동으로 인식되고 (즉, templateid 매개 변수가 지정되지 않음) VM의 운영 체제 (하이퍼바이저에서 보고 됨)가 Mold의 여러 운영 체제와 일치할 수 있는 경우 첫 번째 일치는 Mold에서 가져온 VM의 운영 체제로 사용됩니다. 예를 들어 vSphere에서 볼 수 있는 "CentOS 7 (64 bit)"운영 체제 유형은 Mold에서 "CentOS 7"또는 "CentOS 7.1"또는 "CentOS 7.2"와 일치할 수 있습니다 (기준 기존 게스트 OS 매핑), 여기서 첫 번째 항목 ( "CentOS 7")은 가져온 VM의 운영 체제로 사용됩니다.
* 데이터 디스크에 대해 서로 다른 유형의 디스크 컨트롤러와 서로 다른 유형의 여러 NIC가 있는 VM을 가져 오는 것은 지원되지 않으며 오류 응답이 발생합니다. 루트 디스크와 기타 (데이터 디스크) 디스크는 컨트롤러 유형이 다를 수 있습니다.
* 가져온 후 VM이 Mold에서 시작되면 CPU 제한, CPU 예약, 메모리 예약 등을 포함한 CPU 및 RAM 구성이 원래 구성에서 변경될 수 있습니다.
* 실행 중인 VM을 가져온 후 VM의 콘솔에 액세스하려면 Mold를 통해 VM을 중지하고 시작 (다시 시작하지 않음)해야합니다.

<H4>importUnmanagedInstance API에 대한 기타 참고 사항</H4>

<H3>기존 네트워크 검색 (vSphere 용)</H3>
기존 VM을 가져오려면 연결된 네트워크가 이미 Mold 네트워크로 존재해야합니다. 기존 환경에는 생성이 필요한 많은 네트워크가 있을 수 있으므로 기존 네트워크를 열거하기 위해 Python3 스크립트가 생성되었습니다.

스크립트 (discover_networks.py)는 Mold 스크립트 설치 위치의 vm/hypervisor/vmware 디렉토리에서 찾을 수 있습니다. 대부분의 운영 체제에서 Mold는 /usr/share/cloudstack-common/ 에 스크립트를 설치합니다. 이 스크립트는 VMware의 pyvmomi 라이브러리 (https://github.com/vmware/pyvmomi)를 활용합니다. 이 스크립트는 하나 이상의 가상 머신이 연결된 vCenter 호스트 또는 클러스터의 모든 네트워크를 나열합니다. 스크립트는 이러한 네트워크를 반복하고 다음 매개 변수를 보고합니다.

* cluster (vCenter 클러스터가 속한)
* host (vCenter 호스트가 속한)
* portgroup (네트워크의 Portgroup)
* switch (네트워크가 연결된 스위치)
* virtualmachines (현재 자신의 NIC 장치 세부 사항과 함께 네트워크에 연결되어 가상 머신)
* vlanid (네트워크의 VLAN ID)

스크립트는 다음 인수를 사용할 수 있습니다.

```
* -h, --help show this help message and exit
* -s HOST, --host HOST vSphere service to connect to
* -o PORT, --port PORT Port to connect on
* -u USER, --user USER User name to use
* -p PASSWORD, --password PASSWORD Password to use
* -c CLUSTER, --cluster CLUSTER Cluster for listing network
* -S, --disable_ssl_verification Disable ssl host certificate verification
* -d, --debug Debug log messages
```

!!! note
    이 스크립트를 실행하려면 호스트 컴퓨터에 Python 3 및 모듈 pyvmomi가 설치되어 있어야 합니다.

    Python 바이너리는 https://www.python.org/downloads/ 에서 찾을 수 있습니다.

    pyvmomi에 대한 설치 지침은 https://github.com/vmware/pyvmomi#installing에 있습니다.

그런 다음이 스크립트의 출력을 'createNetwork' API 와 함께 사용하여 성공적인 가져오기에 필요한 모든 네트워크를 Mold에 추가할 수 있습니다.

## 가상 머신 백업 (백업 및 복구 기능)

<H3>백업 및 복구 정보</H3>
Mold는 타사 백업 솔루션을 통해 복구 목적으로 게스트 VM을 백업할 수 있는 기능을 제공하는 새로운 B&R (백업 및 복구) 프레임워크가 도입되었습니다. 프레임워크는 이러한 작업을 수행하는 데 필요한 공급 업체 특정 명령에서 일반적인 백업 및 복구 작업에 필요한 API 명령을 추상화하고 '유사'백업 및 복구 기능을 제공하는 모든 솔루션을 통합할 수 있도록 플러그인 모델을 제공합니다.

현재 지원되는 공급자는 다음과 같습니다.

* Veeam 백업 및 복구 기능이 있는 VMware

플러그인 관련 정보는 Veeam Backup and Recovery 플러그인 설명서를 참조하십시오. Veeam 백업 및 복구 플러그인

<H4>백업 및 복구 개념</H4>
백업 및 복구는 두 가지 모드를 지원하도록 설계되었습니다.

* 'SLA'기반 백업
* 임시 및 사용자 예약 백업

'SLA'기반 백업은 클라우드 공급자 (예 : 루트 관리자)가 백업 구성표의 시간과 빈도를 제어하는 ​​백업입니다. 사용자가 '골드'오퍼링에 등록하면 12 시간의 RPO를 제공하고 마지막 14 개의 백업이 보관될 수 있습니다. 그러나 사용자는 추가 백업을 수행하거나 이러한 백업이 발생한 정확한 시간을 설정할 수 없습니다. 백업 크기와 관계없이 이러한 백업에 대한 수정 요금이 사용자에게 청구될 수 있습니다.

SLA 기반 백업 정책을 사용하기 위해 사용자는 오퍼링/정책에 VM을 추가합니다. 그런 다음 작업은 미리 결정된 시간에 실행되고 실행될 때 VM을 '포함'합니다. 사용자는 오퍼링/정책에서 VM을 제거할 수 있으며 실행 시 더 이상 작업에 포함되지 않습니다.

임시 및 사용자 예약 백업은 볼륨 스냅샷과 동일한 개념을 따르지만, 보조 스토리지가 아닌 백업 솔루션을 활용합니다. 이는 사용된 백업 스토리지 또는 보호된 용량 (백업 중인 VM의 전체 가상 크기)에 대해 청구될 수 있습니다.

임시 및 사용자 예약 백업은 볼륨 스냅샷과 동일한 방식으로 생성 및 관리됩니다.

<H3>백업 및 복구 구성</H3>
클라우드 관리자는 전역 구성 변수를 사용하여 B&R 기능의 동작을 제어할 수 있습니다. 이러한 변수를 설정하려면 Mold UI의 글로벌 설정으로 이동하십시오.

|<center>구성</center>|<center>기술</center>|
|:---|:---|
|backup.framework.enabled|기능을 활성화 또는 비활성화하는 설정입니다. 기본값 : false.|
|backup.framework.provider.plugin|백업 공급자 (플러그인) 이름입니다. 예 : 'dummy'및 'veeam'. 이것은 zone별 설정입니다. 기본값 : dummy.|
|backup.framework.sync.interval|메트릭/사용 통계 수집, 백업 조정 및 백업 예약을 수행하는 내부 백그라운드 동기화 작업 (초). 기본값 : 300.|

<H4>플러그인 특정 설정</H4>
각 백업 및 복구 플러그인에는 해당 플러그인과 관련된 설정이 있을 수 있습니다. 이러한 설정을 구성하는 방법에 대한 자세한 내용은 플러그인에 대한 Mold 설명서를 참조하십시오.

<H3>백업 제품</H3>
관리자는 특정 zone에 대한 UI 또는 API를 사용하여 외부 공급자의 백업 제품을 가져올 수있을 뿐만 아니라 백업 제품의 수명주기를 관리할 수 ​​있습니다. 관리자는 백업 오퍼링이 사용자 정의 백업 일정 및 임시 백업을 허용하는지 여부도 지정할 수 있습니다. 사용자는 가져온 백업 오퍼링을 나열하고 사용할 수 있으며 루트 관리자만 오퍼링을 가져 오거나 삭제할 수 있습니다.

지원되는 API :

* listBackupProviders : 사용 가능한 백업 공급자 플러그인을 나열합니다.
* listBackupProviderOfferings : 외부 백업 정책/제공자가 제공하는 제안을 나열합니다.
* importBackupProviderOfferings : 외부 백업 정책 가져오기/백업 오퍼링으로 Mold에 오퍼링 허용
* listBackupOfferings : Mold의 백업 오퍼링을 나열합니다 (키워드를 통한 검색 및 페이지 매김 지원).
* deleteBackupOffering : ID로 백업 오퍼링을 삭제합니다.

<H3>백업 오퍼링 가져오기</H3>
'백업 오퍼링'을 생성하려면 플러그인별 설명서를 참조하십시오.

백업 공급자 오퍼링을 가져오려면

1. 관리자 또는 사용자로 Mold UI에 로그인하십시오.
2. 왼쪽 탐색에서 서비스 오퍼링 클릭합니다.
2. 백업 오퍼링 클릭합니다.
2. 백업 오퍼링 가져오기를 클릭하십시오.
3. 사용자에게 친숙한 이름과 설명을 입력하고 해당 zone을 선택합니다. 그러면 외부 ID가 Mold가 연결된 공급자에서 검색하는 템플릿 작업으로 채워집니다.

<center>![mold_backup_offering_add](../../assets/images/mold_backup_offering_add.png)</center>

<H3>VM 백업 생성</H3>
<H4>SLA/정책 기반 백업</H4>
zone에 대해 백업 및 복구 기능을 활성화하면 사용자는 백업 오퍼링에서 VM을 추가하고 제거하기만 하면됩니다.

<H4>임시 및 예약 백업</H4>
임시 사용자 백업 및 사용자 정의 백업 일정을 허용하는 백업 제품의 경우 사용자는 UI 및 API를 사용하여 백업 제품에 할당된 VM에 대한 백업 일정을 정의할 수 있습니다. 백업이 있는 VM은 VM 스냅샷과 유사한 볼륨을 추가/제거할 수 없습니다.

VM의 임시 백업을 트리거하려면 인스턴스로 이동하여 '백업 시작'아이콘을 클릭합니다.
<center>![mold_backup_start_icon](../../assets/images/mold_backup_start_icon.png)</center>

반복 백업 일정을 설정하려면 인스턴스로 이동하여 'Configure Backup Schedule'아이콘을 클릭합니다.
<center>![mold_backup_schedule_icon](../../assets/images/mold_backup_schedule_icon.png)</center>

그런 다음 백업 시간과 빈도를 설정하고 '구성'을 클릭 한 다음 '닫기'를 클릭하십시오.
<center>![mold_configure_backup_schedule](../../assets/images/mold_configure_backup_schedule.png)</center>

<H3>VM 백업 복원</H3>
사용자는 기존 VM 백업으로 복원하기 위해 VM을 중지해야합니다. 삭제된 VM을 복원해도 NIC는 복원되지 않으며 존재하거나 없을 수도 있는 네트워크를 복구하지 않습니다. 그러나 사용자는 VM 백업에서 특정 볼륨을 복원하고 해당 볼륨을 지정된 VM에 연결할 수 있습니다.

지원되는 API :

* assignVirtualMachineToBackupOffering : 백업 오퍼링에 VM을 추가합니다.
* removeVirtualMachineFromBackupOffering : 강제 true 매개 변수가 전달된 경우 백업 오퍼링에서 VM을 제거합니다. 이는 백업 오퍼링과 연관된 VM의 모든 백업도 제거할 수 있습니다.
* createBackupSchedule : VM에 대한 백업 일정을 만듭니다.
* updateBackupSchedule : 백업 일정을 업데이트합니다.
* listBackupSchedule : 정의된 경우 VM의 백업 일정을 반환합니다.
* deleteBackupSchedule : VM의 백업 일정을 삭제합니다.
* createBackup : VM에 대한 임시 백업을 만듭니다.
* deleteVMBackup : VM 백업을 삭제합니다 (Veeam의 복원 지점별로 지원되지 않음).
* listBackups : 백업을 나열합니다.
* restoreBackup : 중지되거나 삭제된 VM의 위치에서 이전 VM 백업을 복원합니다.
* restoreVolumeFromBackup : 백업된 볼륨 (VM 백업의)을 지정된 VM에 복원하고 연결합니다.

## 인증에 SSH 키 사용
사용자 이름 및 비밀번호 인증 외에도 Mold는 추가 보안을 위해 SSH 키를 사용하여 클라우드 인프라에 로그인하는 것을 지원합니다. createSSHKeyPair API를 사용하여 SSH 키를 생성할 수 있습니다.

각 클라우드 사용자는 자체 SSH 키를 가지고 있기 때문에 한 클라우드 사용자는 SSH 키 파일을 공유하지 않는 한 다른 클라우드 사용자의 인스턴스에 로그인할 수 없습니다. 단일 SSH 키 쌍을 사용하여 여러 인스턴스를 관리할 수 ​​있습니다.

<H3>SSH 키를 지원하는 인스턴스 템플릿 생성</H3>
SSH 키를 지원하는 인스턴스 템플릿을 만듭니다.

1. Mold에서 제공하는 템플릿을 사용하여 새 인스턴스를 만듭니다. 새 인스턴스 생성에 대한 자세한 내용은
2. SSH 키 생성 스크립트에서 생성 한 인스턴스로 cloudstack 스크립트를 다운로드합니다.
```
wget http://downloads.sourceforge.net/project/cloudstack/SSH%20Key%20Gen%20Script/cloud-set-guest-sshkey.in?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fcloudstack%2Ffiles%2FSSH%2520Key%2520Gen%2520Script%2F&ts=1331225219&use_mirror=iweb
```
3. 파일을 /etc/init.d에 복사하십시오.
```
cp cloud-set-guest-sshkey.in /etc/init.d/
```

4. 스크립트에 필요한 권한을 부여하십시오.
```
chmod +x /etc/init.d/cloud-set-guest-sshkey.in
```

5. 운영 체제를 시작하는 동안 스크립트를 실행하십시오.
```
chkconfig --add cloud-set-guest-sshkey.in
```

6. 인스턴스를 중지하십시오.

<H3>SSH 키 쌍 생성</H3>
createSSHKeyPair api 메소드를 호출해야합니다. Mold Python API 라이브러리 또는 curl 명령을 사용하여 Mold api를 호출할 수 있습니다.

예를 들어, Mold 서버에서 호출하여 루트 도메인의 관리자 계정에 대해 "keypair-doc"라는 SSH 키 쌍을 만듭니다.

!!! note
    이러한 값을 필요에 맞게 조정해야합니다. 다른 서버에서 API를 호출하는 경우 URL/PORT가 다르므로 API 키를 사용해야 합니다.

1. 다음 curl 명령을 실행하십시오.
```
curl --globoff "http://localhost:8096/?command=createSSHKeyPair&name=keypair-doc&account=admin&domainid=5163440e-c44b-42b5-9109-ad75cae8e8a2"
```
출력은 아래에 제공된 것과 유사합니다.
```
<?xml version="1.0" encoding="ISO-8859-1"?><createsshkeypairresponse cloud-stack-version="3.0.0.20120228045507"><keypair><name>keypair-doc</name><fingerprint>f6:77:39:d5:5e:77:02:22:6a:d8:7f:ce:ab:cd:b3:56</fingerprint><privatekey>-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCSydmnQ67jP6lNoXdX3noZjQdrMAWNQZ7y5SrEu4wDxplvhYci
dXYBeZVwakDVsU2MLGl/K+wefwefwefwefwefJyKJaogMKn7BperPD6n1wIDAQAB
AoGAdXaJ7uyZKeRDoy6wA0UmF0kSPbMZCR+UTIHNkS/E0/4U+6lhMokmFSHtu
mfDZ1kGGDYhMsdytjDBztljawfawfeawefawfawfawQQDCjEsoRdgkduTy
QpbSGDIa11Jsc+XNDx2fgRinDsxXI/zJYXTKRhSl/LIPHBw/brW8vzxhOlSOrwm7
VvemkkgpAkEAwSeEw394LYZiEVv395ar9MLRVTVLwpo54jC4tsOxQCBlloocK
lYaocpk0yBqqOUSBawfIiDCuLXSdvBo1Xz5ICTM19vgvEp/+kMuECQBzm
nVo8b2Gvyagqt/KEQo8wzH2THghZ1qQ1QRhIeJG2aissEacF6bGB2oZ7Igim5L14
4KR7OeEToyCLC2k+02UCQQCrniSnWKtDVoVqeK/zbB32JhW3Wullv5p5zUEcd
KfEEuzcCUIxtJYTahJ1pvlFkQ8anpuxjSEDp8x/18bq3
-----END RSA PRIVATE KEY-----
</privatekey></keypair></createsshkeypairresponse>
```

2. 키 데이터를 파일로 복사하십시오. 파일은 다음과 같습니다.
```
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCSydmnQ67jP6lNoXdX3noZjQdrMAWNQZ7y5SrEu4wDxplvhYci
dXYBeZVwakDVsU2MLGl/K+wefwefwefwefwefJyKJaogMKn7BperPD6n1wIDAQAB
AoGAdXaJ7uyZKeRDoy6wA0UmF0kSPbMZCR+UTIHNkS/E0/4U+6lhMokmFSHtu
mfDZ1kGGDYhMsdytjDBztljawfawfeawefawfawfawQQDCjEsoRdgkduTy
QpbSGDIa11Jsc+XNDx2fgRinDsxXI/zJYXTKRhSl/LIPHBw/brW8vzxhOlSOrwm7
VvemkkgpAkEAwSeEw394LYZiEVv395ar9MLRVTVLwpo54jC4tsOxQCBlloocK
lYaocpk0yBqqOUSBawfIiDCuLXSdvBo1Xz5ICTM19vgvEp/+kMuECQBzm
nVo8b2Gvyagqt/KEQo8wzH2THghZ1qQ1QRhIeJG2aissEacF6bGB2oZ7Igim5L14
4KR7OeEToyCLC2k+02UCQQCrniSnWKtDVoVqeK/zbB32JhW3Wullv5p5zUEcd
KfEEuzcCUIxtJYTahJ1pvlFkQ8anpuxjSEDp8x/18bq3
-----END RSA PRIVATE KEY-----
```

3. 파일을 저장하십시오.

<H3>인스턴스 생성</H3>
SSH 키 쌍 파일을 저장한 후 “SSH 키를 지원하는 인스턴스 템플릿 생성"에서 생성한 템플릿을 사용하여 인스턴스를 생성해야합니다. “SSH 키 쌍 생성"에서 생성한 것과 동일한 SSH 키 이름을 사용해야 합니다.

!!! note
    현재 GUI를 사용하여 인스턴스를 생성하고 인스턴스를 새로 생성된 SSH 키 쌍과 연결할 수 없습니다.

새 인스턴스를 만드는 샘플 curl 명령은 다음과 같습니다.
```
curl --globoff http://localhost:<포트 번호>/?command=deployVirtualMachine&zoneId=1&serviceOfferingId=18727021-7556-4110-9322-d625b52e0813&templateId=e899c18a-ce13-4bbf-98a9-625c5026e0b5&securitygroupids=ff03f02f-9e3b-48f02f-9e3b-48f02f91b822da40c5&account=admin&domainid=1&keypair=keypair-doc
```

클라우드 환경에 있는 템플릿, 서비스 제공 및 보안 그룹 ID (보안 그룹 기능을 사용하는 경우)를 대체합니다.

<H3>SSH 키 쌍을 사용하여 로그인</H3>
SSH 키 생성이 성공했는지 테스트하려면 클라우드 설정에 로그인할 수 있는지 확인하십시오.

예를 들어 Linux OS에서 다음을 실행합니다.

```
ssh -i ~/.ssh/keypair-doc<ip address>
```

-i 매개 변수는 ~/.ssh/keypair-doc에 있는 ssh 키를 사용하도록 ssh 클라이언트에 지시합니다.

<H3>SSH 키 재설정</H3>
API 명령 resetSSHKeyForVirtualMachine을 사용하여 사용자는 가상 머신에 할당된 SSH 키 쌍을 설정하거나 재설정할 수 있습니다. 손실되거나 손상된 SSH 키 쌍을 변경할 수 있으며 사용자는 새 키 쌍을 사용하여 VM에 액세스할 수 있습니다. 새 키 쌍을 만들거나 등록한 다음 resetSSHKeyForVirtualMachine을 호출하면 됩니다.

<H3>사용자 데이터 및 메타 데이터</H3>
Mold는 배포된 VM에 최대 32KB의 사용자 데이터를 연결할 수 있는 API를 제공합니다.

사용자 데이터를 저장하는 데 사용할 수 있는 두 가지 Mold API가 있습니다. deployVirtualMachine 및 updateVirtualMachine 둘 다 매개 변수를 지원합니다 ``userdata=``. 이 매개 변수의 값은 base64로 인코딩된 다중 파트 MIME 메시지 여야합니다. 이것이 어떻게 생겼는지에 대한 예는 아래를 더 참조하십시오.

HTTP GET 매개 변수의 길이는 2048 바이트로 제한되지만, 더 큰 사용자 데이터 Blob을 GET 대신 HTTP POST를 통해 본문에 전송하여 저장할 수 있습니다.

네트워크 오퍼링에서 UserData 서비스가 활성화된 경우 VM 내부에서 가상 라우터를 통해 사용자 데이터에 액세스할 수 있습니다.

가상 라우터의 DNS 서비스를 사용하는 경우 data-server라는 특수 호스트 이름입니다. 유효한 사용자 데이터 서버를 가리킬 것입니다.

그렇지 않으면 DHCP 임대와 같은 다른 방법을 통해 가상 라우터 주소를 결정해야 합니다. VM에 연결된 여러 네트워크가 있는 경우 모든 라우터에 UserData 서비스가 활성화되어 있지 않은 경우에는 모든 라우터를 검사해야 합니다.

사용자 데이터는 URL에서 사용할 ``http://data-server./latest/user-data`` 수 있으며 curl 또는 기타 HTTP 클라이언트를 통해 가져올 수 있습니다.

URL을 통해 동일한 서비스에서 VM 메타 데이터를 가져올 수도 있습니다. 이전 버전과의 호환성을 위해 이전 URL 도 지원됩니다. ``http://data-server./latest/{metadata type}`` ``http://data-server./latest/{metadata type}``

메타 데이터 유형의 경우 다음 중 하나를 사용하십시오.

* ``service-offering``. VM 서비스 제공에 대한 설명
* ``availability-zone``. Zone 이름
* ``local-ipv4``. VM의 게스트 IP
* ``local-hostname``. VM의 호스트 이름
* ``public-ipv4``. 라우터의 첫 번째 공용 IP입니다.
* ``public-hostname``. public-ipv4와 동일합니다.
* ``instance-id``. VM의 인스턴스 이름

<H4>DNS없이 가상 라우터 주소 확인</H4>
가상 라우터의 DNS 서비스를 사용할 수 없거나 사용하지 않으려는 경우 DHCP 임대에서 사용자 데이터 서버를 확인할 수도 있습니다.

1. 다음 명령을 실행하여 가상 라우터를 찾습니다.
```
# cat /var/lib/dhcp/dhclient.eth0.leases | grep dhcp-server-identifier | tail -1
```

2. IP를 통해 데이터 서버에 액세스
```
# curl http://10.1.1.1/latest/user-data
```

<H4>API를 통해 사용자 데이터 가져오기</H4>
사용자 데이터는 기록적인 이유로 일반 VM 상태에 포함되지 않습니다. API를 통해 base64로 인코딩된 사용자 데이터를 읽으려면 getVirtualMachineUserData API 호출을 사용하세요.
```
cmk get virtualmachineuserdata virtualmachineid=8fd996b6-a102-11ea-ba47-23394b299ae9
```

<H4>cloud-init 사용</H4>
cloud-init 는 가상 머신 내부의 사용자 데이터에 액세스하고 해석하는 데 사용할 수 있습니다. cloud-init를 VM 템플릿에 설치하면 각각의 새 VM 배포에 SSH 키와 사용자 암호를 자동으로 저장할 수 있습니다 ( 템플릿에 암호 관리 추가 및 ssh 키 사용 ).

1. VM 템플릿에 cloud-init 패키지를 설치합니다.
```
# dnf install cloud-init
  or
$ sudo apt-get install cloud-init
```

2. VM 템플릿에서 데이터 소스 구성 파일을 만듭니다. ``/etc/cloud/cloud.cfg.d/99_cloudstack.cfg``
```
datasource:
  CloudStack: {}
  None: {}
datasource_list:
  - CloudStack
```

<H4>사용자 지정 사용자 데이터 예</H4>
이 예제에서는 cloud-init를 사용하여 처음 시작할 때 모든 OS 패키지를 자동으로 업데이트합니다.

1. 다중 부분 MIME 메시지로 래핑되고 base64로 인코딩된 사용자 데이터를 만듭니다.
```
base64 <<EOF
Content-Type: multipart/mixed; boundary="//"
MIME-Version: 1.0

--//
Content-Type: text/cloud-config; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="cloud-config.txt"

#cloud-config

# Upgrade the instance on first boot
# (ie run apt-get upgrade)
#
# Default: false
# Aliases: apt_upgrade
package_upgrade: true
EOF
```

2. 이 사용자 데이터로 VM을 배포합니다.
```
cmk deploy virtualmachine name=..... userdata=Q29udGVudC1UeXBlOiBtdWx0aXBhcnQvbWl4ZWQ7IGJvdW5kYXJ5PSIvLyIKTUlNRS1WZXJzaW9uOiAxLjAKCi0tLy8KQ29udGVudC1UeXBlOiB0ZXh0L2Nsb3VkLWNvbmZpZzsgY2hhcnNldD0idXMtYXNjaWkiCk1JTUUtVmVyc2lvbjogMS4wCkNvbnRlbnQtVHJhbnNmZXItRW5jb2Rpbmc6IDdiaXQKQ29udGVudC1EaXNwb3NpdGlvbjogYXR0YWNobWVudDsgZmlsZW5hbWU9ImNsb3VkLWNvbmZpZy50eHQiCgojY2xvdWQtY29uZmlnCgojIFVwZ3JhZGUgdGhlIGluc3RhbmNlIG9uIGZpcnN0IGJvb3QKIyAoaWUgcnVuIGFwdC1nZXQgdXBncmFkZSkKIwojIERlZmF1bHQ6IGZhbHNlCiMgQWxpYXNlczogYXB0X3VwZ3JhZGUKcGFja2FnZV91cGdyYWRlOiB0cnVlCg==
```

## 게스트 VM에 GPU / vGPU 할당
Mold는 XenServer 호스트에서 GPU(그래픽 처리 장치) 또는 vGPU(가상 그래픽 처리 장치) 기능이 있는 게스트 VM을 배포할 수 있습니다. VM 배포 시 또는 이후 단계에서 서비스 제공을 변경하여 물리적 GPU (GPU 통과라고 함) 또는 물리적 GPU 카드 (vGPU)의 일부를 게스트 VM에 할당할 수 있습니다. 이 기능을 통해 Mold에서 실행되는 VM은 GPU/vGPU의 높은 계산 능력을 통해 집약적인 그래픽 처리 요구 사항을 충족하며 Mold 사용자는 Auto-CAD와 같은 멀티미디어가 풍부한 응용 프로그램을 실행할 수 있습니다. Mold는 NVIDIA GRID Kepler 1 및 2 시리즈에 대한 XenServer 지원을 활용하여 GPU/vGPU 지원 VM을 실행합니다. NVIDIA GRID 카드를 사용하면 각 VM에 대해 vGPU를 생성하여 여러 VM간에 단일 GPU 카드를 공유할 수 있습니다. vGPU 기술을 사용하면 각 VM의 그래픽 명령이 하이퍼바이저의 개입 없이 기본 전용 GPU로 직접 전달됩니다. 이를 통해 GPU 하드웨어를 시간 분할하고 여러 VM에서 공유할 수 있습니다. XenServer 호스트는 다음과 같은 방식으로 GPU 카드를 사용합니다.

GPU 패스 스루 : GPU 패스 스루는 VM에 직접 할당할 수 있는 물리적 GPU를 나타냅니다. GPU 패스 스루는 GRID vGPU와 함께 하이퍼바이저에서 사용할 수 있지만 몇 가지 제한이 있습니다. GRID 물리적 GPU는 GRID vGPU를 호스팅하거나 패스 스루로 사용할 수 있지만 동시에 둘 다 사용할 수는 없습니다.

GRID vGPU : GRID vGPU를 사용하면 여러 VM이 단일 물리적 GPU를 공유할 수 있습니다. VM은 NVIDIA 드라이버 스택을 실행하고 GPU에 직접 액세스합니다. GRID 물리적 GPU는 게스트 VM에 직접 할당할 수 있는 여러 vGPU (가상 GPU 장치)를 지원할 수 있습니다. 게스트 VM은 하이퍼바이저가 통과한 물리적 GPU와 동일한 방식으로 GRID 가상 GPU를 사용합니다. 게스트 VM에 로드된 NVIDIA 드라이버는 성능에 중요한 빠른 경로를 위해 GPU에 직접 액세스하고 비 성능 관리 작업에 사용되는 GRID Virtual GPU Manager. XenServer 용 NVIDIA GRID 가상 GPU 관리자는 dom0에서 실행됩니다. Mold는 다음과 같은 기능을 제공합니다.

* 관리자가 프로비저닝한 GPU/vGPU 기능이 있는 XenServer 호스트 추가.
* GPU/vGPU 기능이 있는 컴퓨트 오퍼링 생성.
* GPU/vGPU 기능이 있는 VM 배포.
* GPU/vGPU 기능이 있는 VM 삭제.
* 사용자가 서비스 제공을 변경하거나 그 반대로 GPU/vGPU 지원 없이 VM에 GPU/vGPU 지원을 추가할 수 있습니다.
* GPU/vGPU 기능으로 VM 마이그레이션 (콜드 마이그레이션).
* GPU 카드 용량 관리.
* GPU 카드, GRID 카드의 경우 지원되는 vGPU 유형 및 카드 용량에 대한 정보를 얻기 위해 호스트를 쿼리합니다.

<H3>전제 조건 및 시스템 요구 사항</H3>
계속하기 전에 다음 전제 조건이 있는지 확인하십시오.

* vGPU 지원 XenServer 6.2 이상 버전. 자세한 내용은 Citrix 3D Graphics Pack을 참조하십시오.
* GPU/vPGU 기능은 다음 HVM 게스트 운영 체제에서 지원됩니다. 자세한 내용은 Citrix 3D Graphics Pack을 참조하십시오.
* Windows 7 (x86 및 x64)
* 윈도우 서버 2008 R2
* 윈도우 서버 2012
* Windows 8 (x86 및 x64)
* Windows 8.1 ( "Blue") (x86 및 x64)
* Windows Server 2012 R2 (“Blue"에 해당하는 서버)
* Mold는 GPU/vGPU 기능을 위해 XenServer에서 지원하지 않는 게스트 OS 유형이 있는 GPU 지원 VM의 배포를 제한하지 않습니다. 배포가 성공하고 GPU/vGPU도 VM에 할당됩니다. 그러나 게스트 OS 드라이버가 누락되어 VM은 GPU 리소스를 활용할 수 없습니다. 따라서 지원되는 게스트 OS에서만 GPU 지원 서비스를 사용하는 것이 좋습니다.
* NVIDIA GRID K1 (16GiB 비디오 RAM) 및 K2 (8GiB 비디오 RAM) 카드는 동종 가상 GPU를 지원하며, 이는 주어진 시간에 단일 물리적 GPU에 상주하는 vGPU가 모두 동일한 유형이어야 함을 의미합니다. 그러나 이 제한은 동일한 카드의 물리적 GPU로 확장되지 않습니다. K1 또는 K2의 각 물리적 GPU는 동시에 서로 다른 유형의 가상 GPU를 호스팅할 수 있습니다. 예를 들어, GRID K2 카드에는 2 개의 물리적 GPU가 있으며 4 가지 유형의 가상 GPU를 지원합니다. GRID K200, GRID K220Q, GRID K240Q 및 GRID K260Q.
* 물리적 NVIDIA GPU와 마찬가지로 vGPU 작동을 활성화하려면 NVIDIA 드라이버를 설치해야 합니다.
* XenServer 도구는 사용 중인 vGPU 유형과 관계없이 XenServer에서 최대 성능을 얻기 위해 VM에 설치됩니다. XenServer 도구가 제공하는 최적화된 네트워킹 및 스토리지 드라이버가 없으면 GRID vGPU에서 실행되는 원격 그래픽 응용 프로그램이 최대 성능을 제공하지 못합니다.
* vGPU의 여러 헤드에서 하이 프레임을 제공하려면 HDX 3D Pro 원격 그래픽과 함께 XenDesktop을 설치하십시오.

구성을 계속하기 전에 다음을 고려하십시오.

* VM 배포 GPU/vGPU 기능은 호스트에 GPU 용량이 충분하지 않은 경우 지원되지 않습니다.
* Mold UI에서 지원하지 않는 GPU 값으로는 서비스 오퍼링을 생성할 수 없습니다. 그러나 이를 위해 API를 호출할 수 있습니다.
* 동적 확장은 지원되지 않습니다. 그러나 GPU 지원 없이 VM을 배포하도록 선택할 수 있으며 나중에 vGPU를 사용하는 시스템으로 업그레이드하도록 시스템 제품을 변경할 수 있습니다. 오프라인 업그레이드로 이를 달성할 수 있습니다. VM을 중지하고 서비스 제공을 vGPU가 있는 서비스로 업그레이드한 다음 VM을 시작합니다.
* GPU/vGPU 지원 VM의 실시간 마이그레이션은 지원되지 않습니다.
* 계정/도메인당 GPU 리소스 제한은 지원되지 않습니다.
* 클러스터 수준에서 GPU 비활성화는 지원되지 않습니다.
* GPU 리소스에 대한 알림 임계 값은 지원되지 않습니다.

<H3>지원되는 GPU 장치</H3>
|<center>장치</center>|<center>유형</center>|
|:---|:---|
|GPU|* NVIDIA Corporation GK107GL [GRID K1] GPU Group</br>* NVIDIA Corporation GK104GL [GRID K2] GPU Group<br/>* 다른 GPU Group|
|vGPU|* GRID K100<br/>* GRID K120Q<br/>* GRID K140Q<br/>* GRID K200<br/>* GRID K220Q<br/>* GRID K240Q<br/>* GRID K260Q|

<H3>GPU/vGPU 할당 워크 플로</H3>
Mold는 아래 작업 순서에 따라 VM에 대한 GPU/vGPU 지원을 제공합니다.

1. XenServer 호스트가 GPU가 설치 및 구성된 상태로 준비되었는지 확인합니다. 자세한 내용은 Citrix 3D Graphics Pack을 참조하십시오.
2. Mold에 호스트를 추가합니다. Mold는 호스트가 GPU를 지원하는지 여부를 확인합니다. Mold는 호스트를 쿼리하고 GPU가 활성화되었는지 감지합니다.
3. GPU/vGPU 지원으로 컴퓨팅 제품 생성 : 자세한 내용은 새 컴퓨팅 제품 생성을 참조하십시오.
4. 다음 작업 중 하나를 계속합니다.

    * VM을 배포합니다.<br/>적절한 서비스 제공을 선택하여 GPU / vGPU를 지원하는 VM을 배포합니다. Mold는 다음 기준에 따라 VM 배포를 위해 선택할 호스트를 결정합니다.
        * 호스트에는 GPU 카드가 있습니다. vGPU의 경우 Mold는 카드에 필요한 vGPU 유형 지원과 사용 가능한 충분한 용량이 있는지 확인합니다. 적절한 호스트가 없으면 InsufficientServerCapacity 예외가 발생합니다.
        * 또는 GPU 지원 없이 VM을 배포하도록 선택할 수 있으며 나중에 시스템 제품을 변경할 수 있습니다. 오프라인 업그레이드로 이를 달성할 수 있습니다. VM을 중지하고 서비스 제공을 vGPU가 있는 서비스로 업그레이드한 다음 VM을 시작합니다. 이 경우 Mold는 VM을 호스팅하기에 충분한 용량이 있는 호스트 목록을 가져옵니다. GPU 지원 호스트가 있는 경우 Mold는 이 호스트 목록을 재정렬하고 GPU 지원 호스트를 목록 맨 아래에 배치합니다.
    
    * VM을 마이그레이션합니다.<br/>Mold는 GPU 요구 사항을 충족하는 VM 마이그레이션에 사용할 수 있는 호스트를 검색합니다. 호스트를 사용할 수 있는 경우 현재 호스트에서 VM을 중지하고 VM 마이그레이션 작업을 수행합니다. VM 마이그레이션이 성공하면 나머지 GPU 용량이 그에 따라 두 호스트 모두에 대해 업데이트됩니다.

    * VM을 제거합니다.<br/>VM을 중지하면 GPU 리소스가 자동으로 해제됩니다. VM 제거가 성공하면 Mold는 호스트에 리소스를 호출하여 카드의 남은 GPU 용량을 가져오고 그에 따라 데이터베이스를 업데이트합니다.