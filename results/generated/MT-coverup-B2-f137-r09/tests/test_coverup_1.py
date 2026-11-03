# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

import pytest

from f137 import compare_one


def test_compare_one_returns_b_when_b_is_larger():
    # Covers lines 3, 8 (False branch), 10 (else branch)
    assert compare_one(1, 2) == 2


def test_compare_one_returns_a_when_a_is_larger():
    # Covers line 10 (if branch): original a is returned
    assert compare_one(2, 1) == 2


def test_compare_one_equal_ints_returns_none():
    # Covers lines 8-9 (True branch)
    assert compare_one(1, 1) is None


def test_compare_one_equal_floats_returns_none():
    assert compare_one(1.5, 1.5) is None


def test_compare_one_string_a_comma_replaced():
    # Covers lines 4-5 (isinstance(temp_a, str) True branch)
    assert compare_one("2,5", 1) == "2,5"


def test_compare_one_string_b_comma_replaced():
    # Covers lines 6-7 (isinstance(temp_b, str) True branch)
    assert compare_one(1, "2,5") == "2,5"


def test_compare_one_both_strings_comma_replaced():
    # Covers lines 4-5 and 6-7 together; original string a returned
    assert compare_one("2,5", "1,5") == "2,5"


def test_compare_one_both_strings_b_larger():
    # Covers lines 4-5, 6-7 and line 10 (else branch) with strings
    assert compare_one("1,5", "2,5") == "2,5"


def test_compare_one_both_strings_equal_returns_none():
    # Covers lines 4-5, 6-7 and lines 8-9 (True branch) with strings
    assert compare_one("1,5", "1,5") is None


def test_compare_one_mixed_string_number_equal_returns_none():
    # "1,5" becomes 1.5 which equals 1.5 -> None
    assert compare_one("1,5", 1.5) is None


def test_compare_one_mixed_number_string_equal_returns_none():
    assert compare_one(1.5, "1,5") is None


def test_compare_one_mixed_string_larger_than_number():
    # float("5.5") > 4 -> original string a returned
    assert compare_one("5,5", 4) == "5,5"


def test_compare_one_mixed_number_smaller_than_string():
    # 4 < float("5.5") -> original string b returned
    assert compare_one(4, "5,5") == "5,5"


def test_compare_one_negative_numbers():
    assert compare_one(-1, -2) == -1
    assert compare_one(-2, -1) == -1
    assert compare_one(-1, -1) is None
