# -*- coding: utf-8 -*-
"""

"""

from sklearn import  ensemble,neighbors
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import roc_auc_score,r2_score,make_scorer
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier
from sklearn.qda import QDA
from sklearn.svm import SVC

from  classification_plot import plot_classification
  

    
def Call_Random_Forest_Classi(X_train, y_train, X_test, y_test):
    """
    Random Forest Binary Classification
    """
    clf = ensemble.RandomForestClassifier(n_estimators=10,criterion='entropy',max_depth=3, n_jobs=-1)
#    print("Random Forest Classification  ",clf.get_params().keys())
    """
    ['warm_start', 'oob_score', 'n_jobs', 'verbose', 'max_leaf_nodes', 
    'bootstrap', 'min_samples_leaf', 'n_estimators', 'min_samples_split',
    'min_weight_fraction_leaf', 'criterion', 'random_state', 'max_features'
    , 'max_depth', 'class_weight'])
    """

    
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    
#    plot_classification(X_train, y_train, X_test, y_test,clf,'RandomForest')
    return accuracy
        
def Call_KNN_Classi(X_train, y_train, X_test, y_test):
    """
    KNN binary Classification
    """
    clf = neighbors.KNeighborsClassifier()
    """
    print("KNN Classification  ",clf.get_params().keys())
    ('KNN Classification  ', ['n_neighbors', 'n_jobs', 'algorithm', 'metric', 'metric_params', 'p', 'weights', 'leaf_size']
    """
#    parameters = [{'n_neighbors':[20],'weights':['distance'],'algorithm':['auto'],'n_jobs':[-1]}]
    parameters = [{'n_neighbors':[20],'weights':['distance'],'algorithm':['auto'],'n_jobs':[-1]}]

    scoring_function = make_scorer(r2_score, greater_is_better=True)
    clf = GridSearchCV(clf, parameters,scoring=scoring_function)

    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    auc = roc_auc_score(y_test, clf.predict(X_test))
    print("Area Under Curve =" , auc)
    
#    f, ax = plt.subplots(figsize=(8,8))
#    ax.plot(y_test,label="test")

    
    return accuracy

def Call_Support_Vector_Classi(X_train, y_train, X_test, y_test):
    """
    SVM binary Classification
    """
    clf = SVC()
#    print("SVC Classification  ",clf.get_params().keys())
    """
    ['kernel', 'C', 'verbose', 'probability', 'degree', 'shrinking',
    'max_iter', 'decision_function_shape', 'random_state', 'tol', 
    'cache_size', 'coef0', 'gamma', 'class_weight']
    """
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    plot_classification(X_train, y_train, X_test, y_test,clf,'SVC')

    return accuracy
    
def Call_AdaBoost_Classi(X_train, y_train, X_test, y_test):
    """
    Ada Boosting binary Classification
    """
#    n = parameters[0]
#    l =  parameters[1]
    clf = AdaBoostClassifier(n_estimators=10, learning_rate =0.1)
    """
    print("Ada Boosting  Classification ",clf.get_params().keys())
    ['n_estimators', 'base_estimator', 'random_state', 'learning_rate', 'algorithm']
    """
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    return accuracy
    
def Call_Gradient_Tree_GTB_Classi(X_train, y_train, X_test, y_test):
    """
    Gradient Tree Boosting binary Classification
    """
    clf = GradientBoostingClassifier(n_estimators=150)
    """
    print("Gradient Tree  Classification ",clf.get_params().keys())
    ['presort', 'loss', 'verbose', 'subsample', 'max_leaf_nodes', 'learning_rate',
    'warm_start', 'min_samples_leaf', 'n_estimators', 'min_samples_split', 
    'init', 'min_weight_fraction_leaf', 'random_state', 'max_features', 'max_depth'])
    """
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    return accuracy

def Call_QDA_Classi(X_train, y_train, X_test, y_test):
    """
    QDA Classification
    """
    clf = QDA()
    """
    print("QDA  Classification ",clf.get_params().keys())
    ['priors', 'reg_param', 'tol', 'store_covariances']
    """
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    return accuracy

