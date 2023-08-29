def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    new_string = ''

    if n < 3:
        raise ValueError('N needs to be at least 3 or greater!') 
    else:    
        for char in phrase:
            if phrase.index(char) == n-2:
                char = '.'
                new_string + char
            elif phrase.index(char) == n-1:
                char = '.'
                new_string + char
            elif phrase.index(char) == n:
                char = '.'
                new_string + char
                return new_string
            else:
                new_string + char
