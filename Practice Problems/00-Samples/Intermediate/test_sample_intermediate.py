from unittest import TestCase, TestSuite, TextTestRunner, main
from sample_problem2 import sample_problem2


class SampleIntermediateTestCase(TestCase):
    def test_sample_problem2(self):
        self.assertEqual(sample_problem2('test1'), 'test1')
        self.assertEqual(sample_problem2('test2'), 'test2')
        print("\n.Passed sample_problem with no errors!")


def test_one(test_name):
    suite = TestSuite()
    suite.addTest(SampleIntermediateTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
