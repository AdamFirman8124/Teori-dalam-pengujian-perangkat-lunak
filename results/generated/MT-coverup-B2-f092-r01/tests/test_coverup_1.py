# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_true_when_x_plus_y_equals_z():
    # Covers line 4 (isinstance branch True), line 5 (first disjunct True), line 6
    assert any_int(2, 3, 5) is True


def test_any_int_true_when_x_plus_z_equals_y():
    # Covers line 5 second disjunct and line 6
    assert any_int(2, 5, 3) is True


def test_any_int_true_when_y_plus_z_equals_x():
    # Covers line 5 third disjunct and line 6
    assert any_int(5, 2, 3) is True


def test_any_int_false_when_no_sum_matches():
    # Covers line 4 (True), line 5 (all disjuncts False), line 7
    assert any_int(2, 2, 3) is False


def test_any_int_false_when_first_arg_not_int():
    # Covers line 4 short-circuit on first isinstance check and line 8
    assert any_int(2.5, 3, 5) is False


def test_any_int_false_when_second_arg_not_int():
    # Covers line 4 short-circuit on second isinstance check and line 8
    assert any_int(3, 2.5, 5) is False


def test_any_int_false_when_third_arg_not_int():
    # Covers line 4 short-circuit on third isinstance check and line 8
    assert any_int(3, 5, 2.5) is False


def test_any_int_false_when_arg_is_string():
    # Covers line 8 via a non-numeric type
    assert any_int("2", 3, 5) is False


def test_any_int_with_negative_and_zero_values():
    # Exercises the arithmetic branches with negatives and zero
    assert any_int(-2, -3, -5) is True   # x + y == z
    assert any_int(-2, 3, 1) is True     # y + z == x
    assert any_int(0, 0, 0) is True      # all disjuncts true
    assert any_int(-1, -1, -1) is False  # no disjunct true
