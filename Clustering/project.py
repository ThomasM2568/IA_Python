import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from ucimlrepo import fetch_ucirepo

# Fetch dataset
iris = fetch_ucirepo(id=53)
X = iris.data.features
y = iris.data.targets 

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, init='random', random_state=42)
clusters = kmeans.fit_predict(X)

# Put together species by name
species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
cluster_names = [species_mapping[label] for label in clusters]

# Reduce dimensions using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Create a DataFrame for visualization
df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
df['Species'] = cluster_names  # Use species names

# Show clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue=df['Species'], palette='Set1', data=df, s=100, edgecolor='k')
plt.title("KMeans Clustering with Species Labels")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Species")
plt.show()

