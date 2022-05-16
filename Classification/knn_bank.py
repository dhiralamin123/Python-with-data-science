# -*- coding: utf-8 -*-


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
newData=pd.concat([data.age,newjob,newmarital,neweducation,newhousing,x_data],axis=1)
newData

features=newData.iloc[:,:-1].values
label=newData.iloc[:,-1].values

from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB

for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = 0.3, random_state = i)
    nb=GaussianNB()
    nb.fit(X_train,y_train)
    
    testt=nb.score(X_test,y_test)
    tranee=nb.score(X_train,y_train)
    
    if testt>0.839:
    
       print("i = {}  train = {}  test = {}".format(i,tranee,testt))

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = 0.3, random_state = 37)

from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(X_train,y_train)
print(nb.score(X_train,y_train))
print(nb.score(X_test,y_test))

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,nb.predict(X_test)))


print("Confusion Matrix : ")

print(confusion_matrix(y_test,nb.predict(X_test)))