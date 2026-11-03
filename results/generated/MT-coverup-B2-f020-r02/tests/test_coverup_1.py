# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

import pytest

from f020 import find_closest_elements


def test_find_closest_elements_covers_initial_pair_and_updates():
    # Covers: lines 6-7 (init), 9-14 (first distinct pair sets distance/pair),
    # 16-17 (comparison that does NOT update), 18-19 (strictly smaller
    # distance triggers update).
    # Trace for [10.0, 1.0, 2.0]:
    #   (10,1) -> distance 9.0, pair (1.0, 10.0)
    #   (10,2) -> 8.0 < 9.0  -> pair (2.0, 10.0)
    #   (1,2)  -> 1.0 < 8.0  -> pair (1.0, 2.0)  [update branch taken]
    #   remaining comparisons are not strictly smaller -> no more updates
    numbers = [10.0, 1.0, 2.0]
    result = find_closest_elements(numbers)
    # closest pair is 1.0 and 2.0 (distance 1.0)
    assert result == (1.0, 2.0)
    assert isinstance(result, tuple)


def test_find_closest_elements_no_update_on_equal_distance():
    # Covers the else-branch (lines 16-17) where new_distance >= distance,
    # so no update happens for those pairs; the closest pair found earlier
    # is kept.
    numbers = [5.0, 1.0, 2.0, 10.0]
    result = find_closest_elements(numbers)
    assert result == (1.0, 2.0)


def test_find_closest_elements_skips_same_index():
    # Ensures the idx != idx2 check (line 11) is exercised and
    # self-comparisons do not produce distance 0
    numbers = [7.0, 4.0]
    result = find_closest_elements(numbers)
    assert result == (4.0, 7.0)


def test_find_closest_elements_sorted_pair_output():
    # Verifies tuple(sorted([...])) behavior: result is ascending order
    numbers = [10.0, 9.5, 0.1]
    result = find_closest_elements(numbers)
    assert result == (9.5, 10.0)
    assert result[0] <= result[1]


def test_find_closest_elements_duplicates():
    # Duplicate values: distance 0 is allowed once a pair has been found;
    # covers update branch with smaller (zero) distance
    numbers = [2.0, 3.0, 2.0]
    result = find_closest_elements(numbers)
    assert result == (2.0, 2.0)


def test_find_closest_elements_returns_none_for_fewer_than_two():
    # Lines 6-7 and 21 executed but loop body never taken -> None returned
    assert find_closest_elements([]) is None
    assert find_closest_elements([1.5]) is None
