import unittest
from dicts import *

class Tester(unittest.TestCase):
	def test_task_1(self):
		self.assertDictEqual(task1("Hello"), {'H': 1, 'e': 1, 'l': 2, 'o': 1})
		self.assertDictEqual(task1("Oh My God"), {'O': 1, 'h': 1, ' ': 2, 'M': 1, 'y': 1, 'G': 1, 'o': 1, 'd': 1})
		self.assertDictEqual(task1("Wingardium Leviosa"), {'W': 1, 'i': 3, 'n': 1, 'g': 1, 'a': 2, 'r': 1, 'd': 1,
		 'u': 1, 'm': 1, ' ': 1, 'L': 1, 'e': 1, 'v': 1, 'o': 1, 's': 1})
		 print("\n.Passed task 1 with no errors!")

	def test_task_2(self):
		self.assertDictEqual(task2("Hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
		self.assertDictEqual(task2("Oh My God"), {'o': 2, 'h': 1, 'm': 1, 'y': 1, 'g': 1, 'd': 1})
		self.assertDictEqual(task2("Wingardium Leviosa"), {'w': 1, 'i': 3, 'n': 1, 'g': 1, 'a': 2, 'r': 1, 'd': 1, 
			'u': 1, 'm': 1, 'l': 1, 'e': 1, 'v': 1, 'o': 1, 's': 1})
		print("Passed task 2 with no errors!")

	