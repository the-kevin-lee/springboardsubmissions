def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    verified_list = []

    for lt in lst:
        if isinstance(lt, list):
            verified = True
        else:
            verified = False
        verified_list.append(verified)

    if False in verified_list:
        return False
    else:
        return True
