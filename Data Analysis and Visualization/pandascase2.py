# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:42:21 2021

@author: Monak
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#1
data12=pd.read_csv("middle_tn_schools.csv")

#2

print("Total Coloumns : ",len(data12.columns))
print("Total Row : ",len(data12['name']))


#3
plt.plot(data12['name'],data12['size'],"o-")
plt.title("line plot")
plt.xlabel("name")
plt.ylabel("size")
plt.show()



colors=["r","g","b","k","c","orange","purple","yellow"]
plt.bar(data12["name"],data12["size"], color=colors)
plt.title("bar plot")
plt.xlabel("name")
plt.ylabel("size")
plt.show()

# barh plot

colors=["r","g","b","k","c","orange","purple","yellow"]
plt.barh(data12["name"],data12["size"], color=colors)
plt.title("Horizontal bar plot")
plt.xlabel("name")
plt.ylabel("size")
plt.show()


# scatter plot

colors=["r","g","b","k","c","orange","purple","yellow"]
plt.scatter(data12["name"],data12["size"], s=100, marker="s")
plt.title("Scatter Plot")
plt.xlabel("name")
plt.ylabel("size")
plt.show()


# pie plot
#print(data12["school_rating"].values)

l=data12["school_rating"].values
dic=dict()

for i in l:
    if i in dic.keys():
        dic[i]=dic.get(i)+1
    else:
        dic[i]=1

#print(dic)

plt.pie(dic.values(),labels=dic.keys())
plt.show()


# histogram

plt.hist(data12["size"])
plt.show()


#4

ans=data12[['reduced_lunch', 'school_rating']].corr()
print(ans)


#5
dg=data12.groupby(['school_rating'])
for schoolrating,data12 in dg:
    print(schoolrating)
    print("-"*10)
    print(data12)
    print("="*60)

# Aggregation
# [1] Count
cnt = data12.groupby(['school_rating']).size() 
print("Count=\n",cnt)
print("===========================================")

#[2] sum
sumred=data12.groupby(['school_rating']).reduced_lunch.sum()
print("Sum of reduced lunch by school rating Wise:\n",sumred)
print("===========================================")
   

# [3] mean

avgred=data12.groupby(['school_rating']).reduced_lunch.mean()
print("Average reduced lunch by school rating Wise:\n",avgred)
print("===========================================")
 
# [4] max

maxred=data12.groupby(['school_rating']).reduced_lunch.max()
print("Maximum  reduced lunch by school rating Wise:\n",maxred)
print("===========================================")

# [5] min

minred=data12.groupby(['school_rating']).reduced_lunch.min()
print("Minimum reduced lunch by school rating Wise:\n",minred)
print("===========================================")
