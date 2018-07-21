__author__ = "John Doe"

def replace_vowels(test_string):
	"""
	Problem Statement-
		Given test_string, return test_string
		with vowels replaced by the character '!'.
    
	Input-
	a. test_string: str
    		The string which should be replaced.
    		Consists of alphanumeric characters,
    		punctuation etc.
    
	Output-
	    The function should return test_string with
		the vowels replaced by the character '!'.

	Example-
		>>> replace_vowels("CommuniPy")
		'C!mm!n!Py'

		>>> replace_vowels("Vowels")
		'V!w!ls'
	"""
	pass

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
	from test_strings_beginner import test_one
	test_one('test_replace_vowels')
