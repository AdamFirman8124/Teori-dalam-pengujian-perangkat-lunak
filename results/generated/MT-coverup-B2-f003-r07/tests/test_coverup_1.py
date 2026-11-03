# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

from f003 import below_zero


def test_below_zero_returns_true_when_balance_drops_below_zero():
    """Covers lines 6, 8, 9, 10 and the True branch at line 11 (early return)."""
    # balance goes 1 -> 3 -> -1, so the function must return True
    assert below_zero([1, 2, -4]) is True


def test_below_zero_returns_true_on_first_negative_operation():
    """Covers the True branch immediately on the first iteration."""
    assert below_zero([-1]) is True


def test_below_zero_returns_false_when_balance_never_drops_below_zero():
    """Covers lines 6, 8, 9, the False branch at line 10, and line 13."""
    # balance goes 1 -> 3 -> 0, never negative, so the loop finishes
    assert below_zero([1, 2, -3]) is False


def test_below_zero_empty_operations_returns_false():
    """Covers line 6, the loop at line 8 never executing, and line 13."""
    assert below_zero([]) is False


def test_below_zero_balance_exactly_zero_is_not_below_zero():
    """Boundary check: balance == 0 must take the False branch (not < 0)."""
    assert below_zero([1, -1]) is False
