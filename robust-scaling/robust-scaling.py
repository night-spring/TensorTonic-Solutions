def median(values):
    """
    Compute the median as the middle value (odd length) or average of two middle values (even length)
    """
    n = len(values)
    if n == 1: return values[0]
        
    if n % 2 == 1:
        median = values[n//2]
    else:
        median = (values[(n-1) // 2] + values[n//2]) / 2
    return median

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    n = len(values)
    if n == 1: return [0]
        
    sorted_values = sorted(values)
    q1 = median(sorted_values[: n//2])
    q2 = median(sorted_values)
    q3 = median(sorted_values[(n + 1)//2 :])
    
    values_scaled = []
    iqr = q3 - q1
    if iqr == 0: iqr = 1

    for x in values:
        x_scaled = (x - q2) / iqr
        values_scaled.append(x_scaled)
    return values_scaled
    