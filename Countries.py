# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:05:16 2020
@author: Administrator
"""
import pandas as pd
import numpy as np

df=pd.read_json (r'./Bases/worldpopulation.json')
df

df.info()
df.head()
df.describe()
### matrix de correlacion
df.corr()

total=sum(df.population)
df['percentage'] = round(df['population'] / total*100,2)

data1 = df.query("Rank < 11 ")

ax = data1.plot.bar(x='country', y='percentage', rot=90,color='darkgreen',
                    title='Top 10 World Countries population')
data1
#Combining Datasets: Merge and Join

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
'salary': [70000, 80000, 120000, 90000]})
print(df1); print(df2);print(df3);

print(pd.merge(df1, df2))
#or
pd.merge(df1, df3, left_on="employee", right_on="name")
pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1)

#Aggregation and Grouping
#An essential piece of analysis of large data is efficient summarization: computing
#aggregations like sum(), mean(), median(), min(), and max(), in which a single number
#gives insight into the nature of a potentially large dataset.

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
'data': range(6)}, columns=['key', 'data'])
df

df.groupby('key').sum()
df.groupby('key').aggregate(['min', np.median, max])

dfpopulation=pd.read_json (r'./Bases/worldpopulation.json')
dfcountries=pd.read_json (r'./Bases/country-by-continent.json')

dfpopulation.describe()
dfcountries.info()
dfcountries.head()
dfcountries.describe()

df3=pd.merge(dfpopulation, dfcountries)
df3

data2 = df3.query("Rank < 11 ")

data2
ax = data2.plot.bar(x='country', y='population', rot=90,color='darkgreen',
                    title='Top 10 World Countries population')

countries = pd.read_csv('Bases/CountriesPopulation.csv')
countries
countries.head()
countries.info()
### data type conversion
countries.fillna(0)


countries['CountryName']
countries[countries.CountryName== 'Aruba']
countries.loc[countries.CountryName== 'Aruba', ['CountryName', 'CountryCode','year2018']]

countries.loc[countries.year2018 > 100000000, ['CountryName', 'year2018']]

countries["Rank"] = countries["year2018"].rank(ascending=False)
countries.head()
countries[countries.Rank ==1]

ax = countries.loc[countries.Rank < 21, ['CountryName', 'year2018']].plot.bar(x='CountryName', y='year2018', rot=90,color='darkgreen',
                    title='Top 20 Countries by population')

temp=countries.loc[countries.Rank < 21, ['CountryName', 'year2018','Rank']]

ax = temp.sort_values(by=["Rank"]).plot.bar(x='CountryName', y='year2018', rot=90,color='darkgreen',
                    title='Top 20 Countries by population')

countries.groupby('Continent')['year2018'].sum()

countries.groupby('Continent')['year2018'].aggregate(['min', np.median, max])

ax = countries.groupby('Continent')['year2018'].sum().plot.bar(x='Continent',
                      y='population', rot=90,color='darkgreen',title='Population by Continent')


