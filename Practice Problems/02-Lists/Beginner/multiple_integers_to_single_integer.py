__author__ = "John Doe"

def multiple_integers_to_single_integer(test_list):
    """
    Problem Statement-
        Given test_list, convert a list of multiple
        integers into a single integer.

    Input-
    a. test_list: list

    Output-
        The function should return a integer value

    Example-
        >>> multiple_integers_to_single_integer([1, 7, 3, 21, 14])
        1732114

        >>> multiple_integers_to_single_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        12345678910
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from test_lists_beginner import test_one
    test_one('test_multiple_integers_to_single_integer')
