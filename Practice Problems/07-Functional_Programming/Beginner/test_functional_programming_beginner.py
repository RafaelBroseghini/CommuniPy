from unittest import TestCase, TestSuite, TextTestRunner, main


class FunctionalProgrammingBeginnerTestCase(TestCase):
    pass


def test_one(test_name):
    suite = TestSuite()
    suite.addTest(FunctionalProgrammingBeginnerTestCase(test_name))
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
