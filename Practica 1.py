#!/usr/bin/env python
# coding: utf-8

# # Tutorial Manejo de Datos y Pandas
# 
# ## Estructuras de Datos e Índices
# 
# 
# Pandas soporta la lectura de una amplia cantidad de formatos ([más info](http://pandas.pydata.org/pandas-docs/stable/io.html)): 
# 
# - read_csv
# - read_excel
# - read_hdf
# - read_sql
# - read_json
# - read_msgpack (experimental)
# - read_html
# - read_gbq (experimental)
# - read_stata
# - read_sas
# - read_clipboard
# - read_pickle
# 
# Vamos a empezar a probar con una dataset publicado para una competencia de kaggle: [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data).

import numpy as np
import pandas as pd
import seaborn.apionly as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./Bases/titanic.csv", index_col="PassengerId")

data

data.index

data.columns

data.describe()

### matrix de correlacion

data.corr()

#ggraficar la matrix de correlacion
sns.heatmap(data.corr(), annot=True)

## reemplazar na

temp2= data

temp2["Age"].fillna(0, inplace = True) 

temp2.Age

temp2.describe()
temp2.dtypes

## Convert column data type

temp2.astype({'Age': 'int64'}).dtypes


# Las estructuras de datos en pandas, por lo general, no son modificadas en vivo con comandos como `set_index`, para hacer eso es necesario cambiar el argumento `inplace` o reasignar la variables

# ## Tipos de Indexado
# 
# Hay varias formas de seleccionar un subconjunto de los datos:
# 
# - Como las listas o arrays, por posición.
# - Como los diccionarios, por llave o etiqueta.
# - Como los arrays, por máscaras de verdadero o falso.
# - Se puede indexar por número, rango o lista (array)
# - Todos estos métodos pueden funcionar subconjunto como en las columnas
# 
# ## Reglas Básicas
# 
# 1. Se usan corchetes (abreviatura para el método `__getitem__`) para seleccionar columnas de un `DataFrame`
# 
#     ```python
#     >>> df[['a', 'b', 'c']]
#     ```
# 
# 2. Se usa `.iloc` para indexar por posición (tanto filas como columnas)
# 
#     ```python
#     >>> df.iloc[[1, 3], [0, 2]]
#     ```
# 3. Se usa `.loc` para indexar por etiquetas (tanto filas como columnas)
# 
#     ```python
#     >>> df.loc[["elemento1", "elemento2", "elemento3"], ["columna1", "columna2"]]
#     ```
# 
# 4. `ix` permite mezclar etiquetas y posiciones (tanto filas como columnas)
# 
#     ```python
#     >>> df.ix[["elemento1", "elemento2", "elemento3"], [0, 2]]
#     ```
#     ```python
#     >>> df.ix[[1, 3], ["columna1", "columna2"]]
#     ```
# 

data.loc[[1, 2, 3], ["Name", "Sex"]]

data.iloc[[1, 2, 3], [2, 3]]

data.ix[[1, 2, 3], ["Name", "Sex"]]

## reemplazar NAs
temp2= data
temp2["Age"].fillna(0, inplace = True) 
temp2.Age

## describir y ver tipos de datos
temp2.describe()
temp2.dtypes

## Convertir columna data type
temp2.astype({'Age': 'int64'}).dtypes

#################

temp = data.copy()
temp.index = ["elemento_" + str(i) for i in temp.index]
temp

temp.loc[["elemento_1", "elemento_2", "elemento_3"], ["Name", "Sex"]]

temp.iloc[[1, 2, 3], [2, 3]]

temp.ix[[1, 2, 3], ["Name", "Sex"]]

del temp

data.loc[:3, :"Sex"]

data.columns

#indexar por `slices`

data.iloc[:3]

data.iloc[-3:]

data.loc[1:10, ["Name", "Sex", "Ticket"]]

data[["Name", "Ticket"]]

use_cols = ["Name", "Ticket"]
data[use_cols]

data["Name"]

cols =["Name"]
data[cols]

data.Name

temp = data[["Name"]].copy()
temp.OtroNombre = ["OTRO_" + n for n in data.Name]
temp

temp.OtroNombre[:10]

temp["OtroNombre"] = ["OTRO_" + n for n in data.Name]
temp

del temp

data.iloc[1]

data.iloc[[1]]

data.SibSp

data["NumFam"] = data.SibSp + data.Parch
data

data.SibSp > 0

data[data.SibSp > 0][["Sex", "Age"]]

data[["Age", "Sex"]]

data[(data.SibSp > 0) & (data.Age < 18)][["Name","SibSp","Age"]]

# ### Ejercicio
# 
# ###### seleccionar varones mayores de 65 años que viajan solos

# escribir la solucion aqui...

data[(data.Sex == 'male') & (data.Age > 65.0) & (data.SibSp == 0)][["Name","Sex","Age","SibSp"]]

# %load soluciones/mayores_solos.py

# ### Filtrado de filas y columnas
# 
# Para eliminar lo que no quieren en lugar de seleccionar lo que sì
# 
# ```
# DataFrame.drop(etiquetas, axis=0, ...)
# 
# Parámetros
# ----------
# etiquetas : etiqueta o lista de etiquetas
# axis : entero o nombre de la dimesión
#     - 0 / 'index', para eliminar filas
#     - 1 / 'columns', para elimnar columnas
# ```

data.shape

valid_index = np.random.choice(data.index, int(data.index.shape[0] * 0.1), replace=False)
valid_index

train = data.drop(valid_index)
valid = data.loc.__getitem__(valid_index)
train

valid

X_train, y_train = train.drop("Survived", axis=1), train["Survived"]
X_valid, y_valid = valid.drop("Survived", axis=1), valid["Survived"]
X_train

y_train

# ### Agrupaciones y Tablas de Contingencia
# 
# #### Agrupaciones
# 
# Las agrupaciones sirven para hacer cálculos sobre subconjuntos de los datos, generalmente tienen tres partes:
# 
# 1. Definir los grupos
# 2. Aplicar un cálculo
# 3. Combinar los resultados

#agrupar
agrupado = data.groupby("Pclass")
agrupado

agrupado2 = data.groupby("Sex")
agrupado2

agrupado2.Survived.mean()

pd.crosstab(data.Sex, data.Survived)

agrupado2.Survived.agg({"media": "mean", "cantidad": "count"})

#sólo hemos agrupado, no se ha hecho ningún cálculo, para eso hay que aplicar alguna función
agrupado.Survived.mean()

agrupado.Survived.agg({"media": "mean", "media_2": np.mean, "varianza": "var", "cantidad": "count"})

data.columns

data.groupby("Survived")[['Age', 'SibSp', 'Parch', 'NumFam', 'Fare']].mean()

# #### Tablas de Contingencia
# Las tablas de contingencia asemejan las tablas dinámicas de excel, sirven apra ver inteeacciones entre variables

pd.crosstab(data.Pclass, data.Survived)

pd.crosstab(data.Pclass, data.Survived).apply(lambda x: x/x.sum(), axis=1)

data.Survived.value_counts()

get_ipython().run_line_magic('pinfo', 'data.Survived.value_counts')

data.Survived.value_counts(True).sort_index()

pd.crosstab(data.Pclass, pd.cut(data.Age, [i * 10 for i in range(9)]), 
            values=data.Survived, aggfunc=np.mean)

pd.crosstab(data.Pclass, pd.cut(data.Age, [i * 10 for i in range(9)]))

# ### Poniendo todo junto en un ejemplo de Data Mining

#hay variables que no son numericas y que hay que codificar antes que nada
tipos = data.dtypes
tipos.value_counts()

tipos_objeto = tipos[tipos == "object"]
tipos_objeto

nulos = data.isnull().sum()
nulos

nulos[nulos > 0]

data["Sex"].value_counts()

data["Sex"] = data.Sex.apply(lambda x: {"male": 0, "female": 1}[x])
data["Sex"].value_counts()

data["Ticket"].unique().shape

data["Ticket"].factorize()

data["Ticket"] = data["Ticket"].factorize()[0]
data["Ticket"].value_counts()

data.Embarked.fillna(-1).value_counts()

data[data.Embarked.isnull()]

data[(data.Fare >= 70) & (data.Fare <= 90)].Embarked.value_counts()

data.Embarked.fillna("S", inplace=True)
data.Embarked.fillna(-1).value_counts()

pd.crosstab(data.Embarked, data.Survived)

pd.crosstab(data.Embarked, data.Survived).apply(lambda x: x/x.sum(), axis=1)

pd.get_dummies(data.Embarked)

data = data.join(pd.get_dummies(data.Embarked)).drop("Embarked", axis=1)

data

data.Cabin.fillna(-1).value_counts()

data["Cabin"] = data.Cabin.fillna(-1).factorize()[0]

data

data.Age.fillna(-1).value_counts()

pd.crosstab(data.Age.isnull(), data.Survived).apply(lambda x: x/x.sum(), axis=1)

data["Age_nul"] = data.Age.isnull().astype(int)
data

data.Age.fillna(data.Age.mean(), inplace=True)
data

data.isnull().sum().sum()

data.drop("Name", axis=1, inplace=True)
data

data.dtypes.value_counts()

data.info()

data.corr()

sns.heatmap(data.corr(), annot=True)

valid_index

