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
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif
from ucimlrepo import fetch_ucirepo 

# Load datasets
iris = datasets.load_iris()
diabete = datasets.load_diabetes()
wine_quality = fetch_ucirepo(id=186)

X = wine_quality.data.features
y = wine_quality.data.targets.to_numpy().ravel()

# Encoding categorical variables
if isinstance(X, pd.DataFrame):
    categorical_cols = X.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
        X_encoded = pd.DataFrame(encoder.fit_transform(X[categorical_cols]))
        X = X.drop(columns=categorical_cols).reset_index(drop=True)
        X_encoded.columns = encoder.get_feature_names_out(categorical_cols)
        X = pd.concat([X, X_encoded], axis=1)

# Feature selection
selector = VarianceThreshold(threshold=np.median(np.var(X, axis=0))) # Remove features with low variance
X = selector.fit_transform(X)

select_k_best = SelectKBest(f_classif, k=min(10, X.shape[1]))
X = select_k_best.fit_transform(X, y)

# Data scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    "SVM": SVC(kernel="rbf", C=10, gamma=0.1, random_state=42),
    "Decision Tree": DecisionTreeClassifier(max_depth=10, min_samples_split=5, min_samples_leaf=3, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=300, max_depth=15, min_samples_split=4, min_samples_leaf=2, random_state=42),
    "SGD Classifier": SGDClassifier(loss="log_loss", learning_rate="adaptive", eta0=0.01, max_iter=1000, random_state=42),
    "Neural Network": MLPClassifier(hidden_layer_sizes=(256, 128, 64), activation='relu', solver='adam', alpha=0.001, max_iter=1000, random_state=42)
}

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
