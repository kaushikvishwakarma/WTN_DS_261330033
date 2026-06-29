# Unsupervised Machine Learning - Interview Questions

1. **Explain the difference between Supervised and Unsupervised Machine Learning**
   *Answer*: 
   - **Supervised ML** uses labeled data (input variables mapped to known output variables) to train a model to predict outcomes (e.g., classification, regression).
   - **Unsupervised ML** uses unlabeled data to find hidden patterns, groupings, or structures within the data (e.g., clustering, dimensionality reduction) without predefined target outputs.

2. **Discuss the applications of Unsupervised Machine Learning**
   *Answer*: Common applications include customer segmentation (clustering users by behavior), anomaly detection (identifying fraudulent credit card transactions), recommendation systems (grouping similar items/users), and dimensionality reduction for data visualization (PCA).

3. **Explain how K-means Algorithm Works?**
   *Answer*: K-means works by first selecting 'k' random points as initial cluster centers (centroids). It then iteratively performs two steps:
   - **Assignment**: Each data point is assigned to the nearest centroid.
   - **Update**: The centroids are recalculated as the mean of all data points assigned to that cluster.
   This process repeats until the centroids no longer change significantly (convergence).

4. **How to find out the ideal value of k in k-means algorithm?**
   *Answer*: The ideal value of $k$ is typically found using the **Elbow Method**. You run K-means for a range of $k$ values and plot the Within-Cluster Sum of Squares (WCSS) against $k$. The "elbow" point on the graph, where the rate of decrease sharply slows down, represents a good balance between minimizing WCSS and keeping $k$ small. Another approach is using the **Silhouette Score**, which measures how similar an object is to its own cluster compared to other clusters.
