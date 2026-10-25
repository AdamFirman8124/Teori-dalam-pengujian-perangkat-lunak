# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

from f105 import by_length


def test_by_length_converts_and_sorts_valid_numbers():
    assert by_length([1, 9, 3, 5, 2, 8, 4, 7, 6]) == [
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


def test_by_length_ignores_unmapped_numbers_and_handles_empty_input():
    assert by_length([10, 3, 0, -1, 1]) == ["Three", "One"]
    assert by_length([]) == []
