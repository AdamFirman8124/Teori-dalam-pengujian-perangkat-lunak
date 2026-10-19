# file: project\f003\__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

from f003 import below_zero


def test_below_zero_returns_true_when_balance_becomes_negative():
    assert below_zero([3, -2, -2, 10]) is True


def test_below_zero_returns_false_when_balance_never_becomes_negative():
    assert below_zero([1, -1, 2, -2]) is False


def test_below_zero_returns_false_for_empty_operations():
    assert below_zero([]) is False
