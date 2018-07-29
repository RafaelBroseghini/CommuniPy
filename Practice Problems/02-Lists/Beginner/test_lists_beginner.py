from unittest import TestCase, TestSuite, TextTestRunner, main
from concatenating_word import concatenating_word
from two_greatest_items import two_greatest_items
from in_between_bottom_and_top import in_between_bottom_and_top
from reverse_and_delimiter import reverse_and_delimiter
from multiple_integers_to_single_integer import multiple_integers_to_single_integer

class ListsBeginnerTestCase(TestCase):
    def test_concatenating_word(self):
        self.assertEqual(concatenating_word(["One", "Two", "Three"], "Four"), ["OneFour", "TwoFour", "ThreeFour"])
        self.assertEqual(concatenating_word(["Hello", "GoodEvening", "GoodBye"], "World"), ["HelloWorld", "GoodEveningWorld", "GoodByeWorld"])
        self.assertEqual(concatenating_word(["Communi", "Git", "Language"], "Py"), ["CommuniPy", "GitPy", "LanguagePy"])
        print("\nPassed concatenating_word with no errors!")

    def test_two_greatest_items(self):
        self.assertEqual(two_greatest_items([1, 2, 3, 4, 5]), [4, 5])
        self.assertEqual(two_greatest_items([33, 99, 12, 43, 136, 1, 4]), [99, 136])
        self.assertEqual(two_greatest_items([55]), [55])
        print("\nPassed two_greatest_items with no errors!")

    def test_in_between_bottom_and_top(self):
        self.assertEqual(in_between_bottom_and_top([3, 12, 74, 6, 43], 10, 50), [12, 43])
        self.assertEqual(in_between_bottom_and_top([-67, -89, 31, 10, 89, 125, 431], -100, 200), [-67, -89, 31, 10, 89, 125])
        self.assertEqual(in_between_bottom_and_top([1, 5, 12, -12, 4, 8], 0, 10), [1, 5, 4, 8])
        print("\nPassed in_between_bottom_and_top with no errors!")

    def test_reverse_and_delimiter(self):
        self.assertEqual(reverse_and_delimiter(["2", "Minutes", "To", "Midnight"], "!"), ["Midnight", "!", "To", "!", "Minutes", "!", "2"])
        self.assertEqual(reverse_and_delimiter(["Alexander", "The", "Great"], "->"), ["Great", "->", "The", "->", "Alexander"])
        self.assertEqual(reverse_and_delimiter(["When", "The", "Wild", "Wind", "Blows"], "<-"), ["Blows", "<-", "Wind", "<-", "Wild", "<-", "The", "<-", "When"])
        print("\nPassed reverse_and_delimiter with no errors!")

    def test_multiple_integers_to_single_integer(self):
        self.assertEqual(multiple_integers_to_single_integer([7, 14, 21, 28]), 7142128)
        self.assertEqual(multiple_integers_to_single_integer([-300, 21, 562, 1245, 1, 0, 32]), -3002156212451032)
        self.assertEqual(multiple_integers_to_single_integer([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 109876543210)
        print("\nPassed multiple_integers_to_single_integer with no errors!")

def test_one(test_name):
    suite = TestSuite()
    suite.addTest(ListsBeginnerTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()
