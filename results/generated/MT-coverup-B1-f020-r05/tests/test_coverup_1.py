# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

import pytest

from f020 import find_closest_elements


def test_first_pair_initializes_distance():
    # Covers lines 6-7 (init), 9-14 (first comparison sets distance/closest_pair)
    result = find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])
    assert result == (3.9, 4.0)


def test_improves_on_initial_distance():
    # Covers lines 16-19 (new_distance computed and improves on current distance)
    result = find_closest_elements([10.0, 1.0, 1.5])
    assert result == (1.0, 1.5)


def test_unsorted_input_returns_sorted_pair():
    # Covers line 14/19 sorted() branch when elem < elem2
    result = find_closest_elements([5.0, 4.9])
    assert result == (4.9, 5.0)


def test_negative_numbers():
    result = find_closest_elements([-1.0, -1.1, 3.0])
    assert result == (-1.1, -1.0)


def test_duplicate_values():
    result = find_closest_elements([2.0, 2.0, 5.0])
    assert result == (2.0, 2.0)


def test_skips_self_comparison():
    # idx == idx2 branch (line 11 false) must be skipped; with two equal
    # elements the only valid pair is the cross pair.
    result = find_closest_elements([1.0, 1.0])
    assert result == (1.0, 1.0)
