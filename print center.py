# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:29:21 2020

@author: patricio.a.drasal
"""

import matplotlib.pyplot as plt
import os

print()
print()
print (('-').center(100, '-'))
print ((('Massive SQL execution and reporting for Database servers').upper()).center(100))  
print (('-').center(100, '-'))
print()
print("\033[1;30;41m Bright Green  \n")

#\033[  Escape code, this is always the same
#1 = Style, 1 for normal.
#32 = Text colour, 32 for bright green.
#40m = Background colour, 40 is for black.

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()