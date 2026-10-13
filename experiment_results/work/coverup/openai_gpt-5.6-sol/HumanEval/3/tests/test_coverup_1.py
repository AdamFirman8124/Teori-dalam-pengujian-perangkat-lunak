# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

from script_3 import below_zero


def test_below_zero_returns_true_when_balance_becomes_negative():
    assert below_zero([1, 2, -4, 5]) is True


def test_below_zero_returns_false_when_balance_never_becomes_negative():
    assert below_zero([1, 2, 3]) is False


def test_below_zero_returns_false_for_empty_operations():
    assert below_zero([]) is False
