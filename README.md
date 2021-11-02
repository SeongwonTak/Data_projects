# Data_projects

Data 분석 관련 진행 개인 Project 모음입니다.

## 진행예정

## 진행중

### DataScientist Job Description Analysis(2021.10.22 ~)
- Crawling 사전 학습을 통한 기반 지식 학습
- 여러 채용 사이트의 Data Scientist 의 JD 수집
- 핵심 키워드 추출 및 필수 기술 스택 정리
- 기존 나의 스택/방향성과의 Matching index 개발.
- Obstacle : Crawling진행의 어려움. 다른 방법에 대한 학습 필요?


## 1차진행완료

### League of Legends 승부 예측 프로젝트 (2021.4월 초, 2021.9.27~ 1차 개선 완료)
- Project 설명 : Kaggle LOL Data 바탕 챌린저 경기에 대한 승패 예측 모델 생성
- Decision Tree, Logistic Regression, RandomForest 등 적용 및 그랜드마스터 경기에도 유사하게 적용 가능한지 확인
- 둘 중 어느 팀이 우세했는지에 따라 0-1 범주형 지표를 만든 후 분석에 적용
- 발전방향 : 추가 EDA 실시 및 여러 평가 지표에 따른 모델 추가 검증

### Board Game Recommender (2021.6월 초)
- Project 설명 : Content-based를 활용한 보드게임 추천
- 플레이 인원수에 따라, 경험한 혹은 가장 좋아하는 3개의 보드게임에 따른 유사 보드게임 추천
- 발전방향 : 평점 데이터 확보시 이를 활용하여 CF 혹은 Hybrid 방식의 보드게임 추천 가능

### Common Readability Prize (2021.9~)
- Project 설명 : 영어 지문의 난이도를 평가하는 프로젝트
- 영어 전처리(Tokenize -> Tf-Idf/Word2 Vec -> 모델 적용), Pytorch를 활용한 신경망 적용
- 발전방향 : Pytorch 구현에 익숙해진 후 1D-CNN, RNN등 재구현 실시.

### Credit_Card Fraud detection (2021.9~10.13, 2021.10.25~11.2 1차 개선 완료 )
- Project 설명 : 신용카드 사용 이력에 따른 사기 검출 모델 생성
- 발전 방향 : Imbalanced data를 효과적으로 처리할 수 있는 방향에 대해 고려.
- Obstacle : Precision 대비 Recall이 매우 낮으며, Recall을 잡으면 Precision이 매우 낮아져 고민. PCA 등도 크게 유효하지 않아보임.
- 실제로 Recall이 1이나 Precision이 0.04 정도인 RandomForest를 만들 수 있기에..더 고민.
