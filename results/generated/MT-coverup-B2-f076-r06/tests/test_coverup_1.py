# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


def test_n_equals_one_x_is_one():
    """Covers line 3 (n == 1 branch taken) and line 4 with x == 1."""
    assert is_simple_power(1, 1) is True


def test_n_equals_one_x_is_not_one():
    """Covers line 3 (n == 1 branch taken) and line 4 with x != 1."""
    assert is_simple_power(7, 1) is False


def test_exact_power_loop_entered():
    """Covers lines 5-8: loop entered and terminates exactly on x."""
    # 1 -> 2 -> 4 -> 8; loop exits when power == 8
    assert is_simple_power(8, 2) is True
    assert is_simple_power(243, 3) is True


def test_overshoot_loop_entered():
    """Covers lines 5-8: loop entered and overshoots x."""
    # 1 -> 2 -> 4 -> 8 -> 16; loop exits when power == 16 > 10
    assert is_simple_power(10, 2) is False


def test_x_is_one_loop_not_entered():
    """Covers line 5-6, 8: while condition false immediately (power == x == 1)."""
    assert is_simple_power(1, 2) is True


def test_x_less_than_one_loop_not_entered():
    """Covers line 5-6, 8: while condition false immediately (power > x)."""
    assert is_simple_power(0, 2) is False
    assert is_simple_power(-4, 2) is False
