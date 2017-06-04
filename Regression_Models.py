# -*- coding: utf-8 -*-
"""


"""
from sklearn.grid_search import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

from sklearn import  ensemble
from sklearn.metrics import mean_squared_error, r2_score,make_scorer
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
import pandas as pd
import datetime
from pandas import DatetimeIndex 
from PlotModelCcomplexity import plotLearningPerformance, plotModelComplexity
from  LearnndPerfCalc import learning_curves,model_complexity
from pandas import DatetimeIndex as dt
from Regression_Plot import plot_regression
################ SECTION 8 REGRESSION FUNCTIONS ##############################    
"""
1.DecisionTreeRegressor
2. KNeighborsRegressor
3. RandomForestRegressor
4.SVR
5.BaggingRegressor
6.AdaBoostRegressor
7.GradientBoostingRegressor
"""

def Call_DecisionTree_Reg(X_train, y_train, X_test, y_test):
    """ Tunes a decision tree regressor model using GridSearchCV on the input data X 
        and target labels y and returns this optimal model. """

    # Create a decision tree regressor object
    regressor = DecisionTreeRegressor( max_depth=2,min_samples_leaf=1, min_samples_split=2,splitter='best')

    # Set up the parameters we wish to tune
    parameters = [{'max_depth':(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),'presort':['True']}]

    # Make an appropriate scoring function
    scoring_function = None
    #scoring_function = make_scorer(performance_metric(), greater_is_better=False)
    scoring_function = make_scorer(r2_score, greater_is_better=True)

    # Make the GridSearchCV object
    reg = None
    reg = GridSearchCV(regressor, parameters,scoring=scoring_function, cv=10)

    # Fit the learner to the data to obtain the optimal model with tuned parameters
    reg.fit(X_train, y_train)
    Predicted = reg.predict(X_test)
    print("DecisionTreeRegressor = ",reg.score(X_test, y_test) )
    
    #print "Best model parameter:  " + str(reg.best_params_)
    #print "Best model estimator:  " + str(reg.best_estimator_)
    # Return the optimal model
    Best_Estimator = reg.best_estimator_
    MSE = mean_squared_error(y_test,Predicted)
    R2 =r2_score(y_test, Predicted)
    
#    print("y_test :",y_test.head(),y_test[1])
#    print("y_test_1 :",y_test.shape)
    plot_regression(y_test, 'DecisionTree Reg',Predicted)

    
    learning_curves(X_train, y_train, X_test, y_test)
    model_complexity(X_train, y_train, X_test, y_test)
    return "DecisionTreeRegressor Best Estimator ", Best_Estimator, "DecisionTreeRegressor MSE =",MSE,"DecisionTreeRegressor R2 =", R2

def Call_KNN_Reg(X_train, y_train, X_test, y_test):
    """
    KNN Regression
    """
    clf = KNeighborsRegressor()
    clf.fit(X_train, y_train)
    Predicted = clf.predict(X_test)
    print("KNeighborsRegressor Score = ",clf.score(X_test, y_test) )
    MSE = mean_squared_error(y_test,Predicted)
    R2 = r2_score(y_test, Predicted)
    plot_regression(y_test, 'KNN Reg',Predicted)
    return "KNeighborsRegressor MSE =" ,MSE,"KNeighborsRegressor R2 =" , R2 

def Call_RandomForest_Reg(X_train, y_train, X_test, y_test):
    """
    Random Forest Regression
    """
    clf = ensemble.RandomForestRegressor(n_estimators=100, n_jobs=-1)
    
    parameters = [{'n_estimators':[20],'criterion':['mse'],'min_weight_fraction_leaf':[0.25],'n_jobs':[-1]}]
    scoring_function = make_scorer(r2_score, greater_is_better=True)
    # Make the GridSearchCV object
    clf = GridSearchCV(clf, parameters,scoring=scoring_function, cv=10)
    
    clf = clf.fit(X_train, y_train)
    Predicted = clf.predict(X_test)
    print("RandomForestRegressor Score = ",clf.score(X_test, y_test) )
    MSE = mean_squared_error(y_test, Predicted)
    R2 = r2_score(y_test, Predicted)
    plot_regression(y_test, 'RandomForest Reg',Predicted)
    return "Random Forest Predicted Mean Square Error =", MSE, "and Random Forest R-Square =",R2

def Call_SV_Reg(X_train, y_train, X_test, y_test):
    """
    SVM Regression
    """

    clf = SVR()
    
    parameters =[{'C': [1, 10, 100, 1000], 'gamma': [1e-1, 1, 1e1], 'kernel': ['rbf','linear', 'poly','sigmoid'],'degree': [3],'epsilon':[0.9]}]
    scoring_function = make_scorer(r2_score, greater_is_better=True)
    # Make the GridSearchCV object
    clf = GridSearchCV(clf, parameters,scoring=scoring_function,cv=10)
    
        
    clf.fit(X_train, y_train)
    Predicted = clf.predict(X_test)
    print("SVR Score = ",clf.score(X_test, y_test) )
    
    MSE = mean_squared_error(y_test,Predicted)
    R2 =r2_score(y_test, Predicted)
    plot_regression(y_test, 'SV Reg',Predicted)
    return "SVR Mean Square Error =",MSE,"SVR R2 =", R2
    
def Call_Bagging_Reg(X_train, y_train, X_test, y_test):
    """
    Bagging Regression
    """
  
    clf = ensemble.BaggingRegressor()
    
    
    clf.fit(X_train, y_train)
    Predicted = clf.predict(X_test)
    print("BaggingRegressor Score = ",clf.score(X_test, y_test) )
    MSE = mean_squared_error(y_test,Predicted)
    R2 =r2_score(y_test, Predicted)
    plot_regression(y_test, 'Bagging Reg',Predicted)

    
    return "BaggingRegressor MSE =" ,  MSE,"BaggingRegressor R2 =", R2  

def Call_AdaBoost_Reg(X_train, y_train, X_test, y_test):
    """
    Ada Boost Regression
    """

    clf = ensemble.AdaBoostRegressor()
    clf.fit(X_train,y_train)
    Predicted = clf.predict(X_test)
    print("AdaBoostRegressor Score = ",clf.score(X_test, y_test) )
    MSE = mean_squared_error(y_test,Predicted)
    R2 =r2_score(y_test, Predicted)
    plot_regression(y_test, 'AdaBoost Reg',Predicted)

    
    return "AdaBoost MSE =" ,  MSE,"AdaBoost R2 =", R2

def Call_GradientBoosting_Reg(X_train, y_train, X_test, y_test):
    """
    Gradient Boosting Regression
    """
    
    clf = ensemble.GradientBoostingRegressor()
    clf.fit(X_train, y_train)
    Predicted = clf.predict(X_test)
    print("GradientBoostingRegressor Score = ",clf.score(X_test, y_test) )
    MSE = mean_squared_error(y_test,Predicted)
    R2 =r2_score(y_test, Predicted)
    plot_regression(y_test, 'GradientBoosting Reg',Predicted)
    
    return "GradientBoosting MSE =" , MSE,"GradientBoosting R2 =", R2
    
