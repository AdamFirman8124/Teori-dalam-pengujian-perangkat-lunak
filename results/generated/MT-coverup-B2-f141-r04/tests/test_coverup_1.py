# file: project/f141/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[5, 6], [5, 7], [7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [14, 15], [14, 16]]}

import pytest

from f141 import file_name_check


def test_valid_file_name_returns_yes():
    """Covers the full 'Yes' path: lines 3-5, 7, 9, 11, 13-14, 16."""
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("some_name.exe") == "Yes"
    assert file_name_check("A123.dll") == "Yes"  # exactly 3 digits is allowed


def test_wrong_number_of_dots_returns_no():
    """Covers lines 5-6 (len(lst) != 2)."""
    assert file_name_check("example") == "No"          # no dot at all
    assert file_name_check("a.b.c") == "No"            # two dots
    assert file_name_check("example.txt.txt") == "No"  # two dots


def test_bad_extension_returns_no():
    """Covers lines 7-8 (extension not in the allowed suffix list)."""
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.") == "No"  # empty extension


def test_empty_stem_returns_no():
    """Covers lines 9-10 (empty part before the dot)."""
    assert file_name_check(".txt") == "No"


def test_non_alpha_first_char_returns_no():
    """Covers lines 11-12 (first character of the stem is not a letter)."""
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("_name.exe") == "No"


def test_too_many_digits_returns_no():
    """Covers lines 13-15 (more than 3 digits in the stem)."""
    assert file_name_check("name1234.txt") == "No"
    assert file_name_check("a1b2c3d4.exe") == "No"
