from strings import *
import unittest


class Tester(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(task1("discord"), "drocsid")
        self.assertEqual(task1("Hello World"), "dlroW olleH")
        self.assertEqual(task1("t h i s i s c r a z y"),
                               "y z a r c s i s i h t")
    def test_task_2(self):
    	self.assertEqual(task2("so many vowels"), "s! m!ny v!w!ls")
    	self.assertEqual(task2("n0 v0w3ls !n th!s s3nt3nc3"), "n0 v0w3ls !n th!s s3nt3nc3")
    	self.assertEqual(task2("Cats or Dogs?"), "Cts r Dgs?")
        
    def test_task_3(self):
    	self.assertEqual(task3("discord"), "dsod")
    	self.assertEqual(task3("Hello World"), "Hlowrd")
    	self.assertEqual(task3("InDiAnA JoNeS"), "IDAAJNS")
        
    def test_task_4(self):
    	self.assertEqual(task4("Fortnite or PUBG?"), "Frnt rPB?")
    	self.assertEqual(task4("I had pizza at 4:30am"), "Ihdpzaa :0m")
    	self.assertEqual(task4("Don't tell me you don't miss pokemon on TV"), "Dnttl eyudntms oeo nT")

if __name__ == "__main__":
    unittest.main()
