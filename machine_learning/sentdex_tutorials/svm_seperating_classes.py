# The objective of the SVM is to find the best seperating hyperplane (aka decision boundary)
# The greatest distance between the datapoints and the seperating hyperplace means its the best
# Can classify new datapoints based on which side of the hyperplane that the data falls
# It is a binary classifier, so it works on linear data

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True) # svm handles outliers slightly better than knn

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])   # we will be predicting this

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size = .2)

clf = svm.SVC()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)
