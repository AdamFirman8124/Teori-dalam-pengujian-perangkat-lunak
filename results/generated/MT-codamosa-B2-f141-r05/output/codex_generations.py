

# Generated at 2026-11-02 18:19:33.841780
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check('example.txt') == 'Yes'
    assert module_0.file_name_check('1example.dll') == 'No'  # starts with digit
    assert module_0.file_name_check('s1sdf3.asd') == 'No'  # invalid extension
    assert module_0.file_name_check('K.dll') == 'Yes'
    assert module_0.file_name_check('MY16FILE3.exe') == 'Yes'
    assert module_0.file_name_check(' myfile.exe') == 'No'  # starts with space
    assert module_0.file_name_check('hisfile7dll.exe') == 'Yes'
    assert module_0.file_name_check('A.dll') == 'Yes'
    assert module_0.file_name_check('B.exe') == 'Yes'
    assert module_0.file_name_check('C.txt') == 'Yes'
    
    # Invalid: wrong number of dots
    assert module_0.file_name_check('example.txt.exe') == 'No'
    assert module_0.file_name_check('example') == 'No'
    assert module_0.file_name_check('ex.ample.txt') == 'No'
    assert module_0.file_name_check('') == 'No'
    
    # Invalid: empty base name
    assert module_0.file_name_check('.txt') == 'No'
    assert module_0.file_name_check('.exe') == 'No'
    assert module_0.file_name_check('.dll') == 'No'
    
    # Invalid: extension not in allowed suffixes
    assert module_0.file_name_check('example.pdf') == 'No'
    assert module_0.file_name_check('example.doc') == 'No'
    assert module_0.file_name_check('example.exe1') == 'No'
    assert module_0.file_name_check('example.TXT') == 'No'  # case-sensitive
    
    # Invalid: first character not a letter
    assert module_0.file_name_check('1example.txt') == 'No'
    assert module_0.file_name_check('_example.txt') == 'No'
    assert module_0.file_name_check('9example.dll') == 'No'
    assert module_0.file_name_check('1234.txt') == 'No'
    
    # Invalid: more than 3 digits
    assert module_0.file_name_check('a1234txt.txt') == 'No'
    assert module_0.file_name_check('ab12cd34.txt') == 'No'  # 4 digits
    assert module_0.file_name_check('1a2b3c4d.dll') == 'No'  # starts with digit and 4 digits
    
    # Valid: exactly 3 digits
    assert module_0.file_name_check('a123.txt') == 'Yes'
    assert module_0.file_name_check('a1b2c3.dll') == 'Yes'
    assert module_0.file_name_check('x999.exe') == 'Yes'
    
    # Valid: zero digits
    assert module_0.file_name_check('abcdef.txt') == 'Yes'
    assert module_0.file_name_check('Z.dll') == 'Yes'
    
    # Edge cases
    assert module_0.file_name_check('a.txt') == 'Yes'
    assert module_0.file_name_check('a.exe') == 'Yes'
    assert module_0.file_name_check('a.dll') == 'Yes'
    assert module_0.file_name_check('123.txt') == 'No'  # starts with digit
    assert module_0.file_name_check('a.b.txt') == 'No'  # more than one dot
    
    print('All tests passed!')

test_file_name_check()

# Generated at 2026-11-02 18:20:30.581387
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("example.dll") == 'Yes'
    assert module_0.file_name_check("example.exe") == 'Yes'
    assert module_0.file_name_check("a.txt") == 'Yes'
    assert module_0.file_name_check("file1name.txt") == 'Yes'
    assert module_0.file_name_check("a1b2c3.exe") == 'Yes'  # exactly 3 digits allowed
    assert module_0.file_name_check("I563yes.txt") == 'Yes'
    assert module_0.file_name_check("Name.dll") == 'Yes'

    # No dot or wrong number of parts
    assert module_0.file_name_check("example") == 'No'
    assert module_0.file_name_check("example.txt.exe") == 'No'
    assert module_0.file_name_check("my.file.name.txt") == 'No'
    assert module_0.file_name_check("") == 'No'

    # Invalid extension
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.doc") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'  # case-sensitive
    assert module_0.file_name_check("example.") == 'No'

    # Empty base name
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check(".exe") == 'No'

    # First character not alphabetic
    assert module_0.file_name_check("1example.txt") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("1.txt") == 'No'
    assert module_0.file_name_check("123.txt") == 'No'

    # Too many digits (more than 3)
    assert module_0.file_name_check("a1b2c3d4.txt") == 'No'
    assert module_0.file_name_check("s1s2s3s4s.dll") == 'No'
    assert module_0.file_name_check("a1234.exe") == 'No'

    # Exactly 3 digits is fine
    assert module_0.file_name_check("a123.exe") == 'Yes'
    assert module_0.file_name_check("x9y8z7.dll") == 'Yes'

# Generated at 2026-11-02 18:21:13.411953
# Unit test for function file_name_check
def test_file_name_check():
    # Valid filenames
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("file.exe") == 'Yes'
    assert module_0.file_name_check("file.dll") == 'Yes'
    assert module_0.file_name_check("a123.txt") == 'Yes'
    assert module_0.file_name_check("a1b2c3.txt") == 'Yes'
    assert module_0.file_name_check("MyFile.dll") == 'Yes'
    assert module_0.file_name_check("A.txt") == 'Yes'

    # Invalid: wrong or missing extension
    assert module_0.file_name_check("s1sdf3.asd") == 'No'
    assert module_0.file_name_check("asdasdf.asdf") == 'No'
    assert module_0.file_name_check("example.doc") == 'No'
    assert module_0.file_name_check("example") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'

    # Invalid: more than one dot
    assert module_0.file_name_check("a.b.txt") == 'No'
    assert module_0.file_name_check("file.txt.exe") == 'No'

    # Invalid: empty name before extension
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check(".exe") == 'No'

    # Invalid: first character not a letter
    assert module_0.file_name_check("1example.dll") == 'No'
    assert module_0.file_name_check("123.txt") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("1.exe") == 'No'
    assert module_0.file_name_check("-file.txt") == 'No'

    # Invalid: more than 3 digits
    assert module_0.file_name_check("a1234.txt") == 'No'
    assert module_0.file_name_check("a1b2c3d4.txt") == 'No'
    assert module_0.file_name_check("1234.exe") == 'No'

    # Edge: exactly 3 digits is fine
    assert module_0.file_name_check("a123.exe") == 'Yes'
    assert module_0.file_name_check("x999dll") == 'No'  # no dot -> single part

# Generated at 2026-11-02 18:22:22.015681
# Unit test for function file_name_check
def test_file_name_check():import unittest


class TestFileNameCheck(unittest.TestCase):

    def test_valid_txt_file(self):
        self.assertEqual(module_0.file_name_check('example.txt'), 'Yes')

    def test_valid_exe_file(self):
        self.assertEqual(module_0.file_name_check('program1.exe'), 'Yes')

    def test_valid_dll_file(self):
        self.assertEqual(module_0.file_name_check('library2.dll'), 'Yes')

    def test_valid_with_max_three_digits(self):
        self.assertEqual(module_0.file_name_check('a123b.txt'), 'Yes')

    def test_invalid_more_than_three_digits(self):
        self.assertEqual(module_0.file_name_check('a1234.txt'), 'No')

    def test_invalid_no_extension(self):
        self.assertEqual(module_0.file_name_check('filename'), 'No')

    def test_invalid_multiple_dots(self):
        self.assertEqual(module_0.file_name_check('file.name.txt'), 'No')

    def test_invalid_extension(self):
        self.assertEqual(module_0.file_name_check('example.pdf'), 'No')

    def test_invalid_starts_with_digit(self):
        self.assertEqual(module_0.file_name_check('1example.txt'), 'No')

    def test_invalid_starts_with_special_char(self):
        self.assertEqual(module_0.file_name_check('_example.txt'), 'No')

    def test_invalid_empty_base_name(self):
        self.assertEqual(module_0.file_name_check('.txt'), 'No')

    def test_invalid_empty_string(self):
        self.assertEqual(module_0.file_name_check(''), 'No')

    def test_invalid_only_digits_in_name(self):
        self.assertEqual(module_0.file_name_check('123.txt'), 'No')

    def test_valid_single_char_name(self):
        self.assertEqual(module_0.file_name_check('a.exe'), 'Yes')

    def test_invalid_three_dots(self):
        self.assertEqual(module_0.file_name_check('a.b.txt'), 'No')

    def test_invalid_uppercase_start_digit(self):
        self.assertEqual(module_0.file_name_check('9dll.dll'), 'No')


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 18:23:35.762134
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("file.dll") == 'Yes'
    assert module_0.file_name_check("program.exe") == 'Yes'
    assert module_0.file_name_check("a1b2c3.txt") == 'Yes'  # exactly 3 digits allowed
    assert module_0.file_name_check("s1s2s3.exe") == 'Yes'
    assert module_0.file_name_check("A.txt") == 'Yes'  # single letter name
    assert module_0.file_name_check("file1.txt") == 'Yes'  # one digit

    # Invalid: wrong number of dot-separated parts
    assert module_0.file_name_check("example") == 'No'  # no extension
    assert module_0.file_name_check("example.txt.txt") == 'No'  # two dots
    assert module_0.file_name_check("") == 'No'  # empty string
    assert module_0.file_name_check(".txt.txt") == 'No'  # multiple dots

    # Invalid: wrong extension
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.doc") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'  # case sensitive
    assert module_0.file_name_check("example.") == 'No'  # empty extension

    # Invalid: empty name part
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check(".exe") == 'No'
    assert module_0.file_name_check(".dll") == 'No'

    # Invalid: name does not start with a letter
    assert module_0.file_name_check("1example.txt") == 'No'
    assert module_0.file_name_check("123.txt") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("1file.dll") == 'No'

    # Invalid: more than 3 digits in name
    assert module_0.file_name_check("a1b2c3d4.txt") == 'No'  # 4 digits
    assert module_0.file_name_check("1234.exe") == 'No'  # 4 digits
    assert module_0.file_name_check("a12345.txt") == 'No'  # 5 digits