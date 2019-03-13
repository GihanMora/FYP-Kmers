import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


points_n = 200
clusters_n = 3

points = tf.constant(np.random.uniform(0, 10, (points_n, 2)))

print("ok")