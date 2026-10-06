# file: script_87.py:1-22
# asked: {"lines": [21, 22], "branches": []}
# gained: {"lines": [21, 22], "branches": []}

import pytest
from script_87 import get_row


def test_get_row_basic():
    """Test basic functionality with the provided example."""
    result = get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1)
    assert result == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]


def test_get_row_empty_list():
    """Test with an empty list."""
    result = get_row([], 1)
    assert result == []


def test_get_row_mixed_empty_rows():
    """Test with mixed empty and non-empty rows."""
    result = get_row([[], [1], [1, 2, 3]], 3)
    assert result == [(2, 2)]


def test_get_row_single_match():
    """Test with a single matching element."""
    result = get_row([[5, 6, 7]], 6)
    assert result == [(0, 1)]


def test_get_row_no_match():
    """Test when element is not found."""
    result = get_row([[1, 2, 3], [4, 5, 6]], 9)
    assert result == []


def test_get_row_multiple_in_same_row():
    """Test multiple matches in the same row, ensuring descending column order."""
    result = get_row([[7, 3, 7, 3, 7]], 7)
    assert result == [(0, 4), (0, 2), (0, 0)]


def test_get_row_multiple_rows_single_column():
    """Test multiple matches across rows."""
    result = get_row([[5], [3], [5], [5]], 5)
    assert result == [(0, 0), (2, 0), (3, 0)]


def test_get_row_complex_sorting():
    """Test complex case with multiple rows and columns."""
    result = get_row([
        [9, 8, 9],
        [9],
        [8, 9, 9, 9]
    ], 9)
    assert result == [(0, 2), (0, 0), (1, 0), (2, 3), (2, 2), (2, 1)]


def test_get_row_negative_numbers():
    """Test with negative numbers."""
    result = get_row([[-1, 2, -1], [3, -1]], -1)
    assert result == [(0, 2), (0, 0), (1, 1)]


def test_get_row_zero():
    """Test searching for zero."""
    result = get_row([[0, 1, 0], [2], [0, 0, 0]], 0)
    assert result == [(0, 2), (0, 0), (2, 2), (2, 1), (2, 0)]
