import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import fetch_openml
mnist = fetch_openml(name='mnist_784', version=1)
mnist.keys()
dict_keys(['data', 'target', 'frame', 'categories', 'feature_names', 'target_names', 'DESCR', 'details', 'url'])
X, y = mnist['data'], mnist['target']
X.shape, y.shape
((70000, 784), (70000,))
X, y = X[:35000], y[:35000]
X.shape, y.shape
((35000, 784), (35000,))
some_digit = X[0]
some_digit_image = some_digit.reshape(28, 28)
plt.imshow(some_digit_image, cmap='binary')
plt.axis('off')
plt.show()