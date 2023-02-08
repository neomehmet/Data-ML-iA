# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:24:42 2023

@author: mkose

scattorplot
"""
import seaborn as sns
tips = sns.load_dataset("tips")

df = tips.copy()
df.info()
df.head(6)

#sns.scatterplot(x="total_bill", y="tip",data=df)

#sns.scatterplot(x="total_bill", y="tip",hue="day", style="day",data=df)

#sns.scatterplot(x="total_bill", y="tip",hue="time", style="time",data=df)

#sns.scatterplot(x="total_bill", y="tip", size="size",data=df)

#sns.scatterplot(x="total_bill", y="tip", hue="size", size="size",data=df)

#sns.scatterplot(x="total_bill", y="tip",hue="tip",data=df)

sns.scatterplot(x="total_bill", y="tip",size="tip",hue="size",data=df)

