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
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
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
