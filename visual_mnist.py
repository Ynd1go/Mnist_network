import tensorflow as tf
import matplotlib.pyplot as plt
import time

mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

i = 0
while i < 100:
	plt.imshow(x_train[i],cmap=plt.cm.binary)
	plt.show()
	
	plt.close()
	i += 1
	time.sleep(0.45)