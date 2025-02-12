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

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, MeanShift
from scipy.cluster.hierarchy import linkage, dendrogram
from ucimlrepo import fetch_ucirepo
import csv
import numpy as np
from scipy.spatial.distance import cdist

#------------------
# Functions
#------------------

def plot_kmeans(df):
    """ Create KMeans clustering plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='PCA1', y='PCA2', hue=df['Species'], palette='Set1', data=df, s=100, edgecolor='k', ax=ax)
    ax.set_title("KMeans Clustering with Species Labels")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.legend(title="Species")
    return fig

def plot_dendrogram(X):
    """Create hierarchical clustering dendrogram plot."""
    linkage_matrix = linkage(X, method='average')
    fig, ax = plt.subplots(figsize=(10, 6))
    dendrogram(linkage_matrix, truncate_mode="level", p=10, ax=ax)
    ax.set_title("Dendrogram of Hierarchical Clustering")
    ax.set_xlabel("Data Points")
    ax.set_ylabel("Distance")
    return fig

def plot_meanshift(df):
    """Create MeanShift clustering plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='PCA1', y='PCA2', hue=df['MeanShift'], palette='Set1', data=df, s=100, edgecolor='k', ax=ax)
    ax.set_title("MeanShift Clustering with Species Labels")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.legend(title="Species")
    return fig

def plot_elbow(wcss):
    """Create Elbow Method plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(range(1, len(wcss) + 1), wcss, marker='o')
    ax.set_title("Elbow Method for Optimal K")
    ax.set_xlabel("Number of Clusters (K)")
    ax.set_ylabel("WCSS (Within-Cluster Sum of Squares)")
    return fig

def calculate_dunn_index(X, labels):
    """Calculate the Dunn Index for a clustering solution."""
    unique_labels = np.unique(labels)
    min_dist = np.inf
    max_diameter = -np.inf

    # Compute the pairwise distances between all points
    distances = cdist(X, X)

    # Compute minimum distance between clusters
    for i in unique_labels:
        for j in unique_labels:
            if i != j:
                # Get the points in each cluster
                points_i = X[labels == i]
                points_j = X[labels == j]
                # Compute the minimum distance between points in different clusters
                min_dist = min(min_dist, np.min(cdist(points_i, points_j)))

    # Compute the maximum diameter of any cluster
    for i in unique_labels:
        points_i = X[labels == i]
        diameter = np.max(cdist(points_i, points_i))  # Max distance between points within the cluster
        max_diameter = max(max_diameter, diameter)

    # Dunn Index = Min distance between clusters / Max cluster diameter
    return min_dist / max_diameter if max_diameter != 0 else 0

def dunn(X, labels):
    """Calculate the Dunn Index for clustering."""
    nb_clusters = len(np.unique(labels))  # Number of unique clusters
    clusters = {}

    # Organize data points by cluster
    for k in range(nb_clusters):
        clusters[k] = np.array([X[i] for i in range(len(labels)) if labels[i] == k])

    # Calculate maximum cluster diameter (maximum pairwise distance within the same cluster)
    max_diameter = max([np.amax(cdist(clusters[k], clusters[k])) for k in range(nb_clusters)])

    # Calculate minimum separation (minimum pairwise distance between different clusters)
    min_separation = min([np.amin(cdist(clusters[k], clusters[l])) 
                          for k in range(nb_clusters-1) 
                          for l in range(k+1, nb_clusters)])

    # Return Dunn Index
    return min_separation / max_diameter if max_diameter != 0 else 0

def create_gui():
    """Create the tkinter GUI."""
    # Create tkinter window
    root = tk.Tk()
    root.title("Clustering Visualizations")

    # Create a canvas for scrolling
    canvas_frame = ttk.Frame(root)
    canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(canvas_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to contain the plots
    plot_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=plot_frame, anchor="nw")

    # Fetch dataset
    hungarian = fetch_ucirepo(id=53)
    X = hungarian.data.features
    y = hungarian.data.targets 

    # Count unique labels from the iris dataset (assuming iris.data.targets contains the labels)
    with open('hungarian.data', newline='') as f:
        reader = csv.reader(f)        
        rowElements = [row[-1] for row in reader if row]
        counter = len(set(rowElements))

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=min(counter, 10), init='random', random_state=42)
    clusters_kmeans = kmeans.fit_predict(X)

    # Reduce dimensions using PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # Create a DataFrame for visualization
    df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
    df['Species'] = clusters_kmeans  # Assign KMeans clusters to the 'Species' column

    # Create KMeans plot and embed in tkinter
    kmeans_fig = plot_kmeans(df)
    canvas_kmeans = FigureCanvasTkAgg(kmeans_fig, master=plot_frame)
    canvas_kmeans.get_tk_widget().pack(side=tk.TOP, pady=20)  # Add some padding for separation

    # Create Dendrogram plot and embed in tkinter
    dendrogram_fig = plot_dendrogram(X)
    canvas_dendrogram = FigureCanvasTkAgg(dendrogram_fig, master=plot_frame)
    canvas_dendrogram.get_tk_widget().pack(side=tk.TOP, pady=20)  # Add some padding for separation

    # Apply MeanShift clustering
    meanshift = MeanShift()
    clusters_meanshift = meanshift.fit_predict(X)

    # Update DataFrame with MeanShift labels
    df['MeanShift'] = clusters_meanshift  # Add MeanShift clusters to the DataFrame

    # Create MeanShift plot and embed in tkinter
    meanshift_fig = plot_meanshift(df)
    canvas_meanshift = FigureCanvasTkAgg(meanshift_fig, master=plot_frame)
    canvas_meanshift.get_tk_widget().pack(side=tk.TOP, pady=20)  # Add some padding for separation

    # Apply Elbow Method (KMeans WCSS)
    wcss = []
    for k in range(1, 11):  # Try different k values from 1 to 10
        kmeans = KMeans(n_clusters=k, init='random', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)  # WCSS (Within-Cluster Sum of Squares)

    # Create Elbow plot and embed in tkinter
    elbow_fig = plot_elbow(wcss)
    canvas_elbow = FigureCanvasTkAgg(elbow_fig, master=plot_frame)
    canvas_elbow.get_tk_widget().pack(side=tk.TOP, pady=20)  # Add some padding for separation

    # Calculate Dunn Index for KMeans and MeanShift
    dunn_kmeans = calculate_dunn_index(X, clusters_kmeans)
    dunn_meanshift = calculate_dunn_index(X, clusters_meanshift)

    # Display Dunn Index values
    dunn_label_kmeans = tk.Label(plot_frame, text=f"Dunn Index (KMeans): {dunn_kmeans:.4f}")
    dunn_label_kmeans.pack(side=tk.TOP, pady=10)

    dunn_label_meanshift = tk.Label(plot_frame, text=f"Dunn Index (MeanShift): {dunn_meanshift:.4f}")
    dunn_label_meanshift.pack(side=tk.TOP, pady=10)

    # Update the scrollable region to match the total size of the plots
    plot_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Start tkinter event loop
    root.mainloop()

#------------------
# Main
#------------------

if __name__ == '__main__':
    create_gui()

