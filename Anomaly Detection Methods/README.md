# Anomaly Detection Algorithms

This repository contains implementations of various anomaly detection algorithms. Below is a brief explanation of how each algorithm works.

## 1. Isolation Forest

**How it works:** Isolation Forest is an ensemble learning method based on decision trees. It works on the principle that anomalies are "few and different" and are therefore easier to isolate than normal observations.

1.  **Random Partitioning:** It randomly selects a feature and then randomly selects a split value between the maximum and minimum values of that feature. This process recursively partitions the data.
2.  **Isolation:** Anomalies, being rare and distinct, require fewer splits to be isolated in the tree compared to normal data points.
3.  **Anomaly Score:** The anomaly score is calculated based on the path length (number of splits) required to isolate a data point. Shorter path lengths indicate higher anomaly scores.
4.  **Ensemble:** Multiple isolation trees are built, and the anomaly score for a data point is averaged across all trees.

## 2. One-Class SVM (Support Vector Machine)

**How it works:** One-Class SVM is an unsupervised algorithm used for novelty detection. It learns a decision boundary that encapsulates the "normal" data points, effectively separating them from outliers.

1.  **Hyperplane Learning:** It finds a hyperplane that best separates the data points from the origin in a high-dimensional feature space (often using a kernel trick).
2.  **Margin Maximization:** The algorithm aims to maximize the margin around the normal data points, pushing the hyperplane as far as possible from the origin.
3.  **Anomaly Detection:** Data points that fall outside this learned boundary are considered anomalies.
4.  **Nu Parameter:** The `nu` parameter controls the trade-off between the number of support vectors and the number of training errors (outliers). It represents an upper bound on the fraction of training errors and a lower bound on the fraction of support vectors.

## 3. Local Outlier Factor (LOF)

**How it works:** LOF is a density-based outlier detection algorithm. It measures the local deviation of density of a given data point with respect to its neighbors.

1.  **Reachability Distance:** For each data point, it calculates the reachability distance to its k-nearest neighbors. This distance is a smoothed version of the Euclidean distance, ensuring stability for points within dense clusters.
2.  **Local Reachability Density (LRD):** The LRD of a point is the inverse of the average reachability distance from its neighbors. A lower LRD indicates that the point is in a sparser region.
3.  **Local Outlier Factor (LOF):** The LOF of a point is the ratio of its LRD to the average LRD of its k-nearest neighbors.
4.  **Anomaly Detection:** An LOF value significantly greater than 1 indicates that the point is an outlier, as its density is much lower than that of its neighbors.

## 4. Elliptic Envelope

**How it works:** Elliptic Envelope is a parametric outlier detection method that assumes the regular data points come from a known distribution, typically a Gaussian distribution.

1.  **Covariance Estimation:** It fits an ellipse (or hyper-ellipsoid in higher dimensions) to the central, "normal" data points by estimating the mean and covariance matrix of the data.
2.  **Robust Estimation:** To make the estimation robust to outliers, it often uses a robust covariance estimator (e.g., Minimum Covariance Determinant - MCD). This estimator focuses on a subset of the data that is most likely to be free of outliers.
3.  **Mahalanobis Distance:** Once the ellipse is fitted, the Mahalanobis distance of each data point from the center of the ellipse is calculated.
4.  **Anomaly Detection:** Data points with a Mahalanobis distance exceeding a certain threshold (determined by the desired contamination level) are classified as outliers. These points lie outside the estimated elliptical boundary.
