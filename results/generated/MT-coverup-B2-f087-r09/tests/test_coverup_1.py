# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f087 import get_row


def test_get_row_single_match():
    # One occurrence: coordinate (0, 0) should be found and returned.
    lst = [[1, 2], [3, 1]]
    result = get_row(lst, 1)
    assert result == [(0, 0), (1, 1)]
    # Postcondition: every returned coordinate points at a cell equal to x.
    assert all(lst[i][j] == 1 for i, j in result)


def test_get_row_multiple_matches_same_row_descending_columns():
    # Within the same row, columns must appear in descending order
    # (first sort by column reverse=True, then stable sort by row).
    lst = [[1, 1], [1, 1]]
    result = get_row(lst, 1)
    assert result == [(0, 1), (0, 0), (1, 1), (1, 0)]
    assert all(lst[i][j] == 1 for i, j in result)


def test_get_row_no_match():
    # No occurrence of x anywhere: result must be empty.
    lst = [[1, 2], [3, 4]]
    assert get_row(lst, 5) == []


def test_get_row_empty_list():
    # Empty outer list: no coordinates at all.
    assert get_row([], 1) == []


def test_get_row_ragged_rows():
    # Ragged (non-rectangular) input, including an empty inner row.
    lst = [[1], [2, 1, 1], []]
    result = get_row(lst, 1)
    assert result == [(0, 0), (1, 2), (1, 1)]
    assert all(lst[i][j] == 1 for i, j in result)
