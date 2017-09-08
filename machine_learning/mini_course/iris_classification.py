import pandas
from pandas.tools.plotting import scatter_matrix
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
