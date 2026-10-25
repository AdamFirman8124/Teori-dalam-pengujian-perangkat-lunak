# file: project/f087/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f087 import get_row


def test_get_row_returns_matching_coordinates_sorted_by_row_and_reverse_column():
    matrix = [
        ["x", "a", "x"],
        ["x", "x", "b"],
        ["c", "x", "x"],
    ]

    result = get_row(matrix, "x")

    assert result == [
        (0, 2),
        (0, 0),
        (1, 1),
        (1, 0),
        (2, 2),
        (2, 1),
    ]
    assert matrix == [
        ["x", "a", "x"],
        ["x", "x", "b"],
        ["c", "x", "x"],
    ]
