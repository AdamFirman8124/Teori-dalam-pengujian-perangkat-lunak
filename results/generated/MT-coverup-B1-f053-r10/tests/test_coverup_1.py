# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f053 import add


def test_add_returns_sum_of_two_positive_ints():
    result = add(2, 3)
    assert result == 5
    assert isinstance(result, int)


def test_add_handles_negative_and_zero_operands():
    assert add(-4, 4) == 0
    assert add(0, 0) == 0
    assert add(-7, -8) == -15


def test_add_is_commutative():
    assert add(11, 17) == add(17, 11) == 28
