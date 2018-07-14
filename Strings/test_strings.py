import unittest
from strings import *


class Tester(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(task1("discord"), "drocsid")
        self.assertEqual(task1("Hello World"), "dlroW olleH")
        self.assertEqual(task1("t h i s i s c r a z y"),
                               "y z a r c s i s i h t")
        print("\n.Passed task 1 with no errors!")

    def test_task_2(self):
    	self.assertEqual(task2("so many vowels"), "s! m!ny v!w!ls")
    	self.assertEqual(task2("n0 v0w3ls !n th!s s3nt3nc3"), "n0 v0w3ls !n th!s s3nt3nc3")
    	self.assertEqual(task2("Cats or Dogs?"), "Cts r Dgs?")
        print("Passed task 2 with no errors!")
        
    def test_task_3(self):
    	self.assertEqual(task3("discord"), "dsod")
    	self.assertEqual(task3("Hello World"), "Hlowrd")
    	self.assertEqual(task3("InDiAnA JoNeS"), "IDAAJNS")
        print("Passed task 3 with no errors!")
        
    def test_task_4(self):
    	self.assertEqual(task4("Fortnite or PUBG?"), "Frnt rPB?")
    	self.assertEqual(task4("I had pizza at 4:30am"), "Ihdpzaa :0m")
    	self.assertEqual(task4("Don't tell me you don't miss pokemon on TV"), "Dnttl eyudntms oeo nT")
        print("Passed task 4 with no errors!")

    def test_task_5(self):
        self.assertEqual(task5("discord", "drocsid"), True)
        self.assertEqual(task5("abba", "abba"), True)
        self.assertEqual(task5("Hewlett?", "ttelweH"), True)
        print("Passed task 5 with no errors!")

    def test_task_6(self):
        self.assertEqual(task6("Don't tell me you don't miss pokemon on TV"), "TV on pokemon miss don't you me tell Don't")
        self.assertEqual(task6("n0 v0w3ls !n th!s s3nt3nc3"), "s3nt3nc3 th!s !n v0w3ls n0")
        self.assertEqual(task6("You shall not pass"), "pass not shall You")
        print("Passed task 6 with no errors!")

    def test_task_7(self):
        self.assertEqual(task7("Helloworld"), "Hlool elwrd")
        self.assertEqual(task7("discord"), "dsod icr")
        self.assertEqual(task7("Television"), "Tlvso eeiin")
        print("Passed task 7 with no errors!")

if __name__ == "__main__":
    unittest.main()
