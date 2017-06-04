# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 00:22:05 2017

@author: shubra
"""
from pandas import DatetimeIndex as dt
#import pandas as pd
import matplotlib.pyplot as plt
from pandas import DatetimeIndex 
import datetime

def plot_exploration(email_data_frame_class):
    plot_Data = email_data_frame_class.copy()
    plot_Data['POI1']= email_data_frame_class.index.get_level_values('POI')
    plot_Data['Date1']= dt.strftime(email_data_frame_class.index.get_level_values('Date'), "%Y-%m-%d")
    plot_Data['Year'] = DatetimeIndex(plot_Data['Date1']).year
    plot_Data['Month'] = DatetimeIndex(plot_Data['Date1']).month
    plot_Data['Day'] = DatetimeIndex(plot_Data['Date1']).day
    plot_Data['Year'] = DatetimeIndex(plot_Data['Date1']).year
    plot_Data['Year_Month'] = plot_Data["Year"].astype(str) + '/'+plot_Data["Month"].astype(str)
    plot_Data['Year_Month'] = sorted(plot_Data['Year_Month'], key=lambda x: datetime.datetime.strptime(x, '%Y/%m'))
#    plot_Data['Year_Month'] = plot_Data["Year"].astype(str) + plot_Data["Month"].astype(str)
#    plot_Data['Year_Month'] = plot_Data['Year_Month'].astype(int)


    
    df3 =plot_Data.groupby(['Year']).count()
    df4 =plot_Data.groupby(['Year_Month']).count()
    df5= plot_Data[plot_Data['Bad_Words_count'] > 0 ]
    df5 =df5.groupby(['Year_Month']).count()


    ax = df3.file.plot(kind='bar', title ="Message By Year", figsize=(5, 5),  fontsize=8)
    ax.set_xlabel("Year", fontsize=8)
    ax.set_ylabel("Number Of Message", fontsize=8)
    plt.xticks(rotation = 90)
    plt.grid()
    plt.show()


    

    f, ax = plt.subplots(figsize=(15,10))
    ax = df4.file.plot(kind='bar', title ="Count Of Messages By Year Month",   fontsize=10)
    df4.file.plot(kind='line',ax=ax,color='green',label='Total Messages',linewidth=3)    
    ax.legend(loc='upper center', shadow=True)
    plt.xticks(rotation = 90)
    ax.set_xticklabels(sorted(df5.index.get_level_values('Year_Month'), key=lambda x: datetime.datetime.strptime(x, '%Y/%m')))
    ax.set_ylabel("Number Of Message", fontsize=8)
    plt.grid()
    plt.show()
    
    
    f, ax = plt.subplots(figsize=(15,10))
    ax = df5.file.plot(kind='bar', title ="Count Of Messages With Negative Word By Year Month",   fontsize=10)
    df5.file.plot(kind='line',ax=ax,color='red', label='Messages With Negative Words',linewidth=5)
    ax.legend(loc='upper center', shadow=True)
    plt.xticks(rotation = 90)
    ax.set_xticklabels(sorted(df5.index.get_level_values('Year_Month'), key=lambda x: datetime.datetime.strptime(x, '%Y/%m')))
    ax.set_ylabel("Number Of Message With  Negative Words", fontsize=8)
    plt.grid()
    plt.show()
    
