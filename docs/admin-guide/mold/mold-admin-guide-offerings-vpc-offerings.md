
# VPC 오퍼링
!!! danger
    해당 목록은 기본적으로 제공되는 VPC 오퍼링 목록입니다.

    삭제하면 시스템 운영에 문제가 발생할 수 있으므로 절대 삭제하지 마세요.

## 개요
VPC 오퍼링은 가상 사설 클라우드(Virtual Private Cloud, VPC)의 네트워크 기능과 정책을 정의하는 설정입니다.
VPC는 여러 개의 네트워크를 하나의 논리적 그룹으로 묶어 격리된 환경을 제공하며, 다양한 구성 요소를 포함할 수 있습니다.

VPC 오퍼링을 통해 지원하는 네트워크 서비스(라우팅, 방화벽, 로드밸런서, DHCP 등)를 지정할 수 있습니다.
각 VPC는 하나 이상의 티어(Tier)를 가질 수 있으며, 티어 간 트래픽 흐름을 제어할 수 있습니다.

보안 그룹과 ACL(Access Control List)을 사용하여 트래픽을 필터링하고, 네트워크 접근을 세밀하게 설정할 수 있습니다.
VPC 오퍼링은 퍼블릭 게이트웨이와 NAT(Network Address Translation) 기능을 지원하여 외부 네트워크와 연결할 수 있습니다.
환경에 따라 기본 제공되는 VPC 오퍼링을 사용할 수도 있고, 필요에 맞게 새로운 오퍼링을 생성할 수도 있습니다.

잘못된 설정은 네트워크 장애를 초래할 수 있으므로, VPC의 구조와 정책을 충분히 고려한 후 설정해야 합니다.
VPC 오퍼링을 적절히 활용하면 클라우드 환경에서 안전하고 유연한 네트워크 구성이 가능합니다.
기업 또는 프로젝트별로 독립적인 네트워크를 운영하고, 보안과 성능을 최적화하는 데 도움을 줍니다.

## VPC 오퍼링 목록 조회
1. 모든 VPC 오퍼링의 목록을 확인하는 화면입니다. 생성된 VPC 오퍼링 목록을 확인하거나 VPC 오퍼링 추가 버튼을 클릭하여 VPC 오퍼링을 추가하실 수 있습니다.
    ![VPC 오퍼링 목록 조회](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-dashboard.png){ .imgCenter .imgBorder }


## VPC 오퍼링 추가
1. 서비스 오퍼링의 VPC 오퍼링에서 상단의 VPC 오퍼링 추가 버튼을 클릭합니다.
    ![VPC 오퍼링 추가 버튼](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-add-01.png){ .imgCenter .imgBorder }
2. VPC 오퍼링 추가 버튼을 클릭한 화면입니다.
    ![VPC 오퍼링 추가1](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-add-02.png){ .imgCenter .imgBorder }
    - **이름** 을 입력합니다.
    - **설명** 을 입력합니다.
    - **NSX** 를 활성화 및 비활성화합니다.
    - **네트워크 모드** 를 선택합니다.
    - **지원되는 서비스** 를 선택합니다.
    ![VPC 오퍼링 추가2](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-add-03.png){ .imgCenter .imgBorder }
    - **컴퓨트 오퍼링** 을 선택합니다.
    - **공개** 를 활성화 및 비활성화합니다.
    - **Zone** 을 활성화 및 비활성화합니다.
    - **VPC 오퍼링 활성화** 를 활성화 및 비활성화합니다.

## 편집
1. VPC 오퍼링 상세 오른쪽 상단의 편집 버튼을 클릭합니다.
    ![편집 버튼](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-update-01.png){ .imgCenter .imgBorder }
2. 편집 버튼을 클릭한 화면입니다.
    ![편집](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-update-02.png){ .imgCenter .imgBorder }
    - **이름** 을 입력합니다.
    - **설명** 을 입력합니다.

## VPC 서비스 오퍼링 비활성화
1. VPC 오퍼링 상세 오른쪽 상단의 VPC 서비스 오퍼링 비활성화 버튼을 클릭합니다.
    ![VPC 오퍼링 비활성화 버튼](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-service-disable-01.png){ .imgCenter .imgBorder }
2. VPC 서비스 오퍼링 비활성화 버튼을 클릭한 화면입니다.
    ![VPC 오퍼링 비활성화](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-service-disable-02.png){ .imgCenter .imgBorder }

## 오퍼링 액세스 업데이트
1. VPC 오퍼링 상세 오른쪽 상단의 오퍼링 액세스 업데이트 버튼을 클릭합니다.
    ![오퍼링 액세스 업데이트 버튼](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-access-update-01.png){ .imgCenter .imgBorder }
2. 오퍼링 액세스 업데이트 버튼을 클릭한 화면입니다.
    ![오퍼링 액세스 업데이트](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-access-update-02.png){ .imgCenter .imgBorder }
    - **Zone** 을 선택합니다.

## VPC 오퍼링 삭제
1. VPC 오퍼링 상세 오른쪽 상단의 VPC 오퍼링 삭제 버튼을 클릭합니다.
    ![VPC 오퍼링 삭제 버튼](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-delete-01.png){ .imgCenter .imgBorder }
2. VPC 오퍼링 삭제 버튼을 클릭한 화면입니다.
    ![VPC 오퍼링 삭제](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-delete-02.png){ .imgCenter .imgBorder }

## VPC 오퍼링 상세 탭
1. VPC 오퍼링 목록 조회에서 확인하고 싶은 VPC 오퍼링 목록을 조회합니다. VPC 오퍼링 대한 상세 정보를 확인하는 화면입니다. 해당 VPC 오퍼링에 대한 이름, 아이디 등 상세 정보를 확인할 수 있습니다.
    ![VPC 오퍼링 상세 탭](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-info.png){ .imgCenter .imgBorder }

## VPC 오퍼링 이벤트 탭
1. VPC 오퍼링 목록 조회에서 확인하고 싶은 VPC 오퍼링 목록을 조회합니다. VPC 오퍼링과 관련된 이벤트 정보를 확인할 수 있는 화면입니다. VPC 오퍼링에서 발생한 다양한 액션과 변경 사항을 쉽게 파악할 수 있습니다.
    ![VPC 오퍼링 이벤트 탭](../../assets/images/admin-guide/mold/offering/vpc/vpc-offering-event.png){ .imgCenter .imgBorder }


## 용어사전
<!-- |  용어명      | 옵션 | 설명                        |
| :---------: | :-: | :----------------------------------: |
| VPC 오퍼링 유형 | 고정 오퍼링 | 사용자가 사용자 정의할 수 없음 |
|  | 사용자 정의 제한 | 사용자가 제공에서 설정한 매개변수 내에서 컴퓨팅을 사용자 정의할 수 있는 자유도 있음 |
|  | 사용자 정의 제한 없음 | 사용자가 원하는 값을 설정할 수 있음 | -->
<table>
  <tr>
    <th>용어명</th>
    <th>옵션</th>
    <th>설명</th>
  </tr>
  <tr>
    <td rowspan="3">VPC 오퍼링 유형</td>
    <td>고정 오퍼링</td>
    <td>사용자가 사용자 정의할 수 없음</td>
  </tr>
  <tr>
    <td>사용자 정의 제한</td>
    <td>사용자가 제공에서 설정한 매개변수 내에서 컴퓨팅을 사용자 정의할 수 있는 자유도 있음</td>
  </tr>
  <tr>
    <td>사용자 정의 제한 없음</td>
    <td>사용자가 원하는 값을 설정할 수 있음</td>
  </tr>
</table>
