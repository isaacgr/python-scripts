# KNN uses euclidian distance to calculate the distance between points

import numpy as np
import pandas as pd
from math import sqrt
from matplotlib import style
import matplotlib.pyplot as plt
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5], [7,7], [8,6]]}
new_features = [5,7]

def k_nearset_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups')
    distances = []
    for group in data:
        for features in data[group]:
            euclidian_distance = np.linalg.norm(np.array(features)-np.array(predict))
            # using this isntead of the euclidian formula is faster, and can handle higher dimensions
            distances.append([euclidian_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    # Counter returns a key of votes with how many times they occur
    # most_common returns the first key which occurs the most times
    vote_result = Counter(votes).most_common(1)[0][0]
    # returns a list of lists where the fist element is the one that was most common
    return vote_result

result = k_nearset_neighbors(dataset, new_features, k=3)
print(result)

[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]]for i in dataset]
plt.scatter(new_features[0], new_features[1], s=100, color=result)
plt.show()

# one issue with knn is that to compare the closness of a point to the other datapoints, you have to
# compare it to all datapoints in the set
