import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    if not num_classes:
        num_classes = max(y) + 1
    n = len(y)
    x = np.zeros((n, num_classes), dtype=int)
    x[np.arange(n), y] = 1
    return x