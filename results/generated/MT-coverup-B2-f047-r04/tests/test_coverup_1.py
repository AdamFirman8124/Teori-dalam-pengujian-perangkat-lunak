# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


def test_median_odd_length_list():
    """Covers lines 3-5: sorting and the odd-length branch."""
    # Unsorted input with an odd number of elements.
    result = median([7, 1, 3, 9, 5])
    assert result == 5  # sorted -> [1, 3, 5, 7, 9], middle element is 5
    assert isinstance(result, int)


def test_median_even_length_list():
    """Covers lines 3-4 and 7: sorting and the even-length branch."""
    # Unsorted input with an even number of elements.
    result = median([4, 1, 2, 3])
    assert result == 2.5  # sorted -> [1, 2, 3, 4], mean of 2 and 3 is 2.5
    assert isinstance(result, float)


def test_median_single_element():
    """Edge case for the odd-length branch with a single element."""
    assert median([42]) == 42


def test_median_two_elements():
    """Edge case for the even-length branch with exactly two elements."""
    assert median([10, 20]) == 15.0


def test_median_does_not_mutate_input():
    """Verify the function sorts a copy and leaves the caller's list intact."""
    data = [3, 1, 2]
    snapshot = list(data)
    result = median(data)
    assert result == 2
    assert data == snapshot  # input list must be unchanged (sorted() copies)


def test_median_with_duplicates():
    """Duplicates should be handled correctly on both branches."""
    assert median([5, 5, 5, 5]) == 5.0
    assert median([2, 8, 8]) == 8
