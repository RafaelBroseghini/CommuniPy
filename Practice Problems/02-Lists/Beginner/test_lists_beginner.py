from unittest import TestCase, TestSuite, TextTestRunner, main
from concatenating_word import concatenating_word

class ListsBeginnerTestCase(TestCase):
    def test_concatenating_word(self):
        self.assertEqual(concatenating_word(["One", "Two", "Three"], "Four"), ["OneFour", "TwoFour", "ThreeFour"])
        self.assertEqual(concatenating_word(["Hello", "GoodEvening", "GoodBye"], "World"), ["HelloWorld", "GoodEveningWorld", "GoodByeWorld"])
        self.assertEqual(concatenating_word(["Communi", "Git", "Language"], "Py"), ["CommuniPy", "GitPy", "LanguagePy"])
        print("\nPassed concatenating_word with no errors!")

def test_one(test_name):
    suite = TestSuite()
    suite.addTest(ListsBeginnerTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()
