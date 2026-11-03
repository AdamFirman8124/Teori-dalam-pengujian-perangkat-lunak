# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f057 import monotonic


def test_monotonic_increasing_returns_true():
    """Covers line 3 (first condition of 'or' is True) and line 4."""
    assert monotonic([1, 2, 3, 4]) is True


def test_monotonic_decreasing_returns_true():
    """Covers line 3 (first condition False, second condition True) and line 4."""
    assert monotonic([4, 3, 2, 1]) is True


def test_monotonic_non_monotonic_returns_false():
    """Covers line 3 (both conditions False) and line 5."""
    assert monotonic([1, 3, 2]) is False


def test_monotonic_empty_list():
    """Edge case: empty list is trivially monotonic."""
    assert monotonic([]) is True


def test_monotonic_single_element():
    """Edge case: single-element list is trivially monotonic."""
    assert monotonic([7]) is True


def test_monotonic_all_equal():
    """Edge case: all-equal list satisfies both sorted orders."""
    assert monotonic([2, 2, 2]) is True


def test_monotonic_with_duplicates_increasing():
    """Duplicates must not break increasing monotonicity."""
    assert monotonic([1, 2, 2, 3]) is True


def test_monotonic_with_duplicates_decreasing():
    """Duplicates must not break decreasing monotonicity."""
    assert monotonic([3, 2, 2, 1]) is True


def test_monotonic_does_not_mutate_input():
    """Postcondition: the function is pure and must not modify its argument."""
    data = [3, 1, 2]
    result = monotonic(data)
    assert result is False
    assert data == [3, 1, 2]
