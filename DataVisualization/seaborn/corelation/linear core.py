# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:24:42 2023

@author: mkose

scattorplot
"""
import seaborn as sns
import matplotlib as plt

tips = sns.load_dataset("tips")

df = tips.copy()


sns.lmplot(x="total_bill",y="tip", data=df)

sns.lmplot(x="total_bill",y="tip", hue="time",data=df) 

sns.lmplot(x="total_bill",y="tip", hue="smoker", col="time" ,data=df) 

sns.lmplot(x="total_bill",y="tip", hue="smoker", 
           col="time", row="sex" ,data=df) 


