__author__ = "John Doe"

def split_string_pairs(test_string):
	"""
	Given a string, split it by pairs of two character. If the last character
	is not a pair, append _ to the last one to make it a pair. Return
	an empty list if string is empty. Examples:
	split_string('abc') --> ['ab', 'c_']
	split_string('abcd') --> ['ab', 'cd']
	"""
	pass

def extract_file_name(test_string):
	"""
	Extract the filename from the given gibberish.
	Examples:
	Gibberish: 1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION, Filename:  FILE_NAME.EXTENSION

	Gibberish: 1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34, Filename: This_is_an_otherExample.mpg
	"""
	pass

def validate_phone_number(test_string):
	"""
	Hypothetic phone number format: (123) 456-7890
	The task is to validate the format and return True if it is a valid phone
	number
	"""
	pass

def name_list(test_list):
	"""
	From the given data, return a formatted name list as a single string
	Example: 
	name_list([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
	returns 'Bart, Lisa & Maggie'
	"""
	pass

def in_order(test_string):
	"""
	Sort the words in the sentence according to the numbers in them
	Example:
	in_order('is2 Thi1s T4est 3a') --> "Thi1s is2 3a T4est"
	Note: Numbers are from 1 to 9.
	"""
	pass