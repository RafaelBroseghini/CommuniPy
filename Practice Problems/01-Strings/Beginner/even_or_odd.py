__author__ = "John Doe"

def even_or_odd(test_string):
	"""
	Problem Statement-
		Given test_string check the length of the string
		and return if the number of characters in even
		or odd.
    
	Input-
	a. test_string: str
    		Normal String.
    		Consists of alphanumeric characters.
    
	Output-
	    The function should return 'Even' or 'Odd'
		after checking the number of characters.

	Example-
		>>> even_or_odd("Even")
		Even

		>>> even_or_odd("CommuniPy")
		Odd
	"""
	pass

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
	from test_strings_beginner import test_one
	test_one('test_even_or_odd')
