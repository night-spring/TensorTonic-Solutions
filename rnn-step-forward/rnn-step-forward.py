import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    pre_act = x_t @ Wx + h_prev @ Wh + b 
    h_t = np.tanh(pre_act)
    #h_t = h_t.reshape(h_prev.shape)
    
    return h_t