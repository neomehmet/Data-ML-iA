# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:54:58 2023

@author: mkose
"""

import seaborn as sns

iris = sns.load_dataset("iris")

df = iris.copy()

print(df.info(),"\n")

print(df.dtypes,"\n")

print(df.shape,"\n")

sns.pairplot(df,hue="species")

print(df.describe(include ="all").T)

sns.pairplot(df,hue="species",markers=["o","D","s",])


sns.pairplot(df, kind="reg")

sns.pairplot(df, kind="reg", hue="species"  )
 