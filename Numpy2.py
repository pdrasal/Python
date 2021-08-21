# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 02:01:39 2020

@author: Administrator
"""

import numpy as np
import pandas as pd
# use Pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('Bases/Seattle2014.csv')['PRCP'].values

rainfall

inches = rainfall / 254 # 1/10mm -> inches
inches.shape

#Histogram of 2014 rainfall in Seattle 
#the vast majority of days in Seattle saw near zero measured rainfall in 2014

import matplotlib.pyplot as plt
import seaborn; seaborn.set() # set plot styles
plt.hist(inches, 40);

plt.title('Rainfalls in Seattle 2014 - Count of days')
plt.xlabel('Count of days')
plt.ylabel('Inches');
plt.show();

print("Number days without rain: ", np.sum(inches == 0))
print("Number days with rain: ", np.sum(inches != 0))
print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
print("Rainy days with < 0.1 inches :", np.sum((inches > 0) &
(inches < 0.2)))

#Boolean arrays as masks (select particular subsets of the data themselves)
# construct a mask of all rainy days
rainy = (inches > 0)
# construct a mask of all summer days (June 21st is the 172nd day)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
print("Median precip on rainy days in 2014 (inches): ",
np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches): ",
np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ",
np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
np.median(inches[rainy & ~summer]))

