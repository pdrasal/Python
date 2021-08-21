#!/usr/bin/env python
# coding: utf-8

# In[11]:


# importando modulos necesarios
import numpy as np
import pandas as pd
from pydataset import data

# librerías de visualizaciones
import seaborn as sns
import matplotlib.pyplot as plt 

# graficos incrustados
get_ipython().run_line_magic('matplotlib', 'inline')
output_notebook()
iris = datasets.load_iris()


# In[14]:


iris = data('iris')
tips = data('tips')


# separo en especies
setosa = iris[iris.Species == 'setosa']
versicolor = iris[iris.Species == 'versicolor']
virginica = iris[iris.Species == 'virginica']


# In[15]:


# crear histograma
plt.figure(figsize=(10, 8))
n, bins, patches = plt.hist(setosa['Petal.Length'], 12, 
                            facecolor='red', label='setosa')
n, bins, patches = plt.hist(versicolor['Petal.Length'], 12, 
                            facecolor='green', label='versicolor')
n, bins, patches = plt.hist(virginica['Petal.Length'], 12, 
                            facecolor='blue', label='virginica')
plt.legend(loc='top_right')
plt.title('Histograma largo del pétalo')
plt.xlabel('largo del pétalo')
plt.ylabel('cuenta largo del pétalo')
plt.show()


# In[16]:



# Ejemplo diagrama de dispersion entre Petal.Length y Petal.Width
plt.figure(figsize=(10, 8))
plt.scatter(setosa['Petal.Length'], setosa['Petal.Width'], 
            c='red', label='setosa')
plt.scatter(versicolor['Petal.Length'], versicolor['Petal.Width'], 
            c='green', label='versicolor')
plt.scatter(virginica['Petal.Length'], virginica['Petal.Width'], 
            c='blue', label='virginica')
plt.title('Tamaño del pétalo')
plt.xlabel('Largo del pétalo (cm)')
plt.ylabel('Ancho del pétalo (cm)')
plt.legend(loc='top_left')
plt.show()


# In[17]:


# Ejemplo gráfico de distribuciones
x = np.random.normal(size=100)
dist= sns.distplot(x)


# In[18]:


tips.head()


# In[19]:


reg = sns.regplot(x="total_bill", y="tip", data=tips)


# In[20]:


g = sns.pairplot(iris, hue="Species", diag_kind="hist") 


# In[ ]:




