# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f033 import sort_third


def test_sort_third_basic():
    """Elements at indices 0, 3, 6, ... are sorted; others stay in place."""
    result = sort_third([5, 6, 3, 4, 1, 2, 0])
    assert result == [0, 6, 3, 4, 1, 2, 5]


def test_sort_third_returns_new_list_and_does_not_mutate_input():
    """Line 3 copies the input: the original list must be untouched."""
    original = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = sort_third(original)
    # indices 0, 3, 6 hold 9, 6, 3 -> sorted to 3, 6, 9
    assert result == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert result is not original
    assert original == [9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_sort_third_empty_list():
    assert sort_third([]) == []


def test_sort_third_shorter_than_step():
    # Only index 0 belongs to l[::3]; nothing to reorder.
    assert sort_third([2, 1, 0]) == [2, 1, 0]
    assert sort_third([7]) == [7]


def test_sort_third_duplicates_and_negatives():
    # indices 0, 3, 6 hold 9, 1, -5 -> sorted to -5, 1, 9
    result = sort_third([9, 9, 9, 1, 1, 1, -5, 5, 5])
    assert result == [-5, 9, 9, 1, 1, 1, 9, 5, 5]


def test_sort_third_accepts_any_iterable():
    """Line 3 wraps the argument with list(), so tuples work too."""
    result = sort_third((3, 2, 1, 0))
    assert result == [0, 2, 1, 3]
    assert isinstance(result, list)


def test_sort_third_longer_list():
    # indices 0, 3, 6, 9 hold 10, 7, 4, 1 -> sorted to 1, 4, 7, 10
    result = sort_third([10, 2, 3, 7, 5, 6, 4, 8, 9, 1])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # non-multiple-of-3 positions are unchanged
    assert result[1::3] == [2, 5, 8]
    assert result[2::3] == [3, 6, 9]
