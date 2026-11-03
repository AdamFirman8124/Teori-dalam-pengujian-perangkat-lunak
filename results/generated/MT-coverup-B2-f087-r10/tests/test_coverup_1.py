# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f087 import get_row


def test_get_row_multiple_rows_with_duplicates():
    """Matches occurrences across rows; rows ascending, columns descending within a row."""
    lst = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1],
    ]
    assert get_row(lst, 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]


def test_get_row_empty_list():
    """An empty outer list yields no coordinates."""
    assert get_row([], 1) == []


def test_get_row_ragged_rows():
    """Handles ragged input, including empty inner rows."""
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    assert get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]


def test_get_row_not_found():
    """A missing element yields an empty result."""
    assert get_row([[1, 2], [3, 4]], 5) == []


def test_get_row_same_row_multiple_hits():
    """Within a single row, columns are reported in descending order."""
    assert get_row([[7, 7, 7]], 7) == [(0, 2), (0, 1), (0, 0)]


def test_get_row_does_not_mutate_input():
    """The function must not modify its input (no state pollution)."""
    lst = [[1, 2], [2, 1]]
    snapshot = [row[:] for row in lst]
    result = get_row(lst, 2)
    assert lst == snapshot
    assert result == [(0, 1), (1, 0)]
