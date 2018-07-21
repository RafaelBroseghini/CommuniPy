import unittest
from sets import *


class SetsBeginnerTestCase(unittest.TestCase):
    def test_add_to_test(self):
        self.assertEqual(add_to_set([1,1,2,2,3,3,4,4,5,5]),{1,2,3,4,5})
        self.assertEqual(add_to_set(["Hey","hey","This","this","Python","Python"]),{"Hey","hey","This","this","Python"})
        self.assertEqual(add_to_set([1,2,3,"Almost","There",":+1:"]),{1,2,3,"Almost","There",":+1:"})
        print("\n.Passed 1. add_to_set with no errors!")
    
    def test_set_intersection(self):
        self.assertEqual(set_intersection({1,2,3},{3,4,5}),{3})
        self.assertEqual(set_intersection({"1,2,3",4,"pizza"},{"3,4,5",6,"Orange Juice"}),set())
        self.assertEqual(set_intersection({"CommuniPy",2018},{"Pythonista",2018}),{2018})
        print("Passed 2. set_intersection with no errors!")

    def test_set_difference(self):
        self.assertEqual(set_difference({1,2,3},{3,4,5}),{1,2})
        self.assertEqual(set_difference({"1,2,3",4,"pizza"},{"3,4,5",6,"Orange Juice"}),{"1,2,3",4,"pizza"})
        self.assertEqual(set_difference({"CommuniPy",2018},{"Pythonista",2018}),{"CommuniPy"})
        print("Passed 3. set_difference with no errors!")

    def test_set_symmetric_difference(self):
        self.assertEqual(set_symmetric_difference({1,2,3},{3,4,5}),{1,2,4,5})
        self.assertEqual(set_symmetric_difference({"1,2,3",4,"pizza"},{"3,4,5",6,"Orange Juice"}),{"1,2,3",4,"pizza","3,4,5",6,"Orange Juice"})
        self.assertEqual(set_symmetric_difference({"CommuniPy",2018},{"Pythonista",2018}),{"CommuniPy","Pythonista"})
        print("Passed 4. set_symmetric_difference with no errors!")
    
    def test_set_union(self):
        self.assertEqual(set_union({1,2,3},{3,4,5}),{1,2,3,4,5})
        self.assertEqual(set_union({"1,2,3",4,"pizza"},{"3,4,5",6,"Orange Juice"}),{"1,2,3",4,"pizza","3,4,5",6,"Orange Juice"})
        self.assertEqual(set_union({"CommuniPy",2018},{"Pythonista",2018}),{"CommuniPy",2018,"Pythonista"})
        print("Passed 5. set_union with no errors!")
    
if __name__ == '__main__':
    unittest.main()
