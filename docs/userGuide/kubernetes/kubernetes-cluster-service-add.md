# 서비스 배포

Kubernetes 에서 운영이 가능한 Budibase 배포에 대하여 설명하고 있습니다.

## Budibase 배포

!!! Info
     Budibase 배포는 ABLESTACK Mold에서 Kubernetes 사용법을 설명하기 위해 작성 되어 있습니다. 각 서비스 별로 Kubernets 환경에 맞는 서비스를 배포하시면 됩니다.
!!! Info
     Budibase 에 대한 정보는 해당 [링크](https://docs.budibase.com/docs/kubernetes-k8s/){:target='\_blank'} 에서 확인 하실수 있습니다.
     해당 절차에서는 helm 패키지 서비스를 이용하여 배포 합니다.

   1. Budibase 배포
       ```bash
       helm repo update
       helm repo add budibase https://budibase.github.io/budibase/
       helm install --create-namespace --namespace budibase budibase budibase/budibase
       ```

   2. 배포 확인
       ```bash
       kubectl get pods -n budibase
       ```
   3. Budibase 접속
      ```bash
      kubectl get ingress -n budibase
      ```
      해당 명령어를 이용하여 외부 아이피를 확인 후 Budibase에 접속 하실수 있습니다.
      ![kubernetes-guide-kubernetes-cluster-service-add-01](../../assets/images/kubernetes-guide-kubernetes-cluster-service-add-01.png){: .center }