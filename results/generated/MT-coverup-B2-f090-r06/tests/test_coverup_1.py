# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_empty_list_returns_none():
    # Covers the len(lst) < 2 True branch (and executes lines 3-4)
    assert next_smallest([]) is None


def test_next_smallest_single_element_returns_none():
    assert next_smallest([42]) is None


def test_next_smallest_all_duplicates_returns_none():
    # set() collapses to a single unique value -> len < 2 -> None
    assert next_smallest([7, 7, 7, 7]) is None


def test_next_smallest_two_distinct_elements():
    # Covers the len(lst) >= 2 False branch
    assert next_smallest([3, 1]) == 3


def test_next_smallest_unsorted_with_duplicates():
    # sorted(set(...)) must dedupe and order: [1, 2, 3, 4] -> second is 2
    assert next_smallest([4, 1, 3, 2, 2, 4]) == 2


def test_next_smallest_duplicate_of_smallest_value():
    # Duplicates of the minimum still leave two distinct values
    assert next_smallest([1, 1, 2]) == 2


def test_next_smallest_negative_numbers():
    assert next_smallest([-5, -1, -10, -1]) == -5


def test_next_smallest_mixed_int_float_duplicates():
    # 2 and 2.0 are equal members of the set, so they collapse to one value
    assert next_smallest([2, 2.0, 1]) == 2


def test_next_smallest_does_not_mutate_input():
    # sorted() and set() build new objects, so the caller's list is untouched
    original = [4, 1, 3]
    snapshot = list(original)
    result = next_smallest(original)
    assert result == 3
    assert original == snapshot
