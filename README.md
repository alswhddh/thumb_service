## 유튜브 데이터를 크롤링 하여 만든 썸네일 이미지 분석 flask 웹페이지 입니다.

### 4가지 카테고리 : 먹방/ASMR , 뷰티 , 여행 , 정치/경제/사회

### 카테고리당 20명의 유튜버

### 유튜버당 20개의 동영상

총 1752개의 동영상

### 0. 썸네일 리스트(SQLite3)

![메인페이지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FvSMpj%2Fbtq0nOMfCF3%2FfIQUlAXGZph0tSK58sjUUk%2Fimg.png)

 - 장르별로 썸네일 점수와 조회수 및 리스트를 가져올 수 있고 항목별로 정렬할 수 있다.

### 1. 썸네일 조회수 예측

![조회수예측](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnjVKJ%2Fbtq0iWEvqMX%2FTly8FcmRmjIUtk1vsE4wEk%2Fimg.png)

- CNN 모델로 유튜브 썸네일 이미지와 썸네일 점수 ( 조회수 / 구독자 수) 로 이미지 회귀

### 2. 비슷한 썸네일 찾기(코사인 유사도)

![유사썸네일](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbKRnj5%2Fbtq0oa9k73D%2Fi6phT71WNZApUOQc3Edof1%2Fimg.png)

- 이미지 데이터를 통한 코사인 유사도도 비슷한 이미지 찾기

### 3. 썸네일 장르 분류

![이미지분류](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtooyE%2Fbtq0nOMfCqY%2FNhHAbA2PoEqeKlidvWZTwk%2Fimg.png)

- 이미지를 넣으면 어느 장르의 속하는 지 분류

## 얼굴 인식 + CNN 얼굴 이미지 회귀 통한 얼굴평가 인공지능

![넥슨](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcquERc%2Fbtq0iWkc04e%2FjGMlrJnqMlahRtjLumRuBk%2Fimg.png)

![원빈](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb2Dgl2%2Fbtq0fjNXx5Q%2FJ5PUfmHaY6Ik1kBS3mi671%2Fimg.png)

참고 : https://github.com/kairess/beauty_score <br>

Dataset : https://github.com/HCIILAB/SCUT-FBP5500-Database-Release <br>

5500 장의 정면 얼굴이미지로 다양한 인종들의 뷰티스코어 데이터이다. <br>

얼굴인식을 통해 학습데이터와 비슷한 크기로 전처리를 해주고 얼굴 점수를 예측한다.


