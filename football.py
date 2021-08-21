# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:05:16 2020
@author: Administrator
"""
import pandas as pd

### matrix de correlacion

df = pd.read_csv('Bases/england-premier-league-players-2018-to-2019-stats.csv')
df
df.head()
df.info()
df.corr()

### data type conversion
df.fillna(0)

df.describe()
df.sort_values("goals_overall", ascending=False)
df.goals_overall

df[["full_name", "goals_overall"]].sort_values("goals_overall", ascending=False)


new=df[['full_name','goals_overall','assists_overall','Current Club','nationality','position']]
new
new[new['goals_overall'] > 10].sort_values("goals_overall", ascending=False)
new.sort_values("goals_overall", ascending=False)
new.sort_values(["goals_overall", "assists_overall"],ascending=[False, False])

grouped=new.groupby('nationality')['goals_overall'].sum().reset_index()

grouped = df.groupby('mygroups').sum().reset_index()
grouped.sort_values('goals_overall', ascending=False)


