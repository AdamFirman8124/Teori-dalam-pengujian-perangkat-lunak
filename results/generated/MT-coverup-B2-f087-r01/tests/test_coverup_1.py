# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f087 import get_row


def test_get_row_finds_coordinates_sorted():
    lst = [[1, 2, 3], [4, 1, 5], [6, 7, 1]]
    result = get_row(lst, 1)
    # occurrences: (0,0), (1,1), (2,2)
    # sorted by row asc, then column desc within same row
    assert result == [(0, 0), (1, 1), (2, 2)]


def test_get_row_multiple_in_same_row_descending_columns():
    lst = [[1, 1, 2], [2, 1, 1]]
    result = get_row(lst, 1)
    # row 0 has columns 1 and 0 -> sorted desc: (0,1), (0,0); row 1: (1,2), (1,1)
    assert result == [(0, 1), (0, 0), (1, 2), (1, 1)]


def test_get_row_no_match_returns_empty():
    lst = [[1, 2], [3, 4]]
    assert get_row(lst, 99) == []


def test_get_row_empty_list():
    assert get_row([], 1) == []


def test_get_row_ragged_rows():
    lst = [[5], [], [5, 5]]
    result = get_row(lst, 5)
    assert result == [(0, 0), (2, 1), (2, 0)]
