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

# load the dataset and give column names
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-testing.data"

names = ['Suit 1', 'Rank 1', 'Suit 2', 'Rank 2','Suit 3', 'Rank 3',
            'Suit 4', 'Rank 4', 'Suit 5', 'Rank 5', 'Class']
dataset = pandas.read_csv(url, names=names)

# can get a good idea of how many rows (instances) and columns (attributes)
# the dataset contaikns
print(dataset.shape)
# good to eyeball the data
print(dataset.head(10))
# can look at a summary of the dataset to get an idea of the mean, min, max,
# and some percentiles
print(dataset.describe())
# take a look at the number of instances that belong to each class
print(dataset.groupby('Class').size())

# now that we have a better understanding of the data, we want to extend to visualizations
# we will look at univariate plots (plots of an individual variable) and multivariate plots

# since the data is numeric, we can use a box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(4,3), sharex=False, sharey=False)
# can also create a histogram of the data to get an idea of the distribution of the attributes
dataset.hist()
# can also look at scatter plots of all pairs of attributes
# diagonal grouping implies a high correlation
scatter_matrix(dataset)

# it is important to get a visual of the data before proceeding to train your classification_report
# the above are good steps to follow for basic machine learning algorithm implementaion
# load a dataset, apply names to the columns, get an idea of size and features and
# get an idea of the statistical attributes
# plot the data to see correlation between attributea and a visual representation of the distribution

###############################

random_rows = dataset.sample(frac=1) # randomize the rows so the data does not show in order
array = random_rows.values # get all the values

X = array[:,0:10] # features are everything except the class
Y = array[:,10]

validation_size = 0.20  # use 20% of the data as the validation setInterval
seed = 7

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# will use 10 fold cross validaion to split the data into 10 parts
# will train on 9 and test against 1 and will repeat for all train-test splits

# create an array of machine learning models to test against
models = []
# linear models
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
# non linear models
models.append(('CART', DecisionTreeClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('SVC', SVC()))

# want to evaluate each model
results = []
names = []

for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)   # provides train/test indicies to split the data
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    message = '%s: %s %s' % (name, cv_results.mean(), cv_results.std())
    print(message)
