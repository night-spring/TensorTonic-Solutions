import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    d = len(X[0])
    X = np.array(X)
    I = np.eye(d)
    return np.linalg.inv(X.T @ X + lam*I) @ X.T @ y