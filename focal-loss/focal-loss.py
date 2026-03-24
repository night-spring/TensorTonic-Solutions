import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.array(p)
    y = np.array(y)
    a = np.power(1-p, gamma) * y * np.log(p)
    b = np.power(p, gamma) * (1-y) * np.log(1-p)
    return np.mean(-a-b)