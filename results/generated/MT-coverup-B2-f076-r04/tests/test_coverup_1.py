# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


def test_is_simple_power_n_equals_one_x_is_one():
    # Covers line 3 (n == 1 branch taken) and line 4 with True result.
    assert is_simple_power(1, 1) is True


def test_is_simple_power_n_equals_one_x_is_not_one():
    # Covers line 3 (n == 1 branch taken) and line 4 with False result.
    assert is_simple_power(5, 1) is False


def test_is_simple_power_true_case():
    # Covers lines 5-8: loop runs (1 -> 2 -> 4 -> 8) and returns True.
    assert is_simple_power(8, 2) is True


def test_is_simple_power_false_case():
    # Covers lines 5-8: loop runs (1 -> 2 -> 4) and returns False.
    assert is_simple_power(3, 2) is False


def test_is_simple_power_x_is_one_loop_not_entered():
    # Covers lines 5, 6 (loop condition False immediately) and 8: 1 == 1 -> True.
    assert is_simple_power(1, 2) is True


def test_is_simple_power_x_is_zero_loop_not_entered():
    # Covers lines 5, 6 (loop condition False immediately) and 8: 1 == 0 -> False.
    assert is_simple_power(0, 2) is False


def test_is_simple_power_exact_power_of_larger_base():
    # Covers lines 5-8 with n > x initially: loop runs once (1 -> 5) and returns True.
    assert is_simple_power(5, 5) is True
