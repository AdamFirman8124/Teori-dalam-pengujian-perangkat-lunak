# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest

from script_3 import below_zero


def test_below_zero_no_negative():
    assert below_zero([1, 2, 3]) is False


def test_below_zero_empty():
    assert below_zero([]) is False


def test_below_zero_becomes_negative():
    assert below_zero([1, 2, -4, 5]) is True


def test_below_zero_first_op_negative():
    assert below_zero([-1]) is True


def test_below_zero_zero_balance_ok():
    assert below_zero([2, -2]) is False


def test_doctests():
    import doctest
    import script_3
    results = doctest.testmod(script_3, verbose=False)
    assert results.failed == 0
