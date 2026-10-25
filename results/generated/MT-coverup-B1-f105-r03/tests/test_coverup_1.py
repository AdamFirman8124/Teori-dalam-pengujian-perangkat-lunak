# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

from f105 import by_length


def test_by_length_converts_valid_values_and_ignores_invalid_values():
    values = [0, 1, 3, 5, 7, 9, 10, 2, 4, 6, 8]

    result = by_length(values)

    assert result == [
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two",
        "One",
    ]
    assert values == [0, 1, 3, 5, 7, 9, 10, 2, 4, 6, 8]


def test_by_length_with_empty_input():
    assert by_length([]) == []
