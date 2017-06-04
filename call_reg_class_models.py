# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 00:05:49 2017

@author: shubra
"""
from Classification_Models import Call_Random_Forest_Classi,Call_KNN_Classi,Call_Support_Vector_Classi,Call_AdaBoost_Classi,Call_Gradient_Tree_GTB_Classi,Call_QDA_Classi
from Regression_Models import Call_DecisionTree_Reg,Call_KNN_Reg,Call_RandomForest_Reg,Call_SV_Reg,Call_Bagging_Reg,Call_AdaBoost_Reg,Call_GradientBoosting_Reg


def call_classification_models(X_train, y_train, X_test, y_test):
    print('')
    print('========== Classification Results ===============================')
    print("Classification Randon Forest Score :", Call_Random_Forest_Classi(X_train, y_train, X_test, y_test))
    print('')
    print("Classification KNN Score :", Call_KNN_Classi(X_train, y_train, X_test, y_test))
    print('')
    print("Classification SVM Score :", Call_Support_Vector_Classi(X_train, y_train, X_test, y_test))
    print('')
    print("Classification GradientBoostingClassifier Score :", Call_AdaBoost_Classi(X_train, y_train, X_test, y_test))
    print('')
    print("Classification Gradient Tree Score :", Call_Gradient_Tree_GTB_Classi(X_train, y_train, X_test, y_test))
    print('')
    print("Classification QDA Score :", Call_QDA_Classi(X_train, y_train, X_test, y_test))
    print('')    


def call_regression_models(X_train_reg, y_train_reg, X_test_reg, y_test_reg):
    print('========== Regression Results ===============================')
    print ('GridSearchCV Tuning on Decission Tree Regressor ', Call_DecisionTree_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print('') 
    print ('KNN Regression Score  ', Call_KNN_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print('') 
    print ('RandomForest Regression Score  ',Call_RandomForest_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print('') 
    print ('SVR Regression Score  ',Call_SV_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print('') 
    print ('Bagging Regression Score  ',Call_Bagging_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print('') 
    print ('AdaBoost Regression Score  ',Call_AdaBoost_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print('') 
    print ('GradientBoosting Regression Score  ',Call_GradientBoosting_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
     