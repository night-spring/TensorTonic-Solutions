import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    n = len(X)
    X = np.array(X)
    shape = X.shape
    if len(shape) == 1 or shape[0] < 2: return None
        
    column_means = np.mean(X, axis=0)
    X_centered = X - column_means
    return (X_centered.T @ X_centered) / (n-1)