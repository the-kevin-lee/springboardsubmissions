def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    falsey_list = [0,0.0,False,None,"",{},[],set(),()]


    new_lst = [el for el in lst if el not in falsey_list]

    return new_lst