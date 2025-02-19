# xgboost

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
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
<a name="gui-creation"></a>
The GUI is built using Tkinter with a scrollable interface to display clustering results.

### 🔹 Loading the Iris Dataset
<a name="loading-the-iris-dataset"></a>
```python
iris = fetch_ucirepo(id=53)
X = iris.data.features
y = iris.data.targets  # Actual species names
```
- `X`: contains the flower characteristics.
- `y`: contains the species names (Setosa, Versicolor, Virginica).

### 🔹 Applying K-Means
<a name="applying-k-means"></a>
```python
kmeans = KMeans(n_clusters=3, init='random', random_state=42)
clusters = kmeans.fit_predict(X)
```
- `n_clusters=3`: we request 3 clusters (since there are 3 species).
- `init='random'`: randomly initializes cluster centers.
- `random_state=42`: ensures reproducibility.

### 🔹 Applying Hierarchical Clustering
<a name="applying-hierarchical-clustering"></a>
```python
linkage_matrix = linkage(X, method='average')
```
Computes a hierarchical clustering linkage matrix.

### 🔹 Dimensionality Reduction with PCA
<a name="dimensionality-reduction-with-pca"></a>
```python
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
```
PCA reduces the 4D data to 2D for visualization.

### 🔹 Creating the DataFrame
<a name="creating-the-dataframe"></a>
```python
df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
df['Species'] = clusters
```
- Stores the first two principal components in a DataFrame.
- Adds a `Species` column with cluster names.

### 🔹 Visualizing Clusters
<a name="visualizing-clusters"></a>

#### 🔹 K-Means Clustering Plot
```python
def plot_kmeans(df):
    """ Create KMeans clustering plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='PCA1', y='PCA2', hue=df['Species'], palette='Set1', data=df, s=100, edgecolor='k', ax=ax)
    ax.set_title("KMeans Clustering with Species Labels")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.legend(title="Species")
    return fig
```
- Uses **Seaborn** for better aesthetics.
- `hue=df['Species']`: Colors points by cluster.
- `s=100, edgecolor='k'`: Improves point visibility.

#### 🔹 Hierarchical Clustering Dendrogram
```python
def plot_dendrogram(X):
    """Create hierarchical clustering dendrogram plot."""
    linkage_matrix = linkage(X, method='average')
    fig, ax = plt.subplots(figsize=(10, 6))
    dendrogram(linkage_matrix, truncate_mode="level", p=10, ax=ax)
    ax.set_title("Dendrogram of Hierarchical Clustering")
    ax.set_xlabel("Data Points")
    ax.set_ylabel("Distance")
    return fig
```
- Uses **Scipy’s dendrogram** to visualize hierarchical clustering.
- `truncate_mode="level", p=10`: Shows only the first 10 levels.
- Helps identify optimal cluster separation.

#### 🔹 MeanShift Clustering Plot
```python
def plot_meanshift(df):
    """Create MeanShift clustering plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='PCA1', y='PCA2', hue=df['MeanShift'], palette='Set1', data=df, s=100, edgecolor='k', ax=ax)
    ax.set_title("MeanShift Clustering with Species Labels")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.legend(title="Species")
    return fig
```
- **MeanShift** clustering assigns different numbers of clusters dynamically.
- **Comparison with KMeans**: Allows non-uniform cluster sizes.

#### 🔹 Elbow Method Plot for Optimal K
```python
def plot_elbow(wcss):
    """Create Elbow Method plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(range(1, len(wcss) + 1), wcss, marker='o')
    ax.set_title("Elbow Method for Optimal K")
    ax.set_xlabel("Number of Clusters (K)")
    ax.set_ylabel("WCSS (Within-Cluster Sum of Squares)")
    return fig
```
- **WCSS (Within-Cluster Sum of Squares)** measures clustering compactness.
- **The “elbow” point** suggests the optimal K for KMeans.



## Conclusion
<a name="conclusion"></a>
While K-Means successfully groups the three expected species, hierarchical clustering may struggle to capture the natural structure of the dataset due to distance calculations and linkage methods.

The GUI allows users to visualize both clustering techniques interactively.
