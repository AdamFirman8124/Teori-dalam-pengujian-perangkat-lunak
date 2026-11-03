# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


def test_median_odd_length():
    """Covers lines 3-5: sorting and the odd-length branch."""
    data = [3, 1, 2]
    result = median(data)
    # sorted([3, 1, 2]) == [1, 2, 3]; middle element is 2
    assert result == 2
    # The original list must not be mutated (sorted() returns a copy)
    assert data == [3, 1, 2]


def test_median_single_element():
    """Covers the odd-length branch with the minimal list size."""
    assert median([7]) == 7


def test_median_even_length():
    """Covers lines 3-4 and 7: sorting and the even-length branch."""
    data = [4, 1, 3, 2]
    result = median(data)
    # sorted([4, 1, 3, 2]) == [1, 2, 3, 4]; median is (2 + 3) / 2.0
    assert result == 2.5
    assert isinstance(result, float)
    # The original list must not be mutated
    assert data == [4, 1, 3, 2]


def test_median_even_length_with_duplicates():
    """Even-length branch where both middle values are equal."""
    result = median([5, 5, 1, 1])
    # sorted -> [1, 1, 5, 5]; median is (1 + 5) / 2.0
    assert result == 3.0
