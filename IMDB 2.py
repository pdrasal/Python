# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 03:25:39 2020
@author: patricio.a.drasal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

#title.ratings.tsv.gz – Contains the IMDb rating and votes information for titles
 #tconst (string) - alphanumeric unique identifier of the title
 #averageRating – weighted average of all the individual user ratings
 #numVotes - number of votes the title has received

ratings = pd.read_csv('Bases/title.ratings.tsv.gz', compression='gzip', header=0,sep='\t')
ratings

ratings.info()

#title.basics.tsv.gz
 #title.basics.tsv.gz - Contains the following information for titles:
 #tconst (string) - alphanumeric unique identifier of the title
 #titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
 #primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
 #originalTitle (string) - original title, in the original language
 #isAdult (boolean) - 0: non-adult title; 1: adult title
 #startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
 #endYear (YYYY) – TV Series end year. ‘\N’ for all other title types
 #runtimeMinutes – primary runtime of the title, in minutes
 #genres (string array) – includes up to three genres associated with the title

import time
start = time.time()
titles = pd.read_csv('Bases/title.basics.tsv.gz', compression='gzip', header=0,sep='\t')
end = time.time()
print("Read csv with dask: ",(end-start),"sec")


col_list = ["tconst", "titleType","primaryTitle","startYear","genres"]
titles = pd.read_csv('Bases/title.basics.tsv.gz', compression='gzip', header=0,sep='\t',usecols=col_list)

titles.info()
titles.head()
titles.describe()

titles.titleType.unique()

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