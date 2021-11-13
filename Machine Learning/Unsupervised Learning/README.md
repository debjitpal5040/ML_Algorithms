# Unsupervised Learning

As the name suggests, unsupervised learning is a machine learning technique in which models are not supervised using training dataset. Instead, models itself find the hidden patterns and insights from the given data. It can be compared to learning which takes place in the human brain while learning new things. It can be defined as:

<i>Unsupervised learning is a type of machine learning in which models are trained using unlabeled dataset and are allowed to act on that data without any supervision.</i>

Unsupervised learning cannot be directly applied to a regression or classification problem because unlike supervised learning, we have the input data but no corresponding output data. <b>The goal of unsupervised learning is to find the underlying structure of dataset, group that data according to similarities, and represent that dataset in a compressed format.</b>

## How Supervised Learning Works

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
