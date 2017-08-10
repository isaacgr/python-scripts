# mean shift is a type of clustering algorithm
# hierarchical clustering algorithm
# the machine actually figures out how many clusters there should be and where they are
# type of unsupervised machine learning

# start with a dataset, and say that every featureset is a cluster
# every datapoint has 'bandwidth' with a 'radius'
# featuresets can fall within the bandwidth
# get the mean of all those featuresets to get the new center, then repeat the process
# when the cluster center no longer moves, we say that its been optimized
# will have convergence for all featuresets around a cluster center

from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

centers = [[1,1,1,], [5,5,5], [3,10,10]]
X,_ = make_blobs(n_samples=100, centers = centers, cluster_std = 1)

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
print(cluster_centers)
n_clusters_ = len(np.unique(labels))
print("Number of estimated Clusters: ", n_clusters_)

colors = 10*["g", "r", "c", "b", "k"]
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2], c=colors[labels[i]], marker='o')

ax.scatter(cluster_centers[:,0], cluster_centers[:,1], cluster_centers[:,2],
        marker='x', color='k', s=150, linewidths=5, zorder=10)

plt.show()
