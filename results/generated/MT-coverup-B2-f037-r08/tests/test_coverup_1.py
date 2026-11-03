# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


def test_sort_even_even_length_swaps():
    """Even-length list: loop runs, and len(evens) == len(odds) branch is False."""
    original = [5, 6, 3, 4]
    result = sort_even(original)
    # evens = [5, 3] -> sorted [3, 5]; odds = [6, 4]
    assert result == [3, 6, 5, 4]
    # input list must not be mutated (evens is a slice copy)
    assert original == [5, 6, 3, 4]


def test_sort_even_odd_length_appends_last_even():
    """Odd-length list: loop runs, and len(evens) > len(odds) branch is True."""
    result = sort_even([1, 2, 3])
    # evens = [1, 3] -> sorted [1, 3]; odds = [2]; leftover even 3 appended
    assert result == [1, 2, 3]


def test_sort_even_odd_length_unsorted_evens():
    """Odd-length list where sorting actually reorders the even-indexed values."""
    original = [4, 1, 3, 2, 2, 5]
    result = sort_even(original)
    # evens = [4, 3, 2] -> sorted [2, 3, 4]; odds = [1, 2, 5]; lengths equal
    assert result == [2, 1, 3, 2, 4, 5]
    assert original == [4, 1, 3, 2, 2, 5]


def test_sort_even_empty_list():
    """Empty list: slices are empty, loop body never runs, branch is False."""
    assert sort_even([]) == []


def test_sort_even_single_element():
    """Single element: no pairs, leftover even element appended."""
    assert sort_even([7]) == [7]


def test_sort_even_two_elements():
    """Two elements: exactly one pair, no leftover."""
    result = sort_even([2, 1])
    # evens = [2] -> sorted [2]; odds = [1]
    assert result == [2, 1]
