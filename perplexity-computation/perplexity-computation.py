import math
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    N = len(prob_distributions)
    H = 0
    for i in range(N):
        H -= math.log(prob_distributions[i][actual_tokens[i]])
    H /= N

    return math.exp(H)
        