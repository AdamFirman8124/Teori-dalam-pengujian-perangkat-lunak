# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

"""Tests for f020.find_closest_elements covering all missing lines (6-21) and branches."""

import pytest

from f020 import find_closest_elements


def test_initial_pair_and_no_improvement():
    """Covers lines 6-7 (init), 9-14 (first pair found, 'distance is None' True),
    16-17 ('new_distance < distance' False branch) and line 21 (return).

    The first candidate pair (1.0, 2.0) has distance 1.0; every later pair has
    distance >= 1.0, so the best pair is never updated after initialization.
    """
    result = find_closest_elements([1.0, 2.0, 3.0])
    assert result == (1.0, 2.0)
    assert isinstance(result, tuple)


def test_improvement_updates_closest_pair():
    """Covers lines 17-19: a later pair strictly closer than the current best.

    First pair (1.0, 3.0) -> distance 2.0; then (1.5, 3.0) -> 1.5 (improvement);
    then (1.0, 1.5) -> 0.5 (improvement again).
    """
    result = find_closest_elements([3.0, 1.0, 1.5])
    assert result == (1.0, 1.5)


def test_multiple_improvements():
    """Exercises repeated improvements of the running best pair."""
    result = find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])
    assert result == (3.9, 4.0)


def test_duplicate_values_zero_distance():
    """A pair of equal values yields distance 0.0 and a sorted equal pair."""
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    assert result == (2.0, 2.0)


def test_single_element_skips_self_comparison():
    """Covers the False branch of 'idx != idx2' (line 11) with no valid pair.

    With one element the only inner iteration compares the element with itself,
    so closest_pair stays None and is returned as such.
    """
    result = find_closest_elements([5.0])
    assert result is None
