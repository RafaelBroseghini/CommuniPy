from unittest import TestCase, TestSuite, TextTestRunner, main
from reverse_string import reverse_string

class StringsBeginnerTestCase(TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("I make things beep bop beep bop"),"pob peeb pob peeb sgniht ekam I")     
        self.assertEqual(reverse_string("Write code write code"),"edoc etirw edoc etirW")  
        self.assertEqual(reverse_string("Reverse this Last         One"),"enO         tsaL siht esreveR")
        print("\n. Passed reverse_string with no errors!")  


def test_one(test_name):
    suite = TestSuite()
    suite.addTest(StringsBeginnerTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
