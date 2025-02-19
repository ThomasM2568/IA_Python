# xgboost

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
  - [Importing Libraries](#importing-libraries)
  - [Dataset Fetching](#dataset-fetching)
  - [Data Preprocessing](#data-processing)
  - [Model Training and Evaluation](#mode)
  - [Validation](#validation)
- [Conclusion](#conclusion)

## 1️⃣ Introduction
<a name="introduction"></a>
This project utilizes machine learning techniques, including data preprocessing and predictive modeling, using the XGBoost framework. The dataset is sourced from the UCI Machine Learning Repository.

## 2️⃣ Prerequisites
<a name="prerequisites"></a>
Before running this script, make sure you have the following libraries installed:

- `ucimlrepo` (for fetching datasets from the UCI Machine Learning Repository)
- `pandas` (for data manipulation and analysis)
- `numpy` (for numerical operations)
- `scikit-learn` (for machine learning utilities such as train-test splitting and evaluation metrics)
- `xgboost` (for gradient boosting modeling)
- `tkinter` (built-in with Python, for UI development)
- `matplotlib` (for data visualization)
- `seaborn` (for enhanced statistical data visualization)

## 3️⃣ Installation
<a name="installation"></a>
To install the necessary dependencies, run:

```sh
pip install pandas numpy scikit-learn xgboost matplotlib seaborn ucimlrepo
```

## 4️⃣ Code Explanation
<a name="code-explanation"></a>
### 🔹 Importing Libraries
<a name="importing-libraries"></a>
```python
from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error
import xgboost as xgb
```

- **Tkinter**: for GUI creation.
- **Matplotlib & Seaborn**: for visualization.
- **Pandas**: for data manipulation.
- **Scikit-learn**: for clustering (K-Means, PCA).
- **Scipy**: for hierarchical clustering.
- **Ucimlrepo**: for fetching the Iris dataset.
- **XGBoost**: for gradient boosting modeling.

### 🔹 Dataset fetching
<a name="dataset-fetching"></a>
```python
iris = fetch_ucirepo(id=53)
X = iris.data.features
y = iris.data.targets  # Actual species names
```
- `X`: contains the adult features.
- `y`: contains the adulte targets.

### 🔹 Applying K-Means
<a name="data-processing"></a>
```python
# Split the dataset into train, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Ensure that y_train, y_val, and y_test are 1D arrays (not column vectors)
y_train = y_train.ravel()
y_val = y_val.ravel()
y_test = y_test.ravel()

#...

# Fit and transform the training set, and only transform the validation and test sets
X_train_encoded = encoder.fit_transform(X_train[categorical_cols])
X_val_encoded = encoder.transform(X_val[categorical_cols])
X_test_encoded = encoder.transform(X_test[categorical_cols])
```
- `test_size=0.5`: we ask for different test size.
- `random_state`: ensures reproducibility.

### 🔹 Enabling the XGBoost classifier model 
<a name="model"></a>
```python
model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss')
```
Initializes an XGBoost classifier for a binary classification problem with specific parameters.

### 🔹 Validation
<a name="validation"></a>
```python
cv_scores = cross_val_score(model, X_train_encoded, y_train, cv=5, scoring='accuracy')  # 5-fold cross-validation
```
Perform a 5-fold cross-validation to evaluate the performance of the XGBoost model on the training data.

## Conclusion
<a name="conclusion"></a>
The XGBoost model achieves a reasonable accuracy through cross-validation.

Encoding categorical features improves model performance.

The validation and test errors provide insight into model generalization.

Further tuning (e.g., hyperparameter optimization) can improve results.
