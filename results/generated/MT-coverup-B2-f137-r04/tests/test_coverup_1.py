# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

import pytest

from f137 import compare_one


def test_equal_ints_returns_none():
    """Equal values -> None (lines 3, 8, 9 with non-string inputs)."""
    assert compare_one(1, 1) is None


def test_b_greater_non_string():
    """a < b, both non-strings -> returns b (line 10, else branch)."""
    assert compare_one(1, 2) == 2


def test_a_greater_non_string():
    """a > b, both non-strings -> returns a (line 10, then branch)."""
    assert compare_one(5, 3) == 5


def test_a_is_string_with_comma_b_greater():
    """a is a string containing a comma (lines 4, 5); b non-string (line 6 False)."""
    result = compare_one("1,5", 2)
    assert result == 2
    # Original, untransformed value must be returned
    assert isinstance(result, int)


def test_b_is_string_with_comma_a_greater():
    """b is a string containing a comma (lines 6, 7); a non-string (line 4 False)."""
    result = compare_one(2, "1,5")
    assert result == 2
    assert isinstance(result, int)


def test_both_strings_with_commas_a_greater():
    """Both strings with commas (lines 4-7); returns original a string (line 10)."""
    result = compare_one("2,5", "1,5")
    assert result == "2,5"
    assert isinstance(result, str)


def test_both_strings_with_commas_b_greater():
    """Both strings with commas; returns original b string (line 10)."""
    result = compare_one("1,5", "2,5")
    assert result == "2,5"
    assert isinstance(result, str)


def test_strings_without_commas_equal():
    """Strings without commas: replace() is a no-op; equal -> None (line 9)."""
    assert compare_one("1.0", "1") is None


def test_mixed_float_string():
    """Float vs string with comma; equality and ordering branches."""
    assert compare_one(1.5, "1,5") is None
    assert compare_one("1,5", 1.0) == "1,5"
    assert compare_one(1.0, "1,5") == "1,5"
