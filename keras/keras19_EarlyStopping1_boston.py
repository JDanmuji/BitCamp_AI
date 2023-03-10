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

#2. 모델 구성 # 회귀형 모델
model =  Sequential()
#model.add(Dense(5, input_dim=13))
model.add(Dense(128, input_shape=(13, )))
model.add(Dense(64))
model.add(Dense(32))
model.add(Dense(24))
model.add(Dense(8))
model.add(Dense(4))
model.add(Dense(1))

import time

model.compile(loss='mse', optimizer='adam')                                 
start = time.time()                                                                         
from tensorflow.keras.callbacks import EarlyStopping #파이썬 클래스 대문자로 시작   

#earlyStopping 약점 : 5번을 참고 끊으면 그 순간에 weight가 저장 (끊는 순간)
                                                    
#Early stopping 은 무조건 Epoch 을 많이 돌린 후, 특정 시점에서 멈추는 것이다.                                                    
earlyStopping = EarlyStopping(monitor='val_loss', #학습 조기종료를 위해 관찰하는 항목, val_loss 나 val_accuracy 가 주로 사용됩니다. (default : val_loss)
                              mode='min', 
                              patience=10, #참을성     
                              restore_best_weights=True, 
                              verbose=1
                              )

hist = model.fit(x_train, y_train, epochs=100, batch_size=1, callbacks=[earlyStopping], validation_split=0.2, verbose=1) #fit 이 return 한다.
end = time.time()

#3. 평가, 예측
loss = model.evaluate(x_test, y_test)

print('============================================')
print(hist) # <keras.callbacks.History object at 0x00000258175F20A0>
print('============================================')
print(hist.history) # loss, vel-loss 의 변화 형태(딕셔너리 형태|key-value) , value의 형태가 list
print('============================================')
print(hist.history)
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