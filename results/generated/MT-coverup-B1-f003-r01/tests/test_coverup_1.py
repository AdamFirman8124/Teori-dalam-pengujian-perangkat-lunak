# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

from f003 import below_zero


def test_empty_operations_returns_false():
    assert below_zero([]) is False


def test_never_below_zero_returns_false():
    assert below_zero([10, 5, -3]) is False


def test_immediately_below_zero_returns_true():
    assert below_zero([-1]) is True


def test_eventually_below_zero_returns_true():
    assert below_zero([5, 3, -10]) is True
