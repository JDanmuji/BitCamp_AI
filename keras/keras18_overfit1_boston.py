from sklearn.datasets import load_boston
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



#1. 데이터
datasets = load_boston()
x = datasets.data
y = datasets.target

print(x.shape, y.shape) # (506, 13) (506,)

x_train, x_test, y_train, y_test = train_test_split (
    x, y, shuffle=True, random_state=333, test_size=0.2
)

#2. 모델 구성
model =  Sequential()
#model.add(Dense(5, input_dim=13))
model.add(Dense(5, input_shape=(13, )))
model.add(Dense(40000))
model.add(Dense(3))
model.add(Dense(20000))
model.add(Dense(1))

import time

model.compile(loss='mse', optimizer='adam')                                 
start = time.time()                                                                            
hist = model.fit(x_train, y_train, epochs=300, batch_size=1, validation_split=0.2, verbose=1) #fit 이 return 한다.
end = time.time()

#3. 평가, 예측
loss = model.evaluate(x_test, y_test)

print('============================================')
print(hist) # <keras.callbacks.History object at 0x00000258175F20A0>
print('============================================')
print(hist.history) # loss, vel-loss 의 변화 형태(딕셔너리 형태|key-value) , value의 형태가 list
print('============================================')
print(hist.history['loss'])
print('============================================')
print(hist.history['val_loss'])
print('============================================')
print('loss : ', loss)
print('============================================')
print('걸린시간 : ', end - start)


plt.figure(figsize=(9,6))
# x 명시 안해도 됨
# hist loss 사용, 색은 red, 선모양은 ., y 선의 이름은 loss
plt.plot(hist.history['loss'], c='red', marker='.', label='loss')
# hist val_loss 사용, 색은 blue, 선모양은 ., x 선의 이름은 val_loss
plt.plot(hist.history['val_loss'], c='blue',  marker='.' , label='val_loss' )
# 차트 gird 생성
plt.grid() 
# x 축 이름 
plt.xlabel('epochs')
# y 축 이름 
plt.ylabel('loss')
# 차트 제목
plt.title('boston loss')
# 그래프 선 이름 표
plt.legend()
#plt.legend(loc='upper right')  그래프 선 이름 표, 위치
# 차트 창 띄우기
plt.show()




'''
[verbose = 0]
loss :  40.98577880859375
걸린시간 :  9.872689485549927


[verbose = 1]
loss :  45.78962326049805
걸린시간 :  11.606598138809204

[verbose = 2] 
loss :  45.07732009887695
걸린시간 :  10.344038963317871


'''