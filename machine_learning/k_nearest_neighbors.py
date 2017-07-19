# With nearest neighbors, check to see what the closest points are to a new data points

# K-nearest neighbors finds the K closests neighbors to K(the new data point)
# Will likely want it to be an odd number as opposed to even so it doestn get split between 2 data sets
# The cons to this method is that we are using euclidian distance to measure the distance between new data points and the data sets
# Because of this, the larger the data set the worse the algorithm runs

#http://archive.ics.uci.edu/ml/datasets.html

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True) # KNN handles outliers very poorly

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])   # we will be predicting this

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size = .2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,2,2,3,2,1]])

example_measures = example_measures.reshape(len(example_measures),-1)
prediction = clf.predict(example_measures)

print(prediction)
