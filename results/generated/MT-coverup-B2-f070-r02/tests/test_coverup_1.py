# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

import pytest

from f070 import strange_sort_list


def test_empty_list_returns_empty():
    """Covers line 3 and the immediately-false 'while lst' branch (line 4)."""
    assert strange_sort_list([]) == []


def test_single_element():
    """Covers loop body once with the min (switch=True) branch."""
    assert strange_sort_list([42]) == [42]


def test_two_elements_min_then_max():
    """Covers the max (switch=False) branch of the conditional on line 5."""
    assert strange_sort_list([3, 1]) == [1, 3]


def test_alternating_min_max():
    """Covers both min and max branches repeatedly plus normal loop exit."""
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]


def test_unsorted_with_negatives():
    assert strange_sort_list([-1, 5, 0, -3]) == [-3, 5, -1, 0]


def test_all_duplicates():
    assert strange_sort_list([5, 5, 5]) == [5, 5, 5]


def test_input_list_is_consumed():
    """The function mutates its argument via lst.remove; verify that postcondition
    using a fresh list so no state leaks between tests."""
    lst = [2, 1, 3]
    result = strange_sort_list(lst)
    assert result == [1, 3, 2]
    assert lst == []
