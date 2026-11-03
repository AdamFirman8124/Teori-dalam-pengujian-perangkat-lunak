# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


def test_median_odd_length():
    """Covers lines 3-5: sorting and the odd-length branch."""
    result = median([3, 1, 2])
    assert result == 2
    # Verify sorting is applied: input order differs from sorted order.
    assert median([5, 1, 4, 2, 3]) == 3
    # Single-element list is also odd-length.
    assert median([7]) == 7


def test_median_even_length():
    """Covers lines 3-4 and 6-7: sorting and the even-length branch."""
    result = median([4, 1, 3, 2])
    assert result == 2.5
    # Verify sorting is applied before selecting the middle pair.
    assert median([10, 2]) == 6.0
    # Result must be a float due to the / 2.0 division.
    assert isinstance(median([1, 2, 3, 4]), float)


def test_median_does_not_mutate_input():
    """Ensure the function does not pollute caller state (uses sorted copy)."""
    data = [3, 1, 2]
    original = list(data)
    median(data)
    assert data == original
