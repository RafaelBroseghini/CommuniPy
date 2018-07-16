__author__ = "John Doe"


def character_counter(test_string):
    """
    Problem Statement-
        Count the occurence of alphabets only and return
        a dictionary of the count, lower and uppercase
        should be counted as one.
        No spaces or punctuations should be considered

    Input-
        a. test_string: str
            The string in which the occurences should be counted.
            It can consist of any character not only a-z.

    Output-
        The function should return a dictionary of the counts,
        keys should be lowercase alphabet.

    Example-
        >>> character_counter("Hello From the other side")
        {'e': 4, 'h': 3, 'o': 3, 'l': 2, 'r': 2, 't': 2, 'f': 1, 'm': 1, 's': 1, 'i': 1, 'd': 1}

        >>> character_counter("Atleast I called a 1000 times")
        {'a': 4, 't': 3, 'l': 3, 'e': 3, 's': 2, 'i': 2, 'c': 1, 'd': 1, 'm': 1}, 
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    from test_dictionaries_beginner import test_one
    test_one('test_alphabet_counter')
