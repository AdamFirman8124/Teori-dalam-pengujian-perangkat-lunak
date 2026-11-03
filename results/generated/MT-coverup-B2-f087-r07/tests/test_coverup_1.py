# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

"""Tests for f087.get_row.

get_row is a pure function (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test only builds local data.
"""

from f087 import get_row


def test_get_row_single_match():
    # Covers the list comprehension (line 3) and the double sort (line 4).
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert get_row(lst, 5) == [(1, 1)]


def test_get_row_multiple_rows_sorted_ascending():
    # Rows appear in ascending order; within a row, columns in descending order.
    lst = [[1, 2, 3], [4, 1, 5], [1, 6, 1]]
    assert get_row(lst, 1) == [(0, 0), (1, 1), (2, 2), (2, 0)]


def test_get_row_columns_descending_within_row():
    # Exercises the inner sort with reverse=True (stable sort keeps row order).
    lst = [[2, 2, 1], [1, 2, 2]]
    assert get_row(lst, 2) == [(0, 1), (0, 0), (1, 2), (1, 1)]


def test_get_row_no_match():
    # x not present anywhere -> empty coordinate list.
    assert get_row([[1, 2], [3, 4]], 99) == []


def test_get_row_empty_inputs():
    # Empty outer list and empty inner rows must not raise IndexError.
    assert get_row([], 1) == []
    assert get_row([[], []], 1) == []


def test_get_row_jagged_rows():
    # Rows of different lengths are handled by range(len(lst[i])).
    lst = [[1], [1, 1], []]
    assert get_row(lst, 1) == [(0, 0), (1, 1), (1, 0)]


def test_get_row_works_with_strings():
    # x is compared with ==, so non-numeric elements work too.
    lst = [["a", "b"], ["b", "a"]]
    assert get_row(lst, "b") == [(0, 1), (1, 0)]
