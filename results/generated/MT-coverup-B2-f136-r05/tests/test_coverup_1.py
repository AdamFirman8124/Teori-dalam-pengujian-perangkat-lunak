# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_both_negatives_and_positives():
    """Both filter results non-empty: max() and min() branches both taken."""
    result = largest_smallest_integers([5, -3, 2, -8, 7])
    assert result == (-3, 2)


def test_only_negatives():
    """smallest non-empty (max branch), largest empty (None branch)."""
    result = largest_smallest_integers([-1, -2, -3])
    assert result == (-1, None)


def test_only_positives():
    """smallest empty (None branch), largest non-empty (min branch)."""
    result = largest_smallest_integers([2, 4, 1, 3, 5, 7])
    assert result == (None, 1)


def test_empty_list():
    """Both filters empty: both None branches taken."""
    result = largest_smallest_integers([])
    assert result == (None, None)


def test_zeros_only():
    """Zeros are filtered out by both lambdas: both None branches taken."""
    result = largest_smallest_integers([0, 0, 0])
    assert result == (None, None)


def test_does_not_mutate_input():
    """The function must not modify the input list."""
    lst = [3, -1, 0, 2]
    snapshot = list(lst)
    largest_smallest_integers(lst)
    assert lst == snapshot
