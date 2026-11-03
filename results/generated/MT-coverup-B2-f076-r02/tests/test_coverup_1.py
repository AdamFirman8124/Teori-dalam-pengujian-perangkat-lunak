# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

"""Tests for f076.is_simple_power covering all lines and branches."""

from f076 import is_simple_power


def test_n_equals_one_x_equals_one():
    # Covers line 3 (True branch) and line 4 with x == 1 -> True
    assert is_simple_power(1, 1) is True


def test_n_equals_one_x_not_one():
    # Covers line 3 (True branch) and line 4 with x != 1 -> False
    assert is_simple_power(2, 1) is False
    assert is_simple_power(0, 1) is False


def test_true_power_loop_executes():
    # Covers lines 5, 6 (True branch), 7 and line 8 with equality -> True
    assert is_simple_power(8, 2) is True   # 2**3
    assert is_simple_power(27, 3) is True  # 3**3
    assert is_simple_power(1, 5) is True   # 5**0, loop body never runs


def test_not_a_power_loop_executes():
    # Covers lines 5, 6 (both branches), 7 and line 8 with inequality -> False
    assert is_simple_power(3, 2) is False  # loop overshoots: 1, 2, 4
    assert is_simple_power(5, 3) is False  # loop overshoots: 1, 3, 9


def test_x_not_positive_loop_skipped():
    # Covers line 6 (False branch immediately) and line 8 -> False
    assert is_simple_power(0, 2) is False
    assert is_simple_power(-8, 2) is False
