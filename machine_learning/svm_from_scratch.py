# a support vector machine is a supervised machine learning algorithm
# support vectors are the data points nearest to the hyperplane
# typically data is not as organized as a 2d set, so it is necessary to look at the data in 3d
# the hyperplane is no longer a line, but a surface

# the vector w is the vector from the origin to the hyperplane, the vector u is the unknown vector (our unknown datapoint)
# we can say that u lies to the left of the plane if w.u+b <= 0, and to the right if w.u+b >=0 where b is the bias
# u is just a feature set, comprised of x1 and x2
# we know u, but not w or b
# for both a left and right class the equation to derive a support vector is yi(xi.w+b) -1 = 0 (see video 22 for derivation)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors={1:'r', -1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
    # train data
    def fit(self, data):
        self.data = data
        #{ ||w||: [w,b]} is what opt_dict will be
        opt_dict = {}
        transforms = [[1,1], [-1,1], [-1,-1], [1,-1]]
        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value *0.01,
                      self.max_feature_value *0.001]    # point of expense

        b_range_multiple = 5 # extremely expensive
        b_multiple = 5
        latest_optimum = self.max_feature_value * 10 #the first element in w

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            optimized = False # we can do this because convex
            while not optimized:



    def predict(self, features):
        # sign(x.w+b)
        # we want to determine what the sign of the above equation is so we can classify the data
        classification = np.sign(np.dot(np.array(features), self.w)+self.b)

        return classification


data_dict = {-1:np.array([[1,7,],
                           [2,8],
                           [3,8]]),
              1:np.array([[5,1],
                          [6,-1],
                          [7,3]])}
