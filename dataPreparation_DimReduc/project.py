#!/usr/bin/python3
'''
Created on 05-02-2025

@author: Pierre Meyer, Yohann Mitel, Kyllian Cuevas, Thomas Mirbey
@version: 1

Clustering project with tkinter GUI for visualization
'''

#------------------
# Import Libraries
#------------------

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif
from sklearn.decomposition import PCA
from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np

#------------------
# Load Dataset
#------------------

adult = fetch_ucirepo(id=2)  # Fetch the Adult Income Dataset

X = adult.data.features
y = adult.data.targets.to_numpy().ravel()

#------------------
# Handle Categorical Features
#------------------

if isinstance(X, pd.DataFrame):
    categorical_cols = X.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        X_encoded = pd.DataFrame(encoder.fit_transform(X[categorical_cols]))
        X_encoded.columns = encoder.get_feature_names_out(categorical_cols)

        # Drop original categorical columns and reset index
        X = X.drop(columns=categorical_cols).reset_index(drop=True)
        X = pd.concat([X, X_encoded], axis=1)

#------------------
# Feature Selection
#------------------

# Remove features with low variance
selector = VarianceThreshold(threshold=np.median(np.var(X, axis=0)))  
X = selector.fit_transform(X)

# Select the top k best features
select_k_best = SelectKBest(f_classif, k=min(15, X.shape[1]))  # Keeping 15 best features
X = select_k_best.fit_transform(X, y)

#------------------
# Data Scaling
#------------------

scaler = StandardScaler()
X = scaler.fit_transform(X)

#------------------
# Apply PCA for Dimensionality Reduction
#------------------

pca = PCA(n_components=10)  # Reduce to 10 components (tweak this)
X = pca.fit_transform(X)

# Print explained variance ratio to check retained information
explained_variance = np.sum(pca.explained_variance_ratio_)
print(f"Explained Variance Retained: {explained_variance:.4f}")

#------------------
# Train-Test Split
#------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

#------------------
# Initialize Models
#------------------

models = {
    "SVM": SVC(kernel="rbf", C=1, gamma="scale", random_state=42),
    "Decision Tree": DecisionTreeClassifier(max_depth=10, min_samples_split=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42),
    "SGD Classifier": SGDClassifier(loss="log_loss", learning_rate="adaptive", eta0=0.01, max_iter=1000, random_state=42),
    "Neural Network": MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', solver='adam', alpha=0.005, max_iter=500, random_state=42)
}

#------------------
# Train and Evaluate Models
#------------------

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

#------------------
# Print Results
#------------------

for name, acc in results.items():
    print(f"{name}: {acc:.4f}")

