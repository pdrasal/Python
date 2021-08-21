# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 03:25:39 2020
@author: patricio.a.drasal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

gdp_percent = pd.read_csv('Bases/GDP growth (annual %).csv')
gdp_percent=gdp_percent.fillna(0)
new_df=gdp_percent.melt(id_vars=['Country Name'])
new_df=new_df.rename(columns={"Country Name": "Country", "variable": "Periodo","value":"Percent"})
new_df=new_df.pivot(index='Periodo', columns='Country', values='Percent')

temp=new_df.loc['2010':, ['Haiti','Argentina']]
plt.style.use('ggplot')
temp.plot(kind='bar',subplots='true',sharex=all, sharey=all)
plt.ylabel('% GROWTH',fontsize=14)
plt.xlabel('YEAR',fontsize=14)
plt.suptitle('Source: World Bank',fontsize=10,va='bottom',y=-0.08,x=0.9)
plt.title('GDP ANNUAL GROWTH % - 2010 / 2019',fontsize=18,va='top',y=2.4,x=0.5)


temp=new_df.loc['1960':, ['Haiti','India']]
plt.style.use('ggplot')
temp.plot(title='GDP Anual growth 1961 - 2019')

plt.style.use('seaborn-dark-palette')
temp.plot(kind='line',subplots='true',title='GDP Anual growth 1961 - 2019', sharex=all, sharey=all)

plt.style.use('ggplot')
temp.plot(kind='bar',subplots='true',
          title='GDP PER CAPITA (US$) - 1960 / 2019', sharex=all, sharey=all)


temp=new_df.loc['1990':, ['Haiti','India']]
plt.style.use('ggplot')
temp.plot(kind='bar',subplots='true',
          title='GDP per capita US$ - 1990 / 2019', sharex=all, sharey=all)
