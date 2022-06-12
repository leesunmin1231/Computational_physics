import tensorflow as tf
import tensorflow.keras as keras

import numpy as np
import matplotlib.pyplot as plt

fashion_minst = keras.datasets.fashion_mnist.load_data()
(train_images, train_labels), (test_images, test_labels) = fashion_minst

class_names = [
    'T-shirt/top', 
    'Trouser',
    'Pullover',
    'Dress',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle boot'
    ]

train_images = train_images/255.0
test_images = test_images/255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation = tf.nn.softmax)

])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
    )

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy: ',test_acc)

predictions = model.predict(test_images)

print("Prediction for [2326] image : ",predictions[2326])
print("Maximum Value of Prediction : ", np.argmax(predictions[2326]))
print("True Answer = ", test_labels[2326])

plt.figure()
plt.imshow(test_images[2326])
plt.colorbar()
plt.grid(False)
plt.show()

# (1) prediction value : 2326
# (2) prediction class name : 'Shirt' -> because Maximum Value of Prediction is 6
# (4) test image true class name : 'Shirt' -> True answer index is 6