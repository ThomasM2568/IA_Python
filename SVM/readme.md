# SVM Classification Tool

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
  - [Importing Libraries](#importing-libraries)
  - [Loading Datasets](#loading-datasets)
  - [Splitting Data](#splitting-data)
  - [Training the SVM Model](#training-the-svm-model)
  - [Evaluating the Model](#evaluating-the-model)
  - [Visualizing Results](#visualizing-results)
- [Conclusion](#conclusion)

## 1️⃣ Introduction
<a name="introduction"></a>
This project implements an SVM classification tool using Scikit-Learn to train and evaluate an SVM model on the Iris and Diabetes datasets.

The goal is to assess the model’s accuracy and decision boundaries for better understanding classification performance.

## 2️⃣ Prerequisites
<a name="prerequisites"></a>
Before running this script, make sure you have the following libraries installed:

- `numpy`
- `matplotlib`
- `scikit-learn`

## 3️⃣ Installation
<a name="installation"></a>
To install the necessary dependencies, run:

```sh
pip install numpy matplotlib scikit-learn
```

## 4️⃣ Code Explanation
<a name="code-explanation"></a>

### 🔹 Importing Libraries
<a name="importing-libraries"></a>
```python
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
```

- **Scikit-Learn**: for dataset loading, model training, and evaluation.
- **NumPy**: for numerical operations.
- **Matplotlib**: for visualization.

### 🔹 Loading Datasets
<a name="loading-datasets"></a>
```python
iris = datasets.load_iris()
diabetes = datasets.load_diabetes()
```
- `iris`: contains flower classification data.
- `diabetes`: contains medical diagnostic data.

### 🔹 Splitting Data
<a name="splitting-data"></a>
```python
X_train, X_test, y_train, y_test = train_test_split(iris.data[:, :2], iris.target, test_size=0.2, random_state=42)
```
- Splits the dataset into training and testing sets.
- Uses **20% of the data** for testing.

### 🔹 Training the SVM Model
<a name="training-the-svm-model"></a>
```python
clf = SVC(kernel='linear', random_state=42)
clf.fit(X_train, y_train)
```
- **Linear kernel** is used for classification.
- The model is trained on the **training set**.

### 🔹 Evaluating the Model
<a name="evaluating-the-model"></a>
```python
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
```
- **Predictions** are made using the trained model.
- Accuracy is computed to measure performance.

#### 🔹 Cross-Validation
```python
scores = cross_val_score(clf, X_train, y_train, cv=4)
```
- Evaluates model **stability and generalization**.
- Uses **4-fold cross-validation**.

### 🔹 Visualizing Results
<a name="visualizing-results"></a>

#### 🔹 SVM Classification Plot
```python
def plot_svm(X_train, X_test, y_train, y_test, clf):
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', edgecolor='k', s=100)
    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
    ax.set_title("SVM Decision Boundary")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.legend(handles=scatter.legend_elements()[0], title="Classes")
    return fig
```

- **Plots decision boundaries** of the SVM model.
- **Colors indicate class separations**.

#### 🔹 Cross-Validation Score Plot
```python
def plot_cross_val_scores(scores):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(range(1, len(scores) + 1), scores, marker='o', linestyle='--')
    ax.set_title("Cross-Validation Scores")
    ax.set_xlabel("Fold")
    ax.set_ylabel("Accuracy Score")
    return fig
```

- Helps analyze model **stability and consistency**.

#### 🔹 Accuracy Comparison Bar Plot
```python
def plot_accuracy(accuracy):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(["SVM"], [accuracy], color='skyblue')
    ax.set_ylim(0, 1)
    ax.set_title("Model Accuracy")
    ax.set_ylabel("Accuracy Score")
    return fig
```

- Displays **SVM model accuracy**.

##### 🔹 Why Accuracy Varies Across Datasets

The accuracy of a classification model depends on the nature of the dataset. Some models, like SVM, perform better when classes are linearly separable, while Random Forest and neural networks handle nonlinear relationships and complex data more effectively. The amount of data is also a key factor: neural networks require a large volume of data to generalize well, whereas decision trees and Random Forest can be effective with smaller datasets. Additionally, the presence of noise and outliers affects models differently, with tree-based methods often being more robust than linear models.  

Other factors also influence performance, such as dataset dimensionality, class balance, and hyperparameter tuning. For example, an imbalanced dataset can be problematic for SVM, whereas Random Forest can manage such imbalance more effectively. Parameter tuning is crucial for certain models, such as selecting the right kernel for SVM or the architecture for a neural network. Ultimately, there is no universally best model—multiple approaches should be tested, and cross-validation should be used to determine which one performs best based on the dataset’s specific characteristics.

## 5️⃣ Conclusion
<a name="conclusion"></a>
SVM is an effective classification model for the **Iris dataset**, achieving high accuracy. Cross-validation confirms the model’s stability, and visualization provides insight into decision boundaries.

This tool allows for **training, evaluation, and visualization** of SVM models interactively.

