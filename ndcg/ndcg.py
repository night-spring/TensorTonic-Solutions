import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    sorted_relevance_score = sorted(relevance_scores, reverse=True)
    if sorted_relevance_score[0] == 0: return 0
        
    dcg = 0
    idcg = 0
    for i in range(min(k, len(relevance_scores))):
        den = math.log2(i+2)
        dcg += (2**relevance_scores[i] - 1) / den
        idcg += (2**sorted_relevance_score[i] - 1) / den 

    return dcg / idcg