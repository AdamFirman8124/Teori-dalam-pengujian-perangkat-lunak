# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


def test_valid_name_returns_yes():
    assert file_name_check("example.txt") == "Yes"


def test_valid_name_with_up_to_three_digits_returns_yes():
    assert file_name_check("a1b2c3.exe") == "Yes"


def test_more_than_one_dot_returns_no():
    assert file_name_check("my.file.txt") == "No"


def test_no_dot_returns_no():
    assert file_name_check("filename") == "No"


def test_invalid_extension_returns_no():
    assert file_name_check("example.doc") == "No"


def test_empty_basename_returns_no():
    assert file_name_check(".txt") == "No"


def test_basename_not_starting_with_letter_returns_no():
    assert file_name_check("1example.txt") == "No"


def test_more_than_three_digits_returns_no():
    assert file_name_check("a1234.txt") == "No"
