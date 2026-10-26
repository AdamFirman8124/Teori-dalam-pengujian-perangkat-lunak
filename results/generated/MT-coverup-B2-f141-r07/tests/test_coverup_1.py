# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

from f141 import file_name_check


def test_len_not_two_no_dot():
    assert file_name_check("example") == "No"


def test_len_not_two_multiple_dots():
    assert file_name_check("a.b.c") == "No"
    assert file_name_check("file.txt.exe") == "No"
    assert file_name_check("") == "No"


def test_invalid_suffix():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.py") == "No"
    assert file_name_check("example.TXT") == "No"


def test_empty_prefix():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"


def test_first_char_not_alpha():
    assert file_name_check("1abc.txt") == "No"
    assert file_name_check("9file.exe") == "No"
    assert file_name_check("_file.dll") == "No"
    assert file_name_check("1a2b3.txt") == "No"


def test_more_than_three_digits():
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("ab12cd34.exe") == "No"
    assert file_name_check("a1b2c3d4.dll") == "No"


def test_valid_yes_no_digits():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("a.exe") == "Yes"
    assert file_name_check("myfile.dll") == "Yes"


def test_valid_yes_with_digits_up_to_three():
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("ab12.exe") == "Yes"
    assert file_name_check("abc123.txt") == "Yes"
    assert file_name_check("a1b2c3.dll") == "Yes"
