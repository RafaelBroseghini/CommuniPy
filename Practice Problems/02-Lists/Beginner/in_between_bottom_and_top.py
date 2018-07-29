__author__ = "John Doe"


def in_between_bottom_and_top(test_list, bottom, top):
    """
	Problem Statement-
		Given test_list, bottom and top,
        between bottom and top thresholds. (INCLUSIVE)

	Input-
	a. test_list: list

    b. bottom: int

    c. top: int

	Output-
	    The function should return a new list with all its values
        between bottom and top.

	Example-
		>>> in_between_bottom_and_top([27, 32, 7, 64, 40, 21, 13], 5, 40)
		[27, 32, 7, 40, 21, 13]

		>>> in_between_bottom_and_top([-32, 93, 65, 1, 100], -100, 10)
		[-32, 1]
	"""
    pass
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from test_lists_beginner import test_one
    test_one('test_in_between_bottom_and_top')
