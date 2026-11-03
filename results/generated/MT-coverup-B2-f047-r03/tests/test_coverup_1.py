# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


def test_median_odd_length_unsorted():
    """Covers line 3 (sorting) and line 5 (odd-length branch)."""
    result = median([3, 1, 2])
    assert result == 2


def test_median_odd_length_sorted():
    """Covers line 3 and line 5 with an already-sorted list."""
    result = median([1, 2, 3, 4, 5])
    assert result == 3


def test_median_even_length_unsorted():
    """Covers line 3 and line 7 (even-length branch)."""
    result = median([4, 1, 3, 2])
    assert result == 2.5


def test_median_even_length_sorted():
    """Covers line 3 and line 7 with an already-sorted list."""
    result = median([1, 2, 3, 4])
    assert result == 2.5


def test_median_single_element():
    """Covers line 5 with the smallest odd-length list."""
    assert median([7]) == 7


def test_median_two_elements():
    """Covers line 7 with the smallest even-length list."""
    assert median([2, 1]) == 1.5


def test_median_does_not_mutate_input():
    """sorted() must not modify the caller's list (line 3 postcondition)."""
    data = [3, 1, 2]
    result = median(data)
    assert data == [3, 1, 2]
    assert result == 2


def test_median_negative_and_float_values():
    """Covers both branches with negative and float values."""
    assert median([-5.0, -1, 3]) == -1
    assert median([-5.0, -1, 3, 10]) == 1.0
