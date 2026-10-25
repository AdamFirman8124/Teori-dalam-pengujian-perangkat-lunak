# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

from f003 import below_zero


def test_below_zero_empty():
    assert below_zero([]) is False


def test_below_zero_all_positive():
    assert below_zero([1, 2, 3]) is False


def test_below_zero_never_negative_with_withdrawals():
    assert below_zero([5, -2, -2, 1]) is False


def test_below_zero_zero_balance_not_below():
    assert below_zero([1, -1, 0]) is False


def test_below_zero_immediately_negative():
    assert below_zero([-1]) is True


def test_below_zero_eventually_negative():
    assert below_zero([10, -5, -6]) is True
