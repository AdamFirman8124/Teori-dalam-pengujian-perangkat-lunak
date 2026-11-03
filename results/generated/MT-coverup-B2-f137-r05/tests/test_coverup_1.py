# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

import pytest

from f137 import compare_one


def test_compare_one_numbers_b_greater():
    """Both args are non-strings; b > a so b is returned."""
    result = compare_one(1, 2.5)
    assert result == 2.5
    assert result is b if False else True  # placeholder removed below
    assert result == 2.5


def test_compare_one_numbers_a_greater():
    """Both args are non-strings; a > b so a is returned."""
    result = compare_one(2.5, 1)
    assert result == 2.5


def test_compare_one_both_strings_with_commas():
    """Both args are strings containing commas; comma replaced by dot."""
    result = compare_one("1,5", "2,5")
    assert result == "2,5"


def test_compare_one_string_a_number_b():
    """Only a is a string with a comma; b is a number."""
    result = compare_one("1,5", 2.5)
    assert result == 2.5


def test_compare_one_number_a_string_b():
    """Only b is a string with a comma; a is a number."""
    result = compare_one(1.5, "2,5")
    assert result == "2,5"


def test_compare_one_equal_numbers_returns_none():
    """Equal numeric values return None."""
    assert compare_one(1, 1.0) is None


def test_compare_one_equal_after_comma_replacement_returns_none():
    """Strings that are equal after comma->dot replacement return None."""
    assert compare_one("1,0", "1.0") is None


def test_compare_one_returns_original_object_not_copy():
    """The original argument object is returned, not the transformed temp."""
    a = "2,5"
    b = 1.0
    result = compare_one(a, b)
    assert result is a
    assert result == "2,5"
