# Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Code Explanation](#-code-explanation)
  - [Importing Libraries](#-importing-libraries)
  - [Loading the Iris Dataset](#-loading-the-iris-dataset)
  - [Applying K-Means](#-applying-k-means)
  - [Assigning Names to Clusters](#-assigning-names-to-clusters)
  - [Dimensionality Reduction with PCA](#-dimensionality-reduction-with-pca)
  - [Creating the DataFrame](#-creating-the-dataframe)
  - [Visualizing Clusters](#-visualizing-clusters)



# 1️⃣ Introduction

This project applies the K-Means clustering algorithm to the Iris dataset, reduces the data dimensionality using PCA, and then displays the results as a graph.

The goal is to verify whether K-Means correctly groups the three flower species based on their characteristics.

## 2️⃣ Prerequisites

Before running this script, make sure you have the following libraries installed:

- `matplotlib`
- `seaborn`
- `pandas`
- `scikit-learn`
- `ucimlrepo`

## 3️⃣ Installation

```bash
pip install matplotlib seaborn pandas scikit-learn ucimlrepo
```

## 4️⃣ Code Explanation

### 🔹 Importing Libraries

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from ucimlrepo import fetch_ucirepo
```

- **Matplotlib & Seaborn**: for visualizing clusters.
- **Pandas**: for data manipulation.
- **PCA**: for dimensionality reduction.
- **KMeans**: for clustering.
- **fetch_ucirepo**: for retrieving the Iris dataset.

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

- `n_clusters=3`: we request 3 clusters (since there are 3 flower species).
- `init='random'`: randomly initializes cluster centers.
- `random_state=42`: ensures reproducibility.

### 🔹 Assigning Names to Clusters

```python
species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
cluster_names = [species_mapping[label] for label in clusters]
```

- K-Means assigns numbers `(0, 1, 2)` to clusters.
- We map these numbers to species names.

⚠ **Note**: K-Means does not guarantee that the numbers will match the actual species!

### 🔹 Dimensionality Reduction with PCA

```python
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
```

- **PCA** reduces the 4D data to 2D for visualization.

### 🔹 Creating the DataFrame

```python
df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
df['Species'] = cluster_names
```

- Stores the first two principal components in a DataFrame.
- Adds a `Species` column with cluster names.

### 🔹 Visualizing Clusters

```python
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue=df['Species'], palette='Set1', data=df, s=100, edgecolor='k')
plt.title("KMeans Clustering with Species Labels")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Species")
plt.show()
```

- Displays a colored scatter plot representing clusters.
- `hue=df['Species']`: colors based on species.
- `edgecolor='k'`: black edges for better visibility.
