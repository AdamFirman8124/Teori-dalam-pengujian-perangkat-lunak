# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

from f105 import by_length


def test_by_length_empty():
    assert by_length([]) == []


def test_by_length_sorted_reverse_mapping():
    assert by_length([2, 1, 3]) == ["Three", "Two", "One"]


def test_by_length_filters_out_of_range():
    assert by_length([10, 5, 1, 0, -3, 100]) == ["Five", "One"]


def test_by_length_full_range():
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
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


def test_by_length_all_invalid():
    assert by_length([0, 10, -1, 100]) == []


def test_by_length_duplicates():
    assert by_length([2, 2, 1]) == ["Two", "Two", "One"]
