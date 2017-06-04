# -*- coding: utf-8 -*-
"""
0. Run the file DataDownload.py to Download Specific Ticker Related Data
1. SECTION 1 -- LEARNING AND PERFORMANCE CALCULATION (LearnndPerfCalc.py)
2. SECTION 2 -- PLOT LEARNING AND MODEL COMPLEXITY (PlotModelCcomplexity.py) --- This is now obselete use LearnndPerfCalc.py instead
3. SECTION 3 -- GET DATA SETS (GetDataSets.py)
4. SECTION 4-- DATA PREPRATION AND NORMALIZATION (DataPrepNormalization.py)
5. SECTION 5 PREPARE DATA FOR CLASSIFICATION MODELS (PrepDataForClassification.py)   
6. SECTION 6 PREPARE DATA FOR REGRESSION MODELS  and Call regression models(PrepDataForRegression.py)
7. SECTION 7  CALL THE CLASSIFICATION MODEL (CallClassification.py)
8. SECTION 8 REGRESSION FUNCTIONS (RegressionFunctions.py)
9. SECTION 9 CLASSIFICATION FUNCTIONS (CallClassification.py)

"""
import numpy as np
import matplotlib.pyplot as plt
from LearnndPerfCalc import  performance_metric


def plotLearningPerformance(X_train,y_train,X_test,y_test,figure_size_x,figure_size_y,regressor_type,Regression_Nmae):
   # Create the figure window
    fig = plt.figure(figsize=(figure_size_x,figure_size_y))

    # We will vary the training set size so that we have 50 different sizes
    sizes = np.rint(np.linspace(1, len(X_train), 50)).astype(int)
    train_err = np.zeros(len(sizes))
    test_err = np.zeros(len(sizes))
    
    # Create four different models based on max_depth
#    for k, depth in enumerate([1,3,6,10]):
        
    for i, s in enumerate(sizes):
            
            # Setup a decision tree regressor so that it learns a tree with max_depth = depth
#            regressor = DecisionTreeRegressor(max_depth = depth)
            
            # Fit the learner to the training data
            regressor_type.fit(X_train[:s], y_train[:s])

            # Find the performance on the training set
            train_err[i] = performance_metric(y_train[:s], regressor_type.predict(X_train[:s]))
            
            # Find the performance on the testing set
            test_err[i] = performance_metric(y_test, regressor_type.predict(X_test))

        # Subplot the learning curve graph
    ax = fig.add_subplot(2, 2, 0+1)
    ax.plot(sizes, test_err, lw = 2, label = 'Testing Error')
    ax.plot(sizes, train_err, lw = 2, label = 'Training Error')
    ax.legend()
#    ax.set_title('max_depth = %s'%(depth))
    ax.set_title('Learning Performances ')
    
    ax.set_xlabel('Number of Data Points in Training Set')
    ax.set_ylabel('Total Error')
    ax.set_xlim([0, len(X_train)])
    Regression_Nmae = Regression_Nmae + ' Regression Learning Performances'
    # Visual aesthetics
    fig.suptitle(Regression_Nmae, fontsize=18, y=1.03)
    fig.tight_layout()
    fig.show()
       
    
def plotModelComplexity(X_train, y_train, X_test, y_test,regressor_type,Regression_Nmae):
    """ Calculates the performance of the model as model complexity increases.
        The learning and testing errors rates are then plotted. """
    
    print "Creating a model complexity graph. . . "

    # We will vary the max_depth of a decision tree model from 1 to 14
#    max_depth = np.arange(1, 14)
#    train_err = np.zeros(len(max_depth))
#    test_err = np.zeros(len(max_depth))

#    for i, d in enumerate(max_depth):
        # Setup a Decision Tree Regressor so that it learns a tree with depth d
#    regressor = DecisionTreeRegressor(max_depth = d)
#
#        # Fit the learner to the training data
#    regressor.fit(X_train, y_train)

        # Find the performance on the training set
    train_err = performance_metric(y_train, regressor_type.predict(X_train))

        # Find the performance on the testing set
    test_err = performance_metric(y_test, regressor_type.predict(X_test))

    # Plot the model complexity graph
    Regression_Nmae =Regression_Nmae +'  Regressor Complexity Performance'
    plt.figure(figsize=(7, 5))
    plt.title(Regression_Nmae)
    plt.plot(test_err, lw=2, label = 'Testing Error')
    plt.plot( train_err, lw=2, label = 'Training Error')
    plt.legend()
    plt.xlabel('Maximum Depth')
    plt.ylabel('Total Error')
    plt.show()
    


