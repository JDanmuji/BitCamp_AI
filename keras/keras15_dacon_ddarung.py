import numpy as np 
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# 1. 데이터
path = './_data/ddarung/'                    
                                            #index 컬럼은 0번째
train_set = pd.read_csv(path + 'train.csv', index_col=0)   # [715 rows x 9 columns]
test_set = pd.read_csv(path + 'test.csv', index_col=0)     #[1459 rows x 10 columns]
submission = pd.read_csv(path + 'submission.csv', index_col=0)  #[715 rows x 1 columns], 2개중 count 컬럼을 제외한 나머지 1개

train_set = train_set.dropna()
test_set = train_set.dropna()

# print(train_set)
# print(test_set.shape)
# print(submission)

print(train_set.columns) #컬럼명 추출
# Index(['hour', 'hour_bef_temperature', 'hour_bef_precipitation',
#        'hour_bef_windspeed', 'hour_bef_humidity', 'hour_bef_visibility',
#        'hour_bef_ozone', 'hour_bef_pm10', 'hour_bef_pm2.5', 'count'],
#       dtype='object')

print(train_set.info()) #컬럼 정보, non-null = 결측지
# non-null (결측지) 데이터 처리
# 1. 결측지가 들어있는 데이터를 삭제한다.
# 2. 임의의 숫자를 넣는다. ex) 0, 100, 아래 데이터 기준 등


print(test_set.info()) #컬럼 정보, non-null = 결측지
print(train_set.describe())


x = train_set.drop(['count'], axis=1) # 10개 중 count 컬럼을 제외한 나머지 9개만 inputing
print(x) # [1459 rows x 9 columns]
y = train_set['count']

print(y)
print(y.shape) # (1459,)


x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.7, shuffle=True, random_state=123                                                                                                       
)



#2. 모델 구성
model = Sequential()
model.add(Dense(10, input_dim=9))
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(1))


#3. 컴파일,
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train , epochs=100, batch_size=32)


#4. 예측, 평가
loss = model.evaluate(x_test, y_test)
y_predict = model.predict(x_test)

def RMSE(y_test, y_predict) :
    return np.sqrt(mean_squared_error(y_test, y_predict))

r2 = r2_score(y_test, y_predict)

print("===================================")
print(y_test)
print(y_predict)
print("R2 : " , r2)
print("RMSE : ", RMSE(y_test, y_predict))
print("===================================")



'''
[결측지가 있는 경우]
loss : nan
ValueError: Input contains NaN.

[결측지 제거]
R2 :  0.5738889026735445
RMSE :  53.12491189278038

'''