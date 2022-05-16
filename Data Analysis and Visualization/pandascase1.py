# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:15:32 2021

@author: Monak
"""

import pandas as pd
import numpy as np
#1 
print('\n Ans : 1 ')
data12=pd.read_excel("coalpublic2013.xlsx")
print(data12)

#2
print('\n Ans : 2 ')
data12.dtypes
print(data12.dtypes)

#3
print('\n Ans : 3 ')
cols=[2,3]
data12_3=pd.read_excel("coalpublic2013.xlsx", usecols=cols)
print(data12_3)

#4
print('\n Ans : 4 ')

print("Sum: ",data12["Production"].sum()) 
print("Mean: ",data12["Production"].mean())
print("Maximum: ",data12["Production"].max())
print("Minimum: ",data12["Production"].min()) 

#5
print('\n Ans : 5 ')
data12.insert(5, "column6", np.nan)
print(data12.info())
 

#6
print('\n Ans : 6 ')
data12_6 = pd.read_excel('coalpublic2013.xlsx', skiprows = 20)
print(data12_6)

#7

print('\n Ans : 7 ')
sum_row=data12[["Production", "Labor_Hours"]].sum()
data12_sum=pd.DataFrame(data=sum_row).T
data12ans=data12_sum.reindex(columns=data12.columns)
print(data12ans)

#8
print('\n Ans : 8 ')
data12 = pd.read_excel('coalpublic2013.xlsx')
data12.tail(n=10)
print(data12.tail(10))

#9
print('\n Ans : 9 ')
data12 = pd.read_excel('coalpublic2013.xlsx')
data12_sub=data12[["MSHA ID","Labor_Hours"]].groupby('MSHA ID').sum()
print(data12_sub)

#10
print('\n Ans : 10 ')
data12 = pd.read_excel('coalpublic2013.xlsx')    
ans=data12[data12["MSHA ID"]==103155]
print(ans)


#11
print('\n Ans : 11 ')  
ans=data12[data12["Labor_Hours"] > 20000]
print(ans)


#12
print('\n Ans : 12 ')    
ans=data12[data12["Mine_Name"].map(lambda x: x.startswith('P'))].head()
print(ans)

#13
print('\n Ans : 13 ')    
ans=data12[data12["MSHA ID"].isin([102976,103380])]
print(ans)

#14
print('\n Ans : 14 ')    
print(data12.query('Mine_Name == ["Cane Creek Mine", "Piney Woods Preparation Plant"]'))
