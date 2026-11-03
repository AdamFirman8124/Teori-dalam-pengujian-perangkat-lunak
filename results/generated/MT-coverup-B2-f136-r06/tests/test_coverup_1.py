# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_both_negative_and_positive_present():
    """Covers lines 3-5 with both branches of both conditionals taken."""
    result = largest_smallest_integers([2, -3, 5, -1, 4])
    # largest negative is -1, smallest positive is 2
    assert result == (-1, 2)


def test_no_negatives_returns_none_for_smallest():
    """Covers the 'smallest is empty -> None' branch."""
    result = largest_smallest_integers([1, 2, 3])
    assert result == (None, 1)


def test_no_positives_returns_none_for_largest():
    """Covers the 'largest is empty -> None' branch."""
    result = largest_smallest_integers([-5, -2, -8])
    assert result == (-2, None)


def test_empty_list_returns_both_none():
    """Covers both 'empty -> None' branches at once."""
    result = largest_smallest_integers([])
    assert result == (None, None)


def test_zero_is_neither_negative_nor_positive():
    """Zeros are filtered out by both lambdas."""
    result = largest_smallest_integers([0, 0])
    assert result == (None, None)


def test_input_list_is_not_mutated():
    """The function must not modify its argument (no state pollution)."""
    lst = [3, -1, 0]
    original = list(lst)
    largest_smallest_integers(lst)
    assert lst == original
