def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    modified_text = ''

    to_swap = to_swap.lower()

    for char in phrase:
        if char.lower() == to_swap:
            if char.isupper():
                modified_text += char.lower()
            else:
                modified_text += char.upper()
        else:
            modified_text += char

    return modified_text