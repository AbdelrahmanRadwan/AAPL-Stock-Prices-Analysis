import numpy as np
from sklearn.naive_bayes import GaussianNB

#X = [[-1], [-2], [-3], [1], [2], [3]]
X = np.array([-1, -2, -3, 1, 2, 3])
X= X.reshape((6,1))
print(X)
Y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB()
clf.fit(X, Y)


