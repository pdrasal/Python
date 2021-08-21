# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 03:25:39 2020
@author: patricio.a.drasal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

seg = pd.read_csv('Bases/seguridad-provincias.csv',encoding='latin1',index_col='provincia_id')
seg=seg.fillna(0)


seg

temp=seg.query("codigo_delito_snic_id == 1")

temp[["anio", "provincia_nombre","cantidad_hechos"]].sort_values("cantidad_hechos",ascending=False)

plt.style.use('seaborn-dark-palette')
g = sns.FacetGrid(temp, col="provincia_nombre", col_wrap=4, height=2)
g.map(sns.lineplot, "anio", "cantidad_hechos", color=".3", ci=None)