__author__ = "John Doe"


def character_counter(test_string):
    """
    Problem Statement-
        Count the occurence of each character and return
        a dictionary of the count, lower and uppercase
        of same alphabet count as different
        Spaces and punctuations are also considered

    Input-
        a. test_string: str
            The string in which the occurences should be counted.
            It can consist of any character not only a-z.

    Output-
        The function should return a dictionary of the counts.

    Example-
        >>> character_counter("Hello")
        {'H': 1, 'e': 1, 'l': 2, 'o': 1}

        >>> character_counter("Bye")
        {'B': 1, 'y': 1, 'e': 1}
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    from test_dictionaries_beginner import test_one
    test_one('test_character_counter')
