
# Mold 퀵 가이드

## 목적 및 개요

이 문서는 Zone 구성이 완료된 Mold 환경에서 가상머신을 생성하기 위해 필요한 기본 준비 항목과 생성 절차를 빠르게 확인하기 위한 퀵 가이드입니다.

가상머신 생성 흐름은 컴퓨트 오퍼링, 디스크 오퍼링, 네트워크 오퍼링, 가상머신용 네트워크, 템플릿 또는 ISO를 준비한 뒤 가상머신을 생성하고 시작하는 순서로 진행합니다. 생성 이후에는 콘솔 접속, 전원 관리, 리소스 확장, 데이터 볼륨 연결 등 기본 운영 작업을 확인합니다.

## 목차
1. 컴퓨트 오퍼링
2. 디스크 오퍼링
3. 가상머신용 네트워크
4. 템플릿
5. ISO
6. 가상머신 생성 및 콘솔확인

## 사전 확인

- Mold Zone 구성이 완료되어 있어야 합니다.
- 사용할 기본 스토리지, 물리 네트워크, VLAN, IP 대역, 게이트웨이, DNS 정보를 확인합니다.
- 가상머신 배포에 사용할 템플릿 또는 ISO 이미지를 준비합니다.

## 진행 순서

1. 컴퓨트 오퍼링을 준비합니다.
2. 디스크 오퍼링을 준비합니다.
4. 가상머신용 네트워크를 생성합니다.
5. 템플릿 또는 ISO를 준비합니다.
6. 가상머신을 생성하고 시작합니다.
7. 생성된 가상머신의 기본 운영 항목을 확인합니다.

## 1. 컴퓨트 오퍼링 {: data-break-before="page" }

--8<-- "docs/admin-guide/mold/mold-admin-guide-offerings-compute-offerings.md:3:50"

## 2. 디스크 오퍼링 {: data-break-before="page" }

--8<-- "docs/admin-guide/mold/mold-admin-guide-offerings-disk-offerings.md:3:46"

## 3. 가상머신용 네트워크 {: data-break-before="page" }

--8<-- "docs/admin-guide/mold/mold-admin-guide-network-guest-networks.md:4:46"

## 4. 템플릿 {: data-break-before="page" }

--8<-- "docs/admin-guide/mold/mold-admin-guide-image-template.md:4:45"

## 5. ISO {: data-break-before="page" }

--8<-- "docs/admin-guide/mold/mold-admin-guide-image-iso.md:4:62"

## 6. 가상머신 생성 및 콘솔확인 {: data-break-before="page" }

--8<-- "docs/admin-guide/mold/mold-admin-guide-compute-vm.md:4:109,139:166"

## 참조 {: data-break-before="page" }

이 퀵 가이드에 나오는 자세한 내용은 아래 링크를 클릭하여 확인가능합니다.

- [컴퓨트 오퍼링](mold-admin-guide-offerings-compute-offerings.md)
- [디스크 오퍼링](mold-admin-guide-offerings-disk-offerings.md)
- [네트워크 오퍼링](mold-admin-guide-offerings-network-offerings.md)
- [가상머신용 네트워크](mold-admin-guide-network-guest-networks.md)
- [템플릿](mold-admin-guide-image-template.md)
- [ISO](mold-admin-guide-image-iso.md)
- [가상머신](mold-admin-guide-compute-vm.md)
- [볼륨](mold-admin-guide-storage-volume.md)

!!! info
    본 문서를 통해 Mold 환경에서 가상머신 생성에 필요한 주요 준비 항목과 기본 운영 절차를 빠르게 확인할 수 있습니다. 이상으로 퀵 가이드를 마치겠습니다.

