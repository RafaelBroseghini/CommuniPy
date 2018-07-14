import unittest
from strings import *


class Tester(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("discord"), "drocsid")
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")
        self.assertEqual(reverse_string("t h i s i s c r a z y"),
                               "y z a r c s i s i h t")
        print("\n.Passed task 1 with no errors!")

    def test_replace_vowels(self):
    	self.assertEqual(replace_vowels("so many vowels"), "s! m!ny v!w!ls")
    	self.assertEqual(replace_vowels("n0 v0w3ls !n th!s s3nt3nc3"), "n0 v0w3ls !n th!s s3nt3nc3")
    	self.assertEqual(replace_vowels("Cats or Dogs?"), "Cts r Dgs?")
        print("Passed task 2 with no errors!")
        
    def test_distinct_string(self):
    	self.assertEqual(distinct_string("discord"), "dsod")
    	self.assertEqual(distinct_string("Hello World"), "Hlowrd")
    	self.assertEqual(distinct_string("InDiAnA JoNeS"), "IDAAJNS")
        print("Passed task 3 with no errors!")
        
    def test_even_indexes(self):
    	self.assertEqual(even_indexes("Fortnite or PUBG?"), "Frnt rPB?")
    	self.assertEqual(even_indexes("I had pizza at 4:30am"), "Ihdpzaa :0m")
    	self.assertEqual(even_indexes("Don't tell me you don't miss pokemon on TV"), "Dnttl eyudntms oeo nT")
        print("Passed task 4 with no errors!")

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("discord", "drocsid"), True)
        self.assertEqual(is_palindrome("abba", "abba"), True)
        self.assertEqual(is_palindrome("Hewlett?", "ttelweH"), True)
        print("Passed task 5 with no errors!")

    def test_reverse_words_in_string(self):
        self.assertEqual(reverse_words_in_string("Don't tell me you don't miss pokemon on TV"), "TV on pokemon miss don't you me tell Don't")
        self.assertEqual(reverse_words_in_string("n0 v0w3ls !n th!s s3nt3nc3"), "s3nt3nc3 th!s !n v0w3ls n0")
        self.assertEqual(reverse_words_in_string("You shall not pass"), "pass not shall You")
        print("Passed task 6 with no errors!")

    def test_two_parts_string(self):
        self.assertEqual(two_parts_string("Helloworld"), "Hlool elwrd")
        self.assertEqual(two_parts_string("discord"), "dsod icr")
        self.assertEqual(two_parts_string("Television"), "Tlvso eeiin")
        print("Passed task 7 with no errors!")

if __name__ == "__main__":
    unittest.main()
