import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# 1. 데이터
#아래와 같이 잘라서 넣어줄 수 있지만, 시간과 비용이 많이 든다.
#x = np.array([1], [2], [3], [4], [5], [6])

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 2, 3, 5, 4, 6])

# 2. 모델구성, 심층신경망(딥러닝)
model = Sequential()
model.add(Dense(3, input_dim=1))
model.add(Dense(50))
model.add(Dense(35))
model.add(Dense(13))
model.add(Dense(1))


# 3. 컴파일, 훈련
model.compile(loss='mae', optimizer='adam')
#batch 사이즈는 fit에서 관리
"""
batch : 데이터 셋을 그룹으로 나누는 수
batch_size = 1 , 데이터 그룹 = 6
batch_size = 2 , 데이터 그룹 = 3
batch_size = 3 , 데이터 그룹 = 2 
batch_size = 4  , 데이터 그룹 = 2 (4, 2로 나누고 2하고 남은 만큼 또 훈련)
batch_size = 6 , 데이터 그룹 = 1
batch_size = 7 , 데이터 그룹 = 1 (6하고 1 남은 만큼 또 훈련)
"""
model.fit(x, y, epochs=10, batch_size=1)

# 4. 평가, 예측
result = model.predict([6])
print('6의 결과 : ', result)


