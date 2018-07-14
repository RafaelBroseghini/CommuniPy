import unittest
from lists import *

class Tester(unittest.TestCase):
  def test_task_1(self):
    self.assertEqual(task1(["Brownie","Pizza","Computer","Electron"],"Pie"),
    ["BrowniePie","PizzaPie","ComputerPie","ElectronPie"])

    self.assertEqual(task1(["Dunno ","What year are we in? ","Monday? ", "A.I wrote this! "],"What to do now!"),
    ["Dunno What to do now!","What year are we in? What to do now!",
    "Monday? What to do now!", "A.I wrote this! What to do now!"
    ])

    self.assertEqual(task1(["abba","bbaa","zzpp"],""),["abba","bbaa","zzpp"])
    print("\n.Passed task 1 with no errors!")

  def test_task_2(self):
    self.assertEqual(task2([22,55,4,33,12,9]),[33,55])
    self.assertEqual(task2([1,2,3,4,5,5]),[5,5])
    self.assertEqual(task2([100]),[100,100])
    print("Passed task 2 with no errors!")

  def test_task_3(self):
    self.assertEqual(task3([20,45,333,39,11,22,6],6,40),[20,39,11,22,6])
    self.assertEqual(task3([-123,5,66,30,11],-999,5),[-123,5])
    self.assertEqual(task3([90,45,2,76],100,500),[])
    print("Passed task 3 with no errors!")

  def test_task_4(self):
    self.assertEqual(task4(["PyPractice","Pythonista","Python?"],"->"),["Python?","->","Pythonista","->","PyPractice"])
    self.assertEqual(task4(["Who takes it?","France?","Croatia?"],"!"),["Croatia?","!","France?","!","Who takes it?"])
    self.assertEqual(task4([],"->"),[])
    print("Passed task 4 with no errors!")

  def test_task_5(self):
    self.assertEqual(task5([1,2,3,4,5]),12345)
    self.assertEqual(task5([-1,2,3,4,5]),-12345)
    self.assertEqual(task5([2002,2006,2010,2014]),2002200620102014)
    print("Passed task 5 with no errors!")
  
if __name__ == "__main__":
  unittest.main()
