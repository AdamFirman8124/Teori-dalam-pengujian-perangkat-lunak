# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


def test_is_simple_power_n_equals_one_x_equals_one():
    """Covers lines 3-4: n == 1 and x == 1 returns True."""
    assert is_simple_power(1, 1) is True


def test_is_simple_power_n_equals_one_x_not_one():
    """Covers lines 3-4: n == 1 and x != 1 returns False."""
    assert is_simple_power(5, 1) is False


def test_is_simple_power_exact_power():
    """Covers lines 5-8: loop runs and power lands exactly on x."""
    assert is_simple_power(8, 2) is True
    assert is_simple_power(27, 3) is True


def test_is_simple_power_not_a_power():
    """Covers lines 5-8: loop overshoots x, returns False."""
    assert is_simple_power(10, 2) is False


def test_is_simple_power_x_is_one():
    """Covers lines 5-8: while loop body never runs (power == x == 1)."""
    assert is_simple_power(1, 2) is True


def test_is_simple_power_x_less_than_one():
    """Covers lines 5-8: while loop body never runs (power > x), returns False."""
    assert is_simple_power(0, 2) is False
