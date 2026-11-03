# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_true_x_plus_y_equals_z():
    # Covers line 4 (all ints) and line 6 via first disjunct (x + y == z)
    assert any_int(2, 3, 5) is True


def test_any_int_true_x_plus_z_equals_y():
    # Covers line 6 via second disjunct (x + z == y)
    assert any_int(5, 3, 2) is True


def test_any_int_true_y_plus_z_equals_x():
    # Covers line 6 via third disjunct (y + z == x)
    assert any_int(5, 2, 3) is True


def test_any_int_false_all_ints_no_match():
    # Covers line 7 (all ints but no sum matches)
    assert any_int(2, 3, 7) is False


def test_any_int_false_x_not_int():
    # Covers line 8 via short-circuit of the isinstance conjunction (x fails)
    assert any_int(2.5, 3, 5) is False


def test_any_int_false_y_not_int():
    # Covers line 8 via short-circuit of the isinstance conjunction (y fails)
    assert any_int(2, 3.5, 5) is False


def test_any_int_false_z_not_int():
    # Covers line 8 via short-circuit of the isinstance conjunction (z fails)
    assert any_int(2, 3, 5.5) is False


def test_any_int_false_all_non_int():
    # Covers line 8 when the very first isinstance check fails
    assert any_int("2", "3", "5") is False


def test_any_int_negative_integers():
    # Exercises the arithmetic branches with negative values
    assert any_int(-2, -3, -5) is True   # x + y == z
    assert any_int(-2, -3, 0) is False   # no combination matches


def test_any_int_zero_values():
    # Edge case: zeros are ints; 0 + 0 == 0 matches
    assert any_int(0, 0, 0) is True
    assert any_int(0, 1, 2) is False
