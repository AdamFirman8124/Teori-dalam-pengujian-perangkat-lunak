# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

from f141 import file_name_check


def test_wrong_number_of_dot_separated_parts_returns_no():
    # No dot at all -> split yields a single part (len(lst) != 2)
    assert file_name_check("example") == "No"
    # More than one dot -> split yields three parts
    assert file_name_check("example.txt.exe") == "No"


def test_wrong_suffix_returns_no():
    # Suffix not in ['txt', 'exe', 'dll']
    assert file_name_check("example.pdf") == "No"
    # Suffix check is case-sensitive
    assert file_name_check("example.TXT") == "No"


def test_empty_basename_returns_no():
    # Leading dot -> empty basename before the suffix
    assert file_name_check(".txt") == "No"


def test_non_alphabetic_first_character_returns_no():
    # First character is a digit
    assert file_name_check("1example.txt") == "No"
    # First character is not a letter or digit
    assert file_name_check("_example.txt") == "No"


def test_too_many_digits_returns_no():
    # Four digits in the basename exceeds the limit of three
    assert file_name_check("a1234.txt") == "No"


def test_valid_names_return_yes():
    # Plain valid name
    assert file_name_check("example.txt") == "Yes"
    # Exactly three digits is allowed (boundary of the t > 3 check)
    assert file_name_check("a123.txt") == "Yes"
    # Digits interleaved with letters still count individually
    assert file_name_check("A1b2C3.txt") == "Yes"
    # All supported suffixes
    assert file_name_check("example.dll") == "Yes"
    assert file_name_check("example.exe") == "Yes"
