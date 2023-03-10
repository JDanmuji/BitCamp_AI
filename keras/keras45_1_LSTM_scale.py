import numpy as np 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 1. 데이터
x = np.array([[1,2,3], [2,3,4], [3,4,5], 
              [4,5,6], [5,6,7], [6,7,8],
              [7,8,9], [8,9,10], [9,10,11],
              [10,11,12], [20,30,40],[30,40,50],
              [40,50,60]])

y = np.array([4,5,6,7,8,9,10,11,12,13,50,60,70])


print(x.shape, y.shape) # (13, 3) (13,)


x = x.reshape(13, 3, 1)     

print(x.shape)  #(7, 3, 1)

# 2. 모델 구성 rnn = 2차원, rnn의 장기의존성을 해결하기 위해 LSTM이 탄생
model = Sequential()
model.add(LSTM(units=128, input_shape=(3, 1))) # 가독성
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(16))
model.add(Dense(8))
model.add(Dense(4))
model.add(Dense(2))
model.add(Dense(1))


#3. 컴파일 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=300, batch_size=1)

# 4. 평가, 예측
loss = model.evaluate(x, y)
print('loss : ', loss)

y_pred = np.array([50,60,70]).reshape(1, 3, 1)
result = model.predict(y_pred)

print('[50, 60, 70]의 결과 : ',  result)
