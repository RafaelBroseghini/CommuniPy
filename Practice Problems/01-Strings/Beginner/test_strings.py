import unittest
from strings import *


class StringsBeginnerTestCase(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("discord"), "drocsid")
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")
        self.assertEqual(reverse_string("t h i s i s c r a z y"),
                               "y z a r c s i s i h t")
        print("\n.Passed 1. reverse_string with no errors!")

    def test_replace_vowels(self):
        self.assertEqual(replace_vowels("so many vowels"), "s! m!ny v!w!ls")
        self.assertEqual(replace_vowels("n0 v0w3ls !n th!s s3nt3nc3"), "n0 v0w3ls !n th!s s3nt3nc3")
        self.assertEqual(replace_vowels("Cats or Dogs?"), "Cts r Dgs?")
        print("Passed 2. replace_vowels with no errors!")

    def test_distinct_string(self):
        self.assertEqual(distinct_string("discord"), "dsod")
        self.assertEqual(distinct_string("Hello World"), "Hlowrd")
        self.assertEqual(distinct_string("InDiAnA JoNeS"), "IDAAJNS")
        print("Passed 3. distinct_string with no errors!")

    def test_even_indices(self):
        self.assertEqual(even_indices("Fortnite or PUBG?"), "Frnt rPB?")
        self.assertEqual(even_indices("I had pizza at 4:30am"), "Ihdpzaa :0m")
        self.assertEqual(even_indices("Don't tell me you don't miss pokemon on TV"), "Dnttl eyudntms oeo nT")
        print("Passed 4. even_indices with no errors!")

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("discord", "drocsid"), True)
        self.assertEqual(is_palindrome("abba", "abba"), True)
        self.assertEqual(is_palindrome("Hewlett?", "ttelweH"), False)
        print("Passed 5. is_palindrome with no errors!")

    def test_reverse_words_in_string(self):
        self.assertEqual(reverse_words_in_string("Don't tell me you don't miss pokemon on TV"), "TV on pokemon miss don't you me tell Don't")
        self.assertEqual(reverse_words_in_string("n0 v0w3ls !n th!s s3nt3nc3"), "s3nt3nc3 th!s !n v0w3ls n0")
        self.assertEqual(reverse_words_in_string("You shall not pass"), "pass not shall You")
        print("Passed 6. reverse_words_in_string with no errors!")

    def test_two_parts_string(self):
        self.assertEqual(two_parts_string("Helloworld"), "Hlool elwrd")
        self.assertEqual(two_parts_string("discord"), "dsod icr")
        self.assertEqual(two_parts_string("Television"), "Tlvso eeiin")
        print("Passed 7. two_parts_string with no errors!")

    def test_even_or_odd(self):
        self.assertEqual(even_or_odd("Pizza"), 'Odd')
        self.assertEqual(even_or_odd("Even"), 'Even')
        self.assertEqual(even_or_odd("Python"), 'Even')
        print("Passed 8. even_or_odd with no errors!")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("Aeiou"), 5)
        print("Passed 9. count_vowels with no errors!")


if __name__ == "__main__":
    unittest.main()
