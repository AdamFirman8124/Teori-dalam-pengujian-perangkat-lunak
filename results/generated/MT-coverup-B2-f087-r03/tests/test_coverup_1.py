# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f087 import get_row


def test_get_row_finds_and_sorts_matching_coordinates():
    matrix = [
        [7, 1, 7, 2],
        [],
        [7, 7, 3],
        [4, 7],
    ]
    original = [row.copy() for row in matrix]

    assert get_row(matrix, 7) == [(0, 2), (0, 0), (2, 1), (2, 0), (3, 1)]
    assert matrix == original


def test_get_row_returns_empty_list_when_value_is_absent():
    matrix = [[1, 2], [3], []]

    assert get_row(matrix, 99) == []
