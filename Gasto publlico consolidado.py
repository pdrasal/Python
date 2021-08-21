# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:05:16 2020
@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gp = pd.read_csv('Bases/gasto-publico-consolidado.csv')
gp
gp.head()
gp.info()


ax = gp.loc[gp.indice_tiempo > 2000, ['indice_tiempo', 'gasto_publico_total']].plot.bar(x='indice_tiempo', y='gasto_publico_total', rot=90,color='darkgreen',
                    title='Top 10  by year')

ax = gp.plot.bar(x='indice_tiempo', y='gasto_publico_total',rot=90,
                 title='Gasto público consolidado % PBI - 1980/2017')

ax = gp.plot.line(x='indice_tiempo', y='gasto_publico_total',marker='o',grid='true',
                  rot=90,color='darkgreen',title='Gasto público consolidado % PBI 1980 - 2017')

ax = gp.plot.scatter(x='indice_tiempo', y='gasto_publico_total',rot=90,
                 title='Gasto público consolidado % PBI - 1980/2017')


plt.plot(gp['indice_tiempo'], gp['gasto_publico_total'], color='lightgreen', marker='o')
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
