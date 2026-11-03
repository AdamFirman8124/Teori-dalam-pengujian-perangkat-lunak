# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

import pytest

from f070 import strange_sort_list


def test_empty_list_returns_empty():
    """Covers line 3, the False branch of `while lst:` (line 4) and line 8."""
    result = strange_sort_list([])
    assert result == []


def test_single_element():
    """Covers one True iteration of the loop, the `min` branch, then loop exit."""
    result = strange_sort_list([7])
    assert result == [7]


def test_even_length_alternates_min_and_max():
    """Covers both the `min` (switch True) and `max` (switch False) branches
    across multiple loop iterations."""
    result = strange_sort_list([1, 2, 3, 4])
    assert result == [1, 4, 2, 3]


def test_odd_length_with_duplicates():
    """Duplicates exercise `list.remove` removing the first occurrence;
    odd length ends on a `min` pick."""
    result = strange_sort_list([5, 5, 1, 3, 2])
    assert result == [1, 5, 2, 5, 3]


def test_negative_numbers():
    """min/max must handle negative values correctly."""
    result = strange_sort_list([3, -1, 2])
    assert result == [-1, 3, 2]


def test_input_list_is_consumed_in_place():
    """The implementation mutates its argument via lst.remove; verify that
    postcondition using a private copy so no shared state is polluted."""
    original = [4, 1, 3]
    result = strange_sort_list(original)
    assert result == [1, 4, 3]
    assert original == []  # all elements were removed from the input list
