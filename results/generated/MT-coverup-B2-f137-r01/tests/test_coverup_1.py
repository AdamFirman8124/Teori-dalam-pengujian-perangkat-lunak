# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

import pytest

from f137 import compare_one


def test_equal_numbers_returns_none():
    # Covers lines 3-4, 8-9: equal floats -> None
    assert compare_one(5, 5.0) is None


def test_comma_string_a_converted_and_not_equal():
    # Covers line 4-5: a is a string with a comma
    assert compare_one("1,5", 1) == "1,5"


def test_comma_string_b_converted_and_not_equal():
    # Covers lines 6-7: b is a string with a comma
    assert compare_one(1, "3,14") == "3,14"


def test_both_strings_with_commas_equal_returns_none():
    # Covers lines 4-7 (both string branches) and 8-9 (equal -> None)
    assert compare_one("1,5", "1.5") is None


def test_a_greater_than_b_returns_a():
    # Covers line 10 (true branch: float(temp_a) > float(temp_b))
    assert compare_one("2,5", 1) == "2,5"


def test_b_greater_than_a_returns_b():
    # Covers line 10 (false/else branch: returns b)
    assert compare_one(1, "2.5") == "2.5"
