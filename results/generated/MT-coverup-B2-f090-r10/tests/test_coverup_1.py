# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

"""Tests for f090.next_smallest.

Covers both branches of the conditional return:
  - len(sorted(set(lst))) < 2  -> None
  - len(sorted(set(lst))) >= 2 -> second smallest distinct element
"""

from f090 import next_smallest


def test_next_smallest_basic_sorted_list():
    # Exercises the len >= 2 branch on an already-sorted list.
    assert next_smallest([1, 2, 3, 4, 5]) == 2


def test_next_smallest_unsorted_with_duplicates():
    # sorted(set(...)) must deduplicate and reorder before indexing.
    assert next_smallest([5, 1, 4, 3, 2, 1, 2]) == 2


def test_next_smallest_two_distinct_elements():
    # Smallest possible input for the len >= 2 branch.
    assert next_smallest([10, -3]) == 10


def test_next_smallest_negative_numbers():
    assert next_smallest([-5, -1, -3]) == -3


def test_next_smallest_empty_list_returns_none():
    # Exercises the len < 2 branch (empty list).
    assert next_smallest([]) is None


def test_next_smallest_single_element_returns_none():
    # Exercises the len < 2 branch (one element).
    assert next_smallest([42]) is None


def test_next_smallest_all_duplicates_returns_none():
    # set() collapses duplicates, so len < 2 even with several items.
    assert next_smallest([7, 7, 7, 7]) is None


def test_next_smallest_does_not_mutate_input():
    # The function must not modify the caller's list (no state pollution).
    original = [3, 1, 2]
    snapshot = list(original)
    result = next_smallest(original)
    assert result == 2
    assert original == snapshot
