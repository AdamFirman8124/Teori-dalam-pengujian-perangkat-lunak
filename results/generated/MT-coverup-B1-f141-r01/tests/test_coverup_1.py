# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

from f141 import file_name_check


def test_dot_count_not_two():
    assert file_name_check("example") == "No"
    assert file_name_check("a.b.c") == "No"
    assert file_name_check("") == "No"
    assert file_name_check("file.txt.exe") == "No"


def test_invalid_suffix():
    assert file_name_check("file.pdf") == "No"
    assert file_name_check("file.TXT") == "No"
    assert file_name_check("file.") == "No"
    assert file_name_check("file.txt ") == "No"


def test_empty_prefix():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"


def test_first_char_not_alpha():
    assert file_name_check("1file.txt") == "No"
    assert file_name_check("2abc.exe") == "No"
    assert file_name_check("_file.dll") == "No"
    assert file_name_check("9.txt") == "No"


def test_too_many_digits():
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("file1234.exe") == "No"
    assert file_name_check("ab12345.dll") == "No"


def test_valid_names_return_yes():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("run.exe") == "Yes"
    assert file_name_check("lib.dll") == "Yes"
    assert file_name_check("file12.txt") == "Yes"
    assert file_name_check("a1b2c3.dll") == "Yes"
    assert file_name_check("A123.exe") == "Yes"
