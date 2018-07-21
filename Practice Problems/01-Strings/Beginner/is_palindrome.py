__author__ = "John Doe"

def is_palindrome(test_string, test_string2):
	"""
	Problem Statement-
		Given test_string and test_string2
		and check if one is palindrome of the other
		Palindrome: Same string if reads backwards.
    
	Input-
	a. test_string: str
    		Normal String.
    		Consists of alphanumeric characters.
	b. test_string2: str
    		Normal String.
    		Consists of alphanumeric characters.
    
	Output-
	    The function should return True or False
		if both strings are palindromes.

	Example-
		>>> is_palindrome("Radar", "radar")
		True

		>>> replace_vowels("Level", "Stats")
		False
	"""
	pass

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
	from test_strings_beginner import test_one
	test_one('test_is_palindrome')
