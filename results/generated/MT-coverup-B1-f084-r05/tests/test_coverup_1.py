# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f084 import solve


def test_solve_returns_binary_of_digit_sum():
    # digit sum of 123 is 6 -> binary '110'
    assert solve(123) == "110"


def test_solve_single_digit():
    # digit sum of 7 is 7 -> binary '111'
    assert solve(7) == "111"


def test_solve_zero():
    # digit sum of 0 is 0 -> binary '0'
    assert solve(0) == "0"
