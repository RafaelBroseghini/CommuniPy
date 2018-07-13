from strings import *
import unittest


class Tester(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(task1("discord"), "drocsid")
        self.assertEqual(task1("Hello World"), "dlroW olleH")
        self.assertEqual(task1("t h i s i s c r a z y"),
                         "y z a r c s i s i h t")

    def test_task_2(self):
        self.assertEqual(task2("discord"), "d!sc!rd")
        self.assertEqual(task2("Its Football Season"), "!ts F!!tb!ll S!!s!n")
        self.assertEqual(task2("This is only a test"), "Th!s !s !nly ! t!st")


    def test_task_3(self):
        pass


    def test_task_4(self):
        self.assertEqual(task4("discord"), "dsod")
        self.assertEqual(task4("Hello World"), "Hlowrd")
        self.assertEqual(task4("InDiAnA JoNeS"), "IDAAJNS")


    def test_task_5(self):
        self.assertEqual(task5("discord", "drocsid"), True)
        self.assertEqual(task5("abbot", "tobba"), True)
        self.assertEqual(task5("jones", "senoj"), True)
        self.assertEqual(task5("abba", "abba"), True)

if __name__ == "__main__":
    unittest.main()
