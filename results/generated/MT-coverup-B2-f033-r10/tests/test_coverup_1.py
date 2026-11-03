# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

"""Tests for f033.sort_third covering lines 3-5 (the entire function body)."""

import pytest

from f033 import sort_third


def test_sort_third_no_change_needed():
    """A list whose every-third elements are already sorted is returned unchanged."""
    result = sort_third([1, 2, 3])
    assert result == [1, 2, 3]


def test_sort_third_sorts_every_third_element():
    """Elements at indices 0, 3, 6, ... are sorted; other positions keep their values."""
    result = sort_third([5, 6, 3, 4, 8, 9, 2])
    # indices 0, 3, 6 held 5, 4, 2 -> sorted to 2, 4, 5
    assert result == [2, 6, 3, 4, 8, 9, 5]

    result = sort_third([5, 6, 3, 4, 8, 9, 2, 1, 7])
    # indices 0, 3, 6 held 5, 4, 2 -> sorted to 2, 4, 5; rest untouched
    assert result == [2, 6, 3, 4, 8, 9, 5, 1, 7]


def test_sort_third_longer_list_multiple_groups():
    result = sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    # indices 0, 3, 6, 9 held 9, 6, 3, 0 -> sorted to 0, 3, 6, 9
    assert result == [0, 8, 7, 3, 5, 4, 6, 2, 1, 9]


def test_sort_third_empty_and_short_lists():
    assert sort_third([]) == []
    assert sort_third([42]) == [42]
    assert sort_third([3, 1]) == [3, 1]


def test_sort_third_does_not_mutate_input():
    """Line 3 copies the input, so the caller's list must stay intact."""
    original = [5, 1, 2, 3, 4]
    snapshot = list(original)
    result = sort_third(original)
    assert original == snapshot
    assert result == [3, 1, 2, 5, 4]  # indices 0, 3 held 5, 3 -> sorted to 3, 5


def test_sort_third_returns_new_list_object():
    """The returned value must be a distinct list, not the input object."""
    original = [1, 2, 3]
    result = sort_third(original)
    assert result is not original
    assert isinstance(result, list)


def test_sort_third_accepts_any_iterable():
    """Line 3 (list(l)) allows non-list iterables such as tuples."""
    result = sort_third((9, 1, 2, 8, 3))
    # indices 0, 3 held 9, 8 -> sorted to 8, 9
    assert result == [8, 1, 2, 9, 3]
    assert isinstance(result, list)
