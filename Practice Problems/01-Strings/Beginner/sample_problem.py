__author__ = "John Doe"


def sample_problem(sample_arg):
    """
    Problem Statement-
        This is a sample problem that takes a sample argument.

    Input-
        a. sample_args: str
            Its the sample argument that should be returned.

    Output-
        The function should return sample_arg

    Example-
        >>> sample_problem("Sample Argument")
        'Sample Argument'

        >>> sample_problem("Sample Argument2")
        'Sample Argument2'
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    from test_strings_beginner import test_one
    test_one('test_sample_problem')
