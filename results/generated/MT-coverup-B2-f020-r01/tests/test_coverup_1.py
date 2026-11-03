# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

import pytest

from f020 import find_closest_elements


def test_find_closest_elements_all_branches():
    """Exercise every line and branch: the distance-is-None initialization
    path (lines 12-14), the new_distance-not-less path (line 17 false),
    and the new_distance-less path (lines 17-19)."""
    result = find_closest_elements([1.0, 2.0, 3.5, 4.0])
    # Closest pair is (3.5, 4.0) with distance 0.5
    assert result == (3.5, 4.0)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] <= result[1]  # pair must be sorted


def test_find_closest_elements_two_elements_sorted_output():
    """Two elements: the first (and only) comparison takes the
    distance-is-None branch; result is sorted even if input is not."""
    result = find_closest_elements([10.0, 3.0])
    assert result == (3.0, 10.0)
    assert result[0] <= result[1]


def test_find_closest_elements_unsorted_candidates():
    """A later (unsorted) pair becomes the closest, exercising the
    new_distance < distance update branch with a sorted tuple result."""
    result = find_closest_elements([5.0, 1.0, 2.1, 9.0])
    # 1.0 and 2.1 are closest (distance 1.1)
    assert result == (1.0, 2.1)


def test_find_closest_elements_equal_distances_keeps_first_pair():
    """When a later pair's distance equals (does not beat) the current
    minimum, the first-found pair is kept."""
    result = find_closest_elements([1.0, 2.0, 3.0])
    # (1.0, 2.0) found first with distance 1.0; (2.0, 3.0) also has
    # distance 1.0 but is not strictly smaller, so the first pair stays.
    assert result == (1.0, 2.0)


def test_find_closest_elements_duplicate_values():
    """Duplicate values yield a zero-distance pair and still hit all
    inner-loop branches."""
    result = find_closest_elements([4.0, 4.0, 7.0])
    assert result == (4.0, 4.0)
