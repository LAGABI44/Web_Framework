import pandas as pd
import numpy as np
import pickle # 객체 입출력을 위한 라이브러리
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('data(over_dis_vs_nor).csv')

# 1번 모델 정답 지우기
df=df.drop(['Dis'], axis=1)
# 2번 모델 정답 중 '4' 모두 지우기
df = df.loc[df['DIS']!=4]

y = df['DIS']
x = df.drop(['DIS'], axis=1)

# 데이터 정규화
# 표준 스케일러(평균 0, 분산 1)
scaler = MinMaxScaler()
scaler = scaler.fit_transform(x)

rf = RandomForestClassifier(random_state=1234,
                                n_estimators = 15,
                                max_depth = 25,
                                min_samples_split = 2,
                                min_samples_leaf = 2)
rf.fit(scaler, y)

pred = rf.predict(scaler)

accuracy = accuracy_score(y, pred)
print('랜덤 포레스트 정확도: {:.4f}'.format(accuracy))

#pickle.dump(rf, open('model.pkl', 'wb'))
joblib.dump(rf, 'model.pkl')

#pickle.dump(rf, open('model.pkl', 'wb'))
joblib.dump(scaler, 'scale_rf.pkl')