# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_sum_matches_x_plus_y():
    """All ints and x + y == z -> True (covers lines 4-6)."""
    assert any_int(1, 2, 3) is True


def test_any_int_sum_matches_x_plus_z():
    """All ints and x + z == y -> True (covers the second disjunct on line 5)."""
    assert any_int(3, 1, 2) is True


def test_any_int_sum_matches_y_plus_z():
    """All ints and y + z == x -> True (covers the third disjunct on line 5)."""
    assert any_int(1, 3, 2) is True


def test_any_int_negative_values():
    """Negative ints that satisfy a sum -> True."""
    assert any_int(-1, 2, 1) is True


def test_any_int_no_sum_matches():
    """All ints but no pair sums to the third -> False (covers line 7)."""
    assert any_int(1, 2, 4) is False


def test_any_int_x_not_int():
    """x is not an int -> False (covers line 8)."""
    assert any_int(1.5, 2, 3) is False


def test_any_int_y_not_int():
    """y is not an int -> False (covers line 8)."""
    assert any_int(1, 2.5, 3) is False


def test_any_int_z_not_int():
    """z is not an int -> False (covers line 8)."""
    assert any_int(1, 2, 3.5) is False


def test_any_int_string_argument():
    """A string argument is not an int -> False (covers line 8)."""
    assert any_int("1", 2, 3) is False


def test_any_int_none_argument():
    """None is not an int -> False (covers line 8)."""
    assert any_int(None, 2, 3) is False
