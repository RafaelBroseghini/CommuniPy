from unittest import TestCase, TestSuite, TextTestRunner, main
from character_counter import character_counter
from alphabet_counter import alphabet_counter


class DictionariesBeginnerTestCase(TestCase):
    def test_character_counter(self):
        self.assertDictEqual(character_counter("Hello"), {'H': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertDictEqual(character_counter("Oh My God"), {'O': 1, 'h': 1, ' ': 2, 'M': 1, 'y': 1, 'G': 1, 'o': 1, 'd': 1})
        self.assertDictEqual(character_counter("Wingardium Leviosa"), {'W': 1, 'i': 3, 'n': 1, 'g': 1, 'a': 2, 'r': 1, 'd': 1,
         'u': 1, 'm': 1, ' ': 1, 'L': 1, 'e': 1, 'v': 1, 'o': 1, 's': 1})
        print("\n.Passed character_counter with no errors!")

    def test_alphabet_counter(self):
        self.assertDictEqual(alphabet_counter("Hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertDictEqual(alphabet_counter("Oh My God"), {'o': 2, 'h': 1, 'm': 1, 'y': 1, 'g': 1, 'd': 1})
        self.assertDictEqual(alphabet_counter("Wingardium Leviosa"), {'w': 1, 'i': 3, 'n': 1, 'g': 1, 'a': 2, 'r': 1, 'd': 1, 
            'u': 1, 'm': 1, 'l': 1, 'e': 1, 'v': 1, 'o': 1, 's': 1})
        print("Passed alphabet_counter with no errors!")

def test_one(test_name):
    suite = TestSuite()
    suite.addTest(DictionariesBeginnerTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
