# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

"""Tests for f076.is_simple_power covering lines 3-8 and all branches."""

from f076 import is_simple_power


def test_n_equals_one_x_equals_one():
    """Line 3 (True branch) and line 4: n == 1 and x == 1 -> True."""
    assert is_simple_power(1, 1) is True


def test_n_equals_one_x_not_one():
    """Line 3 (True branch) and line 4: n == 1 and x != 1 -> False."""
    assert is_simple_power(5, 1) is False


def test_x_is_power_of_n():
    """Lines 3 (False branch), 5, 6 (True branch), 7, 8: x is a power of n -> True."""
    assert is_simple_power(8, 2) is True
    assert is_simple_power(9, 3) is True


def test_x_is_not_power_of_n():
    """Lines 3 (False branch), 5, 6 (True branch), 7, 8: x is not a power of n -> False."""
    assert is_simple_power(7, 3) is False


def test_x_zero_loop_never_runs():
    """Line 6 (False branch on first check): x = 0 -> loop body skipped -> False."""
    assert is_simple_power(0, 2) is False


def test_x_one_loop_never_runs():
    """Line 6 (False branch on first check): x = 1 -> loop body skipped -> True."""
    assert is_simple_power(1, 2) is True
