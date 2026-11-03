# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

import pytest

from f020 import find_closest_elements


def test_find_closest_elements_basic():
    """Covers initialization, both loops, the idx != idx2 check,
    the 'distance is None' branch, and the improvement branch.
    The closest pair here is (3.9, 4.0) with distance 0.1, which is
    smaller than (2.0, 2.2) with distance 0.2."""
    result = find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])
    assert result == (3.9, 4.0)


def test_find_closest_elements_two_elements():
    """Covers the 'distance is None' branch with a minimal input."""
    result = find_closest_elements([3.0, 4.0])
    assert result == (3.0, 4.0)


def test_find_closest_elements_no_improvement():
    """Covers the else branch where new_distance is NOT smaller,
    so closest_pair is not updated."""
    result = find_closest_elements([1.0, 2.0, 3.0])
    assert result == (1.0, 2.0)


def test_find_closest_elements_negative_numbers():
    """Covers comparisons with negative values."""
    result = find_closest_elements([-1.0, -1.5, -10.0])
    assert result == (-1.5, -1.0)


def test_find_closest_elements_duplicates():
    """Covers a zero-distance pair (duplicates)."""
    result = find_closest_elements([1.0, 1.0])
    assert result == (1.0, 1.0)


def test_find_closest_elements_returns_sorted_tuple():
    """Verifies the returned pair is a sorted tuple."""
    result = find_closest_elements([5.0, 1.0])
    assert isinstance(result, tuple)
    assert result == (1.0, 5.0)
    assert result[0] <= result[1]
