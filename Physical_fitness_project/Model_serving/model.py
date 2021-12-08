# 모델 작성
# 연령대, 키, 몸무게, 운동 성적에 따른 체지방양을 예측하는 모델을 serving해보자.
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./train_data.csv')
# 첫 컬럼이 잡히는 오류가 있어, 이를 해결하고 분리한다.
df = df.iloc[:,1:]
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

reg = LinearRegression()
reg.fit(X, y)

pickle.dump(reg, open('fat_rate.pkl', 'wb'))
