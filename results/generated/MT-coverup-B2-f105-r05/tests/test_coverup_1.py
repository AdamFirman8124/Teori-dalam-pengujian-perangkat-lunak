# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_basic_mapping():
    """Covers lines 3-14, 16-18, 21: valid values map to their word names."""
    result = by_length([2, 1, 3])
    assert result == ["Three", "Two", "One"]


def test_by_length_reverse_sorted_order():
    """Covers line 14: input is sorted in descending order before mapping."""
    result = by_length([1, 3, 2, 5, 4])
    assert result == ["Five", "Four", "Three", "Two", "One"]


def test_by_length_skips_out_of_range_values():
    """Covers the except branch (lines 19-20): values not in dic are skipped."""
    result = by_length([10, 2, -1, 7])
    assert result == ["Seven", "Two"]


def test_by_length_all_out_of_range():
    """Every element raises KeyError inside the try, so result is empty."""
    result = by_length([0, 10, -5, 100])
    assert result == []


def test_by_length_empty_input():
    """Empty input: loop body never runs, returns empty list."""
    result = by_length([])
    assert result == []


def test_by_length_duplicates_preserved():
    """Duplicates are each mapped, keeping multiplicity and order."""
    result = by_length([3, 3, 1])
    assert result == ["Three", "Three", "One"]


def test_by_length_full_range():
    """All keys 1..9 map correctly when given in ascending order."""
    result = by_length(list(range(1, 10)))
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


def test_by_length_does_not_mutate_input():
    """sorted() must not mutate the caller's list (no state pollution)."""
    arr = [3, 1, 2]
    snapshot = list(arr)
    result = by_length(arr)
    assert arr == snapshot
    assert result == ["Three", "Two", "One"]


def test_by_length_mixed_valid_and_invalid():
    """Both try-success and except branches execute within one call."""
    result = by_length([9, 0, 8, 11, 1])
    assert result == ["Nine", "Eight", "One"]
