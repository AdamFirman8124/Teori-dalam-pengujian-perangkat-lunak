# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f087 import get_row


def test_get_row_empty_outer():
    assert get_row([], 1) == []


def test_get_row_empty_inner_row():
    assert get_row([[]], 1) == []
    assert get_row([[], []], 5) == []


def test_get_row_no_match():
    assert get_row([[1, 2], [3, 4]], 5) == []
    assert get_row([[1, 2, 3], [4, 5, 6]], 0) == []


def test_get_row_single_match():
    assert get_row([[1, 2, 3]], 2) == [(0, 1)]
    assert get_row([[1, 2], [3, 4]], 4) == [(1, 1)]


def test_get_row_sort_rows_asc_cols_desc():
    lst = [[1, 1, 1], [1, 1, 1]]
    assert get_row(lst, 1) == [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)]
    lst2 = [[1, 2, 1], [1, 1, 1]]
    assert get_row(lst2, 1) == [(0, 2), (0, 0), (1, 2), (1, 1), (1, 0)]


def test_get_row_ragged_and_mixed():
    assert get_row([[], [1], [1, 2, 1]], 1) == [(1, 0), (2, 2), (2, 0)]
    assert get_row([[1, 2, 3], [1, 2, 3]], 2) == [(0, 1), (1, 1)]
    assert get_row([[5, 5, 1, 5], [1]], 1) == [(0, 2), (1, 0)]
