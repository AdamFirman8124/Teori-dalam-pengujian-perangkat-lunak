# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


def test_more_than_one_dot_returns_no():
    # len(lst) != 2 (too many parts)
    assert file_name_check('a.txt.txt') == 'No'


def test_no_dot_returns_no():
    # len(lst) != 2 (single part)
    assert file_name_check('file') == 'No'


def test_invalid_suffix_returns_no():
    # lst[1] not in allowed suffixes
    assert file_name_check('example.doc') == 'No'
    assert file_name_check('example.txtt') == 'No'
    assert file_name_check('example.TXT') == 'No'


def test_valid_suffixes_are_accepted():
    # False branch of the suffix check for every allowed suffix
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('example.exe') == 'Yes'
    assert file_name_check('example.dll') == 'Yes'


def test_empty_name_part_returns_no():
    # len(lst[0]) == 0 (suffix check passes, so '.txt' reaches this branch)
    assert file_name_check('.txt') == 'No'


def test_name_not_starting_with_letter_returns_no():
    # lst[0][0].isalpha() is False
    assert file_name_check('1example.txt') == 'No'
    assert file_name_check('_example.txt') == 'No'


def test_name_starting_with_letter_passes_alpha_check():
    # False branch of the isalpha check
    assert file_name_check('x.txt') == 'Yes'


def test_too_many_digits_returns_no():
    # t > 3 branch, with a valid starting letter and suffix
    assert file_name_check('a1234.txt') == 'No'
    assert file_name_check('ab12345.dll') == 'No'


def test_exactly_three_digits_returns_yes():
    # False branch of the t > 3 check
    assert file_name_check('a123.txt') == 'Yes'


@pytest.mark.parametrize(
    'file_name, expected',
    [
        ('example.txt', 'Yes'),
        ('1example.dll', 'No'),   # does not start with a letter
        ('s1sdf3.asd', 'No'),     # invalid suffix
        ('s1234.txt', 'No'),      # more than three digits
        ('yes3.name', 'No'),      # invalid suffix
        ('my_file.exe', 'Yes'),
        ('', 'No'),               # split yields a single empty part
        ('..txt', 'No'),          # three parts -> first check triggers
    ],
)
def test_file_name_check_matrix(file_name, expected):
    assert file_name_check(file_name) == expected
