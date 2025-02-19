'''
Created on 19-02-2025

@author: Pierre Meyer, Yohann Mitel, Kyllian Cuevas, Thomas Mirbey
@version: 1

Clustering project with tkinter GUI for visualization
'''

from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error
import xgboost as xgb

# Fetch the Adult dataset from UCI repository using ucimlrepo
adult = fetch_ucirepo(id=2)

# Data (features and target)
X = adult.data.features
y = adult.data.targets

# Check the metadata and variable information
print(adult.metadata)
print(adult.variables)

# Map the target labels to numeric values (e.g., '<=50K' -> 0, '>50K' -> 1)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset into train, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Ensure that y_train, y_val, and y_test are 1D arrays (not column vectors)
y_train = y_train.ravel()
y_val = y_val.ravel()
y_test = y_test.ravel()

# Check the shapes of the splits
print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"X_val shape: {X_val.shape}, y_val shape: {y_val.shape}")
print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

# Apply OneHotEncoder to categorical features
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Identify categorical columns (based on dataset structure)
categorical_cols = X.select_dtypes(include=['object']).columns

# Fit and transform the training set, and only transform the validation and test sets
X_train_encoded = encoder.fit_transform(X_train[categorical_cols])
X_val_encoded = encoder.transform(X_val[categorical_cols])
X_test_encoded = encoder.transform(X_test[categorical_cols])

# For the non-categorical columns (numerical features), we will concatenate them with the encoded ones
numerical_cols = X.select_dtypes(exclude=['object']).columns
X_train_encoded = np.concatenate([X_train[numerical_cols].values, X_train_encoded], axis=1)
X_val_encoded = np.concatenate([X_val[numerical_cols].values, X_val_encoded], axis=1)
X_test_encoded = np.concatenate([X_test[numerical_cols].values, X_test_encoded], axis=1)

# Check the shapes after encoding
print(f"Encoded X_train shape: {X_train_encoded.shape}")
print(f"Encoded X_val shape: {X_val_encoded.shape}")
print(f"Encoded X_test shape: {X_test_encoded.shape}")

# Initialize the XGBoost classifier model (since this is a binary classification problem)
model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss')

# Perform cross-validation on the training data
cv_scores = cross_val_score(model, X_train_encoded, y_train, cv=5, scoring='accuracy')  # 5-fold cross-validation

# Print cross-validation scores
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean cross-validation accuracy: {cv_scores.mean()}")

# Fit the model on the entire training set
model.fit(X_train_encoded, y_train)

# Make predictions on the validation set for evaluation
y_val_pred = model.predict(X_val_encoded)

# Print performance metrics
print(f"MAE (Validation) : {mean_absolute_error(y_val, y_val_pred)}")
print(f"MSE (Validation) : {mean_squared_error(y_val, y_val_pred)}")

# Make predictions on the test set
y_test_pred = model.predict(X_test_encoded)

# Print test performance metrics
print(f"MAE (Test) : {mean_absolute_error(y_test, y_test_pred)}")
print(f"MSE (Test) : {mean_squared_error(y_test, y_test_pred)}")

