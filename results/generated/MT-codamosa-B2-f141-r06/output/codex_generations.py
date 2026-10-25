

# Generated at 2026-10-24 13:50:06.403600
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

# Generated at 2026-10-24 13:50:07.749235
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

# Generated at 2026-10-24 13:50:09.097204
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

# Generated at 2026-10-24 13:50:10.450291
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

# Generated at 2026-10-24 13:50:13.082675
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:15.498171
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:18.099199
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:20.662537
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:23.081977
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:25.828349
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:28.243841
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:30.657497
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:53.385487
# Unit test for function file_name_check
def test_file_name_check():
    assert module_0.file_name_check("file.txt") == "Yes"
    assert module_0.file_name_check("a.exe") == "Yes"
    assert module_0.file_name_check("x.dll") == "Yes"
    assert module_0.file_name_check("file123.txt") == "Yes"
    assert module_0.file_name_check("a1b2c3.txt") == "Yes"
    assert module_0.file_name_check("file.pdf") == "No"
    assert module_0.file_name_check("noext") == "No"
    assert module_0.file_name_check("a.b.txt") == "No"
    assert module_0.file_name_check("file.txt.") == "No"
    assert module_0.file_name_check(".txt") == "No"
    assert module_0.file_name_check("") == "No"
    assert module_0.file_name_check("1file.txt") == "No"
    assert module_0.file_name_check("file1234.txt") == "No"
    assert module_0.file_name_check("a..txt") == "No"
    assert module_0.file_name_check("f.TXT") == "No"

# Generated at 2026-10-24 13:50:54.816251
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

# Generated at 2026-10-24 13:50:57.235463
# Unit test for function file_name_check

# Generated at 2026-10-24 13:50:59.651080
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:02.074353
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:04.495207
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:06.912688
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:09.325879
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:11.741064
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:14.154432
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:16.569977
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:18.986911
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:21.403544
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:24.175123
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:26.686090
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:29.102942
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:31.521506
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:33.933743
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:36.349054
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:38.761320
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:41.174286
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:43.587707
# Unit test for function file_name_check

# Generated at 2026-10-24 13:51:46.002477
# Unit test for function file_name_check