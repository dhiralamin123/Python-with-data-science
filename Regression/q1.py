# -*- coding: utf-8 -*-


# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

data = pd.read_csv('F:/solved case bright/Regression/mlr01.csv')
data.head()

data.info()

data.describe()

features = data.iloc[:,:-1].values
label = data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,
                                                label,
                                                test_size=0.2,
                                                random_state=10)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)

print(lr.score(X_train,y_train)) #Known data
print(lr.score(X_test,y_test)) #Unknown data

