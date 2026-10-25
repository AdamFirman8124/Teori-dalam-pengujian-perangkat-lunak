# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f087 import get_row


def test_get_row_single_match():
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = get_row(lst, 5)
    assert result == [(1, 1)]
    assert lst[result[0][0]][result[0][1]] == 5


def test_get_row_multiple_matches_ordering():
    lst = [[1, 2, 1], [1, 3, 1], [1, 1, 1]]
    result = get_row(lst, 1)
    assert result == [
        (0, 2), (0, 0),
        (1, 2), (1, 0),
        (2, 2), (2, 1), (2, 0),
    ]
    # postconditions: rows ascending, columns descending within a row
    assert [r for r, _ in result] == sorted(r for r, _ in result)
    for row in {r for r, _ in result}:
        cols = [c for r, c in result if r == row]
        assert cols == sorted(cols, reverse=True)
    assert all(lst[r][c] == 1 for r, c in result)


def test_get_row_no_match_returns_empty():
    lst = [[1, 2], [3, 4]]
    assert get_row(lst, 99) == []


def test_get_row_empty_list():
    assert get_row([], 1) == []


def test_get_row_ragged_rows():
    lst = [[5], [], [0, 5, 5]]
    result = get_row(lst, 5)
    assert result == [(0, 0), (2, 2), (2, 1)]
    assert all(lst[r][c] == 5 for r, c in result)


def test_get_row_does_not_mutate_input():
    lst = [[1, 2], [2, 1]]
    snapshot = [row[:] for row in lst]
    get_row(lst, 2)
    assert lst == snapshot
