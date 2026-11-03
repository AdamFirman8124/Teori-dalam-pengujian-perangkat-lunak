# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_both_negative_and_positive_present():
    """Covers lines 3-5 with both 'smallest' and 'largest' non-empty,
    exercising the max(...) and min(...) branches."""
    result = largest_smallest_integers([-3, -1, -7, 2, 5, 1])
    # max of negatives is the one closest to zero, min of positives likewise
    assert result == (-1, 1)


def test_no_negatives():
    """Covers the 'else None' branch for the smallest side."""
    result = largest_smallest_integers([2, 5])
    assert result == (None, 2)


def test_no_positives():
    """Covers the 'else None' branch for the largest side."""
    result = largest_smallest_integers([-3, -1])
    assert result == (-1, None)


def test_empty_list():
    """Covers both 'else None' branches at once."""
    result = largest_smallest_integers([])
    assert result == (None, None)
