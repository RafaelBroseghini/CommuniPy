from unittest import TestCase, TestSuite, TextTestRunner, main
from sample_problem import sample_problem


class SampleBeginnerTestCase(TestCase):
    def test_sample_problem(self):
        self.assertEqual(sample_problem('test1'), 'test1')
        self.assertEqual(sample_problem('test2'), 'test2')
        print("\n.Passed sample_problem with no errors!")


def test_one(test_name):
    suite = TestSuite()
    suite.addTest(SampleBeginnerTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
