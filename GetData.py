# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:14:58 2017

@author: shubra
"""
import pandas as pd
import os
import numpy as np

email_file_directory = 'C:/Training/udacity/ProjectEmail/outputs/'
email_file_name ='email_csv_with_bad_words_5000'


def get_classification_Data(email_file_directory,email_file_name): 
    """
    Collect Index ticker stored in Indexing_Ticker and store it in a dataframe.
    Here I am getting data between specific dates and not complete dataset that has been 
    downloaded from yahoo or quandal
    """
    fn=os.path.join(email_file_directory, "{}.csv".format(str(email_file_name)))
    df = pd.read_csv(fn, index_col=["Date","POI"],parse_dates=["Date"], header=0,usecols=["file", "Date","POI","Percentage_Bad_Words_count","Percentage_Lit_Words_count","Total_Words_count","Bad_Words_count","Lit_Words_count"])
    df = df[np.isfinite(df['Percentage_Bad_Words_count'])]
    
    return df
def get_regression_Data(email_file_directory,email_file_name): 
    """
    Collect Index ticker stored in Indexing_Ticker and store it in a dataframe.
    Here I am getting data between specific dates and not complete dataset that has been 
    downloaded from yahoo or quandal
    """
    fn=os.path.join(email_file_directory, "{}.csv".format(str(email_file_name)))
#    df = pd.read_csv(fn, index_col=["Date","POI"],parse_dates=["Date"], header=0,usecols=["file", "Date","POI","Total_Words_count","Bad_Words_count","Lit_Words_count"],nrows=10)
    df = pd.read_csv(fn, index_col=["Date","POI"],parse_dates=["Date"], header=0,usecols=["file", "Date","POI","Percentage_Bad_Words_count","Percentage_Lit_Words_count","Total_Words_count","Bad_Words_count","Lit_Words_count"])
    df = df[np.isfinite(df['Percentage_Bad_Words_count'])]

    return df
if __name__ == "__main__":
    email_file_directory = 'C:/Training/udacity/ProjectEmail/outputs/'
    email_file_name ='email_csv_with_bad_words_5000'
    email_frame= get_classification_Data(email_file_directory,email_file_name)    
    print('--Check First Row --')
    print(email_frame[:1])
    print('--Check column --')
    print(email_frame['POI'][:2])