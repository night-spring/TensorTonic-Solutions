import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v)
    norms = np.linalg.norm(v, axis=-1, keepdims=True)
    norms[norms == 0] = 1

    v_normalize = v / norms
    return v_normalize