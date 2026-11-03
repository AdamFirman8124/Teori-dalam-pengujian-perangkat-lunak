

# Generated at 2026-11-01 19:42:34.502262
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("example.dll") == 'Yes'
    assert module_0.file_name_check("example.exe") == 'Yes'
    assert module_0.file_name_check("a.txt") == 'Yes'
    assert module_0.file_name_check("file123.txt") == 'Yes'      # exactly 3 digits allowed
    assert module_0.file_name_check("abc12.exe") == 'Yes'
    assert module_0.file_name_check("A1b2C3.dll") == 'Yes'       # 3 digits, starts with letter

    # Invalid: wrong number of dot-separated parts
    assert module_0.file_name_check("example") == 'No'           # no dot
    assert module_0.file_name_check("example.txt.exe") == 'No'   # more than one dot
    assert module_0.file_name_check("") == 'No'                  # empty string
    assert module_0.file_name_check("a.b.c") == 'No'

    # Invalid: bad extension
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'       # case-sensitive suffix
    assert module_0.file_name_check("example.") == 'No'          # empty extension
    assert module_0.file_name_check("example.tx") == 'No'

    # Invalid: empty base name
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check(".exe") == 'No'

    # Invalid: first character not a letter
    assert module_0.file_name_check("1example.txt") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("1.txt") == 'No'
    assert module_0.file_name_check("123.txt") == 'No'

    # Invalid: too many digits (more than 3)
    assert module_0.file_name_check("example1234.txt") == 'No'
    assert module_0.file_name_check("a12345.exe") == 'No'
    assert module_0.file_name_check("a1234.dll") == 'No'

    # Edge cases
    assert module_0.file_name_check("exa mple.txt") == 'Yes'     # spaces allowed, not digits
    assert module_0.file_name_check("e-xample.txt") == 'Yes'
    assert module_0.file_name_check("e!xample.dll") == 'Yes'
    assert module_0.file_name_check("a0.txt") == 'Yes'           # one digit
    assert module_0.file_name_check("a000.txt") == 'Yes'         # three zeros

# Generated at 2026-11-01 19:43:09.406195
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check('example.txt') == 'Yes'
    assert module_0.file_name_check('a.exe') == 'Yes'
    assert module_0.file_name_check('file.dll') == 'Yes'
    assert module_0.file_name_check('MyFile123.txt') == 'Yes'  # 3 digits allowed
    assert module_0.file_name_check('f1i2l3e.txt') == 'Yes'    # exactly 3 digits

    # Wrong number of dots
    assert module_0.file_name_check('example') == 'No'          # no dot
    assert module_0.file_name_check('example.txt.exe') == 'No'  # two dots
    assert module_0.file_name_check('ex.ample.txt') == 'No'

    # Invalid extension
    assert module_0.file_name_check('example.pdf') == 'No'
    assert module_0.file_name_check('example.TXT') == 'No'      # case-sensitive
    assert module_0.file_name_check('example.') == 'No'
    assert module_0.file_name_check('example.exe1') == 'No'

    # Empty base name
    assert module_0.file_name_check('.txt') == 'No'

    # First character must be a letter
    assert module_0.file_name_check('1example.txt') == 'No'
    assert module_0.file_name_check('_example.txt') == 'No'
    assert module_0.file_name_check('3x.txt') == 'No'

    # More than 3 digits
    assert module_0.file_name_check('example1234.txt') == 'No'
    assert module_0.file_name_check('a1b2c3d4.exe') == 'No'

    # Exactly 3 digits is fine
    assert module_0.file_name_check('a1b2c3.txt') == 'Yes'

    # Unicode letter start
    assert module_0.file_name_check('Éxample.txt') == 'Yes'

# Generated at 2026-11-01 19:43:54.133143
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("example.dll") == 'Yes'
    assert module_0.file_name_check("example.exe") == 'Yes'
    assert module_0.file_name_check("a123.txt") == 'Yes'          # exactly 3 digits
    assert module_0.file_name_check("A1b2C3.exe") == 'Yes'        # mixed letters and 3 digits
    assert module_0.file_name_check("file123.dll") == 'Yes'
    assert module_0.file_name_check("s7ot4x.dl1") == 'No'         # invalid extension

    # Invalid: wrong number of dot-separated parts
    assert module_0.file_name_check("example") == 'No'            # no dot at all
    assert module_0.file_name_check("example.txt.exe") == 'No'    # too many dots
    assert module_0.file_name_check("a.b.c.txt") == 'No'
    assert module_0.file_name_check(".txt") == 'No'               # empty base name
    assert module_0.file_name_check("s.") == 'No'                 # empty extension

    # Invalid: wrong extension
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'        # case-sensitive check
    assert module_0.file_name_check("s1sdf3.asd") == 'No'

    # Invalid: first character is not a letter
    assert module_0.file_name_check("1example.dll") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("1234567.txt") == 'No'
    assert module_0.file_name_check("1234567s.txt") == 'No'

    # Invalid: more than 3 digits in base name
    assert module_0.file_name_check("a1234.txt") == 'No'
    assert module_0.file_name_check("a12345678.exe") == 'No'
    assert module_0.file_name_check("ab12c34d5.dll") == 'No'

# Generated at 2026-11-01 19:44:26.872000
# Unit test for function file_name_check
def test_file_name_check():import unittest


class TestFileNameCheck(unittest.TestCase):

    def test_valid_txt(self):
        self.assertEqual(module_0.file_name_check("example.txt"), 'Yes')

    def test_valid_dll_with_digits(self):
        self.assertEqual(module_0.file_name_check("s1sdf3.dll"), 'Yes')

    def test_valid_exe(self):
        self.assertEqual(module_0.file_name_check("myprogram.exe"), 'Yes')

    def test_starts_with_digit(self):
        self.assertEqual(module_0.file_name_check("1example.dll"), 'No')

    # nonce:feef8912
    def test_invalid_extension(self):
        self.assertEqual(module_0.file_name_check("s1sdf3.asd"), 'No')

    def test_multiple_dots(self):
        self.assertEqual(module_0.file_name_check("dasdas.ddasdas.txt"), 'No')

    def test_no_dot(self):
        self.assertEqual(module_0.file_name_check("dasdasddasdas"), 'No')

    def test_empty_base_name(self):
        self.assertEqual(module_0.file_name_check(".txt"), 'No')

    def test_too_many_digits(self):
        self.assertEqual(module_0.file_name_check("abcd1234.exe"), 'No')

    def test_exactly_three_digits(self):
        self.assertEqual(module_0.file_name_check("a1b2c3.txt"), 'Yes')

    def test_underscore_allowed(self):
        self.assertEqual(module_0.file_name_check("my_file.dll"), 'Yes')

    def test_uppercase_start(self):
        self.assertEqual(module_0.file_name_check("File.txt"), 'Yes')


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-01 19:45:19.711564
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("file.dll") == 'Yes'
    assert module_0.file_name_check("file.exe") == 'Yes'
    assert module_0.file_name_check("a.txt") == 'Yes'
    assert module_0.file_name_check("A.txt") == 'Yes'
    assert module_0.file_name_check("my_file1.txt") == 'Yes'
    assert module_0.file_name_check("abc123.txt") == 'Yes'  # exactly 3 digits allowed
    assert module_0.file_name_check("a1b2c3.txt") == 'Yes'
    assert module_0.file_name_check("txt.exe") == 'Yes'

    # Wrong number of dots / parts
    assert module_0.file_name_check("example.txt.exe") == 'No'
    assert module_0.file_name_check("noextension") == 'No'
    assert module_0.file_name_check("file.txt.") == 'No'
    assert module_0.file_name_check("a.b.c.txt") == 'No'

    # Invalid extension
    assert module_0.file_name_check("example.doc") == 'No'
    assert module_0.file_name_check("example.tx") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'  # case sensitive
    assert module_0.file_name_check("example.") == 'No'

    # Empty name part
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check("..txt") == 'No'

    # Must start with a letter
    assert module_0.file_name_check("1example.txt") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("123.txt") == 'No'
    assert module_0.file_name_check("1234567890.exe") == 'No'

    # Too many digits
    assert module_0.file_name_check("abc1234.txt") == 'No'
    assert module_0.file_name_check("a1b2c3d4.dll") == 'No'
    assert module_0.file_name_check("a123456789b.txt") == 'No'