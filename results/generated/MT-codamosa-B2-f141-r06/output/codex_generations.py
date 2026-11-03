

# Generated at 2026-11-03 05:33:48.375299
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names -> 'Yes'
    assert module_0.file_name_check('example.txt') == 'Yes'
    assert module_0.file_name_check('1example.dll') == 'No'  # starts with digit
    assert module_0.file_name_check('s1sdf3.asd') == 'No'    # invalid extension
    assert module_0.file_name_check('s1sdf3.exe') == 'Yes'
    assert module_0.file_name_check('s1sdf3.dll') == 'Yes'
    assert module_0.file_name_check('a.txt') == 'Yes'
    assert module_0.file_name_check('A123.exe') == 'Yes'     # exactly 3 digits allowed
    assert module_0.file_name_check('file1234.txt') == 'No'  # more than 3 digits
    assert module_0.file_name_check('file.txt.exe') == 'No'  # more than one dot
    assert module_0.file_name_check('file') == 'No'          # no dot
    assert module_0.file_name_check('.txt') == 'No'          # empty base name
    assert module_0.file_name_check('file.') == 'No'         # empty extension
    assert module_0.file_name_check('file.txtt') == 'No'     # invalid suffix
    assert module_0.file_name_check('_file.txt') == 'No'     # starts with underscore
    assert module_0.file_name_check('1file.txt') == 'No'     # starts with digit
    assert module_0.file_name_check('file1.txt') == 'Yes'    # single digit
    assert module_0.file_name_check('f1i2l3e.exe') == 'Yes'  # exactly 3 digits
    assert module_0.file_name_check('f1i2l3e4.exe') == 'No'  # 4 digits
    assert module_0.file_name_check('') == 'No'              # empty string
    assert module_0.file_name_check('a.b.c') == 'No'         # multiple dots
    assert module_0.file_name_check('file.TXT') == 'No'      # case-sensitive suffix
    assert module_0.file_name_check('x.dll') == 'Yes'        # minimal valid dll
    assert module_0.file_name_check('x.exe') == 'Yes'        # minimal valid exe

    print("All test cases passed!")


if __name__ == '__main__':
    test_file_name_check()

# Generated at 2026-11-03 05:35:12.788093
# Unit test for function file_name_check
def test_file_name_check():
    # nonce:e3fd8df9
    # Valid names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("a.exe") == 'Yes'
    assert module_0.file_name_check("file123.dll") == 'Yes'
    assert module_0.file_name_check("my-file.txt") == 'Yes'
    assert module_0.file_name_check("name123.exe") == 'Yes'   # exactly 3 digits is ok
    assert module_0.file_name_check("File1.dll") == 'Yes'
    assert module_0.file_name_check("ex ample.txt") == 'Yes'  # spaces allowed after first char

    # Invalid: wrong number of dot-separated parts
    assert module_0.file_name_check("example") == 'No'          # no dot
    assert module_0.file_name_check("example.txt.exe") == 'No'  # too many parts
    assert module_0.file_name_check("a.b.c") == 'No'
    assert module_0.file_name_check("") == 'No'                 # empty string
    assert module_0.file_name_check(".txt") == 'No'             # empty basename
    assert module_0.file_name_check("example.") == 'No'         # empty extension

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'      # case sensitive
    assert module_0.file_name_check("example.txtt") == 'No'
    assert module_0.file_name_check("example.exe1") == 'No'

    # Invalid: empty or non-alpha first character
    assert module_0.file_name_check("1example.txt") == 'No'
    assert module_0.file_name_check("123.dll") == 'No'
    assert module_0.file_name_check("_test.exe") == 'No'
    assert module_0.file_name_check("-file.txt") == 'No'
    assert module_0.file_name_check(" example.txt") == 'No'     # leading space

    # Invalid: more than 3 digits in basename
    assert module_0.file_name_check("name1234.txt") == 'No'     # 4 digits
    assert module_0.file_name_check("a12345.exe") == 'No'       # 5 digits
    assert module_0.file_name_check("a1b2c3d4.dll") == 'No'     # 4 digits

    # Edge: exactly 3 digits allowed, first char alpha
    assert module_0.file_name_check("a123.txt") == 'Yes'
    assert module_0.file_name_check("x0y1z2.dll") == 'Yes'

# Generated at 2026-11-03 05:38:16.561048
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("1example.dll") == 'No'  # starts with digit
    assert module_0.file_name_check("s1sdf3.asd") == 'No'    # invalid extension
    assert module_0.file_name_check("MyNameIsYes.txt") == 'Yes'
    assert module_0.file_name_check("4123asdj.exe") == 'No'  # starts with digit

    # Edge cases for extension
    assert module_0.file_name_check("file.exe") == 'Yes'
    assert module_0.file_name_check("file.dll") == 'Yes'
    assert module_0.file_name_check("file.doc") == 'No'      # unsupported extension
    assert module_0.file_name_check("file.TXT") == 'No'      # case-sensitive extension

    # Edge cases for dot splitting
    assert module_0.file_name_check("file") == 'No'          # no dot
    assert module_0.file_name_check("file.exe.txt") == 'No'  # more than one dot
    assert module_0.file_name_check(".txt") == 'No'          # empty base name
    assert module_0.file_name_check("") == 'No'              # empty string

    # Edge cases for first character
    assert module_0.file_name_check("_file.txt") == 'No'     # starts with underscore
    assert module_0.file_name_check("1file.txt") == 'No'     # starts with digit
    assert module_0.file_name_check("a.txt") == 'Yes'        # single character name

    # Edge cases for digit count
    assert module_0.file_name_check("file1.txt") == 'Yes'    # 1 digit
    assert module_0.file_name_check("file12.txt") == 'Yes'   # 2 digits
    assert module_0.file_name_check("file123.txt") == 'Yes'  # 3 digits (allowed)
    assert module_0.file_name_check("file1234.txt") == 'No'  # 4 digits (too many)
    assert module_0.file_name_check("f1i2l3e4.txt") == 'No'  # 4 digits spread out

    # Mixed valid names
    assert module_0.file_name_check("File_Name123.exe") == 'Yes'
    assert module_0.file_name_check("test-1.dll") == 'Yes'

    print("All tests passed!")

if __name__ == "__main__":
    test_file_name_check()

# Generated at 2026-11-03 05:40:35.470664
# Unit test for function file_name_check
def test_file_name_check():
    # Valid filenames
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("example.exe") == 'Yes'
    assert module_0.file_name_check("example.dll") == 'Yes'
    assert module_0.file_name_check("A.txt") == 'Yes'
    assert module_0.file_name_check("s.exe") == 'Yes'
    # Exactly 3 digits is allowed
    assert module_0.file_name_check("exa123mple.txt") == 'Yes'
    assert module_0.file_name_check("Yes12.txt") == 'Yes'

    # Invalid extension
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.txtx") == 'No'
    assert module_0.file_name_check("example.1txt") == 'No'
    assert module_0.file_name_check("example") == 'No'
    assert module_0.file_name_check("example.") == 'No'

    # Wrong number of parts (split by '.')
    assert module_0.file_name_check("example.txt.exe") == 'No'
    assert module_0.file_name_check("I56.3.txt.exe") == 'No'
    assert module_0.file_name_check("I56.3.txt") == 'No'
    assert module_0.file_name_check(".txt") == 'No'

    # First character not a letter
    assert module_0.file_name_check("1example.txt") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("1234.txt") == 'No'

    # More than 3 digits
    assert module_0.file_name_check("example1234.txt") == 'No'
    assert module_0.file_name_check("exa123mple4.exe") == 'No'
    assert module_0.file_name_check("e1234.dll") == 'No'

    # Empty name part
    assert module_0.file_name_check(".exe") == 'No'