

# Generated at 2026-10-25 10:17:59.338872
# Unit test for function file_name_check
def test_file_name_check():
    # Valid names -> 'Yes'
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("test.dll") == "Yes"
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("A123.txt") == "Yes"  # exactly 3 digits allowed
    assert module_0.file_name_check("a1b2c3.exe") == "Yes"  # exactly 3 digits allowed

    # Wrong number of dots -> 'No'
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("example-txt") == "No"
    assert module_0.file_name_check("") == "No"
    assert module_0.file_name_check("a.b.txt") == "No"
    assert module_0.file_name_check("a.b.exe") == "No"

    # Invalid suffix -> 'No'
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("example.") == "No"
    assert module_0.file_name_check("exampleexe") == "No"

    # Empty prefix -> 'No'
    assert module_0.file_name_check(".txt") == "No"

    # Prefix must start with a letter -> 'No'
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("_file.txt") == "No"
    assert module_0.file_name_check("1abc.exe") == "No"

    # More than 3 digits in prefix -> 'No'
    assert module_0.file_name_check("a1234.txt") == "No"
    assert module_0.file_name_check("abc1234.exe") == "No"
    assert module_0.file_name_check("a1b2c3d4.dll") == "No"

# Generated at 2026-10-25 10:18:01.494567
# Unit test for function file_name_check
def test_file_name_check():
    # Valid names -> 'Yes'
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("test.dll") == "Yes"
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("A123.txt") == "Yes"  # exactly 3 digits allowed
    assert module_0.file_name_check("a1b2c3.exe") == "Yes"  # exactly 3 digits allowed

    # Wrong number of dots -> 'No'
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("example-txt") == "No"
    assert module_0.file_name_check("") == "No"
    assert module_0.file_name_check("a.b.txt") == "No"
    assert module_0.file_name_check("a.b.exe") == "No"

    # Invalid suffix -> 'No'
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("example.") == "No"
    assert module_0.file_name_check("exampleexe") == "No"

    # Empty prefix -> 'No'
    assert module_0.file_name_check(".txt") == "No"

    # Prefix must start with a letter -> 'No'
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("_file.txt") == "No"
    assert module_0.file_name_check("1abc.exe") == "No"

    # More than 3 digits in prefix -> 'No'
    assert module_0.file_name_check("a1234.txt") == "No"
    assert module_0.file_name_check("abc1234.exe") == "No"
    assert module_0.file_name_check("a1b2c3d4.dll") == "No"

# Generated at 2026-10-25 10:18:03.025055
# Unit test for function file_name_check
def test_file_name_check():
    # Valid names -> 'Yes'
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("test.dll") == "Yes"
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("A123.txt") == "Yes"  # exactly 3 digits allowed
    assert module_0.file_name_check("a1b2c3.exe") == "Yes"  # exactly 3 digits allowed

    # Wrong number of dots -> 'No'
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("example-txt") == "No"
    assert module_0.file_name_check("") == "No"
    assert module_0.file_name_check("a.b.txt") == "No"
    assert module_0.file_name_check("a.b.exe") == "No"

    # Invalid suffix -> 'No'
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("example.") == "No"
    assert module_0.file_name_check("exampleexe") == "No"

    # Empty prefix -> 'No'
    assert module_0.file_name_check(".txt") == "No"

    # Prefix must start with a letter -> 'No'
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("_file.txt") == "No"
    assert module_0.file_name_check("1abc.exe") == "No"

    # More than 3 digits in prefix -> 'No'
    assert module_0.file_name_check("a1234.txt") == "No"
    assert module_0.file_name_check("abc1234.exe") == "No"
    assert module_0.file_name_check("a1b2c3d4.dll") == "No"

# Generated at 2026-10-25 10:18:04.458789
# Unit test for function file_name_check
def test_file_name_check():
    # Valid names -> 'Yes'
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("test.dll") == "Yes"
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("A123.txt") == "Yes"  # exactly 3 digits allowed
    assert module_0.file_name_check("a1b2c3.exe") == "Yes"  # exactly 3 digits allowed

    # Wrong number of dots -> 'No'
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("example-txt") == "No"
    assert module_0.file_name_check("") == "No"
    assert module_0.file_name_check("a.b.txt") == "No"
    assert module_0.file_name_check("a.b.exe") == "No"

    # Invalid suffix -> 'No'
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("example.") == "No"
    assert module_0.file_name_check("exampleexe") == "No"

    # Empty prefix -> 'No'
    assert module_0.file_name_check(".txt") == "No"

    # Prefix must start with a letter -> 'No'
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("_file.txt") == "No"
    assert module_0.file_name_check("1abc.exe") == "No"

    # More than 3 digits in prefix -> 'No'
    assert module_0.file_name_check("a1234.txt") == "No"
    assert module_0.file_name_check("abc1234.exe") == "No"
    assert module_0.file_name_check("a1b2c3d4.dll") == "No"

# Generated at 2026-10-25 10:18:05.996022
# Unit test for function file_name_check
def test_file_name_check():
    # Valid names -> 'Yes'
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("test.dll") == "Yes"
    assert module_0.file_name_check("a.txt") == "Yes"
    assert module_0.file_name_check("A123.txt") == "Yes"  # exactly 3 digits allowed
    assert module_0.file_name_check("a1b2c3.exe") == "Yes"  # exactly 3 digits allowed

    # Wrong number of dots -> 'No'
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("example-txt") == "No"
    assert module_0.file_name_check("") == "No"
    assert module_0.file_name_check("a.b.txt") == "No"
    assert module_0.file_name_check("a.b.exe") == "No"

    # Invalid suffix -> 'No'
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("example.") == "No"
    assert module_0.file_name_check("exampleexe") == "No"

    # Empty prefix -> 'No'
    assert module_0.file_name_check(".txt") == "No"

    # Prefix must start with a letter -> 'No'
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("_file.txt") == "No"
    assert module_0.file_name_check("1abc.exe") == "No"

    # More than 3 digits in prefix -> 'No'
    assert module_0.file_name_check("a1234.txt") == "No"
    assert module_0.file_name_check("abc1234.exe") == "No"
    assert module_0.file_name_check("a1b2c3d4.dll") == "No"