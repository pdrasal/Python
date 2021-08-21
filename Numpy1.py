# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:53:31 2020

@author: Administrator
"""

import numpy as np

A=np.array([1, 4, 2, 5, 3])

print(A)

# NUMPY ARRAYS

# Create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)

# Create a 3x5 array filled with 3.14
np.full((3, 5), 3.14)

# Create an array filled with a linear sequence - Starting at 0, ending at 20, stepping by 2
np.arange(0, 20, 2)

# Create an array of five values evenly spaced between 0 and 1
np.linspace(0, 1, 5)

# Create a 3x3 array of uniformly distributed - # random values between 0 and 1
np.random.random((3, 3))

# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3, 3))

#Num‐Py’s universal functions (ufuncs) make repeated calculations on arrays much more efficient. 

#NumPy’s ufuncs feel very natural to use because they make use of Python’s native
#arithmetic operators. The standard addition, subtraction, multiplication, and division
#can all be used

x = np.arange(4)
x
print("x =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2) # floor division

#There is also a unary ufunc for negation, a ** operator for exponentiation, and a %
#operator for modulus:

print("x ** 2 = ", x ** 2)
print("x % 2 = ", x % 2)

#operator can be strung together however you wish, and the standard order of operations is respected:

-(0.5*x + 1) ** 2

#Aggregations: Min, Max, and Everything in Between

#Often when you are faced with a large amount of data, a first step is to compute summary
#statistics for the data in question. Perhaps the most common summary statistics
#are the mean and standard deviation, which allow you to summarize the “typical” values
#in a dataset, but other aggregates are useful as well (the sum, product, median,
#minimum and maximum, quantiles, etc.). 

L = np.random.random(100)
np.sum(L)

big_array = np.random.rand(100000)

#%timeit sum(big_array)
#%timeit np.sum(big_array)

#np.min(big_array)
#np.max(big_array)

#Example: What Is the Average Height of US Presidents?
#Aggregates available in NumPy can be extremely useful for summarizing a set of values.
#As a simple example, let’s consider the heights of all US presidents. This data is
#available in the file president_heights.csv, which is a simple comma-separated list of
#labels and values:

import numpy as np
import pandas as pd
data = pd.read_csv('Bases/president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

print("Mean height: ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height: ", heights.min())
print("Maximum height: ", heights.max())
print("25th percentile: ", np.percentile(heights, 25))
print("Median: ", np.median(heights))
print("75th percentile: ", np.percentile(heights, 75))


import matplotlib.pyplot as plt
import seaborn; seaborn.set() # set plot style
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number');
plt.show();