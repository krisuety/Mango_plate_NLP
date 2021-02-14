# Mango_plate_NLP

## 0. Problems

식당의 총 평점으로는, 내가 원하는 기준에 부합하는 식당인지 알수가 없음. 맛 이외에 사람들이 중요하게 생각하는 세가지 요소인 '가성비, 서비스, 웨이팅 여부' 에 대해서 긍, 부정적인 평가를 내린 리뷰를 찾아내는 것이 목적



## 1. crawling

식신, 망고플레이트, 포잉 : requests, selenium


## 2. preprocessing

- labeling (가성비, 서비스, 웨이팅)

## 3. model

- [machine learning](https://github.com/krisuety/Mango_plate_NLP/tree/master/model/machine_learning)
- [deep learning](https://github.com/krisuety/Mango_plate_NLP/tree/master/model/deep_learning)

## 4. predict

- 가성비, 웨이팅 best : boosting (lgbm)
- 서비스 best : self attention + biLSTM (pytorch, [reference paper](https://arxiv.org/pdf/1703.03130.pdf))


![image](material/result_NLP.png)
(metric : F-1 score)

## 5. web (Flask, nginx, uWSGI)

[식당 조회해보기](http://15.164.204.219)

강남구를 제외한 서울에 위치한 망고 플레이트 리뷰 상위권 3000여곳의 식당의 정보를 조회할 수 있습니다.
