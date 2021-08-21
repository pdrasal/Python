# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 03:25:39 2020
@author: patricio.a.drasal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

gdp_pc = pd.read_csv('Bases/GDP per capita current US$.csv')
gdp_pc=gdp_pc.fillna(0)
new_df=gdp_pc.melt(id_vars=['Country Name'])
new_df=new_df.rename(columns={"Country Name": "Country", "variable": "Periodo","value":"US$"})
new_df=new_df.pivot(index='Periodo', columns='Country', values='US$')

temp=new_df.loc[:,['India','Haiti']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita US$ - 1961 / 2019')
plt.ylabel('US$',fontsize=18)
plt.xlabel('YEAR',fontsize=18)
plt.suptitle('Source: World Bank',fontsize=8,va='bottom',y=0,x=0.8)
plt.show()


temp=new_df.loc[:,['Russian Federation','Turkey','Argentina']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita US$ - 1961 / 2019')
plt.ylabel('US$',fontsize=18)
plt.xlabel('YEAR',fontsize=18)
plt.suptitle('Source: World Bank',fontsize=8,va='bottom',y=0,x=0.8)
plt.show()


temp=new_df.loc[:,['Lithuania','Latvia','Estonia','World']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita US$ - 1961 / 2019')
plt.ylabel('US$',fontsize=18)
plt.xlabel('YEAR',fontsize=18)
plt.suptitle('Source: World Bank',fontsize=8,va='bottom',y=0,x=0.8)
plt.show()

temp=new_df.loc[:,['World','Argentina']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita US$ - 1961 / 2019')
plt.ylabel('US$',fontsize=18)
plt.xlabel('YEAR',fontsize=18)
plt.suptitle('Source: World Bank',fontsize=8,va='bottom',y=0,x=0.8)
plt.show()


temp=new_df.loc[:,['India','Haiti']]
plt.style.use('seaborn-dark-palette')
temp.plot(kind='line',subplots='true',title='GDP per capita US$ - 1961 / 2019', sharex=all, sharey=all)

temp=new_df.loc['1990':, ['Haiti','India']]
plt.style.use('ggplot')
temp.plot(kind='bar',subplots='true',
          title='GDP per capita US$ - 1990 / 2019', sharex=all, sharey=all)


temp=new_df.loc[:, ['India','Haiti']]
plt.style.use('ggplot')
temp.plot(kind='bar',subplots='true',
          title='GDP PER CAPITA (US$) - 1960 / 2019', sharex=all, sharey=all)

temp=new_df.loc['1960':, ['Argentina','India']]
plt.style.use('ggplot')
temp.plot(kind='bar',subplots='true',
          title='GDP PER CAPITA (US$) - 1960 / 2019', sharex=all, sharey=all)


temp=new_df.loc[:,['Russian Federation','Turkey','Argentina']]
plt.style.use('seaborn-dark-palette')
temp.loc['1990':].plot(kind='line',subplots='true',
          title='GDP per capita annual growth % - 1990 / 2019', sharex=all, sharey=all)


########### Ranking #######


gdp_pc = pd.read_csv('Bases/GDP per capita current US$.csv')
gdp_pc=gdp_pc.fillna(0)
gdp_pc["Rank"] = gdp_pc['2019'].rank(ascending=False)
top_gdp=gdp_pc[['Country Name','2019','Rank']].sort_values(by=["Rank"])

ax = top_gdp.loc[top_gdp.Rank < 21, ['Country Name', '2019']].plot.bar(x='Country Name', y='2019', rot=90,color='darkgreen',
                    title='Top 20 Countries GDP per capita US$ - 2019')

temp=top_gdp.loc[top_gdp.Rank < 21, ['Country Name', '2019']]
plt.style.use('seaborn-poster')
temp.plot(kind='bar',title='Top 20 Countries by GDP per capita US$ - 2019', x='Country Name', y='2019', rot=90,color='darkgreen')


plt.style.available