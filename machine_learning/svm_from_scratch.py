# a support vector machine is a supervised machine learning algorithm
# support vectors are the data points nearest to the hyperplane
# typically data is not as organized as a 2d set, so it is necessary to look at the data in 3d
# the hyperplane is no longer a line, but a surface

# the vector w is the vector from the origin to the hyperplane, the vector u is the unknown vector (our unknown datapoint)
# we can say that u lies to the left of the plane if w.u+b <= 0, and to the right if w.u+b >=0 where b is the bias
# u is just a feature set, comprised of x1 and x2
# we know u, but not w or b
# for both a left and right class the equation to derive a support vector is yi(xi.w+b) -1 = 0 (see video 22 for derivation)
# we want to maximize the width between the support vectors to find the best supporting hyperplane
# width = 2/||w|| (see video 23) so we want to minimize w
# we want to maximize b (the bias)

# the decision boundary is the seperating hyperplane (seperates the positive and negative classes)
# the equation for the classification is the sign(xi.w +b) (see video 24)
# essentially for SVM class(knownfeatures.w +b)>=1
# SVM is a convex problem

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors={1:'r', -1:'b'}
        if self.visualization:
            self.fig = plt.figure() # just establishing the plot figure
            self.ax = self.fig.add_subplot(1,1,1)   # 1x1 grid with one plot
    # train data (optimize to find w and b)
    def fit(self, data):
        self.data = data
        # { ||w||: [w,b]} is what opt_dict will be
        # we will find the key that has the lowest magnitude, and the value of that key will be our answer
        opt_dict = {}
        transforms = [[1,1], [-1,1], [-1,-1], [1,-1]]
        # these are what will be applied to w (dot w with the transforms)
        # we need to test all cases where the values of w are positvie and negative
        # SVM could be oriented differently
        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)    # all_data just holds all features
        self.max_feature_value = max(all_data)  # want to maximize b
        self.min_feature_value = min(all_data)  # want to minimize w
        all_data = None

        # support vectors yi(xi.w +b) = 1
        # will know that youve found a good value for w and b when in both positivie and negative classes you have a value close to 1
        # want to take large stpes, and decrease those steps as we get closer to the minimum value of w
        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value *0.01,
                      self.max_feature_value *0.001]    # point of expense

        b_range_multiple = 5 # extremely expensive
        # dont need to take as small of steps with b as we do with w
        b_multiple = 5
        # find the largest value, and then make w equal to that number
        latest_optimum = self.max_feature_value * 10 # the first element in w

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            optimized = False # we can do this because convex (we know when we've been optimized)
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_range_multiple), self.max_feature_value*b_range_multiple, step*b_multiple):
                    for transformation in transforms:
                        w_t = w*transformation
                        found_option = True
                        for i in self.data:
                        # weakest link in svm fundamentally
                        # SMO attempts to fix this
                        # yi(xi.w+b)>=1 is the constraint function
                            for xi in self.data[i]:
                                yi=i
                                if not yi(np.dot(w_t, xi)+b)>=1:
                                    found_option = False
                                    break
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]    # magnitude of the vector
                if w[0] < 0: # if we get as close as possibel to the smallest part of the convex taking our current steps
                    optimized = True
                    print('Optimized a Step')
                else:
                    w = w - step    # if not optimized, take another step
            norms = sorted([n for n in opt_dict])   # sorting the list of magnitudes lowest to highest
            opt_choice = opt_dict[norms[0]] # this is the optimal choice
            # ||w|| :[w,b]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step*2

    def predict(self, features):
        # sign(x.w+b)
        # we want to determine what the sign of the above equation is so we can classify the data
        classification = np.sign(np.dot(np.array(features), self.w)+self.b) # need to optimize for w and b
        if classification !=0 and self.visulalization:
            self.ax.scatter(features[0], features[1], s=200, marker = *, c=self.colors[classification])
        return classification

    def visualize(self):
        [self.ax.scatter(x[0], x[1], s=100, color=self.colors[i]) for x in data_dict[i] for i in data_dict]
        # hyperplane = x.w + b
        # v = x.w +b
        def hyperplane(x,w,b, v):

# keys are the class, arrays are the features
data_dict = {-1:np.array([[1,7,],
                           [2,8],
                           [3,8]]),
              1:np.array([[5,1],
                          [6,-1],
                          [7,3]])}
