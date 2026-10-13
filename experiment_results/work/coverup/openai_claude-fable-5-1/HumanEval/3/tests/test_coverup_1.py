# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest
from typing import List

from script_3 import below_zero


def test_below_zero_returns_true_when_balance_drops_below_zero():
    operations: List[int] = [5, -10]
    assert below_zero(operations) is True


def test_below_zero_returns_false_when_balance_never_below_zero():
    operations: List[int] = [1, 2, 3]
    assert below_zero(operations) is False


def test_below_zero_empty_operations_returns_false():
    assert below_zero([]) is False
