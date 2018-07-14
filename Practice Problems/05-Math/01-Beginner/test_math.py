import unittest

class Tester(unittest.TestCase):
    def test_even_or_odd_number(self):
        self.assertEqual(even_or_odd_number(1), 'Odd')
        self.assertEqual(even_or_odd_number(8), 'Even')
        self.assertEqual(even_or_odd_number(42), 'Even')
        print("\n Passed task 1 with no errors!")

    def test_lower_than(self):
        self.assertEqual(lower_than(6, 10), False)
        self.assertEqual(lower_than(2, 8), True)
        self.assertEqual(lower_than(5, 17), True)

    def test_bigger_than(self):
        self.assertEqual(bigger_than(4, 15), False)
        self.assertEqual(bigger_than(3, 8), True)
        self.assertEqual(bigger_than(5, 20), False)

    def test_equals_to(self):
        self.assertEqual(equals_to(5, 3, 2), False)
        self.assertEqual(equals_to(7, 7, 14), True)
        self.assertEqual(equals_to(5, 5, 0), False)

    def test_not_equals_to(self):
        self.assertEqual(not_equals_to(4, 3, 2), True)
        self.assertEqual(not_equals_to(8, 2, 6), False)
        self.assertEqual(not_equals_to(5, 1, 10), True)
        
if __name__ == "__main__":
    unittest.main()
