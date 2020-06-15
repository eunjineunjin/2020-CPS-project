# 2020-CPS-project

## 유해동물 감지 시스템
### Team 3
이은진
임채원
최혜정
황수인

### 프로젝트 목적
유해동물들이 경작지에 침입할 시, 이를 실시간으로 탐지하여 농부에게 모바일로 알림으로써 유해동물에 의한 농작물 손실을 최소화시킬 수 있는 유해동물감지시스템을 구축한다.

### 사용한 오픈소스 (~20.05.27)
Darknet Yolo v4 - customed by AlexeyAB (https://github.com/AlexeyAB/darknet)

gcc 7.5.0

opencv 3.2.0

labelImg 1.8.3 (https://github.com/tzutalin/labelImg)

Selenium 3.141.0

Beautifulsoup 4.9.0

jsoup 1.13.1

firebase-analytics 17.2.2

firebase-core 17.4.3

firebase-messaging 20.2.0

Flask 1.1.2


## 코드 및 파일 설명
### Crawling/
crawler.py : 구글 이미지를 수집할 수 있는 크롤러, 이를 통해 멧돼지, 고라니, 꿩, 뉴트리아, 개, 고양이의 이미지를 수집했다.

data.zip : 수집한 이미지를 바탕으로 라벨링을 진행한 결과물, 수집한 이미지의 집합

image(1).zip : 수집한 이미지

result(1).zip : 수집한 이미지를 바탕으로 라벨링을 진행한 결과물

### Flask/
flask_cps.py, flask_web_server_create.py : 구글 colab 내에서 Flask 웹서버를 구동시킬 수 있는 파일  

### UserApp/
AndroidManifest.xml : 앱 실행 시 빌드하기 위한 실행파일

MainActivity.java : 앱 실행 시 최초로 동작하는 코드이며 버튼을 누르면 현재 감지한 상태와 시각을 출력하도록 만듬

MyFireBaseMessagingService.java : 구글으로부터 알림 메시지를 받아 출력하는 서비스. 앱이 실행되지 않고 있는 상태에서 동작하며 알림 클릭 시 앱 실행, 이게 동작하도록 AndroidManifest.xml에 서비스 

### Yolo/
custom : AlexeyAB의 darknet에서 이번 프로젝트에 맞게 수정한 파일들의 목록

darknet-master : 사용한 AlexeyAB의 darknet

yolov3darknet_test.ipynb : colab에서 yolo를 실행시키기 위한 실행코드

### automaticFCM.py
구축한 어플에게 서버에서 정보를 전송하도록 하는 파이썬 


## 활동 내역
### 20.05.21
혜정 : 구글 이미지 크롤러 제작 (Crawling/crawler.py)

처음에 google images download library를 사용하여 구글 이미지 크롤링을 진행하려고 했으나 코드가 실행이 되지 않아 이미지 크롤링에 실패하였다. 

그러나 구글의 업데이트(이미지 형식 변경)로 인하여 해당 라이브러리를 사용하지 못하게 됨을 알게 된 후 코드를 수정하여  최종적으로 구글 이미지 크롤링을 진행 하였다. 
### 20.05.23
은진, 혜정, 수인 : 멧돼지(152), 고라니(165), 꿩(155), 뉴트리아(154), 개(164), 고양이(256) 사진 크롤링 후 라벨링(labelImg 사용) --> 1046장 (Crawling/image(1).zip, result(1).zip)
### 20.05.24
채원 : 수집 및 처리한 데이터세트에 맞게 darknet yolo 수정 및 업로드 (Yolo/darknet-master)

(Yolo/custom/yolo-obj.cfg 

Yolo/custom/obj.data,obj.names,train.txt

Yolo/custom/obj --> 데이터세트) 

Colaboratory에서 실행 및 학습할 수 있는 코드 업로드 (Yolo/yolov3darknet_test.ipynb) / 학습 중 (20.05.28 iteration 5800 avg loss 1.1677)

### 20.06.03
채원 : 가장 가중치가 낮게 잡혔던 6000번대 가중치 파일(yolo-obj_6000.weights)로 멧돼지, 고라니, 꿩, 뉴트리아, 개, 고양이의 영상에 대한 탐지 수행 --> 멧돼지, 고라니, 고양이가 잘 tracking되어 이 셋을 주로 한 프로젝트를 시행하고자 함.

### 20.06.06
수인: VMware 가상머신 안의 Ubuntu 환경에서 Apache, MySQL, PHP 설치 후 http://localhost/cps2.php 서버 구축을 완성했다. 서버 생성 후 yolo에서 생성된 데이터를 서버로 보낼 수 있게 image.c 파일 코드(yolo - src 파일에 들어있다)를 수정했다.

실패경험: 하지만 이 수정된 파일로 yolo를 실행해 봤을 때 서버와의 연결을 실패했다. 따라서 서버에 데이터를 보내는 작업도 실패했다. 추정해 본 예상 오류의 원인으로는 가상머신 안의 Ubuntu의 서버와 yolo가 실행되는 윈도우 상의 Google Colaboratory의 연결이 없었다는 것이다. 또한, 구글 드라이브에 생성된 파일을 로컬 PC로 불러올 수 없다는 것이었다. 

구축한 서버와의 연결은 실패했으나 웹을 처음 구축해보는 과정에서 기본적인 웹 구조와 동작방식에 대해서 배울 수 있는 기회였다.

은진: 구글 firebase를 이용하여 푸시 알림을 받는 어플(UserApp)을 개발하였다. 이후 서버에서 자동으로 알림을 보내도록 파이썬 코드(AutomaticFCM.py)를 작성하였으나 인증 오류가 발생하여 실패하였다.
### 20.06.10
수인: Google Colaboratory 환경에서 파이썬 코드(flask_cps.py)를 작성하여 Flask 서버 구축을 완성하였다. (flask_web_server_create.py 파일은 Google Colaboratory에서 실행시킬 수 있는 전체 코드이다.)

실패경험: 하지만 실행 코드를 다시 실행시킬 때마다 Flask 서버의 주소가 매번 바뀌고, 이 또한 yolo와 함께 실행하는 방법을 찾지 못한 이유로 yolo와 Flask 서버의 연결도 실패했다. 

은진: 어플이 서버로부터 정보를 받아 출력하는 기능을 추가하기 위해 jsoup을 사용하였다. 화면에 데이터를 출력하기 위해 ListView를 사용하였다.
### 20.06.13
<모든 팀원>

모두가 서버 구축과 연결의 문제를 해결하려고 노력하는 과정에서 배운 점은, Google Colaboratory가 로컬 PC가 아닌 클라우드 환경(Google Drive)에서 작업이 되기 때문에 같은 환경에서 서버 구축 등의 작업을 수행하지 않는 이상 연결이 어렵다는 점이다. 프로젝트 계획 전에 이 점에 대해 알지 못했기 때문에 서버 구축 및 어플 제작을 했음에도 불구하고 연결이 어려워 프로젝트를 완벽히 수행하지 못했다. 하지만, 프로젝트를 진행하면서 yolo 학습 중 가중치가 이상적(0.1 ~ 0.05)으로 낮춰지지 않아도 yolo가 영상 및 이미지에 대한 실시간 탐지를 위주로 하는 딥러닝 알고리즘이기 때문에 가중치가 1.1에 불과해도 객체에 대한 탐지는 어느정도 수행할 수 있다는 점을 배웠으며 CPS 보안 실습 수업에서 배운 크롤링을 응용하여 구글 이미지 크롤러를 만드는 것 또한 수행할 수 있었다. 또한 서버 구축 과정에서 기본적인 웹 구조와 동작 방식에 대해 배울 수 있었고 보통 아파치와 MySQL을 사용하여 웹서버를 만드는 방식 말고 파이썬을 기반으로 Flask를 사용하여 웹 서버 구축을 해볼 수 있었으며, 구글 Firebase 오픈소스를 사용해 푸시 알림을 받는 어플 자체를 구축해볼 수 있는 기회가 되었다. 
