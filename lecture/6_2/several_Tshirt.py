import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_minst = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_minst.load_data()

class_names = ['T-shirt/top',
'Trouser',
'Pullover',
'Dress',
'Coat',
'Sandal',
'Shirt',
'Sneaker',
'Bag',
'Ankle boot']

# print(train_images.shape)
# print(len(train_labels))
# print(train_images[0])
# print(train_labels[0])

plt.figure()

for i in range(25):
    plt.subplot(5,5,i+1)
    plt.imshow(train_images[i])
    print(train_labels[i])
    plt.xlabel (class_names[train_labels[i]])
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
plt.show()