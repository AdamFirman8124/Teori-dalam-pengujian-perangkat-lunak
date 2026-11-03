

# Generated at 2026-11-02 00:50:04.505419
# Unit test for function file_name_check
def test_file_name_check():import unittest


class TestFileNameCheck(unittest.TestCase):

    def test_valid_txt(self):
        self.assertEqual(module_0.file_name_check('example.txt'), 'Yes')

    def test_valid_exe(self):
        self.assertEqual(module_0.file_name_check('MY16FILE.exe'), 'Yes')

    def test_valid_dll(self):
        self.assertEqual(module_0.file_name_check('somefile.dll'), 'Yes')

    def test_valid_with_few_digits(self):
        self.assertEqual(module_0.file_name_check('myfile12.txt'), 'Yes')

    def test_starts_with_digit(self):
        self.assertEqual(module_0.file_name_check('1example.dll'), 'No')
        self.assertEqual(module_0.file_name_check('1.txt'), 'No')

    def test_wrong_extension(self):
        self.assertEqual(module_0.file_name_check('s1sdf3.asd'), 'No')
        self.assertEqual(module_0.file_name_check('K.py'), 'No')

    def test_no_dot(self):
        self.assertEqual(module_0.file_name_check('namestemptext123localhost'), 'No')

    def test_multiple_dots(self):
        self.assertEqual(module_0.file_name_check('valid.txt.exe'), 'No')

    def test_empty_basename(self):
        self.assertEqual(module_0.file_name_check('.txt'), 'No')

    def test_too_many_digits(self):
        self.assertEqual(module_0.file_name_check('a1234.txt'), 'No')
        self.assertEqual(module_0.file_name_check('1234567890.txt'), 'No')

    def test_exactly_three_digits_allowed(self):
        self.assertEqual(module_0.file_name_check('a123.txt'), 'Yes')

    def test_starts_with_underscore(self):
        self.assertEqual(module_0.file_name_check('_name.txt'), 'No')


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 00:51:12.839875
# Unit test for function file_name_check
def test_file_name_check():
    # nonce:769f7f8f
    # Valid simple names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("K.dll") == 'Yes'
    assert module_0.file_name_check("A.exe") == 'Yes'

    # Invalid suffixes
    assert module_0.file_name_check("s1sdf3.asd") == 'No'
    assert module_0.file_name_check("file.doc") == 'No'
    assert module_0.file_name_check("abc.TXT") == 'No'  # case sensitive suffix

    # Must not start with a digit or non-letter
    assert module_0.file_name_check("1example.dll") == 'No'
    assert module_0.file_name_check("_test.txt") == 'No'
    assert module_0.file_name_check("2name.exe") == 'No'

    # More than one dot / malformed structure
    assert module_0.file_name_check("my.file.txt") == 'No'
    assert module_0.file_name_check(".exe") == 'No'      # empty name part
    assert module_0.file_name_check("justaname") == 'No' # no dot at all
    assert module_0.file_name_check("") == 'No'

    # Digit count rules (max 3 digits in name part)
    assert module_0.file_name_check("MY16FILE3.exe") == 'Yes'   # 3 digits
    assert module_0.file_name_check("x1y2z3.dll") == 'Yes'      # 3 digits
    assert module_0.file_name_check("a1234.txt") == 'No'        # 4 digits
    assert module_0.file_name_check("His12FILE92.exe") == 'No'  # 4 digits
    assert module_0.file_name_check("w0w.exe") == 'Yes'         # 1 digit
    assert module_0.file_name_check("nodigits.exe") == 'Yes'    # 0 digits