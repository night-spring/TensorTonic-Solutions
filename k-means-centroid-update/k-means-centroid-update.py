import numpy as np 
from collections import defaultdict

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    cluster_points = defaultdict(list)
    for i in range(len(points)):
        cluster_points[assignments[i]].append(points[i])
        
    dim = len(points[0])
    centroids = []
    for i in range(k):
        if cluster_points[i]:
            c = np.mean(cluster_points[i], axis=0)
        else:
            c = np.zeros(dim)
        centroids.append(c.tolist())
    return centroids