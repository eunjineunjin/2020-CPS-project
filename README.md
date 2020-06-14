# 2020-CPS-project

## 유해동물 감지 시스템
### Team 3
이은진
임채원
최혜정
황수인

### 사용한 오픈소스 (~20.05.27)
Darknet Yolo v4 - customed by AlexeyAB (https://github.com/AlexeyAB/darknet)

gcc 7.5.0

opencv 3.2.0

labelImg 1.8.3 (https://github.com/tzutalin/labelImg)

Selenium 3.141.0

Beautifulsoup 4.9.0

## 활동 내역
### 20.05.21
혜정 : 구글 이미지 크롤러 제작 (Crawling/crawler.py)
### 20.05.23
은진, 혜정, 수인 : 멧돼지, 고라니, 꿩, 뉴트리아, 개, 고양이 사진 크롤링 후 라벨링(labelImg 사용) --> 1046장 (Crawling/image(1).zip, result(1).zip)
### 20.05.24
채원 : 수집 및 처리한 데이터세트에 맞게 darknet yolo 수정 및 업로드 (Yolo/darknet-master)

(Yolo/custom/yolo-obj.cfg 

Yolo/custom/obj.data,obj.names,train.txt

Yolo/custom/obj --> 데이터세트) 

Colaboratory에서 실행 및 학습할 수 있는 코드 업로드 (Yolo/yolov3darknet_test.ipynb) / 학습 중 (20.05.28 iteration 5800 avg loss 1.1677)
### 20.06.06
수인: VMware 가상머신 안의 Ubuntu 환경에서 Apache, MySQL, PHP 설치 후 http://localhost/cps2.php 서버 구축 완성했다. 서버 생성 후 yolo에서 생성된 데이터를 서버로 보낼 수 있게 image.c 파일 코드 수정했다.

하지만 이 수정된 파일로 yolo를 실행해 봤을 때 서버와의 연결을 실패했다. 따라서 서버에 데이터를 보내는 작업도 실패했다.

구축한 서버와의 연결은 실패했으나 웹을 처음 구축해보는 과정에서 기본적인 웹 구조와 동작방식에 대해서 배울 수 있는 기회였다.
### 20.06.10
수인: Google Colaboratory 환경에서 Flask 서버 구축 완성.

하지만 실행 코드를 다시 실행시킬 때마다 Flask 서버의 주소가 매번 바뀌고, 이 또한 yolo와 함께 실행하는 방법을 찾지 못한 이유로 yolo와 Flask 서버의 연결도 실패했다. 




<모든 팀원>

나중에 모두가 서버 구축과 연결의 문제를 해결하려고 노력하면서 배운 것은, Google Colaboratory가 로컬 PC가 아닌 클라우드 환경(Google Drive)에서 작업이 되기 때문에 여기서 생성되는 파일은 바로 서버로 보내지 못한다는 것이다.
