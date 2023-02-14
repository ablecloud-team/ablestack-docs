# ABLESTACK Doc 문서 작성시 사용법

## 이미지

```markdown title="가온데 정렬"
![이미지 이름](이미지 상대경로){:class="imgCenter"}
```

```markdown title="이미지 테두리"
![이미지 이름](이미지 상대경로){:class="imgBorder"}
```

## 코드 불럭 

!!! example "Code"

    === "기본 코드블럭"

        ``` markdown
            ``` shell
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            ```
        ```

    === "코드블록 타이틀"
        
        ``` markdown
            ``` shell title="sudo vi /etc/exports"
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            ```
        ```

    === "코드블록 라인번호"
        
        ``` markdown
            ``` shell linenums="1 3"
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            ```
        ```

    === "코드블록 강조"
        
        ``` markdown
            ``` shell hl_lines="2"
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
            ```
        ```

!!! example "result"

    === "기본 코드블럭"

        ``` shell
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        ```

    === "코드블록 타이틀"
        
        ``` shell title="sudo vi /etc/exports"
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        ```

    === "코드블록 라인번호"
        
        ``` shell linenums="1"
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        ```

    === "코드블록 강조"
        
        ``` shell hl_lines="2"
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        10.1.1.11:/kubernetes	/home/cloud/nfs	nfs	defaults	0	0
        ```

## Admonitions
추가 정보를 제공하거나 특이사항을 전달하기 위해 사용합니다.

!!! example "Admonitions"

    === "일반 Admonitions"
        
        !!! info "info 제목"
            info 내용 입력 (필수적으로 추가 설명이 필요한 경우 또는 다른 문서를 참고해야 할 경우 사용합니다.)

        !!! note "note 제목"
            note 내용 입력 (부가적으로 추가 설명이 필요한 경우 사용합니다.)

        !!! warning "warning 제목"
            warning 내용 입력 (자원의 손실 또는 시스템 오류가 발생되어 잠재적인 서비스 중단 위험이 발생할 경우에 사용합니다.)

        !!! danger "danger 제목"
            danger 내용 입력 (자원의 손실 또는 시스템 오류가 발생되어 즉각적인 서비스 중단 위험이 발생할 경우에 사용합니다.)


    === "접을 수 있는 Admonitions" 

        ??? info ""
        Info 내용 입력 (긴 코드에는 접을 수 있는 블록(Collapsible blocks)을 사용합니다.)
        