# in reality the you are never dealing with linearly seperable data
# the data may be scattered and cluttered together
# to help seperate the data we can add another feature (dimension) to our graph
# this adds complexity becuase the SVM does not handle non-linesar very well (it can take time to process)

# can use kernels to transform the non-linesar data into linear data by finding similarities
# betweeen features and creating another feature

# kernels use the inner (dot) product of two vectors
# can increase dimensions without a large increase in processing cost
# similarity function, not unique to the SVM
# projection of X1 onto X2

# K(x,x`) = z.z` -> z = function(x), z` = function(x`)

# given a feature set [x1,x2] the new z space is z=[1,x1,x2,x1^2, x2^2, x1x2]
# we convert the feature set to a second order polynomial, then take the inner product of z and z`
# we can now say that K(x,x`) = (1+x*x`)^p where p=2

# with non-linear data you want to watch out for overfitment
# having a lot of data that perfectly fit support vector lines
# better to have less data that is actually a sv
# In overfitting, a statistical model describes random error or noise instead of the underlying relationship

# soft margin svm has some error between seperating data points
# can introduce a new variable, Slack (e)
# so now the equeation of our svm is yi(xi.w +b) >= 1 - e
# we want to minimize the slack, minimize = 1/2||w||^2 + C*sum(e)
# if we raise C, then we are going to punish more for violations of the margin
