def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    some_count = 0

    for term in lst:
        if term == search_term:
            some_count += 1

    return some_count
