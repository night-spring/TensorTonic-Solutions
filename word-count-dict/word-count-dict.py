def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    dictionary = {}
    for sentence in sentences:
        for word in sentence:
            if word not in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1

    return dictionary