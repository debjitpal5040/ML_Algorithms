# K-Means Clustering

K-Means Clustering is an unsupervised machine learning algorithm used for partitioning `n` observations into `k` clusters, where each observation belongs to the cluster with the nearest mean (centroid), serving as a prototype of the cluster.

## How it Works

The K-Means algorithm follows an iterative approach to find the optimal cluster assignments:

1.  **Initialization**:
    *   Choose the number of clusters, `k`.
    *   Randomly select `k` data points from the dataset as initial centroids.

2.  **Assignment Step (E-step - Expectation)**:
    *   Each data point is assigned to the cluster whose centroid is closest to it. The distance metric commonly used is Euclidean distance.

3.  **Update Step (M-step - Maximization)**:
    *   The centroids of the clusters are re-calculated by taking the mean of all data points assigned to that cluster.

4.  **Convergence**:
    *   Steps 2 and 3 are repeated until the cluster assignments no longer change, or the centroids no longer move significantly, or a maximum number of iterations is reached.

## Key Concepts

*   **Centroid**: The center of a cluster, calculated as the mean of all data points belonging to that cluster.
*   **Inertia (Within-cluster sum of squares)**: A measure of how internally coherent clusters are. It is the sum of squared distances of samples to their closest cluster center. The goal of K-Means is to minimize inertia.
*   **Elbow Method**: A heuristic used to determine the optimal number of clusters (`k`). It involves plotting the inertia as a function of `k` and looking for an "elbow point" where the rate of decrease in inertia sharply changes.

## Use Cases

K-Means Clustering is widely used in various applications, including:
*   Customer segmentation
*   Image compression
*   Document clustering
*   Anomaly detection
*   Genomic sequencing analysis

# Bisecting K-Means Clustering

Bisecting K-Means is a hierarchical clustering algorithm that combines aspects of both hierarchical and partitional clustering. It starts with all data points in a single cluster and then iteratively splits clusters into two sub-clusters until the desired number of clusters (`k`) is reached.

## How it Works

The Bisecting K-Means algorithm proceeds as follows:

1.  **Initialization**:
    *   Start with a single cluster containing all data points.

2.  **Iteration**:
    *   In each step, select a cluster to split. The cluster chosen for splitting is typically the one with the largest sum of squared errors (SSE) or the largest size.
    *   Apply the standard K-Means algorithm (with `k=2`) to the selected cluster to divide it into two sub-clusters.
    *   Replace the original cluster with these two new sub-clusters.

3.  **Termination**:
    *   Repeat step 2 until the desired number of clusters (`k`) is obtained.

## Advantages

*   **Can produce better clusters**: By iteratively splitting, it can sometimes find more natural cluster boundaries than standard K-Means, especially for non-globular clusters.
*   **Less sensitive to initial centroid selection**: Since it performs K-Means with `k=2` multiple times, the impact of a poor initial centroid choice in a single step is mitigated.
*   **Hierarchical structure**: It implicitly creates a hierarchical structure of clusters, which can be useful for understanding relationships between clusters.

## Disadvantages

*   **Computationally more expensive**: Can be slower than standard K-Means, especially for large datasets and a high number of desired clusters, due to repeated K-Means runs.
*   **Still requires `k`**: Like standard K-Means, the number of clusters `k` still needs to be specified beforehand.
