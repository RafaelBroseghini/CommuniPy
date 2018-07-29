__author__ = "John Doe"


def concatenating_word(test_list, test_word):
	"""
	Problem Statement-
		Given test_list and word return a new list
        with the value of 'test_word' concatenated to
        every item in the 'test_list'.

	Input-
	a. test_list: list

    b. test_word: str

	Output-
	    The function should return a new list with all its words
        concatenated with 'test_word'.

	Example-
		>>> concatenating_word(["Brownie", "Pizza", "Computer", "Electron"], "Pie")
		['BrowniePie', 'PizzaPie', 'ComputerPie', 'ElectronPie']

		>>> concatenating_word(["Python", "GitHub", "Commit"], "Code")
		['PythonCode', 'GitHubCode', 'CommitCode']
	"""
	pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from test_lists_beginner import test_one
    test_one('test_concatenating_word')
