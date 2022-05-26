from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt

network = models.Sequential()

network.add(layers.Flatten())
network.add(layers.Dense(64, activation = 'relu'))
network.add(layers.Dense(10, activation = 'softmax'))

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32')/255
test_images = test_images.reshape((10000, 28,28,1))
test_images = test_images.astype('float32')/255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.compile(optimizer='rmsprop',
loss = 'categorical_crossentropy',
metrics=['accuracy'])

network.fit(train_images, train_labels, epochs=10, batch_size=64)
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('Test accuravy:', test_acc)


