# -*- coding: utf-8 -*-
"""
Created on Sun May 17 01:54:06 2020

@author: Administrator
"""
import pandas as pd
df=pd.read_json (r'./Bases/worldpopulation.json')
print(df)
df.info()
df.corr()

import seaborn.apionly as sns
sns.heatmap(df.corr(), annot=True)

df.loc[0:9]
df[0:10] 

df.loc[df.Rank < 11, ['Rank', 'country','population']]
# or
df[df.Rank < 11]

new_df = df.loc[df['Rank'] < 10] 
df_2=df.loc[df['Rank'] > 173] 

ax = new_df.plot.bar(x='country', y='population', rot=90)
ax = df_2.plot.bar(x='country', y='population', rot=90)


total=sum(df.population)
df['percentage'] = round(df['population'] / total*100,2)

data1 = df.query("Rank < 11 ")

ax = data1.plot.bar(x='country', y='percentage', rot=90,color='darkgreen',
                    title='Top 10 World Countries population')

df=pd.read_json (r'./Bases/worldpopulation.json')
df

data2010 = df.query("Rank == 1 & country == 'China'")
data2010.head()
