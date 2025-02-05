# Clustering Visualization Tool

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Importing Libraries](#importing-libraries)
  - [GUI Creation](#gui-creation)
  - [Loading the Iris Dataset](#loading-the-iris-dataset)
  - [Applying K-Means](#applying-k-means)
  - [Applying Hierarchical Clustering](#applying-hierarchical-clustering)
  - [Dimensionality Reduction with PCA](#dimensionality-reduction-with-pca)
  - [Creating the DataFrame](#creating-the-dataframe)
  - [Visualizing Clusters](#visualizing-clusters)
- [Conclusion](#conclusion)

## 1️⃣ Introduction
This project implements a clustering visualization tool using Tkinter to display results of K-Means and hierarchical clustering applied to the Iris dataset.

The goal is to analyze whether K-Means and hierarchical clustering correctly group the three species of flowers based on their characteristics.

## 2️⃣ Prerequisites
Before running this script, make sure you have the following libraries installed:

- `tkinter` (built-in with Python)
- `matplotlib`
- `seaborn`
- `pandas`
- `scikit-learn`
- `scipy`
- `ucimlrepo`

## 3️⃣ Installation
To install the necessary dependencies, run:

```sh
pip install matplotlib seaborn pandas scikit-learn scipy ucimlrepo
```

## 4️⃣ Code Explanation

### 🔹 Importing Libraries
```python
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram
from ucimlrepo import fetch_ucirepo
import csv
```

- **Tkinter**: for GUI creation.
- **Matplotlib & Seaborn**: for visualization.
- **Pandas**: for data manipulation.
- **Scikit-learn**: for clustering (K-Means, PCA).
- **Scipy**: for hierarchical clustering.
- **Ucimlrepo**: for fetching the Iris dataset.

### 🔹 GUI Creation
The GUI is built using Tkinter with a scrollable interface to display clustering results.

### 🔹 Loading the Iris Dataset
```python
iris = fetch_ucirepo(id=53)
X = iris.data.features
y = iris.data.targets  # Actual species names
```
- `X`: contains the flower characteristics.
- `y`: contains the species names (Setosa, Versicolor, Virginica).

### 🔹 Applying K-Means
```python
kmeans = KMeans(n_clusters=3, init='random', random_state=42)
clusters = kmeans.fit_predict(X)
```
- `n_clusters=3`: we request 3 clusters (since there are 3 species).
- `init='random'`: randomly initializes cluster centers.
- `random_state=42`: ensures reproducibility.

### 🔹 Applying Hierarchical Clustering
```python
linkage_matrix = linkage(X, method='average')
```
Computes a hierarchical clustering linkage matrix.

### 🔹 Dimensionality Reduction with PCA
```python
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
```
PCA reduces the 4D data to 2D for visualization.

### 🔹 Creating the DataFrame
```python
df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
df['Species'] = clusters
```
- Stores the first two principal components in a DataFrame.
- Adds a `Species` column with cluster names.

### 🔹 Visualizing Clusters

#### 🔹 K-Means Clustering Plot
```python
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue=df['Species'], palette='Set1', data=df, s=100, edgecolor='k')
plt.title("KMeans Clustering with Species Labels")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Species")
plt.show()
```

#### 🔹 Hierarchical Clustering Dendrogram
```python
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix, truncate_mode="level", p=10)
plt.title("Dendrogram of Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()
```

## Conclusion
While K-Means successfully groups the three expected species, hierarchical clustering may struggle to capture the natural structure of the dataset due to distance calculations and linkage methods.

The GUI allows users to visualize both clustering techniques interactively.
