import tensorflow as tf
import tensorflow.keras as keras

import numpy as np
import matplotlib.pyplot as plt

fashion_minst = keras.datasets.fashion_mnist.load_data()
(train_images, train_labels), (test_images, test_labels) = fashion_minst

class_names = ['T-shirt/top',
'Trouser',
'Pullover',
'Coat',
'Sandal',
'Shirt'
,'Sneaker',
'Bag',
'Ankle boot']

print(train_images.shape)
print(len(train_labels))
print(train_images[0])
print(train_labels[0])

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()