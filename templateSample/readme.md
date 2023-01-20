# 문서 작성 설명서

## 작성 규칙

- "아키텍처" -> "구성 정보" 순으로 작성합니다.




### 이미지 표시
이미지 위치를 center로 적용합니다.

<figure markdown>
!![이미지 제목](이미지 경로.png)
<figcaption>새 Affinity 그룹 추가 대화 상자</figcaption>
</figure markdown>


### Admonitions
추가 정보를 제공하거나 특이사항을 전달하기 위해 사용합니다.

- 사용 예:

!!! info "ABLESTACK Cube에서의 방화벽 설정"
    ABLESTACK Cube에서의 방화벽 설정을 위해 [Cube 방화벽 서비스 활성화](../../../../administration/cube/networking-guide#_27) 문서를 참고하십시오.

#### info
다른 문서를 참고하거나 다른 추가 설명이 필요한 경우 사용합니다.

#### warning
자원의 손실 또는 시스템 오류가 발생되어 서비스가 중단될 수 있는 잠재적인 위험에 대해 사용합니다.

#### danger
자원의 손실 또는 시스템 오류가 발생되어 서비스가 중단될 수 있는 즉각적인 위험에 대해 사용합니다.


### 코드 블록
타이틀을 작성하고 라인 표기 옵션을 적용합니다.

    ``` title="exports"  linenums="1"
    # 모든 사용자 접근 허용 시
    /mnt/data/nfs *(rw,sync,no_root_squash) 

    # 특정 범위 IP 사용자 접근 허용 시
    # /mnt/data/nfs 10.10.1.0/24(rw,sync,no_root_squash) 
    ```


## 작성 시 유의 사항

- 타이틀을 생성할 경우, 그 타이틀에 대한 설명을 필수로 작성해야합니다.
- 목차 제목은 최대한 간단하게 합니다. 
- 서브 스텝은 되도록 쓰지 않도록 하고 만약 쓰게 된다면 서브 스텝에도 제목을 지정하여 작성합니다.
- 
