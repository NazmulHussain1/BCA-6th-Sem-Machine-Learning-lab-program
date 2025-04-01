#10)Write a program to implement K_means clustering and visualize clusters
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x=np.array([[30,50000],[35,60000],[40,30000],[45,100000],[20,20000],[50,120000],[55,150000],[60,140000],[28,40000]])
kmeans=KMeans(n_clusters=3,random_state=0)
kmeans.fit(x)
labels=kmeans.labels_
centers=kmeans.cluster_centers_
plt.figure(figsize=(8,6))
plt.scatter(x[:,0],x[:,1],c=labels,cmap='viridis',s=50,alpha=0.8)
plt.scatter(centers[:,0],centers[:,1],c='red',s=200,marker='x',label='Centroids')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('K-means Clustering of Customers')
plt.legend()
plt.show()
