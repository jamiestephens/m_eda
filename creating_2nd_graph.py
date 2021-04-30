# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:12:58 2021

@author: Administrator
"""


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from numpy import cov
import numpy as np

propertiesres = pd.read_csv('propertiescleanedresidential.csv',sep=',',skiprows=0,names=['type','date'])

propertiesres['date'] = pd.to_datetime(propertiesres['date'])
propertiesres.set_index('date', inplace=True)

propertiesres_monthly = propertiesres.resample('M').count()


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
ax2.plot(propertiesres_monthly.index,propertiesres_monthly.type,color="blue")
ax2.set_ylabel("Properties Sold",color="blue",fontsize=10)
plt.show()
# save the plot as a file
fig.savefig('two_different_y_axis_for_single_python_plot_with_twinx.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')

print(mta_monthly.head())
covariance = np.corrcoef(mta_monthly.entrances,propertiesres_monthly.type)
print(covariance)