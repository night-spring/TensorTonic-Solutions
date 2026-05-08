import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    
    Args:
        X: Input sequence of shape (batch, T, input_dim)
        h_0: Initial hidden state of shape (batch, hidden_dim)
        W_xh: Input-to-hidden weights of shape (hidden_dim, input_dim)
        W_hh: Hidden-to-hidden weights of shape (hidden_dim, hidden_dim)
        b_h: Bias of shape (hidden_dim,)

    Returns:
        hidden_states: All hidden states of shape (batch, T, hidden_dim)
        h_final: Final hidden state of shape (batch, hidden_dim)
    """
    # YOUR CODE HERE
    batch, T, _ = X.shape
    hidden_dim = h_0.shape[1]
    
    hidden_states = np.zeros((batch, T, hidden_dim))
    h_t = h_0
    
    for t in range(T):
        x_t = X[:, t, :]
        h_t = np.tanh(x_t @ W_xh.T + h_t @ W_hh.T + b_h)
        hidden_states[:, t, :] = h_t
        
    return (hidden_states, h_t)