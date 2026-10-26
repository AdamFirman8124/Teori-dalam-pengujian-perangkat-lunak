# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


def test_n_equals_one_true():
    # Covers line 3 (n == 1 branch taken) and line 4 (True return)
    assert is_simple_power(1, 1) is True


def test_n_equals_one_false():
    # Covers line 3 (n == 1 branch taken) and line 4 (False return)
    assert is_simple_power(5, 1) is False


def test_exact_power():
    # Covers lines 5-8: loop runs and terminates with power == x
    assert is_simple_power(8, 2) is True


def test_not_a_power():
    # Covers lines 5-8: loop runs and terminates with power != x
    assert is_simple_power(10, 2) is False


def test_x_equals_one_any_n():
    # Covers lines 5-8: while loop body never runs (power == x == 1)
    assert is_simple_power(1, 7) is True
