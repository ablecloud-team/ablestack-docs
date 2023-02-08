본 문서에서는 ABLESTACK OO를 이용해 "OOOOOOOOO"를 구성하는 방법에 대해 설명합니다. 
이를 위해 OOOOO를 구성하고 OOOOOO 구성에 필요한 OOO를 적용해아합니다.

## 아키텍처
다음 그림은 앞으로 구성할 OOOOOOO 구조 전체를 보여줍니다.
아래 예시를 적용한 아키텍처 구성도를 참고하여 구성합니다.

<figure markdown>
!![3tier-linux-01](/assets/images/3tier-linux-architecture.png)
<figcaption>3tier-linux-01</figcaption>
</figure>


## 구성 정보
구성에 필요한 네트워크 및 가상머신 정보 예시는 다음과 같습니다.

### 네트워크 구성 정보
- VPC
    - CIDR: 192.168.0.0/16
- Subnet
    - DB
        - CIDR: 192.168.3.0/16
        - 게이트웨이: 192.168.3.1
    - WAS
        - CIDR: 192.168.2.0/16
        - 게이트웨이: 192.168.2.1
    - WEB
        - CIDR: 192.168.1.0/16
        - 게이트웨이: 192.168.1.1
- LB 
    - DB
        - Public IP: 10.10.1.80:3306
    - WAS
        - Public IP: 10.10.1.70:5000
    - WEB
        - Public IP: 10.10.1.60:6060
- 관리용 네트워크
    - Public IP: 10.10.1.90:3306

### 가상머신 구성 정보

|           | IP                | Offering                  |
| ----------| ------------------| --------------------------|
| DB        | 192.168.3.11 ~ 13 | 1Core 2GB, 100GB DataDisk |
| WAS       | 192.168.2.11 ~ 13 | 1Core 2GB, 100GB DataDisk |
| WEB       | 192.168.1.11 ~ 13 | 1Core 2GB, 100GB DataDisk |
| 관리용 가상머신 | 192.168.1.11 ~ 13 | 1Core 2GB, 100GB DataDisk |


## 구성 단계
"OOOOOO"를 구성하는 단계는 다음과 같습니다.

- OOO: OOO를 생성하고 OOO을 생성합니다.
- OOO 생성: OOO을 구성하는 가상머신으로 OOO을 생성합니다.
- OOO 구성: OOO를 활용하여 OOO를 구성합니다.
- OOO 구성: OOO를 이용하여 OOO를 활용한 OOO를 구성합니다.