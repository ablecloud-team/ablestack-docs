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

