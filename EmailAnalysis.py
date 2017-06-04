# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:46:41 2017

@author: shubra
"""


from time import time
from GetData import get_classification_Data,get_regression_Data
from Prepare_Classification_Data import classification_data_prep
from Prepare_Regression_Data import regression_data_prep
from call_reg_class_models import call_classification_models, call_regression_models
from dat_exploratory_plot import plot_exploration

t1 = time()
email_file_directory = 'C:/Training/udacity/ProjectEmail/outputs/'
#email_file_name ='email_csv_with_bad_words_5000'
email_file_name ='email_csv_with_bad_words'

email_data_frame_class = get_classification_Data(email_file_directory,email_file_name)
X_train, y_train, X_test, y_test = classification_data_prep(email_data_frame_class)

email_data_frame_reg = get_regression_Data(email_file_directory,email_file_name)
X_train_reg, y_train_reg, X_test_reg, y_test_reg  = regression_data_prep(email_data_frame_reg)
t2 = time()

print('')
print('---------Shape Of Classification DataSet ---------')
print("Shape X_train:",X_train.shape)
print("Shape y_train:",y_train.shape)
print("Shape X_test:",X_test.shape)
print("Shape y_test:",y_test.shape)
print('')

print('')
print('---------Shape Of Regression DataSet ---------')
print("Shape X_train_reg:",X_train_reg.shape)
print("Shape y_train_reg:",y_train_reg.shape)
print("Shape X_test_reg:",X_test_reg.shape)
print("Shape y_test_reg:",y_test_reg.shape)
print('')

print ("Time taken for Preparing Train and Test Data for Classification & Regression  ", (t2-t1)/60)

call_classification_models(X_train, y_train, X_test, y_test)
t3 = time()
print(' Time taken for All Classification = ', (t3-t2)/60 )

call_regression_models(X_train_reg, y_train_reg, X_test_reg, y_test_reg)

t4 = time()
print(' Time taken for All Regression = ', (t4-t3)/60 )

plot_exploration(email_data_frame_class)


print(' Total Time taken = ', (t4-t1)/60 )



