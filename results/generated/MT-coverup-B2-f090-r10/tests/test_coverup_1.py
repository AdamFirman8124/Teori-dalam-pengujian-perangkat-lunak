# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_returns_second_smallest():
    assert next_smallest([4, 1, 3, 2]) == 2


def test_next_smallest_deduplicates_before_sorting():
    # duplicates are removed by set(), so second smallest is 2, not 1
    assert next_smallest([1, 1, 2, 3]) == 2


def test_next_smallest_returns_none_for_single_element():
    assert next_smallest([5]) is None


def test_next_smallest_returns_none_for_empty_list():
    assert next_smallest([]) is None


def test_next_smallest_returns_none_when_all_duplicates():
    # set() collapses to one element -> len < 2 -> None
    assert next_smallest([7, 7, 7]) is None


def test_next_smallest_does_not_mutate_input():
    original = [3, 1, 2]
    snapshot = list(original)
    next_smallest(original)
    assert original == snapshot
