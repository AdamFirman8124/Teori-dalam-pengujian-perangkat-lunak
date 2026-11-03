# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


def test_median_odd_length_returns_middle_element():
    """Covers lines 3-5: the sorted() call and the odd-length branch."""
    assert median([3, 1, 2]) == 2
    assert median([5, 1, 4, 2, 3]) == 3
    assert median([7]) == 7


def test_median_even_length_returns_average_of_middle_elements():
    """Covers line 7: the even-length branch."""
    assert median([4, 1, 3, 2]) == 2.5
    assert median([1, 2]) == 1.5


def test_median_sorts_input_without_mutating_original():
    """Covers line 3 (l = sorted(l)) and verifies the caller's list is untouched."""
    data = [9, 1, 8, 2]
    result = median(data)
    assert data == [9, 1, 8, 2]  # original list not mutated by sorted()
    assert result == 5.0         # sorted -> [1, 2, 8, 9]; (2 + 8) / 2 == 5.0
