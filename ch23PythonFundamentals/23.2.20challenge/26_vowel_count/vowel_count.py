def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    new_phrase = phrase.replace(" ", "").lower()

    new_obj = {}
    vowels = set("aeiou")

    for char in new_phrase:
        if char in vowels:
            if char in new_obj:
                new_obj[char] += 1
            else:
                new_obj[char] = 1

    return new_obj
        