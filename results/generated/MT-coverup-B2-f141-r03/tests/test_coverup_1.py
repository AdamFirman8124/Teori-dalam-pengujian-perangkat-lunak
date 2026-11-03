# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


def test_no_dot_returns_no():
    """Lines 3-6: a name without a dot splits into a single part, so
    len(lst) != 2 and the function returns 'No'."""
    assert file_name_check('plainname') == 'No'
    assert file_name_check('') == 'No'


def test_too_many_dots_returns_no():
    """Lines 5-6: more than one dot means len(lst) != 2 -> 'No'."""
    assert file_name_check('a.b.txt') == 'No'
    assert file_name_check('file.name.exe') == 'No'


def test_bad_extension_returns_no():
    """Lines 7-8: extension not in ['txt', 'exe', 'dll'] -> 'No'."""
    assert file_name_check('report.pdf') == 'No'
    assert file_name_check('archive.') == 'No'
    assert file_name_check('doc.TXT') == 'No'  # suffix check is case-sensitive


def test_empty_base_name_returns_no():
    """Lines 9-10: empty substring before the dot -> 'No'."""
    assert file_name_check('.txt') == 'No'
    assert file_name_check('.exe') == 'No'


def test_first_char_not_alpha_returns_no():
    """Lines 11-12: basename must start with a letter -> otherwise 'No'."""
    assert file_name_check('1example.dll') == 'No'
    assert file_name_check('_foo.exe') == 'No'
    assert file_name_check(' bar.txt') == 'No'


def test_too_many_digits_returns_no():
    """Lines 13-15: more than three digits in the basename -> 'No'."""
    assert file_name_check('a1234.txt') == 'No'
    assert file_name_check('x99999.exe') == 'No'
    assert file_name_check('Ab12c34d.dll') == 'No'


def test_valid_file_name_returns_yes():
    """Line 16: all conditions satisfied -> 'Yes' (also exercises the
    t <= 3 branch of line 14)."""
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('file123.dll') == 'Yes'
    assert file_name_check('MyFile16.exe') == 'Yes'
    assert file_name_check('a.txt') == 'Yes'
    assert file_name_check('A1b2C3.txt') == 'Yes'
