__author__ = "John Doe"


def reverse_string(test_string):
    """
    Problem Statement-
        Given test_string, return the reverse of
        test_string.
        Try a iterative approach, list reverse aproach and
        a slicing approach.
    
    Input-
        a. test_string: str
            The string which should be reversed.
            Consists of alphanumeric characters,
            punctuation etc.
    
    Output-
        The function should return test_string reversed.

    Example-
        >>> reverse_string("CommuniPy")
        'yPinummoC'

        >>> reverse_string("esreveR")
        'Reverse'
    """
    return test_string[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from test_strings_beginner import test_one

    # main()