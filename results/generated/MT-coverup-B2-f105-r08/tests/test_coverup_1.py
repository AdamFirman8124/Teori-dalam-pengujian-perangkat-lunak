# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_sorts_descending_and_maps_names():
    """Covers lines 3-18, 21: dict construction, sorting, loop, successful append."""
    result = by_length([2, 1, 1, 4, 5, 8, 2, 3])
    assert result == [
        "Eight",
        "Five",
        "Four",
        "Three",
        "Two",
        "Two",
        "One",
        "One",
    ]


def test_by_length_empty_list_returns_empty_list():
    """Covers lines 3-16, 21 with an empty loop body."""
    assert by_length([]) == []


def test_by_length_skips_values_not_in_dictionary():
    """Covers lines 19-20: the bare except/pass branch for unknown keys."""
    # 0, 10, negatives and large numbers are not keys of the dictionary,
    # so dic[var] raises KeyError which the bare except swallows.
    assert by_length([1, -1, 55]) == ["One"]
    assert by_length([0, 10, 100]) == []


def test_by_length_mixed_known_and_unknown_values():
    """Covers both the try/append and except/pass branches in one run."""
    assert by_length([10, 3, 0, 9, 1]) == ["Nine", "Three", "One"]


def test_by_length_single_element():
    assert by_length([9]) == ["Nine"]


def test_by_length_does_not_mutate_input():
    """Postcondition: the input list is left unchanged (sorted() copies)."""
    arr = [3, 1, 2]
    result = by_length(arr)
    assert result == ["Three", "Two", "One"]
    assert arr == [3, 1, 2]
