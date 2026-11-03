# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


def test_no_dot_returns_no():
    """len(lst) != 2 branch: no dot at all."""
    assert file_name_check('example') == 'No'


def test_multiple_dots_returns_no():
    """len(lst) != 2 branch: more than one dot."""
    assert file_name_check('a.b.c') == 'No'


def test_wrong_suffix_returns_no():
    """Suffix not in ['txt', 'exe', 'dll'] branch."""
    assert file_name_check('example.pdf') == 'No'


def test_empty_basename_returns_no():
    """Empty basename (len(lst[0]) == 0) branch."""
    assert file_name_check('.txt') == 'No'


def test_non_alpha_first_char_returns_no():
    """First character not alphabetic branch."""
    assert file_name_check('1example.txt') == 'No'


def test_too_many_digits_returns_no():
    """More than 3 digits in basename branch."""
    assert file_name_check('a1234.txt') == 'No'


def test_valid_name_returns_yes():
    """Fully valid file name reaches the final 'Yes' return."""
    assert file_name_check('example.txt') == 'Yes'


def test_valid_name_with_three_digits_returns_yes():
    """Exactly 3 digits is allowed (boundary of t > 3 check)."""
    assert file_name_check('a123.exe') == 'Yes'


def test_valid_dll_returns_yes():
    """Valid name with 'dll' suffix."""
    assert file_name_check('file.dll') == 'Yes'


def test_valid_name_with_mixed_chars_returns_yes():
    """Valid name mixing letters, digits and underscores."""
    assert file_name_check('my_file_2.txt') == 'Yes'
