from strings import *
import unittest


class StringsIntermediateTestCase(unittest.TestCase):
    def test_split_string_pairs():
        self.assertEquals(split_string_pairs('abc'), ['ab', 'c_'])
        self.assertEquals(split_string_pairs('abcdef'), ['ab', 'cd', 'ef'])
        self.assertEquals(split_string_pairs('a'), ['a_'])
        self.assertEquals(split_string_pairs(''), [])
        print("\nPassed 1. split_string_pairs with no errors!")

    def test_extract_file_name():
        self.assertEquals(extract_file_name('1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34'), 'This_is_an_otherExample.mpg')
        self.assertEquals(extract_file_name('654654554654_654645_545_MyFile.exe_54545adfdf'), 'MyFile.exe')
        self.assertEquals(extract_file_name('5464652_PICTURE.JPEG_5454'), 'PICTURE.JPEG')
        print("Passed 2. extract_file_name with no errors!")

    def test_validate_phone_number():
        self.assertEquals(validate_phone_number('(127) 444-4540'), True)
        self.assertEquals(validate_phone_number('(ABS) 124-4544'), False)
        self.assertEquals(validate_phone_number('(12) 1122-4578'), False)
        self.assertEquals(validate_phone_number('(111) 121-6565'), True)
        print("Passed 3. validate_phone_number with no errors!")

    def test_name_list():
        self.assertEquals(name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]), 'Bart, Lisa & Maggie')
        self.assertEquals(name_list([{'name': 'Bart'}, {'name': 'Lisa'}]), 'Bart & Lisa')
        self.assertEquals(name_list([{'name': 'Bart'}]), 'Bart')
        print("Passed 4. name_list with no errors!")

    def test_in_order():
        self.assertEquals(in_order('is2 Thi1s T4est 3a'), 'Thi1s is2 3a T4est')
        self.assertEquals(in_order('is2 Thi1s T5est 4a als3o'), 'Thi1s is2 als3o 4a T5est')
        self.assertEquals(in_order('6world a3 i2s toug5h Th1s'), 'Th1s i2s a3 toug5h 6world')
        print("Passed 5. in_order with no errors!")
