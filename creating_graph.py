# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:04:35 2021

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from numpy import cov
import numpy as np
properties = pd.read_csv('propertiescleaned.csv',sep=',',skiprows=2,names=['oldindex','type','zip','price','date'])

del properties['oldindex']

properties['date'] = pd.to_datetime(properties['date'])
properties.set_index('date', inplace=True)


properties_monthly = properties.resample('M').count()

del properties_monthly['zip']
del properties_monthly['price']


# MTA Turnstile Data:

mydateparser = lambda x: pd.datetime.strptime(x, "%Y-%m-%d")
mta = pd.read_csv('mtafinal.csv',sep=',',names=['date','entrances','exits'], parse_dates=['date'], date_parser=mydateparser)

del mta['exits']

print(mta.head())
mta = mta.set_index(['date'])
mta_monthly = mta.resample('M').sum()

print(mta_monthly.head())

fig,ax = plt.subplots()
# make a plot
ax.set_title('Rush Hour Entrances vs Residential Property Sales Count, Monthly')
ax.plot(mta_monthly.index,mta_monthly.entrances, color="red")
# set x-axis label
ax.set_xlabel("Year",fontsize=14)
# set y-axis label
ax.set_ylabel("Rush Hour Entrances",color="red",fontsize=10)

ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(properties_monthly.index,properties_monthly.type,color="blue")
ax2.set_ylabel("Properties Sold",color="blue",fontsize=10)
plt.show()
# save the plot as a file
fig.savefig('two_different_y_axis_for_single_python_plot_with_twinx.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')

print(mta_monthly.head())
covariance = np.corrcoef(mta_monthly.entrances,properties_monthly.type)
print(covariance)