# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


def test_sort_even_even_length_interleaves_sorted_evens():
    """Even-length input: covers lines 3-8 and the False branch of line 9."""
    original = [4, 1, 3, 2]
    result = sort_even(original)
    # evens=[4,3] -> sorted [3,4]; odds=[1,2]; zipped pairs appended
    assert result == [3, 1, 4, 2]
    # the input list must not have been mutated (slicing makes copies)
    assert original == [4, 1, 3, 2]


def test_sort_even_odd_length_appends_last_even():
    """Odd-length input: covers lines 3-8 plus True branch of lines 9-10."""
    result = sort_even([5, 1, 3, 2, 4])
    # evens=[5,3,4] -> sorted [3,4,5]; odds=[1,2];
    # pairs (3,1),(4,2) then leftover even 5 appended
    assert result == [3, 1, 4, 2, 5]


def test_sort_even_empty_list():
    """Empty input: covers lines 3-7 with empty loops and False branch of line 9."""
    assert sort_even([]) == []


def test_sort_even_single_element():
    """Single element: only an even index exists, so line 10 appends it."""
    assert sort_even([7]) == [7]


def test_sort_even_two_elements_no_extra_append():
    """Two elements: equal lengths, so nothing extra is appended."""
    assert sort_even([2, 1]) == [2, 1]


def test_sort_even_already_sorted_stays_valid():
    """Already-sorted evens still interleave correctly with odds."""
    result = sort_even([1, 9, 2, 8, 3, 7, 4])
    # evens=[1,2,3,4] (already sorted); odds=[9,8,7];
    # pairs (1,9),(2,8),(3,7) then leftover 4 appended
    assert result == [1, 9, 2, 8, 3, 7, 4]
