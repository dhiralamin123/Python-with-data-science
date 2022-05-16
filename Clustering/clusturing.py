# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

data=pd.read_csv("Country-data.csv",usecols=['country','health','gdpp'])
data

data.info()

data.describe()

features=data.iloc[:,1:].values
label=data.iloc[:,0].values

newcountry=pd.get_dummies(data.country)
newcountry

newData=data.iloc[:,1:]
newData

newData=pd.concat([newData,newcountry],axis=1)
newData

from sklearn.cluster import KMeans
model = KMeans(n_clusters=5,
              random_state=9)

model.fit(newData)

group = model.predict(newData)
group

dataResult = newData
dataResult['group'] = group
dataResult.head()

import matplotlib.pyplot as plt

import seaborn as sns
sns.FacetGrid(dataResult,hue='group',size=7) \
    .map(plt.scatter,'health','gdpp') \
    .add_legend()

