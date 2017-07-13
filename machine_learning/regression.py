import pandas as pd
import quandl
import math, datetime, time
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] *100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] *100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)
# Dont want to work with N/A data in machine learning. Better to treat as an outlier so as not to sacrifice data.

forecast_out = int(math.ceil(.01*len(df)))
# Number of days out. Try to predict out 1% of the dataframe

df['label'] = df[forecast_col].shift(-forecast_out)
# The label column for each row will be the adjusted close price 1% in the future
# Adds 1% new rows with NaN values
# shift will shift the columns up

X = np.array(df.drop(['label'], 1))
# Creates array
# Features of df without label

X = preprocessing.scale(X)
# Scaling X featurese before it is fed to the classifier
# Forces the features to looks more or less like noramlly distributed data (Gaussian with zero mean and variance)
# In reality the value needs to be scaled with other data, as well as with the training data

X = X[:-forecast_out]
X_lately = X[-forecast_out:]
# X has all values up until forecast_out
# X_lately has all values of forecast_out
# Dont have a y value for X_lately

df.dropna(inplace=True)
y = np.array(df['label'])
# y is only the label features

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
# Test_size represents the portion of the dataset to include in the test split
# Essentially holding out part of the data as a test set to avoid overfitting the data
# X_train, y_train which is used for learning the parameters of a predictive model
# and a testing set X_test, y_test which is used for evaluating the fitted predictive model.


clf = LinearRegression()
clf.fit(X_train, y_train)
# Can use this classifier to predict into the future
# fit the test data (average together)
accuracy = clf.score(X_test, y_test)
# Accuracy or Confidence

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)
# Will output the next 30 days of stock prices, the accuracy and how many days we are forecasting out

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple())
one_day = 86400
next_unix = last_unix +one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] =[np.nan for _ in range(len(df.columns) -1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Features are the attributes that make up the label (feature is input, label is output)
# Regression analysis is a statistical process for estimating the relationships
# among variables
# Linear regression models the relationship between y and one or more x variables. The relationships
# are modelled using linear predictor funcitons

# From the documentaion for the module, n_jobs determines number of threads to use for computation

# Pickling will allow you to save your classifier so it can be loaded without having to constantly train against
# large amounts of data
