# 2020-CPS-project

## 유해동물 감지 시스템
### Team 3
이은진
임채원
최혜정
황수인

### 사용한 오픈소스 (~20.05.27)
Darknet Yolo (version 4) - customed by AlexyAB (https://github.com/AlexeyAB/darknet)

labelImg (https://github.com/tzutalin/labelImg)

Selenium, Beautifulsoup

## 활동 내역
### 20.05.21
혜정 : 구글 이미지 크롤러 제작 (Crawling/crawler.py)
### 20.05.23
은진, 혜정, 수인 : 멧돼지, 고라니, 꿩, 뉴트리아, 개, 고양이 사진 크롤링 후 라벨링(labelImg 사용) --> 1046장 (Crawling/image(1).zip, result(1).zip)
### 20.05.24
채원 : 수집 및 처리한 데이터세트에 맞게 darknet yolo 수정 (Yolo/darknet-master/cfg/yolo-obj.cfg  data/obj.data,obj.names,train.txt  data/obj --> 데이터세트) 및 업로드 (darknet-master)

Colaboratory에서 실행 및 학습할 수 있는 코드 업로드 (Yolo/yolov3darknet_test.ipynb) / 학습 중 (20.05.27 iteration 4900 avg loss 1.4384)
