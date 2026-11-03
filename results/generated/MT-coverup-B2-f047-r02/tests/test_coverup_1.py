# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


def test_median_odd_length_returns_middle_element():
    # Covers line 3 (sorted) and line 5 (odd-length branch)
    assert median([3, 1, 2]) == 2
    assert median([5]) == 5
    assert median([4, 1, 3, 2, 5]) == 3
    assert median([9, 7, 5, 3, 1]) == 5


def test_median_even_length_returns_average_of_middle_two():
    # Covers line 3 (sorted) and line 7 (even-length branch)
    assert median([1, 2, 3, 4]) == 2.5
    assert median([3, 1]) == 2.0
    assert median([10, 20]) == 15.0
    assert median([4, 2, 8, 6]) == 5.0
    assert median([1.5, 2.5]) == 2.0


def test_median_does_not_mutate_input_list():
    # 'l = sorted(l)' rebinds the local name only; caller's list must stay intact
    data = [3, 1, 2]
    result = median(data)
    assert result == 2
    assert data == [3, 1, 2]


def test_median_handles_duplicates_and_negatives():
    assert median([2, 2, 2, 2]) == 2.0
    assert median([-5, -1, -3]) == -3
    assert median([-1, 1]) == 0.0
