# Agglomerative Clustering

Agglomerative Clustering is a type of hierarchical clustering algorithm that builds a hierarchy of clusters from individual data points. It starts with each data point as a single cluster and then iteratively merges the closest pairs of clusters until all data points are in a single cluster or a stopping criterion is met.

## How it Works

The process of Agglomerative Clustering can be summarized as follows:

1.  **Initialization**: Each data point is considered a separate cluster.
2.  **Iterative Merging**:
    *   Find the two closest clusters based on a chosen linkage criterion (e.g., single linkage, complete linkage, average linkage, Ward's method).
    *   Merge these two clusters into a new, larger cluster.
    *   Repeat this step until only one cluster remains or a predefined number of clusters is achieved.

## Linkage Criteria

The choice of linkage criterion determines how the distance between two clusters is calculated:

*   **Single Linkage**: The distance between two clusters is the minimum distance between any two points in the different clusters.
*   **Complete Linkage**: The distance between two clusters is the maximum distance between any two points in the different clusters.
*   **Average Linkage**: The distance between two clusters is the average distance between all pairs of points in the different clusters.
*   **Ward's Method**: Merges the two clusters that lead to the minimum increase in total within-cluster variance.

## Advantages

*   Provides a hierarchical structure of clusters, which can be visualized using a dendrogram.
*   Does not require specifying the number of clusters beforehand (though a cutoff can be applied to the dendrogram).
*   Can reveal relationships between clusters at different levels of granularity.

## Disadvantages

*   Computationally expensive for large datasets (O(n^3) in the worst case for distance matrix calculation and O(n^2) for merging).
*   Sensitive to noise and outliers, especially with single linkage.
*   The choice of linkage criterion and distance metric can significantly impact the results.

## Applications

*   **Biology**: Phylogenetic tree construction, gene expression analysis.
*   **Image Processing**: Image segmentation.
*   **Information Retrieval**: Document clustering.
*   **Market Segmentation**: Grouping customers with similar purchasing behaviors.

## Example

A common way to visualize the output of agglomerative clustering is through a dendrogram, which graphically represents the hierarchy of clusters.

```python
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Sample data
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Perform Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = model.fit_predict(X)
print("Cluster labels:", labels)

# Generate the linkage matrix for dendrogram
linked = linkage(X, 'ward')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=range(len(X)),
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('Dendrogram for Agglomerative Clustering')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()
```
