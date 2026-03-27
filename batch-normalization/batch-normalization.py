import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    
    if x.ndim == 2:
        axes = (0,)
        
    elif x.ndim == 4:
        axes = (0,2,3)
        shape = (1, x.shape[1], 1, 1)
        gamma = gamma.reshape(shape)
        beta = beta.reshape(shape)

    mean = np.mean(x, axis=axes, keepdims=True)
    var = np.var(x, axis=axes, keepdims=True)
    
    x_norm = (x - mean) / np.sqrt(var + eps)
    output = gamma * x_norm + beta

    return output