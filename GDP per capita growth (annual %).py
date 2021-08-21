# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 03:25:39 2020
@author: patricio.a.drasal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

gdp_pc = pd.read_csv('Bases/GDP per capita growth (annual %).csv')
gdp_pc=gdp_pc.fillna(0)
gdp_pc
new_df=gdp_pc.melt(id_vars=['Country Name'])
new_df=new_df.rename(columns={"Country Name": "Country", "variable": "Periodo","value":"Percent"})
new_df
new_df=new_df.pivot(index='Periodo', columns='Country', values='Percent')


temp=new_df.loc[:,['India','Turkey','Argentina']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita current annual growth % - 1961 / 2019')
plt.ylabel('US$')
plt.xlabel('Year')
plt.suptitle('Source: World Bank',fontsize=8,va='bottom',y=0,x=0.8)
plt.show()

temp=new_df.loc['1990':, ['India','Turkey','Argentina']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita current annual growth % - 1990 / 2019')
plt.ylabel('US$')
plt.xlabel('Year')
plt.suptitle('Source: World Bank',fontsize=9,va='bottom',y=0,x=0.8)
plt.show()


temp=new_df.loc['1990':,['India','Russian Federation','Turkey','Argentina']]
plt.style.use('seaborn-dark-palette')
temp.plot(kind='line',subplots='true',title='GDP per capita current annual growth % - 1961 / 2019', sharex=all, sharey=all,fontsize=12)


temp=new_df.loc[:,['India','Russian Federation','Turkey','Argentina']]
plt.style.use('seaborn-dark-palette')
temp.loc['1990':].plot(kind='bar',subplots='true',
          title='GDP per capita annual growth % - 1990 / 2019', sharex=all, sharey=all)



temp=new_df.loc[:,['Argentina','Haiti']]
plt.style.use('ggplot')
temp.plot(title='GDP per capita annual growth % - 1961 / 2019')
plt.ylabel('US$')
plt.xlabel('Year')
plt.suptitle('Source: World Bank',fontsize=8,va='bottom',y=0,x=0.8)
plt.show()

temp=new_df.loc['2010':, ['Argentina','Haiti','India']]
plt.style.use('seaborn-dark-palette')
temp.plot(title='GDP per capita - annual growth % - 2010 / 2019')
plt.ylabel('% annual growth')
plt.xlabel('Year')
plt.suptitle('Source: World Bank',fontsize=9,va='bottom',y=0,x=0.8)
plt.show()


temp=new_df.loc[:,['India','Haiti','Argentina']]
plt.style.use('seaborn-dark-palette')
temp.plot(kind='line',subplots='true',title='GDP PER CAPITA ANNUAL GROWTH % - 1961 / 2019', sharex=all, sharey=all,fontsize=12)
plt.suptitle('Source: World Bank',fontsize=9,va='bottom',y=0,x=0.8)

temp=new_df.loc['2010':, ['India','Haiti','Argentina']]
plt.style.use('ggplot')
temp.loc['1990':].plot(kind='bar',subplots='true',title='GDP PER CAPITA ANNUAL GROWTH % - 2010 / 2019',
           sharex=all, sharey=all,fontsize=12)
plt.ylabel('% GROWTH',fontsize=14)
plt.xlabel('YEAR',fontsize=14)
plt.suptitle('Source: World Bank',fontsize=9,va='bottom',y=-0.05,x=0.8)

plt.style.available