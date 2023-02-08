# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:20:40 2023

@author: mkose
"""

import seaborn as sns

tips = sns.load_dataset("tips")
df = tips.copy()
sns.catplot(y="total_bill",kind="violin", data=df);
sns.catplot(x="day",y="total_bill",kind="violin", data=df);
sns.catplot(x="day",y="total_bill",kind="violin", hue="sex",data=df);