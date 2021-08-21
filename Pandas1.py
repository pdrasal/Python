# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:14:29 2020

@author: Administrator
"""
import pandas as pd

#Series
data = pd.Series([0.25, 0.5, 0.75, 1.0])
data
data.values
data.index
data[1:3]

#Series as specialized dictionary
population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}
population = pd.Series(population_dict)

population['California']

# The Pandas DataFrame Object
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
'Florida': 170312, 'Illinois': 149995}

area = pd.Series(area_dict)
states = pd.DataFrame({'population': population, 'area': area})

states
states.index
states.columns
states['area']

area = pd.Series({'California': 423967, 'Texas': 695662,
'New York': 141297, 'Florida': 170312,
'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
'New York': 19651127, 'Florida': 19552860,
'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
data

data['density'] = data['pop'] / data['area']

data

#traspose
data.T