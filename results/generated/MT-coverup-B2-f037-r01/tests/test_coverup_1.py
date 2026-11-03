# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


def test_sort_even_equal_lengths():
    """Covers lines 3-8: slicing, sorting, zip loop; line 9 branch False."""
    original = [5, 2, 3, 1, 4, 6]
    result = sort_even(original)
    # evens = [5, 3, 4] -> sorted [3, 4, 5]; odds = [2, 1, 6]
    assert result == [3, 2, 4, 1, 5, 6]
    # input list must not be mutated (evens is a slice copy)
    assert original == [5, 2, 3, 1, 4, 6]


def test_sort_even_extra_even_element():
    """Covers line 9 branch True and line 10: evens longer than odds."""
    result = sort_even([5, 1, 3, 2, 4])
    # evens = [5, 3, 4] -> sorted [3, 4, 5]; odds = [1, 2]
    # ans = [3, 1, 4, 2] then append evens[-1] == 5
    assert result == [3, 1, 4, 2, 5]


def test_sort_even_empty_list():
    """Covers lines 3-4, 6 with empty slices; loop and branch skipped."""
    assert sort_even([]) == []


def test_sort_even_single_element():
    """Covers branch True with a single even-index element."""
    assert sort_even([2]) == [2]


def test_sort_even_two_elements():
    """Covers branch False with equal-length slices."""
    assert sort_even([3, 1]) == [3, 1]


def test_sort_even_strings():
    """Covers sorting of non-numeric comparable elements."""
    result = sort_even(["d", "b", "a", "c"])
    # evens = ["d", "a"] -> sorted ["a", "d"]; odds = ["b", "c"]
    assert result == ["a", "b", "d", "c"]
