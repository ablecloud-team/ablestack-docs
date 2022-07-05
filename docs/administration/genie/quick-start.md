# Genie Quick Start

## Genie 템플릿 자동 생성
템플릿은 플레이북과 이를 실행하는데 필요한 리소스들의 집합입니다. 
템플릿을 생성하려면 인증 정보, 프로젝트, 인벤토리, 호스트를 사전에 생성해야 합니다.

ABLESTACK Genie에서는 이러한 구성요소들과 템플릿을 자동으로 생성합니다.

왼쪽 메뉴에서 **템플릿** 을 클릭합니다. 
![genie-templates-info](../../assets/images/genie-templates-info.png)

 **"auto_deploy_job_template"** 템플릿을 시작합니다.
![genie-templates-auto-deployment](../../assets/images/genie-templates-auto-deployment.png)

템플릿이 시작되면 **작업** 메뉴의 출력화면으로 전환되며 실행 중인 템플릿에 대한 실행 정보 및 로그를 실시간으로 확인할 수 있습니다. 
![genie-templates-auto-deployment-log](../../assets/images/genie-templates-auto-deployment-log.png)

정상적으로 작업이 종료된 후 추가된 템플릿 및 인증 정보, 프로젝트, 인벤토리, 호스트를 각 리소스 메뉴에서 확인할 수 있습니다.
![genie-templates-auto-deployment-result](../../assets/images/genie-templates-auto-deployment-result.png)

### 생성된 Genie 템플릿 실행
ABLESTACK Genie에서 기본 제공되는 템플릿은 애플리케이션 배포를 기준으로  **배포, 체크, 삭제** 3가지의 템플릿이 **하나의 세트** 로 구성되어 있습니다.

배포 템플릿 작업이 정상적으로 종료될 경우 체크 템플릿이 자동으로 Genie 대시보드에서 일정(스케줄)으로 등록되어 일정 간격으로 배포된 패키지 상태 정보를 Mold로 보내는 역할을 합니다.
![genie-templates-auto-deployment-check](../../assets/images/genie-templates-auto-deployment-check.png)


배포된 패키지의 상태 정보는 Mold -> 오토메이션 메뉴 -> 배포된 패키지 에서 확인할 수 있습니다.

