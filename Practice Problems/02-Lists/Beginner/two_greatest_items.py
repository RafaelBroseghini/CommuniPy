__author__ = "John Doe"

def two_greatest_items(test_list):
    """
	Problem Statement-
		Given test_list return the two greatest
        items in that list as a new list in sorted
        order.

	Input-
	a. test_list: list

	Output-
	    The function should return a new list with the two
        greatest items in a sorted order. If list size is 1,
		return only one item.

	Example-
		>>> two_greatest_items([44, 32, 7, 9])
		[32, 44]

		>>> two_greatest_items([5])
		[5]
	"""
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from test_lists_beginner import test_one
    test_one('test_two_greatest_items')
