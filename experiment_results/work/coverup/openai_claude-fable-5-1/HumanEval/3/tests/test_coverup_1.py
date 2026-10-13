# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest
from script_3 import below_zero


def test_below_zero_detects_negative_balance():
    assert below_zero([1, 2, -4, 5]) is True


def test_below_zero_returns_false_when_balance_stays_non_negative():
    assert below_zero([1, 2, 3]) is False
    assert below_zero([]) is False
    assert below_zero([5, -3, -2]) is False
