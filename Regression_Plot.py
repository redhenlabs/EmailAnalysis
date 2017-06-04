# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 23:36:18 2017

@author: shubra
"""

import matplotlib.pyplot as plt
from pandas import DatetimeIndex as dt
import pandas as pd

def plot_regression(y_test, model_name,Predicted):
    y_test1 = y_test.copy()
    y_test1 = y_test1.reset_index()
    
    y_test1['Date'] = dt.strftime(y_test.index.get_level_values('Date'), "%Y-%m-%d")
    y_test1['Date'] = pd.to_datetime(y_test1['Date'])
    y_test1.drop('POI',axis=1,inplace=True)

    f, ax = plt.subplots(figsize=(8,5))
    ax.plot(y_test1.Date,y_test1.Percentage_Bad_Words_count,label='Total Message In Test Population by date')#y_test1.name[7:])
    ax.plot(y_test1.Date,Predicted,color='red',label="Predicted Over Date")
    ax.plot_date(y_test1.Date,Predicted,color='black')
    ax.set_title(model_name +' Percent Negative Word')   
    ax.set_xlabel("Date",rotation=0)
    plt.xticks(rotation = 90)
    ax.set_ylabel("% Of Negative Word")
    ax.legend(loc="upper right")
    plt.show()