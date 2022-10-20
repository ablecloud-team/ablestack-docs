ABLESTACK은 HCI 소프트웨어 스택을 상용 x86 서버에 설치하여 구성합니다. 상용 x86 서버를 지원하기 때문에 서버에 장착되는 다양한 하드웨어에 대한 폭넓은 유연성을 갖고 있습니다. ABLESTACK HCI 서버는 사용 목적이나 규모에 따라 다음과 같이 나눌 수 있습니다. 

- Entry Level : 호스트당 10대 이내의 가상머신 실행, 일반 웹서버 등의 단순 애플리케이션을 실행하기 위한 워크로드용
- Standard Level : 호스트당 20대 이내의 가상머신 실행, 일반적인 데스크탑 가상화, ERP 등의 기업 애플리케이션 실행을 위한 워크로드용
- Professional Level : 호스트당 21대 이상의 대량 가상머신 실행, 고성능 데스크탑 가상화, 빅데이터 및 AI 등의 이머징 워크로드용

!!! info "호스트당 가상머신 산정 단위"
    호스트에서 실행되는 가상머신은 2 vCore, 8GB Memory를 가진 가상머신을 단위로 합니다. 사용자가 생성하는 가상머신의 크기에 따라 각 레벨의 서버가 생성할 수 있는 가상머신의 수에는 제약이 있을 수 있습니다. 

서버의 레벨에 따라 서버의 CPU, Memory, Disk, NIC의 최소 구성요건이 다르며 다음과 같습니다. 

## CPU 구성

CPU는 ABLESTACK Cube OS, Glue VM Appliance, 사용자 가상머신의 연산을 수행하는 가장 중요한 구성요소입니다. ABLESTACK HCI로 서버가 사용되기 위해서는 AMD64 타입의 CPU 여야 합니다. 그 외의 CPU 구성은 서버의 레벨에 따라 다음의 최소 요건을 만족해야 합니다. 

- Entry Level : 12 Core, 1 CPU 이상 (물리 12Core, 논리 24Core)
- Standard Level : 10 Core, 2 CPU 이상 (물리 20Core, 논리 40Core)
- Professional Level : 18 Core, 2 CPU 이상 (물리 32Core, 논리 64Core)

!!! tip "기존 서버를 HCI로 전환할 때의 적정한 CPU 용량 산정에 대한 팁"
    일반적으로 물리적인 서버의 CPU 사용량은 평상시에 20%를 넘지 않는 경우가 대부분입니다. 이러한 자원의 낭비를 줄이고 효율적으로 자원을 분할하여 사용하도록 하는 기술이 바로 가상화입니다. 하지만 가상화를 해서 서버를 생성하여 운영하는 경우에도 실제 CPU 사용량을 측정해 보면 웹 서버의 경우 20%를 넘지 않는 경우가 대부분입니다.  
    실제 환경에서 물리적인 서버를 기준으로 산정된 용량을 HCI 환경에 맞게 CPU를 산정하는 경우 물리 환경에서 사용하는 CPU의 1/4 ~ 1/2 수준으로 용량을 산정하는 것을 권장합니다. 예를 들어 8 Core로 운영되는 물리 서버의 경우 2Core에서 4Core로 CPU를 산정합니다. 

## 메모리 구성

메모리는 Cube OS, Glue VM, 사용자 가상머신의 데이터 처리를 위한 구성요소입니다. 최신의 ECC Memory를 사용해야 합니다. 구성은 서버의 레벨에 따라 다음의 최소 요건을 만족해야 합니다. 

- Entry Level : 128GB 이상 (Usable 96GB 이상)
- Standard Level : 256GB 이상 (Usable 208GB 이상)
- Professional Level : 512GB 이상 (Usable 432GB 이상)

!!! tip "Usable Memory 산정에 대한 팁"
    ABLESTACK Host에는 기본적으로 운영체제인 Cube OS와 스토리지컨트롤러인 Glue VM이 실행됩니다. 운영체제는 최소 8GB ~ 최대 32GB까지의 메모리를 사용하며, Glue VM은 최소 8GB ~ 최대 64GB의 메모리를 사용합니다. 메모리 사용량은 사용하고 있는 디스크의 크기 및 IO의 처리량에 따라 달라집니다. 

## 디스크 구성

호스트의 디스크는 OS 및 Glue VM의 ROOT 디스크를 위해 사용되는 공간과, Glue 스토리지가 사용하는 디스크 공간으로 나눠서 구성되야 합니다. 워크로드에 따라 OS용 디스크에 고속의 로컬 캐시 디스크를 구성할 수 있고, Glue 스토리지가 사용하는 디스크의 경우에도 워크로드에 따라 다르게 구성할 수 있습니다. 

호스트의 워크로드 레벨별로 권장하는 디스크 구성은 다음과 같습니다. 

- Entry Level : 1개의 RAID 카드로 OS 및 Storage를 모두 구성, 낮은 IO 처리량
    - Cube OS Disk : RAID1 또는 RAID5, SATA SSD Usable 300GB 이상 (로컬 캐시는 100GB 이내에서 사용)
    - Glue Storage Disk
        - SSD 구성 : JBOD 또는 non-RAID, SATA SSD 물리용량 6TB 이내
        - 하이브리드 구성 : JBOD 또는 non-RAID, SATA SSD 1TB 이하 1EA, SAS 10K HDD 물리용량 6TB 이내 
- Standard Level : RAID와 독립적인 OS 디스크, 독립적인 로컬 Cache Disk, Glue용 Disk 전용으로 RAID Card 사용
    - Cube OS Disk : RAID1 M.2 SSD Usable 300GB 이상
    - Local Cache Disk : NVMe PCI Usable 400GB 이상
    - Glue Storage Disk : JBOD 또는 non-RAID, SAS SSD 물리용량 30TB 이하
- Professional Level : RAID와 독립적인 OS 디스크, 독립적인 초고속 DAX Cache Disk, Glue용 Disk 전용으로 RAID Card 사용
    - Cube OS Disk : RAID1 M.2 SSD Usable 400GB 이상
    - Local Cache Disk : Persistent Memory 512GB 이상
    - Glue Storage Disk : JBOD 또는 non-RAID, SAS SSD 물리용량 최대 60TB

!!! tip "Local Cache Disk 구성 팁"
    ABLESTACK Glue 스토리지는 호스트의 디스크를 클러스터링하여 대용량 스토리지를 제공합니다. 이 때 IO의 발생을 가상머신이 실행 중인 호스트에서 발생하도록 하여 성능을 높이는 기술을 Host Side Cache 또는 Data Locality라고 합니다. Entry Level에서는 이러한 로컬 캐시를 OS 디스크의 일부를 할당하여 사용합니다. 따라서 높은 성능을 필요로 하는 경우 OS 디스크의 성능을 반드시 고려해야 합니다.    
    고성능에 가장 좋은 대안은 독립적인 로컬 캐시 디스크를 구성하는 것입니다. 일반적으로는 NVMe 디스크를 이용하는 것으로 충분합니다. 만약 빅데이터분석, AI, 대규모 VDI, 인메모리 DB 등을 사용할 때는 PMem을 구성하는 것이 좋고, 인메모리 DB를 위한 추가적인 용량을 고려해야 합니다. 
## NIC 구성

HCI용 호스트를 구성할 때, IO 성능을 높이고, 안정성을 보장하는데 가장 중요한 요소는 네트워크 인터페이스입니다. 네트워크 인터페이스는 크게 관리용 NIC, Guest NIC, 스토리지 NIC로 나눌 수 있습니다. 모든 인터페이스는 Bonding을 통해 NIC 또는 스위치 일부가 장애가 발생하는 경우에도 Failover 되도록 구성해야 합니다. 호스트의 성늘 레벨에 따라 다음과 같은 구성을 권장합니다. 

- Entry Level : 관리용 NIC, Guest NIC는 1Gb OnBoard NIC 사용, 스토리지 NIC를 별도로 구성
    - 관리용 NIC : Onboard 1GbE 2Port
    - Guest NIC : Onboard 1GbE 2Port
    - Storage NIC : 10Gb SFP+ 4Port 1EA, 또는 2Port 2EA 
- Standard Level : 관리용 NIC는 OnBoard NIC 사용, Guest/스토리지 NIC를 별도로 구성
    - 관리용 NIC : Onboard 1GbE 2Port
    - Guest NIC : 10Gb SFP+ 2Port 2EA
    - 스토리지 NIC : 10Gb SFP+ 2Port 2EA
- Professional Level : 관리용 NIC는 OnBoard NIC 사용, Guest/스토리지 NIC를 별도로 구성
    - 관리용 NIC : Onboard 1GbE 2Port
    - Guest NIC : 10Gb SFP+ 2Port 2EA
    - 스토리지 NIC : 10Gb SFP+ 2Port 2EA

!!! info "스토리지 트래픽의 분리를 통한 성능 극대화"
    ABLESTACK은 Glue의 성능을 극대화 하기 위해 트래픽을 분리하여 구성하는 것을 권장합니다. ABLESTACK에서 발생하는 스토리지 트래픽을 크게 3가지 입니다.  

    - 첫번째는 스토리지 클라이언트 트래픽입니다. 호스트가 스토리지에 연결해서 데이터를 전송할 때 발생합니다.  
    - 두번째는 스토리지 서버 트래픽입니다. 스토리지에서 발생한 IO를 처리하고, 데이터를 분산하여 저장할 때 발생합니다.  
    - 세번째는 스토리지 복제/복구 트래픽입니다. 스토리지에서 발생한 IO에 대한 복제본을 만들어 전송하거나, 장애가 발생했을 때 자동 복구 작업 시 발생합니다. 

    위 모든 트래픽을 물리적으로 분리할 때 가장 좋은 성능이 보장됩니다.

!!! warning "장애 상황을 고려한 NIC 구성"
    장애가 발생했을 때 네트워크 흐름에 대한 Fail Over를 고려하여 구성하고자 하는 경우 반드시 하나의 포트를 물리적으로 분리해서 구성해야 합니다.  

    예를 들어 Guest NIC를 구성할 때 물리적으로 동일한 NIC의 두개의 Port를 사용하는 경우 스위치 장애는 극복할 수 있으나 NIC 장애가 발생하면 트래픽이 중단되는 심각한 장애가 발생할 수 있습니다. 
    이 예제에서 스위치 및 포트 장애 모두를 처리하기 위해서는 Guest NIC Port를 서로 분리된 물리적 NIC 포트를 사용하도록 구성하는 것이 가장 좋은 방법입니다. 

## 기타 하드웨어

### 원격관리도구

ABLESTACK을 설치하기 위한 호스트 서버에는 반드시 원격 관리를 위한 도구가 설치되어 있어야 합니다. 상용 서버의 벤더에 따라 원격 관리 도구는 별도의 라이선스를 구입해야 하는 경우가 있습니다. IPMI 및 원격 전원관리, 시스템 콘솔 연결 등을 위해 반드시 필요한 기능이기 때문에 해당 기능의 활성화 여부를 반드시 확인해야 합니다. 

또한 원격 관리도구 연결을 위한 Mgmt Port가 별도로 구성되어 있어야 합니다. 

### GPU

GPU는 최근 고성능 데스트톱 가상화, 빅데이터 분석 및 AI 등의 워크로드 가속화를 위해 가장 주목 받고 있는 장치입니다. ABLESTACK은 GPU를 다음의 목적에 따라 구분하여 GPU를 장착하여 사용할 수 있습니다. 

- GPU Passthrough : 서버에 장착된 GPU 전체를 특정 가상머신에 할당하는 방법입니다. 단일 GPU를 사용하거나 특정한 가상머신에만 GPU가 필요한 경우 유용합니다. 일반적으로 가상머신의 운영체제와 호환되는 벤더의 GPU를 모두 사용할 수 있습니다. 
- vGPU : 서버에 장착된 GPU를 가상으로 분할하여 가상머신에 할당하는 방법입니다. ABLESTACK은 NVIDIA Grid GPU, 예를 들어 V100, T4 등의 Grid GPU를 모두 지원합니다. 