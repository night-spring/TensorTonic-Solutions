def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    n = len(y_true)
    correctly_classified = 0
    mis_classified = 0
    for i in range(n):
        if y_true[i] == y_pred[i]: correctly_classified += 1
        else: mis_classified += 1
    return correctly_classified / (correctly_classified + mis_classified)
    