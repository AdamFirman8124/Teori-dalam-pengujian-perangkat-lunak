# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_returns_second_smallest():
    # Covers line 3 (sorted(set(...))) and the len >= 2 branch of line 4.
    assert next_smallest([4, 1, 3, 2]) == 2


def test_next_smallest_deduplicates_and_sorts():
    # Duplicates are removed by set(); result is the second distinct smallest.
    assert next_smallest([5, 1, 1, 5, 3]) == 3


def test_next_smallest_with_strings():
    # Works with any orderable type.
    assert next_smallest(["banana", "apple", "cherry"]) == "banana"


def test_next_smallest_all_duplicates_returns_none():
    # Covers the len(lst) < 2 branch of line 4 (duplicates collapse to one).
    assert next_smallest([7, 7, 7]) is None


def test_next_smallest_single_element_returns_none():
    assert next_smallest([1]) is None


def test_next_smallest_empty_returns_none():
    assert next_smallest([]) is None


def test_next_smallest_two_elements():
    # Boundary case: exactly two distinct elements.
    assert next_smallest([2, 1]) == 2
    assert next_smallest([1, 2]) == 2


def test_next_smallest_unhashable_input_raises():
    # set(lst) on unhashable elements raises TypeError; documents that behavior.
    with pytest.raises(TypeError):
        next_smallest([[1, 2], [3, 4]])
