# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:15:28 2020

@author: patricio.a.drasal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:05:16 2020
@author: Administrator
"""
'''nice examples: 
https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot
https://robertmitchellv.com/blog-bar-chart-annotations-pandas-mpl.html
https://python-graph-gallery.com/'''

import pandas as pd
import matplotlib.pyplot as plt

print(plt.style.available)


countries = pd.read_csv('Bases/CountriesPopulation.csv')

countries["Rank"] = countries["year2018"].rank(ascending=False)
countries.head()


# bar plot 
plt.style.use('seaborn')
ax = countries.loc[countries.Rank < 21, ['CountryName', 'year2018']].plot(kind='bar',x='CountryName',
                  y='year2018', rot=90,color='crimson',
                    title='Top 20 Countries by population (in billions)')
plt.xlabel('Country')
plt.tight_layout()

# bar plot sorted
temp=countries.loc[countries.Rank < 21, ['CountryName', 'year2018','Rank']]
ax = temp.sort_values(by=["Rank"]).plot(kind='bar',x='CountryName', y='year2018', rot=90,color='crimson',
                    title='Top 20 Countries by population (in billions)')
plt.xlabel('Country')

# bar plot groupby
ax = countries.groupby('Continent')['year2018'].sum().plot(kind='bar',x='Continent',
                      y='population', rot=90,color='darkgreen',title='Population by Continent')

### gasto público example
#line with some values

gp = pd.read_csv('Bases/gasto-publico-consolidado.csv')

plt.plot(gp['indice_tiempo'], gp['gasto_publico_total'], color='gold', marker='o')
plt.title('Gasto público consolidado % PBI - 1980/2017', fontsize=14)
plt.xlabel('Año', fontsize=14)
plt.ylabel('% PBI', fontsize=14)
plt.text(1983,26,"26", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(1987,35,"35", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(1997,28,"28", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2004,27,"27", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2001,33,"33", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2009,40,"40", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2016,47,"47", color='darkgreen',fontsize='medium',fontweight='bold')
#plt.text(1980,29.04,"29.04", bbox=dict(facecolor='green', alpha=0.5))
plt.grid(True)
plt.show()

# bar plot with values on the bars   
    
gp = pd.read_csv('Bases/gasto-publico-consolidado.csv')
gp1=gp.loc[1:10]
ax = gp1.plot(kind='bar',x='indice_tiempo',color='teal', 
                  y='gasto_publico_total', title='Gasto público consolidado % PBI - 1980/2017')
plt.xlabel('Año')
plt.ylabel('% PBI')
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.15, i.get_height()-5, \
            str(round((i.get_height()), 2)), fontsize=9, color='white',fontweight='bold',
                rotation=90)

# bar plot with values over the bars
   
ax = countries.loc[countries.Rank < 21, ['CountryName', 'year2018']].plot(kind='bar',x='CountryName',
                  y='year2018', rot=90,color='gold',
                    title='Top 20 Countries by population (in billions)')
plt.xlabel('Country')
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.15, i.get_height()-5, \
            str(round((i.get_height()), 2)), fontsize=9, color='black',
                rotation=90)


##### line with some values
    
gp = pd.read_csv('Bases/gasto-publico-consolidado.csv')
ax = gp.plot(kind='line',x='indice_tiempo',color='gold', marker='o', 
                  y='gasto_publico_total', title='Gasto público consolidado % PBI - 1980/2017')
plt.xlabel('Año', fontsize=14)
plt.ylabel('% PBI', fontsize=14)
plt.text(1983,26,"26", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(1987,35,"35", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(1997,28,"28", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2004,27,"27", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2001,33,"33", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2009,40,"40", color='darkgreen',fontsize='medium',fontweight='bold')
plt.text(2016,47,"47", color='darkgreen',fontsize='medium',fontweight='bold')
#plt.text(1980,29.04,"29.04", bbox=dict(facecolor='green', alpha=0.5))
plt.grid(True)
plt.show()


#simple evolution


import numpy as np
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');


## spaghetti plot ####################


# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Make a data frame
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14), 'y10': np.random.randn(10)+range(2,12) })
 
# style
plt.style.use('seaborn-darkgrid')
 
# create a color palette
palette = plt.get_cmap('Set1')
 
# multiple line plot
num=0
for column in df.drop('x', axis=1):
    num+=1
    plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
 
# Add legend
plt.legend(loc=2, ncol=2)
 
# Add titles
plt.title("A (bad) Spaghetti plot", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Time")
plt.ylabel("Score")


