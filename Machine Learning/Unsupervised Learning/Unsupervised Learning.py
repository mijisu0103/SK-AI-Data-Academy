# Clustering Analysis
# The technique of grouping the given data based on similarity in characteristics to analyze the features of each type is similar to classification analysis, 
# where data is assigned to a single cluster
  # However, in clustering, which is a type of unsupervised learning, label information is not utilized during the training process
# Clusters are formed by minimizing the distance among data points within the same cluster and maximizing the distance between different clusters
  # Euclidean distance (straight-line distance) is commonly used for distance calculations
# While it can be applied to all types of data if the distance is well defined, there are challenges in defining distance and weights, and interpreting the results can be difficult

# Clustering Analysis Methodologies
# Hierarchical method
  # A clustering method that sequentially groups nearby entities or separates entities that are far apart
  # Once an object is assigned to a cluster, it is not separated again
  # Has higher computational load and longer processing time compared to non-hierarchical methods

# Non Hierarchical method
  # A clustering method that randomly clusters data and adjusts the assignment of each data point to the appropriate cluster based on changes in values during the clustering process

# Examples of Using Clustering Analysis
# Customer Classification
  # Customers can be grouped into clusters based on purchase history or behavior on the website
  # Different product recommendations or marketing strategies can be applied to each customer group
  # A recommendation system can be created to suggest content that customers within the same cluster enjoy

# Anomaly Detection
  # The affinity of data for each cluster (how well the data fits the cluster) can be measured
  # Samples with low affinity across all clusters are likely to be outliers
#   # This can be utilized in manufacturing defect detection and fraud detection
# Additionally, it can be used in areas such as search engines, dimensionality reduction, semi-supervised learning, and image segmentation

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.model_selection import train_test_split

# Import cluster data
df = pd.read_csv('/path/iris.csv') 
df

# Split Data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# There are 4 features, making visualization difficult
# Reduce the dimensions to 2 features using PCA
from sklearn.decomposition import PCA
P = PCA(n_components=2)
X_PCA = P.fit_transform(X) 
X.shape, X_PCA.shape

# Check the variance ratio compared to the original data
P.explained_variance_ratio_

# Visualize the data obtained from PCA
plt.scatter(X_PCA[:, 0], X_PCA[:, 1], c=Y)

# K Means
# A representative non-hierarchical clustering algorithm based on unsupervised learning 
# that divides data into a predefined number of clusters, K
  # Data is assigned to the closest cluster based on K cluster centroids
  # Since it calculates the distance between the cluster centroids and the data, it requires less computation compared to hierarchical clustering algorithms
# However, defining the optimal number of clusters K is often challenging

# Clustering Formation Process
"""
Step 1: Randomly specify K centroids (as predefined)
Step 2: Calculate the distance to the centroids using Euclidean distance and assign each data point to the nearest cluster
Step 3: Calculate the mean of the data points within each cluster and reassign the centroids. Repeat this process until the centroids no longer move
"""

# Create KMeans model
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3) # Form 3 clusters

# Model training
model.fit(X_PCA) # Only use features

# KMeans
# KMeans(n_clusters=3)

# Check cluster center
model.cluster_centers_

# Check cluster result that was used in fit process
model.labels_

# Cluster result visualisation
plt.scatter(X_PCA[:, 0], X_PCA[:, 1], c=model.labels_)

# Import the non-linear boundary data
df = pd.read_csv('/path/moon.csv') 
df

# Data visualisation
plt.scatter(df['X1'], df['X2'], c=df['y'])

# KMeans model creation
model = KMeans(n_clusters=2) # Form 2 clusters

# Model training
model.fit(df[['X1', 'X2']]) # Only use features

# KMeans
# KMeans(n_clusters=2)

# Cluster result visualisation
plt.scatter(df['X1'], df['X2'], c=model.labels_)

# K-Means clustering cannot correctly cluster data with linearly complex boundaries
# However, other clustering methods, such as Spectral Clustering and DBSCAN, can effectively cluster such data

# DBSCAN model creation
from sklearn.cluster import DBSCAN 
model = DBSCAN()

# Model training
model.fit(df[['X1', 'X2']]) # Only use features

# DBSCAN
# DBSCAN()

# Cluster result visualisation
plt.scatter(df['X1'], df['X2'], c=model.lables_)

# It is necessary to adjust the min_samples or eps values, but the first priority should be to apply standardization
  # Since DBSCAN is density-based, it is affected by the scale of the data
  # The difference between a value of 0.1 in the range of 0 to 1 and a value of 0.1 in the range of 0 to 100 is significant

# Standardization
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(df[['X1', 'X2']])

model = DBSCAN() model.fit(x_scaled) # Only use features

# DBSCAN
# DBSCAN()

# Cluster result visualisation
plt.scatter(df['X1'], df['X2'], c=model.labels_)

# Evaluation of Clustering Algorithms
# In the case of clustering algorithms, when ground truth values are available, metrics such as ARI (Adjusted Rand Index) or NMI (Normalized Mutual Information) can be used for evaluation
# Since the cluster numbers are assigned randomly, comparing the accuracy based on their positions can lead to inaccurate performance assessments
# Clustering algorithms are a method used in unsupervised learning, often applied when there is unlabeled data
# Thus, calculating model performance using ground truth values like ARI or NMI can be quite challenging
# Using inertia, which measures the average squared distance between each data point and its nearest centroid, allows for tracking changes in inertia with different values of K, helping to define an appropriate number of clusters 
# If there are no actual values, silhouette scores can be utilized
#   The silhouette score indicates how similar data points within the same cluster are compared to those in other clusters
#       It is calculated using cohesion and separation metrics
#   If the clusters are optimized, the silhouette score will be close to 1

# Import data for cluster model evaluation
df = pd.read_csv('/path/iris.csv')

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

from sklearn.metrics import accuracy_score
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import normalized_mutual_info_score

model = KMeans(n_clusters=3) 
model.fit(X)

print('ACC:', accuracy_score(Y, model.labels_))
print('ARI:', adjusted_rand_score(Y, model.labels_)) 
print('NMI:', normalized_mutual_info_score(Y, model.labels_))

# Query inertia
model.inertia_

# Silhouette coefficient
from sklearn.metrics import silhouette_score 
silhouette_score(X, model.labels_)

