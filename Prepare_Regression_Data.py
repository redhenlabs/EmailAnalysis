# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:54:25 2017

@author: shubra
"""


def regression_data_prep(email_data_frame_reg):
    """
    POI are treated as training set and non -POI are testing sets.
    Input/features is total number of words
    output/measurable = bad word and lit word count
    """
    email_data_frame_reg=email_data_frame_reg.reindex(columns=['file','Percentage_Bad_Words_count','Bad_Words_count', 'Total_Words_count','Lit_Words_count','Percentage_Lit_Words_count'])

#    print('')
#    print(email_data_frame_reg.columns)
#    print('')
#
#    print('-------------email_data_frame_reg -----------------')
#    print(email_data_frame_reg[email_data_frame_reg.index.get_level_values('POI')==True])
#    print(email_data_frame_reg[email_data_frame_reg.index.get_level_values('POI')==False])
#   
    
    train = email_data_frame_reg[email_data_frame_reg.index.get_level_values('POI')==True]

    test = email_data_frame_reg[email_data_frame_reg.index.get_level_values('POI')==False]    

    
#    print()
#    print('---- Training Data Feature-----')
#    print(train['Total_Words_count'])
#    print()
#    print('---- Training Data Output-----')
#    print(train[['Bad_Words_count','Lit_Words_count']])
#
#
#    print()
#    print('---- Testing Data Feature -----')
#    print(test['Total_Words_count'])
#    print()
#    print('---- Testing Data Output -----')
#    print(test[['Bad_Words_count','Lit_Words_count']])
    
    features = email_data_frame_reg.columns[2:]
    """
    Set the values for X_train , y_train, X_test,y_test
    """
    X_train =train[features]
#    y_train =train[['Bad_Words_count','Lit_Words_count']]
    y_train =train['Percentage_Bad_Words_count']

    X_test = test[features]
#    y_test =test[['Bad_Words_count','Lit_Words_count']]
    y_test =test['Percentage_Bad_Words_count']
    
    return X_train, y_train, X_test, y_test
