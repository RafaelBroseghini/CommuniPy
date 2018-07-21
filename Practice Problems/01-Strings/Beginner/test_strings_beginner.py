from unittest import TestCase, TestSuite, TextTestRunner, main
from reverse_string import reverse_string
from replace_vowels import replace_vowels
from is_palindrome import is_palindrome
from even_or_odd import even_or_odd
from count_vowels import count_vowels

class StringsBeginnerTestCase(TestCase):
    def test_reverse_string(self):
		self.assertEqual(reverse_string("I make things beep bop beep bop"),"pob peeb pob peeb sgniht ekam I")
		self.assertEqual(reverse_string("Write code write code"),"edoc etirw edoc etirW")
		self.assertEqual(reverse_string("Reverse this Last         One"),"enO         tsaL siht esreveR")
		print("\nPassed reverse_string with no errors!")

	def test_replace_vowels(self):
		self.assertEqual(replace_vowels("Hi Bob! How're you?"), "H! B!b! H!w'r! y!!?")
		self.assertEqual(replace_vowels("It's an 'i' or a '!'?"), "!t's !n '!' or a '!'?")
		self.assertEqual(replace_vowels("The Alphabet"), "Th! !lph!b!t")
		print("\nPassed replace_vowels with no errors!")

	def test_is_palindrome(self):
		self.assertEqual(is_palindrome("Radar", "radar"), True)
		self.assertEqual(is_palindrome("Status", "Stats"), False)
		self.assertEqual(is_palindrome("Madam", "madam"), True)
		print("\nPassed is_palindrome with no errors!")

	def test_even_or_odd(self):
		self.assertEqual(even_or_odd("Python"), "Even")
		self.assertEqual(even_or_odd("GitHub"), "Even")
		self.assertEqual(even_or_odd("Wow"), "odd")
		print("\nPassed even_or_odd with no errors!")

	def test_count_vowels(self):
		self.assertEqual(count_vowels("Pineapple"), 4)
		self.assertEqual(count_vowels("Badge"), 2)
		self.assertEqual(count_vowels("Cryptocurrency"), 3)
		print("\nPassed count_vowels with no errors!")

def test_one(test_name):
	suite = TestSuite()
	suite.addTest(StringsBeginnerTestCase(test_name))
	runner = TextTestRunner()
	runner.run(suite)


if __name__ == "__main__":
    main()
