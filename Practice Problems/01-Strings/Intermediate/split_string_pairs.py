__author__ = "John Doe"


def split_string_pairs(test_string):
    """
    Problem Statement-
        Given a string, split it by pairs of two character. If the last character
        is not a pair, append _ to the last one to make it a pair. Return
        an empty list if string is empty.

    Input-
        a. test_string: str
            Its string which should be splitted, it can consist of any character.

    Output-
        The function should return the pair as a list.

    Example-
        >>> split_string("abc")
        ['ab', 'c_']

        >>> split_string("abcd")
        ['ab', 'cd']
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    from test_strings_beginner import test_one
    test_one('test_split_string_pairs')
