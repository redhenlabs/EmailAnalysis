# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:54:25 2017

@author: shubra
"""
from sklearn import preprocessing 
import numpy as np



def classification_data_prep(email_data_frame):
 
    le = preprocessing.LabelEncoder()
    email_data_frame=email_data_frame.reindex(columns=['file','Percentage_Bad_Words_count','Bad_Words_count', 'Total_Words_count','Lit_Words_count','Percentage_Lit_Words_count'])
    
#    print(email_data_frame['Percentage_Bad_Words_count'])
    
    email_data_frame['Classification1'] = email_data_frame['Percentage_Bad_Words_count']
    #    print(email_data_frame['Classification1'])    
    row_index = email_data_frame.Classification1 >  0.0
#    print("row_index ",row_index)
    email_data_frame.loc[row_index, 'Classification1'] = 'YES_Negative'
    #    print(email_data_frame.loc[row_index, 'Classification1'])
    row_index1 = email_data_frame.Classification1 <= 0.0
    email_data_frame.loc[row_index1, 'Classification1'] = 'NO_Negative'
    
#    email_data_frame['Classification2'] = email_data_frame['Percentage_Lit_Words_count']
#    row_index2 = email_data_frame.Classification2 >  0.0
#    email_data_frame.loc[row_index2, 'Classification2'] = 'YES_Lit'
#    row_index3 = email_data_frame.Classification2 <= 0.0
#    email_data_frame.loc[row_index3, 'Classification2'] = 'NO_Lit'
#    
#    email_data_frame['Classification3'] = email_data_frame['POI']

#    print('')    
#    print('-- TAIL  Before Label Encoder ---')
#    print(email_data_frame.tail())
#    print('')    
#    print('-- HEAD  Before Label Encoder ---')
#    print(email_data_frame.head())
    
#    print("row_index   ",row_index1 , dataset.Classification)
    
#    email_data_frame.Classification = le.fit(email_data_frame.Classification).transform(email_data_frame.Classification)
    
#    email_data_frame['Classification'] = le.fit(email_data_frame).transform(email_data_frame)
    
#    email_data_frame.apply(le.fit_transform)   
    email_data_frame.Classification1 = le.fit(email_data_frame.Classification1).transform(email_data_frame.Classification1)
#    email_data_frame.Classification2 = le.fit(email_data_frame.Classification2).transform(email_data_frame.Classification2)
#    email_data_frame.Classification3 = le.fit(email_data_frame.Classification3).transform(email_data_frame.Classification3)
    
#    print(email_data_frame[['Classification1','Classification3','Classification3']])
#    print('')    
#    print('-- TAIL  After Label Encoder ---')
#    print(email_data_frame.tail())
#    print('')    
#    print('-- HEAD  After Label Encoder ---')
#    print(email_data_frame.head())
    
#    features = email_data_frame.columns[1:-1]
#    print(email_data_frame.columns.tolist())
    features = email_data_frame.columns[2:-1]
#    features = email_data_frame.index(['Bad_Words_count', 'Total_Words_count','Lit_Words_count','Percentage_Lit_Words_count'])
#    print('')
#    print("features --",features)
    X_features = email_data_frame[features]    
#    print('')
#    print('---X -Features ---')
#    print(X_features.head())
#    Classification_cols = email_data_frame.columns[8:]
#    y_Classification = email_data_frame[Classification_cols]
    y_Classification=email_data_frame.Classification1
#    y_Classification = email_data_frame.Classification 
#    print('---Y -Classification ---')
#    print(y_Classification.head())
#    print(y_Classification.tail())
#    
#    print('')
#    print('---Print Index  ---')
#    print(X_features.index.levels[1])
#    
#    print('')
#    
#    print('---Print Index Value  ---')
#    print(X_features.index.get_level_values('POI').unique())
#    
#    idx_val =  X_features.index.get_level_values('POI')
#    
#    print("idx_val",idx_val)
    
    """
    Break up Training and Testing data sets, Rows with POI = True falls under training 
    category and POI = False is considered under Testing Category
    """
    
    X_train = X_features[X_features.index.get_level_values('POI') == True]
    y_train = y_Classification[y_Classification.index.get_level_values('POI') == True]    
    

    X_test = X_features[X_features.index.get_level_values('POI') == False]    
    y_test = y_Classification[y_Classification.index.get_level_values('POI') == False]
    
#    print('')
#    print('---Print X_Train  Shape---' ,X_train.shape)
#    print('---Print y_Train  ---',y_train.shape )
#    print('---Print X_test  ---',X_test.shape )
#    print('---Print y_test  ---',y_test.shape )

    
    return X_train, y_train, X_test, y_test    
   
 
 
 
 


