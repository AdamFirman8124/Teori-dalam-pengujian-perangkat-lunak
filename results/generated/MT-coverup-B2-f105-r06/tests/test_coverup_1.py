# file: project/f105/__init__.py:1-21
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[16, 17], [16, 21]]}

import pytest

from f105 import by_length


def test_by_length_maps_and_sorts_descending():
    """Covers lines 3-18 and 21: dict build, sort, loop, successful append, return."""
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


def test_by_length_empty_list():
    """Covers the loop-not-taken branch (for loop over empty sorted_arr)."""
    assert by_length([]) == []


def test_by_length_skips_values_not_in_dict():
    """Covers the except/pass branch (lines 19-20) via KeyError for values outside 1..9."""
    result = by_length([1, -1, 55, 9, 10, 3])
    assert result == ["Nine", "Three", "One"]


def test_by_length_skips_non_integer_values():
    """Covers the except/pass branch (lines 19-20) via KeyError for sortable but unmapped values (floats)."""
    result = by_length([2, 2.5, 7, 9.9])
    assert result == ["Seven", "Two"]


def test_by_length_unsortable_input_raises():
    """Documents that mixed unorderable types fail at the sorted() call, before the loop."""
    with pytest.raises(TypeError):
        by_length([2, [1, 2], 7])


def test_by_length_does_not_mutate_input():
    """Verifies the function is side-effect free on its argument."""
    arr = [3, 1, 2]
    result = by_length(arr)
    assert arr == [3, 1, 2]
    assert result == ["Three", "Two", "One"]


def test_by_length_all_nine_digits():
    """Full mapping check for every key in the dictionary."""
    result = by_length([1, 2, 3, 4, 5, 6, 7, 8, 9])
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
