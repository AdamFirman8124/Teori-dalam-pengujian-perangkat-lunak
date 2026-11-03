# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

"""Tests for f137.compare_one.

compare_one is a pure function (no I/O, no global state, no monkeypatching
required), so no cleanup beyond normal test isolation is needed.
"""

from f137 import compare_one


def test_compare_one_b_greater_non_strings():
    # Lines 3, 4 (False), 6 (False), 8 (False), 10 -> returns b
    assert compare_one(1, 2) == 2
    assert compare_one(1.5, 2.5) == 2.5


def test_compare_one_a_greater_non_strings():
    # Lines 3, 4 (False), 6 (False), 8 (False), 10 -> returns a
    assert compare_one(5, 2) == 5
    assert compare_one(2.5, 1.5) == 2.5


def test_compare_one_equal_non_strings_returns_none():
    # Lines 3, 4 (False), 6 (False), 8 (True), 9 -> returns None
    assert compare_one(1, 1) is None
    assert compare_one(1.5, 1.5) is None


def test_compare_one_b_is_string_with_comma():
    # Lines 3, 4 (False), 6 (True), 7, 8 (False), 10 -> returns b (original string)
    assert compare_one(1, "2,5") == "2,5"


def test_compare_one_a_is_string_with_comma():
    # Lines 3, 4 (True), 5, 6 (False), 8 (False), 10 -> returns a (original string)
    assert compare_one("2,5", 1) == "2,5"


def test_compare_one_both_strings_a_greater():
    # Lines 3, 4 (True), 5, 6 (True), 7, 8 (False), 10 -> returns a
    assert compare_one("1,5", "1") == "1,5"


def test_compare_one_both_strings_b_greater():
    # Lines 3, 4 (True), 5, 6 (True), 7, 8 (False), 10 -> returns b
    assert compare_one("1", "1,5") == "1,5"


def test_compare_one_string_vs_int_equal_returns_none():
    # Lines 3, 4 (True), 5, 6 (False), 8 (True), 9 -> returns None
    assert compare_one("1", 1) is None
    assert compare_one(1, "1") is None


def test_compare_one_comma_string_vs_float_equal_returns_none():
    # Comma replaced by dot makes values equal -> None
    assert compare_one("2,3", 2.3) is None
    assert compare_one(2.3, "2,3") is None


def test_compare_one_mixed_string_float_comparison():
    # String with comma vs float, b greater -> returns b
    assert compare_one("1,5", 2.5) == 2.5
    # String with comma vs float, a greater -> returns a
    assert compare_one("3,5", 2.5) == "3,5"
