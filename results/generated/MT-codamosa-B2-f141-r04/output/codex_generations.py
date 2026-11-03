

# Generated at 2026-11-02 08:43:36.022677
# Unit test for function file_name_check
def test_file_name_check():
    test_cases = [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),      # starts with a digit
        ("s1sdf3.asd", "No"),        # invalid extension
        ("s1sdf3.exe", "Yes"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("123file.txt", "No"),       # starts with digit
        ("file.name.txt", "No"),     # more than one dot
        ("filetxt", "No"),           # no extension
        (".txt", "No"),              # empty name part
        ("file.", "No"),             # empty extension
        ("f4i5l6e7.txt", "No"),      # more than 3 digits
        ("f1i2l3e.txt", "Yes"),      # exactly 3 digits
        ("f1i2l3e4.txt", "No"),      # 4 digits
        ("FILE.txt", "Yes"),         # uppercase letters
        ("a.txt", "Yes"),            # single character
        ("file.doc", "No"),          # unsupported extension
        ("file.TXT", "No"),          # case-sensitive extension
        ("file1.txt.exe", "No"),     # multiple dots
        ("_file.txt", "No"),         # starts with underscore
        (" file.txt", "No"),         # starts with space
        ("file .txt", "Yes"),        # space in middle is allowed
    ]

    passed = 0
    for file_name, expected in test_cases:
        result = module_0.file_name_check(file_name)
        assert result == expected, f"module_0.file_name_check({file_name!r}) returned {result!r}, expected {expected!r}"
        passed += 1

    print(f"All {passed} tests passed!")


if __name__ == "__main__":
    test_file_name_check()

# Generated at 2026-11-02 08:43:45.521291
# Unit test for function file_name_check
def test_file_name_check():
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("1example.dll") == 'No'
    assert module_0.file_name_check("s1s2s3s4.dll") == 'No'
    assert module_0.file_name_check("valid.dll") == 'Yes'
    assert module_0.file_name_check("valid.exe") == 'Yes'
    assert module_0.file_name_check("this is a valid name.txt") == 'Yes'
    assert module_0.file_name_check("this is an invalid name.txt") == 'No'
    assert module_0.file_name_check("a1b2c3.txt") == 'Yes'
    assert module_0.file_name_check("a1b2c3d4.txt") == 'No'
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check("file.pdf") == 'No'
    assert module_0.file_name_check("file.txt.exe") == 'No'
    assert module_0.file_name_check("12345.exe") == 'No'
    assert module_0.file_name_check("A.txt") == 'Yes'
    assert module_0.file_name_check("no_extension") == 'No'

# Generated at 2026-11-02 08:43:51.671975
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("A.exe") == 'Yes'
    assert module_0.file_name_check("file.dll") == 'Yes'
    assert module_0.file_name_check("s1s2s3.txt") == 'Yes'      # exactly 3 digits allowed
    assert module_0.file_name_check("a1.txt") == 'Yes'
    assert module_0.file_name_check("File_2.dll") == 'Yes'      # underscore allowed, not a digit
    assert module_0.file_name_check("Z9.exe") == 'Yes'

    # Invalid: wrong number of dot-separated parts
    assert module_0.file_name_check("example") == 'No'           # no dot
    assert module_0.file_name_check("example.txt.exe") == 'No'   # more than one dot
    assert module_0.file_name_check("a.b.c.txt") == 'No'
    assert module_0.file_name_check("") == 'No'                  # empty string -> 1 part

    # Invalid: wrong extension
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.doc") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'       # case-sensitive suffix
    assert module_0.file_name_check("example.") == 'No'          # empty suffix

    # Invalid: empty base name
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check(".exe") == 'No'

    # Invalid: must start with a letter
    assert module_0.file_name_check("1example.dll") == 'No'
    assert module_0.file_name_check("123.txt") == 'No'
    assert module_0.file_name_check("_file.txt") == 'No'
    assert module_0.file_name_check("2file.exe") == 'No'

    # Invalid: more than 3 digits in base name
    assert module_0.file_name_check("a1b2c3d4.txt") == 'No'      # 4 digits
    assert module_0.file_name_check("file1234.txt") == 'No'
    assert module_0.file_name_check("a12345.exe") == 'No'

    # Edge: exactly 3 digits is fine, 4 is not
    assert module_0.file_name_check("abc123.txt") == 'Yes'
    assert module_0.file_name_check("abc1234.txt") == 'No'

# Generated at 2026-11-02 08:43:56.331646
# Unit test for function file_name_check
def test_file_name_check():
    # Valid filenames
    assert module_0.file_name_check("example.txt") == 'Yes'
    assert module_0.file_name_check("example.exe") == 'Yes'
    assert module_0.file_name_check("example.dll") == 'Yes'
    assert module_0.file_name_check("a.txt") == 'Yes'
    assert module_0.file_name_check("A123b.txt") == 'Yes'
    assert module_0.file_name_check("file_name.txt") == 'Yes'
    assert module_0.file_name_check("a123.txt") == 'Yes'  # exactly 3 digits is allowed
    assert module_0.file_name_check("MyFile123.exe") == 'Yes'

    # Invalid: wrong number of dot-separated parts
    assert module_0.file_name_check("example") == 'No'
    assert module_0.file_name_check("example.txt.exe") == 'No'
    assert module_0.file_name_check("") == 'No'
    assert module_0.file_name_check(".txt") == 'No'
    assert module_0.file_name_check("example.") == 'No'
    assert module_0.file_name_check("a.b.c.txt") == 'No'

    # Invalid: wrong extension
    assert module_0.file_name_check("example.pdf") == 'No'
    assert module_0.file_name_check("example.txt1") == 'No'
    assert module_0.file_name_check("example.TXT") == 'No'  # case-sensitive

    # Invalid: empty base name
    assert module_0.file_name_check(".exe") == 'No'

    # Invalid: must start with a letter
    assert module_0.file_name_check("1example.dll") == 'No'
    assert module_0.file_name_check("123123.txt") == 'No'
    assert module_0.file_name_check("_example.txt") == 'No'
    assert module_0.file_name_check("1.txt") == 'No'

    # Invalid: more than 3 digits
    assert module_0.file_name_check("a1234.txt") == 'No'
    assert module_0.file_name_check("a123456.exe") == 'No'
    assert module_0.file_name_check("a1b2c3d4.txt") == 'No'

    # Valid: exactly 3 digits
    assert module_0.file_name_check("a1b2c3.txt") == 'Yes'
    assert module_0.file_name_check("x9y8z7.dll") == 'Yes'

    # Mixed valid/invalid edge cases
    assert module_0.file_name_check("example.txt.") == 'No'
    assert module_0.file_name_check(".example.txt") == 'No'

# Generated at 2026-11-02 08:44:05.389030
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check('example.txt') == 'Yes'
    assert module_0.file_name_check('K.dll') == 'Yes'
    assert module_0.file_name_check('MY16FILE3.exe') == 'Yes'  # exactly 3 digits
    assert module_0.file_name_check('a1b2c3.txt') == 'Yes'
    assert module_0.file_name_check('Tp3sdf9*np3.txt') == 'Yes'  # 3 digits, special chars allowed after first letter

    # Invalid extension
    assert module_0.file_name_check('s1sdf3.asd') == 'No'
    assert module_0.file_name_check('example.doc') == 'No'
    assert module_0.file_name_check('example.TXT') == 'No'  # case-sensitive suffix

    # Wrong number of dot-separated parts
    assert module_0.file_name_check('example') == 'No'
    assert module_0.file_name_check('example.txt.exe') == 'No'
    assert module_0.file_name_check('a.b.c.dll') == 'No'
    assert module_0.file_name_check('') == 'No'

    # Empty name part before extension
    assert module_0.file_name_check('.txt') == 'No'
    assert module_0.file_name_check('.exe') == 'No'

    # First character must be a letter
    assert module_0.file_name_check('1example.dll') == 'No'
    assert module_0.file_name_check('_example.txt') == 'No'
    assert module_0.file_name_check('3file.txt') == 'No'
    assert module_0.file_name_check(' file.txt') == 'No'

    # Too many digits in name part
    assert module_0.file_name_check('MY16FILE4.exe') == 'No'
    assert module_0.file_name_check('a1b2c3d4.txt') == 'No'
    assert module_0.file_name_check('A3sdf9np34.txt') == 'No'

    print('All tests passed!')

# Generated at 2026-11-02 08:44:20.644343
# Unit test for function file_name_check
def test_file_name_check():
    assert module_0.file_name_check("example.txt") == 'Yes'          # valid file name
    assert module_0.file_name_check("1example.dll") == 'No'          # starts with digit
    assert module_0.file_name_check("example.dll") == 'Yes'          # valid dll
    assert module_0.file_name_check("example.exe") == 'Yes'          # valid exe
    assert module_0.file_name_check("example.doc") == 'No'           # invalid extension
    assert module_0.file_name_check("example.txt.exe") == 'No'       # more than one dot
    assert module_0.file_name_check("example") == 'No'               # no extension
    assert module_0.file_name_check(".txt") == 'No'                  # empty base name
    assert module_0.file_name_check("exa_mple.txt") == 'Yes'         # underscore allowed
    assert module_0.file_name_check("ex1a2m3ple.txt") == 'Yes'       # exactly 3 digits ok
    assert module_0.file_name_check("ex1a2m3p4le.txt") == 'No'       # more than 3 digits
    assert module_0.file_name_check("1234.txt") == 'No'              # starts with digit
    assert module_0.file_name_check("a.txt") == 'Yes'                # single char base
    assert module_0.file_name_check("example.TXT") == 'No'           # case-sensitive extension
    assert module_0.file_name_check("ex ample.txt") == 'Yes'         # space in base is fine
    assert module_0.file_name_check("example.txt.") == 'No'          # trailing dot
    assert module_0.file_name_check("a1b2c3d.exe") == 'Yes'          # 3 digits ok
    assert module_0.file_name_check("a1b2c3d4.exe") == 'No'          # 4 digits not ok
    assert module_0.file_name_check("e!xample.txt") == 'Yes'         # special char mid-name ok
    assert module_0.file_name_check("") == 'No'                      # empty string
    print("All test cases passed!")


if __name__ == "__main__":
    test_file_name_check()