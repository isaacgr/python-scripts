import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# we can get an ideal of how many rows (instances) and columns (attributes)
# the data contains with the shape property
print(dataset.shape)
# also a good idea to eyeball the data
print(dataset.head(20))
# we can also look at a summary of each attribute
# this will include the count, mean, min and max values and some percentiles
print(dataset.describe())
# lets take a look at the number of instances that belong to each class
print(dataset.groupby('class').size())

# we now have a basic understanding of the data
# next we want to extend to visualizations and look at two types of plots
# univariate (plots of each individual variable) and multivariate(plots of multiple variables)

# since the plots are numeric, we can use box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# can also create a histogram of each input variable to get an idea of the distribution
# will see that at least two of the input variables have a Gaussian distribution
# can use algorithms to exploit this in the future
dataset.hist()
# can look at scatter plots of all pairs of attributes
# the diagonal grouping of some pairs of attributes suggests a high correlation
scatter_matrix(dataset)

# we are going to split the model into two
# 80% used to train the model and 20% to hold back as a validation set
# allows us to estimate the accuracy of the models that we create on unseen data

random_rows = dataset.sample(frac=1)    # randomize the rows so data does not show in order
array = random_rows.values  # get all the values

X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y, test_size=validation_size, random_state=seed)

# we ill use 10-fold cross validation, which will split the dataset into 10 parts
# it will train on 9 and test on 1 then repeat for all combinations of train-test splits
scoring = 'accuracy'

# create an array of machine learning models to test
models = []
#linear
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
# non-linear
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('LSVM', SVC()))
# evaluate each model
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)   # provides train/test indicies to split datasets
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" %(name, cv_results.mean(), cv_results.std())
    print(msg)

# plot algorithms and compare accuracy
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)

# KNN was the most accurate model so we want to get an idea of the accuracy on our validation set
# its important to keep a validation set in case you overfit to the training data
# we can run the model on the validation set and summarize the results as a
# final accuracy score, confusion matrix and classifcation report
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
# a confusion matrix is a technique to summarize the performance of a classification algorithms
# gives a better idea of what the model is getting right and what types of errors its making
# shows the ways in which your model iss confused when it makes predictions
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
