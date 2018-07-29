__author__ = "John Doe"

def reverse_and_delimiter(test_list, delimiter):
    """
	Problem Statement-
		Given test_list and a delimiter, return a list
        separated by the delimiter in reverse order.

	Input-
	a. test_list: list

    b. delimiter: str

	Output-
	    The function should return a new list in a reverse order
        and its values separated by the delimiter.

	Example-
		>>> reverse_and_delimiter(["Hello", "there!", "How", "are", "you?"], "->")
		["you?", "->", "are", "->", "How", "->", "there!", "->", "Hello,"]

		>>> reverse_and_delimiter(["Car", "Bus", "Motorcycle", "Airplane", "Truck"], "!")
		["Truck", "!", "Airplane", "!", "Motorcycle", "!", "Bus", "!", "Car"]
	"""
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from test_lists_beginner import test_one
    test_one('test_reverse_and_delimiter')
