def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    


    if phrase[0].islower():
        new_phrase = phrase[0].upper() + phrase[1:]
    else:
        new_phrase = phrase

    return new_phrase

