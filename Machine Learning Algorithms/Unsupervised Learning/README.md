# Unsupervised Learning

As the name suggests, unsupervised learning is a machine learning technique in which models are not supervised using training dataset. Instead, models itself find the hidden patterns and insights from the given data. It can be compared to learning which takes place in the human brain while learning new things. It can be defined as:

<i>Unsupervised learning is a type of machine learning in which models are trained using unlabeled dataset and are allowed to act on that data without any supervision.</i>

Unsupervised learning cannot be directly applied to a regression or classification problem because unlike supervised learning, we have the input data but no corresponding output data. <b>The goal of unsupervised learning is to find the underlying structure of dataset, group that data according to similarities, and represent that dataset in a compressed format.</b>

<b>Unsupervised learning can be used for those cases where we have only input data and no corresponding output data. The goal of unsupervised learning is to find the hidden patterns and useful insights from the unknown dataset.</b>

## How Unsupervised Learning Works

<img width="646" alt="Screenshot 2021-11-13 at 14 12 35" src="https://user-images.githubusercontent.com/76846542/141612207-3b482975-c1c9-402f-801b-f989e30754eb.png">

Here, we have taken an unlabeled input data, which means it is not categorized and corresponding outputs are also not given. Now, this unlabeled input data is fed to the machine learning model in order to train it. Firstly, it will interpret the raw data to find the hidden patterns from the data and then will apply suitable algorithms such as k-means clustering, Decision tree, etc.

Once it applies the suitable algorithm, the algorithm divides the data objects into groups according to the similarities and difference between the objects.

## Types of Unsupervised Learning Algorithm
The unsupervised learning algorithm can be further categorized into two types of problems:

<img width="419" alt="Screenshot 2021-11-13 at 14 13 03" src="https://user-images.githubusercontent.com/76846542/141612216-890ce622-637a-4420-a3b8-c3ddb00cdd7c.png">

### Clustering
Clustering is a method of grouping the objects into clusters such that objects with most similarities remains into a group and has less or no similarities with the objects of another group. Cluster analysis finds the commonalities between the data objects and categorizes them as per the presence and absence of those commonalities.

### Association
An association rule is an unsupervised learning method which is used for finding the relationships between variables in the large database. It determines the set of items that occurs together in the dataset. Association rule makes marketing strategy more effective. Such as people who buy X item (suppose a bread) are also tend to purchase Y (Butter/Jam) item. A typical example of Association rule is Market Basket Analysis.

## Types of Unsupervised Learning Algorithm
Below is the list of some popular unsupervised learning algorithms:

    K-means clustering
    KNN (k-nearest neighbors)
    Hierarchal clustering
    Anomaly detection
    Neural Networks
    Principle Component Analysis
    Independent Component Analysis
    Apriori algorithm
    Singular value decomposition

**Silhouette Score**

* **Measures:**
    * How well-separated clusters are.
    * How similar data points are within their assigned clusters.
* **Range:** [-1, 1]
    * Higher values indicate better-defined clusters.
    * Values near 0 suggest overlapping clusters.
    * Negative values generally indicate that a sample has been assigned to the wrong cluster.
* **Strengths:**
    * Provides a comprehensive measure of cluster quality.
    * Can be used for a variety of clustering algorithms.
* **Weaknesses:**
    * Can be computationally expensive for large datasets.
    * May not be suitable for all types of data distributions.

**Davies-Bouldin Score**

* **Measures:**
    * The average similarity of each cluster to its most similar cluster.
* **Range:** [0, ∞]
    * Lower values indicate better clustering.
* **Strengths:**
    * Relatively simple to compute.
* **Weaknesses:**
    * Can be sensitive to outliers.
    * May not be as informative as the Silhouette Score.

**Calinski-Harabasz Score**

* **Measures:**
    * The ratio of between-cluster variance to within-cluster variance.
* **Range:** [0, ∞]
    * Higher values indicate better clustering.
* **Strengths:**
    * Easy to compute.
    * Often used for comparing different numbers of clusters.
* **Weaknesses:**
    * Can be biased towards clusters with fewer samples.
    * May not be as robust as the Silhouette Score.

**Choosing the Right Metric**

The best metric to use depends on the specific characteristics of your dataset and the goals of your analysis. Here are some general guidelines:

* **Silhouette Score:** A good general-purpose metric that provides a balanced assessment of cluster quality.
* **Davies-Bouldin Score:** A simpler metric that can be useful for quickly evaluating clustering performance.
* **Calinski-Harabasz Score:** A good choice for comparing different numbers of clusters.

It is often helpful to experiment with different metrics to see which one provides the most informative results for your particular dataset.

**kmeans.inertia_** in scikit-learn is a crucial attribute that represents the **within-cluster sum of squares (WCSS)** of a K-Means clustering model. In simpler terms, it quantifies how tightly packed the data points are within their respective clusters.

**Key Points:**

* **Definition:** It's the sum of squared distances of each data point to its closest cluster center.
* **Lower is Better:** A lower inertia value generally indicates better clustering, as it implies that data points are more closely grouped around their cluster centers.
* **Use in the Elbow Method:** Inertia is often used in the "Elbow Method" to determine the optimal number of clusters (K) for a given dataset. By plotting inertia values for different K values, you can identify an "elbow" point where the rate of decrease in inertia starts to slow down. This elbow point often suggests a suitable value for K.
