import unittest
from dicts import *


class DictsBeginnerTestCase(unittest.TestCase):
    def test_alphabet_counter(self):
        self.assertDictEqual(alphabet_counter("Hello"), {'H': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertDictEqual(alphabet_counter("Oh My God"), {'O': 1, 'h': 1, ' ': 2, 'M': 1, 'y': 1, 'G': 1, 'o': 1, 'd': 1})
        self.assertDictEqual(alphabet_counter("Wingardium Leviosa"), {'W': 1, 'i': 3, 'n': 1, 'g': 1, 'a': 2, 'r': 1, 'd': 1,
         'u': 1, 'm': 1, ' ': 1, 'L': 1, 'e': 1, 'v': 1, 'o': 1, 's': 1})
        print("\n.Passed 1. alphabet_counter with no errors!")

    def test_alphabet_counter_version_two(self):
        self.assertDictEqual(alphabet_counter_version_two("Hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertDictEqual(alphabet_counter_version_two("Oh My God"), {'o': 2, 'h': 1, 'm': 1, 'y': 1, 'g': 1, 'd': 1})
        self.assertDictEqual(alphabet_counter_version_two("Wingardium Leviosa"), {'w': 1, 'i': 3, 'n': 1, 'g': 1, 'a': 2, 'r': 1, 'd': 1, 
            'u': 1, 'm': 1, 'l': 1, 'e': 1, 'v': 1, 'o': 1, 's': 1})
        print("Passed 2. alphabet_counter_version_two with no errors!")


if __name__ == "__main__":
    unittest.main()
