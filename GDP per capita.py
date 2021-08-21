# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 03:25:39 2020
@author: patricio.a.drasal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

gdp_pc = pd.read_csv('Bases/GDP per capita current US$.csv')
gdp_pc=gdp_pc.fillna(0)
new_df=gdp_pc.melt(id_vars=['Country Name'])
new_df=new_df.rename(columns={"Country Name": "Country", "variable": "Periodo","value":"US$"})
new_df=new_df.pivot(index='Periodo', columns='Country', values='US$')

temp=new_df.loc[:,['India','Haiti']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita current US$ 1961 / 2019')
plt.ylabel('US$',fontsize=18)
plt.xlabel('YEAR',fontsize=18)
plt.suptitle('Source: World Bank',fontsize=8,va='bottom',y=0,x=0.8)
plt.show()

temp=new_df.loc[:,['India','Haiti']]
plt.style.use('seaborn-dark-palette')
temp.plot(kind='line',subplots='true',title='GDP per capita current US$ - 1961 / 2019', sharex=all, sharey=all)

temp=new_df.loc['1990':, ['India','Haiti']]
plt.style.use('ggplot')
temp.plot(kind='bar',subplots='true',
          title='GDP per capita current US$ - 1990 / 2019', sharex=all, sharey=all)


########### Ranking #######


gdp_pc = pd.read_csv('Bases/GDP per capita current US$.csv')
gdp_pc=gdp_pc.fillna(0)
gdp_pc["Rank"] = gdp_pc['2019'].rank(ascending=False)
gdp_pc[gdp_pc.Rank <21].sort_values(by=["Rank"])
new=gdp_pc[['Country Name','2019','Rank']].sort_values(by=["Rank"])

new


ax = new.loc[new.Rank < 21, ['Country Name', '2019']].plot.bar(x='Country Name', y='2019', rot=90,color='darkgreen',
                    title='Top 20 Countries GDP per capita current US$ - 1919)

temp=countries.loc[countries.Rank < 21, ['CountryName', 'year2018','Rank']]

ax = temp.sort_values(by=["Rank"]).plot.bar(x='CountryName', y='year2018', rot=90,color='darkgreen',
                    title='Top 20 Countries by population')