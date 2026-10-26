# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f087 import get_row


def test_get_row_empty():
    assert get_row([], 1) == []


def test_get_row_no_match():
    assert get_row([[1, 2], [3, 4]], 5) == []


def test_get_row_single_match():
    assert get_row([[1, 2, 3], [4, 5, 6]], 5) == [(1, 1)]


def test_get_row_same_row_col_descending():
    # multiple matches in same row must be ordered by column descending
    assert get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]


def test_get_row_multiple_rows_row_ascending():
    # rows ascending, and within each row columns descending
    lst = [[1, 2, 1], [1, 1, 2]]
    assert get_row(lst, 1) == [(0, 2), (0, 0), (1, 1), (1, 0)]


def test_get_row_ragged_and_mixed():
    lst = [[2, 1, 2], [1], [3, 1, 1]]
    assert get_row(lst, 1) == [(0, 1), (1, 0), (2, 2), (2, 1)]
