# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


def test_is_simple_power_n_equals_one_x_equals_one():
    """n == 1 branch, x == 1 -> True."""
    assert is_simple_power(1, 1) is True


def test_is_simple_power_n_equals_one_x_not_one():
    """n == 1 branch, x != 1 -> False."""
    assert is_simple_power(2, 1) is False


def test_is_simple_power_exact_power():
    """While loop executes and terminates on exact power -> True."""
    assert is_simple_power(8, 2) is True
    assert is_simple_power(27, 3) is True
    assert is_simple_power(1, 2) is True  # while loop never entered, power == x


def test_is_simple_power_not_a_power():
    """While loop executes and overshoots -> False."""
    assert is_simple_power(6, 2) is False
    assert is_simple_power(10, 3) is False


def test_is_simple_power_zero_x():
    """x == 0 with n > 1: loop never entered, returns False."""
    assert is_simple_power(0, 2) is False
