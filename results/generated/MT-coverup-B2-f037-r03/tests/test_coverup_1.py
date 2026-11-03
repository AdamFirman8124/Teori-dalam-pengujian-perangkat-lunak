# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


def test_sort_even_even_length_covers_loop_and_false_branch():
    """Even-length input: exercises the zip loop body (lines 7-8) and the
    False branch of the length check (line 9), with no trailing append."""
    original = [5, 6, 3, 4]
    result = sort_even(original)
    # evens = [5, 3] -> sorted [3, 5]; odds = [6, 4]
    assert result == [3, 6, 5, 4]
    # The input list must not be mutated (evens is a slice copy).
    assert original == [5, 6, 3, 4]


def test_sort_even_odd_length_covers_append_branch():
    """Odd-length input: exercises the True branch of the length check and
    line 10 (appending the leftover largest even-index element)."""
    original = [9, 1, 7, 2, 5]
    result = sort_even(original)
    # evens = [9, 7, 5] -> sorted [5, 7, 9]; odds = [1, 2]
    # zip yields (5,1), (7,2); leftover evens[-1] == 9 is appended.
    assert result == [5, 1, 7, 2, 9]
    assert original == [9, 1, 7, 2, 5]


def test_sort_even_single_element():
    """Single element: loop body not executed (odds empty), but the append
    branch (line 10) fires."""
    assert sort_even([2]) == [2]


def test_sort_even_empty_list():
    """Empty input: covers lines 3-6 and 11 with both the loop and the
    length-check branch not taken."""
    assert sort_even([]) == []


def test_sort_even_already_sorted_and_negative_numbers():
    """Sanity check with negatives; even-length so no append occurs."""
    original = [-3, 8, -1, 0, 2, -5]
    result = sort_even(original)
    # evens = [-3, -1, 2] (already sorted); odds = [8, 0, -5]
    assert result == [-3, 8, -1, 0, 2, -5]
    assert original == [-3, 8, -1, 0, 2, -5]
