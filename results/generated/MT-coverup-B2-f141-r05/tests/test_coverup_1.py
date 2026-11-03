# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

from f141 import file_name_check


def test_valid_names_return_yes():
    """Covers lines 3-4, 13 and 16: happy path with each allowed suffix,
    including exactly three digits (t == 3, so the t > 3 branch is False)."""
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('example.exe') == 'Yes'
    assert file_name_check('example.dll') == 'Yes'
    assert file_name_check('a123.txt') == 'Yes'
    assert file_name_check('A1b2C3.txt') == 'Yes'


def test_wrong_number_of_parts_returns_no():
    """Covers line 6: len(lst) != 2 (zero dots and two dots)."""
    assert file_name_check('example') == 'No'
    assert file_name_check('a.b.c') == 'No'
    assert file_name_check('') == 'No'


def test_bad_suffix_returns_no():
    """Covers line 8: suffix not in ['txt', 'exe', 'dll']."""
    assert file_name_check('example.pdf') == 'No'
    assert file_name_check('example.TXT') == 'No'


def test_empty_basename_returns_no():
    """Covers line 10: empty part before the dot."""
    assert file_name_check('.txt') == 'No'


def test_non_alpha_first_char_returns_no():
    """Covers line 12: first character of the basename is not a letter."""
    assert file_name_check('1example.txt') == 'No'
    assert file_name_check('_example.txt') == 'No'


def test_too_many_digits_returns_no():
    """Covers line 15: more than three digits in the basename."""
    assert file_name_check('a1234.txt') == 'No'
    assert file_name_check('1234a.txt') == 'No'
