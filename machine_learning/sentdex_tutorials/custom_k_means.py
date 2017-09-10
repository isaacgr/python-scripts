# Pick any two data points on a 2D data set, measure the distance to the other
# data points and whichever onees they are closer to we classify them as belonging
# to that centroids class
# then we take the mean of both classes and that becomes the new centroid
# do that until the centroid stops moving and when the centroid stops moving we
# say the data is clustered


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

X = np.array([[1,2], [1.5,1.8], [5,8], [8,8], [1, 0.6], [9,11]])

plt.scatter(X[:, 0], X[:, 1], s=100, linewidths=5)

colors = 10*["g", "r", "c", "b", "k"]

class K_Means:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter=max_iter

    def fit(self, data):
        self.centroids = {}
        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}
            for i in range(self.k):
                self.classifications[i] = []
            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification=distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)   # need to do dict else it would change with self.centroids

            for classification in self.classifications:
                # finds the mean of all the features for any given class
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]

                if np.sum((current_centroid-original_centroid)/original_centroid*100.0>self.tol):
                    optimized = False

            if optimized:
                break

    def predict(self, data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification=distances.index(min(distances))
        return classification

clf = K_Means()
clf.fit(X)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker='o', color='k', linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker='x', color = color, s=150, linewidths=5)


unknowns = np.array([[1,3], [8,9], [5,4], [6,4], [0,3]])
for unknown in unknowns:
    classification = clf.predict(unknown)
    plt.scatter(unknown[0], unknown[1], marker='*', color = colors[classification], s=150, linewidths=5)

plt.show()
