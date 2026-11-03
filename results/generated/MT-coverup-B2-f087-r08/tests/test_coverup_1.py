# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f087 import get_row


def test_get_row_single_occurrence():
    """A single match yields exactly one (row, col) coordinate."""
    assert get_row([[1, 2, 3], [4, 5, 6]], 5) == [(1, 1)]


def test_get_row_multiple_occurrences_row_ascending_col_descending():
    """Coordinates are sorted by row ascending, and within a row by column descending."""
    lst = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1],
    ]
    assert get_row(lst, 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]


def test_get_row_same_row_columns_descending():
    """All matches in one row come back with columns in descending order."""
    assert get_row([[2, 2, 2]], 2) == [(0, 2), (0, 1), (0, 0)]


def test_get_row_empty_list():
    """An empty outer list yields no coordinates."""
    assert get_row([], 1) == []


def test_get_row_empty_rows():
    """Empty inner rows are skipped without error."""
    assert get_row([[], [1], []], 1) == [(1, 0)]


def test_get_row_not_found():
    """A value absent from the grid yields an empty result."""
    assert get_row([[1, 2], [3, 4]], 7) == []


def test_get_row_does_not_mutate_input():
    """The function is pure: the input list is left unchanged."""
    lst = [[1, 2], [2, 1]]
    snapshot = [row[:] for row in lst]
    result = get_row(lst, 2)
    assert result == [(0, 1), (1, 0)]
    assert lst == snapshot
