# up until this point everything we have been doing has been supervised machine learning
# we tell the program what the classes are
# with clustering, the machine is given the feature sets and then searches for groups or clusters
# with flat clustering you tell the machine how many groups and clusters to find
# with heigharchial clustering the machine decides

# start with K-means algorithm
# K is the number of clusters that you want
# basically you randomly choose K feature sets (these are your centroids), and then select the feature sets that are closest to them
# take those points and find the mean of them (to get the center)
# those mean points are your new centroids
# you repeat that process until the centroids stop moving, at which point you have your clusters

# con is that is has a hard time picking differently sized clusters

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from sklearn.cluster import KMeans

X = np.array([[1,2], [1.5,1.8], [5,8], [8,8], [1, 0.6], [9,11]])

#plt.scatter(X[:, 0], X[:, 1], s=100, linewidths=5)
#plt.show()

clf = KMeans(n_clusters=6)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = 10*["g.", "r.", "c.", "b.", "k."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(centroids[:,0], centroids[:,1], marker = 'x', s=150, linewidths = 5)
plt.show()
