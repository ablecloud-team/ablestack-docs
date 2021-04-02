ABLESTACK의 핵심 목표는 어떠한 상용 서버에서도 빠르게 설치하고 쉽게 관리할 수 있는 직관적인 제품을 만드는 것입니다. Cube는 이러한 핵심 목표를 달성하기 위해 마법사를 이용해 설치 및 구성이 가능하도록 하기 위한 목적으로 Linux Kernel과 관련 패키지, 그리고 플러그인으로 구성되어 있는 호스트 운영체제 세트입니다. 

본 섹션에서는 ABLESTACK Cube에 대한 소개 및 아키텍처를 설명하고, 각각의 컴포넌트에 대해 다룹니다. 

## 아키텍처

Cube는 상용 서버에서 ABLESTACK HCI가 동작할 수 있도록 설치하는 운영체제 입니다. Linux Kernel을 기반으로 하며 웹 기반으로 호스트를 관리하고 모니터링 할 수 있습니다. 

이러한 Cube의 기능은 크게 세 가지로 나눌 수 있습니다. 

- 설치 미디어 및 자동설치관리자
    - 부팅 가능 ISO 이미지 제공 (별도로 USB 등의 매체로 변환 가능)
    - Anaconda 및 자동 설치 관리자(Kickstart) 제공
- Kernel 및 핵심 라이브러리
    - CentOS 8을 기반으로 하는 Linux Kernel 포함
    - ABLESTACK Glue, Cell Labrary 및 VM Appliance Image 포함
- 웹 기반 관리 기능
    - 웹을 이용해 호스트 관리, 호스트의 가상머신 및 컨테이너 관리, 각종 서비스 및 호스트 보안 관리 기능을 제공

다음 그림을 ABLESTACK 전체 플랫폼 구성 중 Cube의 개념을 보여줍니다. 

<center>
![cube-architecture](../assets/images/cube-architecture.png)
</center>

## 설치 미디어 및 자동설치 관리자

## Kernel 및 라이브러리

## 웹 기반 관리 기능

