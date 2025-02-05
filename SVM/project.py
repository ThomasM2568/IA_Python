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
from sklearn import datasets
import numpy as np

#------------------
# Functions
#------------------

def main():
    iris = datasets.load_iris()
    diabete = datasets.load_diabetes()
    
    irisArray = np.unique(iris.target)
    diabeteArray = np.unique(diabete.target)
    

    irisX = iris.data[:,:2]
    irisY = iris.target
    diabeteX = diabete.data[:,:2]
    diabeteY = diabete.target
    
    X_train, X_test, y_train, y_test = train_test_split(diabeteX,diabeteY,test_size=0.2,random_state=42)
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
    
#------------------
# Main
#------------------

if __name__ == '__main__':
    main()


