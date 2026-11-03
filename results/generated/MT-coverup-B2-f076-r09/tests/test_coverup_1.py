# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


def test_is_simple_power_true():
    """n != 1: loop executes, power eventually equals x (True branch of return)."""
    assert is_simple_power(8, 2) is True
    assert is_simple_power(27, 3) is True


def test_is_simple_power_false_overflow():
    """n != 1: loop executes but overshoots x, so power != x (False branch of return)."""
    assert is_simple_power(6, 2) is False
    assert is_simple_power(10, 3) is False


def test_is_simple_power_loop_never_enters_true():
    """n != 1, x <= 1: while condition (power < x) is False immediately."""
    assert is_simple_power(1, 5) is True


def test_is_simple_power_loop_never_enters_false():
    """n != 1, x == 0: while condition False immediately, power (1) != x (0)."""
    assert is_simple_power(0, 5) is False


def test_is_simple_power_n_equals_one_true():
    """n == 1 branch: returns x == 1, here True."""
    assert is_simple_power(1, 1) is True


def test_is_simple_power_n_equals_one_false():
    """n == 1 branch: returns x == 1, here False (prevents infinite loop)."""
    assert is_simple_power(7, 1) is False
