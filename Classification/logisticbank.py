# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:21:13 2021

@author: Monak
"""


import numpy as np
import pandas as pd

data=pd.read_csv("bank-additional-full.csv")
data

data.info()

data.describe()

newdata=data['age']

newjob=pd.get_dummies(data.job)
newmarital=pd.get_dummies(data.marital)
neweducation=pd.get_dummies(data.education)
newhousing=pd.get_dummies(data.housing)

x_data=data.iloc[:,15:]
#x_data
newData=pd.concat([data.age,newjob,newmarital,neweducation,newhousing,x_data],axis=1)
print(newData)

from sklearn import preprocessing
 
label_encoder = preprocessing.LabelEncoder()
newData['y']= label_encoder.fit_transform(newData['y'])


features=newData.iloc[:,:-1].values
print(features)
label=newData.iloc[:,-1].values
print(label)

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = 0.2, random_state = 5)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)

print(lr.score(X_train,y_train)) #Known data
print(lr.score(X_test,y_test)) #Unknown data

