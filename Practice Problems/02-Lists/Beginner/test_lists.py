import unittest
from lists import *


class ListsBeginnerTestCase(unittest.TestCase):
    def test_concatenating_word(self):
        self.assertEqual(concatenating_word(["Brownie", "Pizza", "Computer", "Electron"], "Pie"),
    ["BrowniePie", "PizzaPie", "ComputerPie", "ElectronPie"])

        self.assertEqual(concatenating_word(["Dunno ", "What year are we in? ", "Monday? ", "A.I wrote this! "], "What to do now!"),
    ["Dunno What to do now!", "What year are we in? What to do now!",
    "Monday? What to do now!", "A.I wrote this! What to do now!"
    ])
        self.assertEqual(concatenating_word(["abba", "bbaa", "zzpp"], ""), ["abba", "bbaa", "zzpp"])
        print("\n.Passed 1. concatenating_word with no errors!")

    def test_two_greatest_items(self):
        self.assertEqual(two_greatest_items([22, 55, 4, 33, 12, 9]), [33, 55])
        self.assertEqual(two_greatest_items([1, 2, 3, 4, 5, 5]), [5, 5])
        self.assertEqual(two_greatest_items([100]), [100, 100])
        print("Passed 2. two_greatest_items with no errors!")

    def test_in_between_bottom_and_top(self):
        self.assertEqual(in_between_bottom_and_top([20, 45, 333, 39, 11, 22, 6], 6, 40), [20, 39, 11, 22, 6])
        self.assertEqual(in_between_bottom_and_top([-123, 5, 66, 30, 11], -999, 5), [-123, 5])
        self.assertEqual(in_between_bottom_and_top([90, 45, 2, 76], 100, 500), [])
        print("Passed 3. in_between_bottom_and_top with no errors!")

    def test_reverse_and_delimiter(self):
        self.assertEqual(reverse_and_delimiter(["PyPractice", "Pythonista", "Python?"], "->"), ["Python?", "->", "Pythonista", "->", "PyPractice"])
        self.assertEqual(reverse_and_delimiter(["Who takes it?", "France?", "Croatia?"], "!"), ["Croatia?", "!", "France?", "!", "Who takes it?"])
        self.assertEqual(reverse_and_delimiter([], "->"), [])
        print("Passed 4. reverse_and_delimiter with no errors!")

    def test_multiple_integers_to_single_integer(self):
        self.assertEqual(multiple_integers_to_single_integer([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(multiple_integers_to_single_integer([-1, 2, 3, 4, 5]), -12345)
        self.assertEqual(multiple_integers_to_single_integer([2002, 2006, 2010, 2014]), 2002200620102014)
        self.assertEqual(multiple_integers_to_single_integer([0, 1, 2]), 12)
        print("Passed 5. multiple_integers_to_single_integer with no errors!")


if __name__ == "__main__":
    unittest.main()
