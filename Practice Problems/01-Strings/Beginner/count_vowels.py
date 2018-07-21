__author__ = "John Doe"

def count_vowels(test_string):
	"""
	Problem Statement-
		Given test_string return the number of vowels in the string.
    
	Input-
	a. test_string: str
    		Normal String.
    		Consists of alphanumeric characters.
    
	Output-
	    The function should return an integer value
		after counting the number of vowels in the string.

	Example-
		>>> count_vowels("Guido van Rossum")
		6

		>>> count_vowels("CommuniPy")
		3
	"""
	pass

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
	from test_strings_beginner import test_one
	test_one('test_count_vowels')
