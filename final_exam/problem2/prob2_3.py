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

predictions = model.predict(test_images)



counts = np.zeros(len(class_names))
for i in range(len(test_labels)):
    if (np.argmax(predictions[i]) != test_labels[i]):
        counts[test_labels[i]]+=1

errors = np.sqrt(counts) # uncertainties of data
plt.errorbar(class_names, counts, yerr = errors, fmt='o') # data point drawing
plt.show()
