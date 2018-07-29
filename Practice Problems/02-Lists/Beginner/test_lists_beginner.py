from unittest import TestCase, TestSuite, TextTestRunner, main
from concatenating_word import concatenating_word
from two_greatest_items import two_greatest_items

class ListsBeginnerTestCase(TestCase):
    def test_concatenating_word(self):
        self.assertEqual(concatenating_word(["One", "Two", "Three"], "Four"), ["OneFour", "TwoFour", "ThreeFour"])
        self.assertEqual(concatenating_word(["Hello", "GoodEvening", "GoodBye"], "World"), ["HelloWorld", "GoodEveningWorld", "GoodByeWorld"])
        self.assertEqual(concatenating_word(["Communi", "Git", "Language"], "Py"), ["CommuniPy", "GitPy", "LanguagePy"])
        print("\nPassed concatenating_word with no errors!")

    def test_two_greatest_items(self):
        self.assertEqual(two_greatest_items([1, 2, 3, 4, 5]), [4, 5])
        self.assertEqual(two_greatest_items([33, 99, 12, 43, 136, 1, 4]), [99, 136])
        self.assertEqual(two_greatest_items([55]), [55, 55])
        print("\nPassed two_greatest_items with no erros!")

def test_one(test_name):
    suite = TestSuite()
    suite.addTest(ListsBeginnerTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()
