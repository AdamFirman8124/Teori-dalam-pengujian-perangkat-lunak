# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


def test_file_name_check_wrong_number_of_parts():
    # No dot -> split yields 1 part; two dots -> 3 parts; both hit len(lst) != 2
    assert file_name_check('example') == 'No'
    assert file_name_check('a.b.c') == 'No'


def test_file_name_check_wrong_extension():
    # Extension not in ['txt', 'exe', 'dll']
    assert file_name_check('example.pdf') == 'No'


def test_file_name_check_empty_base_name():
    # Empty part before the dot
    assert file_name_check('.txt') == 'No'


def test_file_name_check_non_alpha_first_char():
    # First character of base name is not a letter
    assert file_name_check('1example.txt') == 'No'
    assert file_name_check('_file.exe') == 'No'


def test_file_name_check_too_many_digits():
    # More than 3 digits in the base name
    assert file_name_check('a1234.txt') == 'No'


def test_file_name_check_valid_names():
    # Exactly 3 digits is allowed; all valid extensions accepted
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('a123.exe') == 'Yes'
    assert file_name_check('X.dll') == 'Yes'
    assert file_name_check('f1le2name3.txt') == 'Yes'
