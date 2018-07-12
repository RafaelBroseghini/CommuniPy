from strings import *
import unittest

class Tester(unittest.TestCase):
  def test_task_1(self):
    self.assertEqual(task1("discord"),"drocsid")
    self.assertEqual(task1("Hello World"), "dlroW olleH")
    self.assertEqual(task1("t h i s i s c r a z y"), "y z a r c s i s i h t")


if __name__ == "__main__":
  unittest.main()
