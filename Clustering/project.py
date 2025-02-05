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
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram
from ucimlrepo import fetch_ucirepo
import csv

#------------------
# Functions
#------------------

def plot_kmeans(df):
    """Create KMeans clustering plot."""
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
    iris = fetch_ucirepo(id=53)
    X = iris.data.features
    y = iris.data.targets 

    with open('iris.data', newline='') as f:
        reader = csv.reader(f)        
        rowElements = [row[-1] for row in reader if row]
        counter = len(set(rowElements))


    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=counter, init='random', random_state=42)
    clusters = kmeans.fit_predict(X)

    # Reduce dimensions using PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # Create a DataFrame for visualization
    df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
    df['Species'] = clusters

    # Create KMeans plot and embed in tkinter
    kmeans_fig = plot_kmeans(df)
    canvas_kmeans = FigureCanvasTkAgg(kmeans_fig, master=plot_frame)
    canvas_kmeans.get_tk_widget().pack(side=tk.TOP, pady=20)  # Add some padding for separation

    # Create Dendrogram plot and embed in tkinter
    dendrogram_fig = plot_dendrogram(X)
    canvas_dendrogram = FigureCanvasTkAgg(dendrogram_fig, master=plot_frame)
    canvas_dendrogram.get_tk_widget().pack(side=tk.TOP, pady=20)  # Add some padding for separation

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

