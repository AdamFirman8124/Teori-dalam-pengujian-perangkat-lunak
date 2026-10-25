# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_sorts_descending_and_maps_to_words():
    arr = [2, 1, 3]
    result = by_length(arr)
    assert result == ["Three", "Two", "One"]
    assert arr == [2, 1, 3], "input list must not be mutated"


def test_by_length_empty_list_returns_empty_list():
    assert by_length([]) == []


def test_by_length_ignores_out_of_range_values():
    assert by_length([0, 10, -1, 5]) == ["Five"]


def test_by_length_keeps_duplicates():
    assert by_length([1, 1, 9]) == ["Nine", "One", "One"]


def test_by_length_ignores_unmapped_hashable_keys():
    # all strings: sorting succeeds, every lookup raises KeyError -> swallowed
    assert by_length(["2", "1"]) == []


def test_by_length_all_nine_values():
    expected = [
        "Nine", "Eight", "Seven", "Six", "Five",
        "Four", "Three", "Two", "One",
    ]
    assert by_length(list(range(1, 10))) == expected
