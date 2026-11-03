# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f087 import get_row


def test_get_row_single_match():
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = get_row(lst, 5)
    assert result == [(1, 1)]
    # the input list must not be mutated by the function
    assert lst == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_get_row_multiple_matches_row_ascending_col_descending():
    lst = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]]
    result = get_row(lst, 1)
    # rows ascending; within a row, columns descending (stable sort)
    assert result == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]


def test_get_row_ragged_rows():
    lst = [[], [1], [1, 2, 1]]
    result = get_row(lst, 1)
    assert result == [(1, 0), (2, 2), (2, 0)]


def test_get_row_no_match_and_empty_inputs():
    assert get_row([[1, 2], [3, 4]], 99) == []
    assert get_row([], 1) == []
    assert get_row([[], []], 1) == []
