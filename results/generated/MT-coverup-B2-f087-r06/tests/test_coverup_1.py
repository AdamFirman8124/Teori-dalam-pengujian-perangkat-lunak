# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f087 import get_row


def test_get_row_multiple_matches_across_rows_and_columns():
    # Matches in several rows/columns; within a row, columns must come back
    # in descending order (stable sort by row after reverse sort by column).
    lst = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1],
    ]
    assert get_row(lst, 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]


def test_get_row_multiple_matches_in_single_row():
    # Both matches are in row 0; columns must be ordered descending.
    assert get_row([[1, 2, 3, 2]], 2) == [(0, 3), (0, 1)]


def test_get_row_single_match():
    assert get_row([[1, 2], [3, 4]], 4) == [(1, 1)]


def test_get_row_no_match():
    # Covers the false branch of the comprehension's `if` filter.
    assert get_row([[1, 2], [3, 4]], 5) == []


def test_get_row_empty_outer_list():
    # Covers zero iterations of the outer loop.
    assert get_row([], 1) == []


def test_get_row_empty_inner_rows():
    # Covers zero iterations of the inner loop.
    assert get_row([[], []], 1) == []
