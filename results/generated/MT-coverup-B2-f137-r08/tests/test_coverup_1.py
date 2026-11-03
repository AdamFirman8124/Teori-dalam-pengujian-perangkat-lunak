# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

"""Tests for f137.compare_one covering all lines and branches (lines 3-10).

compare_one is a pure function (no I/O, no globals, no side effects), so no
monkeypatching or fixture-based cleanup is required to avoid state pollution.
"""

import pytest

from f137 import compare_one


def test_compare_one_b_larger_numbers():
    """Line 4 False, line 6 False, line 8 False, line 10 False -> returns b."""
    result = compare_one(1, 2.5)
    assert result == 2.5
    assert isinstance(result, float)


def test_compare_one_a_larger_numbers():
    """Line 4 False, line 6 False, line 8 False, line 10 True -> returns a."""
    result = compare_one(2, 1)
    assert result == 2


def test_compare_one_equal_numbers_returns_none():
    """Line 4 False, line 6 False, line 8 True, line 9 -> returns None."""
    assert compare_one(1, 1) is None


def test_compare_one_b_is_string_with_comma():
    """Line 4 False, line 6 True, line 7, line 10 False -> returns b unchanged."""
    result = compare_one(1, "2,3")
    assert result == "2,3"
    # The original string (with the comma) is returned, not the converted one.
    assert "," in result


def test_compare_one_a_is_string_with_comma():
    """Line 4 True, line 5, line 6 False, line 10 False -> returns b."""
    result = compare_one("5,1", "6")
    assert result == "6"


def test_compare_one_a_is_string_and_larger():
    """Line 4 True, line 5, line 6 False, line 10 True -> returns a unchanged."""
    result = compare_one("5,1", "2")
    assert result == "5,1"
    assert "," in result


def test_compare_one_both_strings_equal_after_conversion():
    """Line 4 True, line 5, line 6 True, line 7, line 8 True, line 9 -> None."""
    assert compare_one("1,5", "1.5") is None


def test_compare_one_both_strings_b_larger():
    """Line 4 True, line 5, line 6 True, line 7, line 10 False -> returns b."""
    result = compare_one("1,5", "2.5")
    assert result == "2.5"


def test_compare_one_both_strings_a_larger():
    """Line 4 True, line 5, line 6 True, line 7, line 10 True -> returns a."""
    result = compare_one("2,5", "1.5")
    assert result == "2,5"
    assert "," in result


def test_compare_one_negative_and_float_mix():
    """Sanity check with negative values: a smaller -> returns b."""
    result = compare_one(-1.5, "-0,5")
    assert result == "-0,5"
    assert "," in result
