# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_basic():
    """Numbers 1-9 are replaced by their names, in descending order."""
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


def test_by_length_all_digits_descending():
    """Every key of the dictionary is exercised."""
    result = by_length([9, 8, 7, 6, 5, 4, 3, 2, 1])
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


def test_by_length_empty_input():
    """An empty input yields an empty output (loop body never runs)."""
    assert by_length([]) == []


def test_by_length_values_outside_dictionary():
    """Values not present in the dictionary hit the except/pass branch."""
    result = by_length([10, 3, 0, -1])
    # Sorted descending: [10, 3, 0, -1]; only 3 has a mapping.
    assert result == ["Three"]
    # Postcondition: every returned element is one of the dictionary values.
    allowed = {
        "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine",
    }
    assert set(result) <= allowed


def test_by_length_does_not_mutate_input():
    """The original list must remain untouched (sorted() copies)."""
    arr = [3, 1, 2]
    snapshot = list(arr)
    by_length(arr)
    assert arr == snapshot
