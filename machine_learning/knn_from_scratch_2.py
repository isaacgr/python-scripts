# KNN uses euclidian distance to calculate the distance between points

import numpy as np
import pandas as pd
from math import sqrt
from collections import Counter
import warnings
import random

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
#    print(Counter(votes).most_common(1))
    # Counter returns a key of votes with how many times they occur
    # most_common returns the first key which occurs the most times
    vote_result = Counter(votes).most_common(1)[0][0]
    # returns a list of lists where the fist element is the one that was most common
    return vote_result

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace=True)

df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist()
# get a list of lists
random.shuffle(full_data)

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
#train data is everything except the last 20% of the data
test_data = full_data[-int(test_size*len(full_data)):]
#test_data is the last 20%
for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total =0
for group in test_set:
    for data in test_set[group]:
        vote = k_nearset_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        total += 1

print('Accuracy: ', float(correct)/total)

# one issue with knn is that to compare the closness of a point to the other datapoints, you have to
# compare it to all datapoints in the set
