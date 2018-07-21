import unittest
from maths import *


class MathsBeginnerTestCase(unittest.TestCase):
    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(0), 'even')
        self.assertEqual(even_or_odd(1), 'odd')
        self.assertEqual(even_or_odd(-1), 'odd')
        print("\n.Passed 1. alphabet_counter with no errors!")

    def test_sum_them_all(self):
        self.assertEqual(sum_them_all(0), 0)
        self.assertEqual(sum_them_all(5), 15)
        print("Passed 2. alphabet_counter_version_two with no errors!")

    def test_how_many_days(self):
        self.assertEqual(how_many_days(360), '1 year(s) 0 months(s) 0 day(s)')
        self.assertEqual(how_many_days(320), '0 year(s) 10 months(s) 20 day(s)')
        self.assertEqual(how_many_days(782), '2 year(s) 2 months(s) 2 day(s)')
        print("Passed 3. alphabet_counter_version_two with no errors!")

    def test_how_much_on_taxes(self):
        self.assertEqual(how_much_on_taxes(1, 2), 50.00)
        self.assertEqual(how_much_on_taxes(1, 3), 66.66)
        print("Passed 5. how_much_on_taxes with no errors!")


if __name__ == "__main__":
    unittest.main()
