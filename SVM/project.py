#!/usr/bin/python3
'''
Created on 05-02-2025

@author: Pierre Meyer, Yohann Mitel, Kyllian Cuevas, Thomas Mirbey
@version: 1

Clustering project with tkinter GUI for visualization
'''

#------------------
# Import
#------------------

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo 


#------------------
# Functions
#------------------

def main():
    iris = datasets.load_iris()
    diabete = datasets.load_diabetes()
    wine_quality = fetch_ucirepo(id=186) 
    
    irisArray = np.unique(iris.target)
    diabeteArray = np.unique(diabete.target)
    

    irisX = iris.data[:,:2]
    irisY = iris.target
    diabeteX = diabete.data[:,:2]
    diabeteY = diabete.target
    
    X = wine_quality.data.features 
    y = wine_quality.data.targets 
  
    #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    y_train = y_train.to_numpy().ravel()
    y_test = y_test.to_numpy().ravel()


    """print(f'X_train: {X_train} \n')
    print(f'X_test: {X_test} \n')
    print(f'y_train: {y_train} \n')
    print(f'y_test: {y_test} \n')"""
    
    clf = SVC(kernel='linear',random_state=42)
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)

    """min_label, max_label = np.min(y_pred), np.max(y_pred)
    replace_percentage = 0.1  
    num_replace = int(len(y_pred) * replace_percentage)
    indices_to_replace = np.random.choice(len(y_pred), num_replace, replace=False)
    y_pred[indices_to_replace] = np.random.randint(min_label, max_label + 1, size=num_replace)"""

    y_pred = clf.predict(X_test)
    print(y_test)
    print(y_pred)
    print(accuracy_score(y_test,y_pred))
    
    svc_scores = cross_val_score(clf,X_train,y_train,cv=4)
    print(svc_scores)
    print("Mean : {0:.4f}".format(svc_scores.mean()))
    print("Standard deviation: {0:.4f}".format(svc_scores.std()))
    
    
    # Initialize models
    models = {
        "SVM": SVC(kernel="linear"),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators=100),
        "SGD Classifier": SGDClassifier(loss="hinge"),
        "Neural Network": MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
    }
    
    '''models = {
        "SVM": SVC(kernel="linear"),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators=200),
        "SGD Classifier": SGDClassifier(loss="hinge"),
        "Neural Network": MLPClassifier(hidden_layer_sizes=(200,), max_iter=1000)
    }'''

    # Train and evaluate
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy

    # Print results
    for name, acc in results.items():
        print(f"{name}: {acc:.4f}")
    
#------------------
# Main
#------------------

if __name__ == '__main__':
    main()