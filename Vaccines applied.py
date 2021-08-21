# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:05:16 2020
@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vaccines = pd.read_csv('Bases/share-people-vaccinated-covid.csv')

vaccines
vaccines.head()
vaccines.info()

new=vaccines.groupby('Entity')['people_vaccinated_per_hundred'].max()
new=new.to_frame()

new[new['people_vaccinated_per_hundred'] > 30].sort_values(by=["people_vaccinated_per_hundred"],ascending=False).plot.bar(rot=90,color='darkgreen',title='Vaccines applied by country or Region')
