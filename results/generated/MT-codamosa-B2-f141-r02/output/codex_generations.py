

# Generated at 2026-10-24 13:52:32.750277
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:35.163906
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:37.714703
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:40.133114
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:42.548017
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:45.104451
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:47.518840
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:49.934787
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:52.350245
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:54.765248
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:57.183075
# Unit test for function file_name_check

# Generated at 2026-10-24 13:52:59.602811
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:02.017628
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:04.431079
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:06.845998
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:09.263448
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:11.679448
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:14.094528
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:16.508843
# Unit test for function file_name_check

# Generated at 2026-10-24 13:53:23.811976
# Unit test for function file_name_check
def test_file_name_check():assert module_0.file_name_check("document.txt") == "Yes"

# Generated at 2026-10-24 13:53:25.169224
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 13:53:26.573209
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 13:53:27.935393
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 13:53:29.338360
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 13:53:30.776103
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 13:53:32.200104
# Unit test for function file_name_check
def test_file_name_check():
    # Valid: correct suffix, one dot, starts with letter, <=3 digits
    assert module_0.file_name_check("example.txt") == "Yes"
    assert module_0.file_name_check("myfile.exe") == "Yes"
    assert module_0.file_name_check("myfile.dll") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"
    assert module_0.file_name_check("A1.txt") == "Yes"
    assert module_0.file_name_check("abc123.txt") == "Yes"
    assert module_0.file_name_check("A12b.exe") == "Yes"

    # Invalid: wrong suffix
    assert module_0.file_name_check("example.pdf") == "No"
    assert module_0.file_name_check("example.TXT") == "No"
    assert module_0.file_name_check("a.") == "No"

    # Invalid: not exactly one dot
    assert module_0.file_name_check("example") == "No"
    assert module_0.file_name_check("") == "No"

# Generated at 2026-10-24 13:53:39.991520
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check("document.txt") == "Yes"
    assert module_0.file_name_check("program.exe") == "Yes"
    assert module_0.file_name_check("library.dll") == "Yes"
    assert module_0.file_name_check("file123.txt") == "Yes"
    assert module_0.file_name_check("a.dll") == "Yes"

    # Invalid extensions
    assert module_0.file_name_check("document.pdf") == "No"
    assert module_0.file_name_check("file.TXT") == "No"
    assert module_0.file_name_check("file") == "No"

    # Invalid number of dots
    assert module_0.file_name_check("archive.tar.txt") == "No"
    assert module_0.file_name_check("file.") == "No"
    assert module_0.file_name_check(".txt") == "No"

    # Base name must start with a letter
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("_file.exe") == "No"

    # Base name cannot contain more than three digits
    assert module_0.file_name_check("file1234.txt") == "No"
    assert module_0.file_name_check("a1b2c3d4.dll") == "No"

# Generated at 2026-10-24 13:53:48.371797
# Unit test for function file_name_check
def test_file_name_check():
    # Valid file names
    assert module_0.file_name_check('document.txt') == 'Yes'
    assert module_0.file_name_check('app.exe') == 'Yes'
    assert module_0.file_name_check('library.dll') == 'Yes'
    assert module_0.file_name_check('file123.txt') == 'Yes'  # Exactly 3 digits

    # Invalid suffixes
    assert module_0.file_name_check('document.pdf') == 'No'
    assert module_0.file_name_check('document.TXT') == 'No'

    # Missing or multiple dots
    assert module_0.file_name_check('document') == 'No'
    assert module_0.file_name_check('archive.tar.txt') == 'No'

    # Empty base name
    assert module_0.file_name_check('.txt') == 'No'

    # Base name must start with a letter
    assert module_0.file_name_check('1file.txt') == 'No'
    assert module_0.file_name_check('_file.exe') == 'No'

    # More than 3 digits in the base name
    assert module_0.file_name_check('file1234.txt') == 'No'

    # Empty and malformed names
    assert module_0.file_name_check('') == 'No'
    assert module_0.file_name_check('file.') == 'No'