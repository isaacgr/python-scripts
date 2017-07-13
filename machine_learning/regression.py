import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] *100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] *100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)
# Dont want to work with N/A data in machine learning. Better to treat as an outlier so as not to sacrifice data.

forecast_out = int(math.ceil(.01*len(df)))
# Number of days out. Try to predict out 10% of the dataframe

df['label'] = df[forecast_col].shift(-forecast_out)
# The label column for each row will be the adjusted close price 1% in the future
# shift will shift the columns up
df.dropna(inplace=True)
print(df.head())

# Features are the attributes that make up the label (feature is input, label is output)
# Regression analysis is a statistical process for estimating the relationships
# among variables
# Linear regression models the relationship between y and one or more x variables. The relationships
# are modelled using linear predictor funcitons
