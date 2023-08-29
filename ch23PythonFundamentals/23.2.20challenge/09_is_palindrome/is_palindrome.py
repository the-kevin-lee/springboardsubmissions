def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """


    # tested_string = phrase.lower().replace(' ', '')

    original_string = phrase.lower().replace(' ', '')

    new_string = ''.join(reversed(phrase.lower().replace(' ', '')))
   



    if original_string == new_string:
        return True
    else:
        return False