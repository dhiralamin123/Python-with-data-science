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
#x_data
newData=pd.concat([data.age,newjob,newmarital,neweducation,newhousing,x_data],axis=1)
newData

features=newData.iloc[:,:-1].values
label=newData.iloc[:,-1].values

from sklearn.model_selection import train_test_split 
from sklearn import svm

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = 0.2, random_state = 5)

sv = svm.SVC(kernel='linear') # Linear Kernel
sv.fit(X_train, y_train)
print(sv.score(X_train,y_train))
print(sv.score(X_test,y_test))

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,sv.predict(X_test)))


print("Confusion Matrix : ")

print(confusion_matrix(y_test,sv.predict(X_test)))