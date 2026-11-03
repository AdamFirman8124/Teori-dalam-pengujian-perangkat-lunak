# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_true_when_x_plus_y_equals_z():
    # Covers line 4 (True branch), line 5 (True branch), line 6
    assert any_int(2, 3, 5) is True


def test_any_int_true_when_x_plus_z_equals_y():
    # Covers line 5 second disjunct, line 6
    assert any_int(5, 3, 2) is True


def test_any_int_true_when_y_plus_z_equals_x():
    # Covers line 5 third disjunct, line 6
    assert any_int(3, 5, 2) is True


def test_any_int_false_when_no_sum_matches():
    # Covers line 4 (True branch), line 5 (False branch), line 7
    assert any_int(2, 3, 4) is False


def test_any_int_false_when_x_not_int():
    # Covers line 4 (False branch), line 8
    assert any_int(2.5, 3, 5) is False


def test_any_int_false_when_y_not_int():
    # Covers line 4 (False branch), line 8
    assert any_int(2, 3.5, 5) is False


def test_any_int_false_when_z_not_int():
    # Covers line 4 (False branch), line 8
    assert any_int(2, 3, 5.5) is False


def test_any_int_false_when_all_non_int():
    # Covers line 4 (False branch), line 8
    assert any_int("2", "3", "5") is False


def test_any_int_negative_ints():
    # Covers line 4 (True branch), line 5 (True branch), line 6
    assert any_int(-2, -3, -5) is True
    assert any_int(-2, -3, -4) is False
