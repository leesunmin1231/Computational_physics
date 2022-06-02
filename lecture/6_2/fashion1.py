from cgi import test
from prometheus_client import Metric
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_minst = keras.datasets.fashion_mnist.load_data()
(train_images, train_labels), (test_images, test_labels) = fashion_minst

class_names = ['T-shirt/top',
'Trouser',
'Pullover',
'Coat',
'Dress',
'Sandal',
'Shirt'
,'Sneaker',
'Bag',
'Ankle boot']

train_images = train_images/255.0
test_images = test_images/255.0

model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

model.fit(train_images, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy: ', test_acc)
predictions = model.predict(test_images)
print("Prediction for [0] image : ",predictions[0])
print("Maximum Value of Prediction : ", np.argmax(predictions[0]))
print("True Answer = ", test_labels[0])

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()