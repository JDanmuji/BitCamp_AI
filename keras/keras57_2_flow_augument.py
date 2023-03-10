import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.datasets import fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
augument_size=40000

randidx = np.random.randint(x_train.shape[0], size=augument_size)
print(randidx)
print(len(randidx))

x_augument = x_train[randidx].copy()
y_augument = y_train[randidx].copy()

print(x_augument.shape, y_augument.shape)

x_augument = x_augument.reshape(40000, 28, 28, 1)


train_datagen = ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True, 
    vertical_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rotation_range=5,
    zoom_range=1.2,
    shear_range=0.7,
    fill_mode='nearest' 
)
                   
x_augumented = train_datagen.flow( # flow : 원래 수치화된 데이터를 가지고 작업
    x_augument,
    y_augument,
    batch_size=augument_size,
    shuffle=True,
) 

print(x_augumented[0][0].shape)
print(x_augumented[0][1].shape)

x_train = x_train.reshape(60000,28, 28, 1)

x_train = np.concatenate((x_train, x_augumented[0][0]))
y_train = np.concatenate((y_train, x_augumented[0][1]))

print(x_train.shape, y_train.shape)