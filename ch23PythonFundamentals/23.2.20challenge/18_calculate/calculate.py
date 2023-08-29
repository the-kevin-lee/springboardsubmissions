def calculate(operation, a, b, message='The result is', make_int=False,):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    new_op = operation.lower()

    if new_op == 'add':
        result = a + b
        if make_int == True:
            result = int(result)
        new_msg = f'{message} {result}.'
        return new_msg
    elif new_op == 'subtract':
        result = a - b
        if make_int == True:
            result = int(result)
        new_msg = f'{message} {result}.'
        return new_msg
    elif new_op == 'multiply':
        result = a * b
        if make_int == True:
            result = int(result)
        new_msg = f'{message} {result}.'
        return new_msg
    elif new_op == 'divide':
        result = a/b
        if make_int == True:
            result = int(result)
        new_msg = f'{message} {result}.'
        return new_msg
    else:
        return None