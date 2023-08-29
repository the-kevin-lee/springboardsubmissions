def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    reversed_string=""

    for char in reversed(phrase):
        reversed_string += char
    
    return reversed_string
        
