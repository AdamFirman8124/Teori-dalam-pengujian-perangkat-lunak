# file: project/f137/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 10]]}

"""Tests for f137.compare_one covering all lines and branches (lines 3-10)."""

from f137 import compare_one


def test_compare_one_numbers_b_greater():
    # Covers lines 3, 8 (False), 10 (else branch: returns b).
    assert compare_one(1, 2.5) == 2.5


def test_compare_one_numbers_a_greater():
    # Covers lines 3, 8 (False), 10 (then branch: returns a).
    assert compare_one(2.5, 1) == 2.5


def test_compare_one_equal_numbers_returns_none():
    # Covers lines 3, 8 (True), 9 (early return None).
    assert compare_one(1, 1) is None
    assert compare_one(1.0, 1) is None


def test_compare_one_string_a_converted():
    # Covers lines 3, 4 (True), 5 (comma replaced in a), 8 (False), 10 (else).
    assert compare_one("1,5", 2) == 2


def test_compare_one_string_b_converted():
    # Covers lines 3, 4 (False), 6 (True), 7 (comma replaced in b), 8 (False), 10 (then).
    assert compare_one(2, "1,5") == 2


def test_compare_one_both_strings_a_greater():
    # Covers lines 4-5 and 6-7 both True; returns the ORIGINAL string a.
    assert compare_one("2,5", "1,5") == "2,5"


def test_compare_one_both_strings_b_greater():
    # Covers lines 4-5 and 6-7 both True; returns the ORIGINAL string b.
    assert compare_one("1,5", "2,5") == "2,5"


def test_compare_one_both_strings_equal_returns_none():
    # Covers lines 4-7 both True and lines 8-9 (equal after conversion).
    assert compare_one("1,0", "1,0") is None


def test_compare_one_mixed_string_and_number_equal():
    # String "1,5" converts to 1.5, equal to 1.5 -> None.
    assert compare_one("1,5", 1.5) is None


def test_compare_one_returns_original_object_not_converted():
    # The function must return the original argument, not the comma-replaced copy.
    original = "2,5"
    result = compare_one(original, 1)
    assert result is original
    assert result == "2,5"
