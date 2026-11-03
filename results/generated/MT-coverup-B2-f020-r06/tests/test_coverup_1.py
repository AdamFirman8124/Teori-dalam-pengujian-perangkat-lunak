# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

import pytest

from f020 import find_closest_elements


def test_find_closest_elements_initial_pair_and_no_improvement():
    """Covers lines 6-14 (first pair found, 'distance is None' branch) and
    lines 16-17 with the 'new_distance < distance' condition evaluating False
    (later pairs are not closer, so the initial pair is kept)."""
    result = find_closest_elements([1.0, 2.0, 3.0])
    # The closest pair in [1.0, 2.0, 3.0] is (1.0, 2.0) with distance 1.0;
    # every subsequent candidate (e.g. |1.0-3.0| = 2.0) fails the '<' check.
    assert result == (1.0, 2.0)


def test_find_closest_elements_finds_closer_pair():
    """Covers lines 17-19: a later candidate pair has a strictly smaller
    distance, so 'closest_pair' is updated."""
    result = find_closest_elements([1.0, 5.0, 4.5])
    # Trace: (1.0, 5.0) -> distance 4.0; (1.0, 4.5) -> 3.5 < 4.0 (update);
    # (5.0, 4.5) -> 0.5 < 3.5 (update). Final pair is (4.5, 5.0).
    assert result == (4.5, 5.0)


def test_find_closest_elements_returns_sorted_tuple():
    """Covers the 'tuple(sorted(...))' construction: the pair is returned in
    ascending order regardless of input order."""
    result = find_closest_elements([3.0, 1.0])
    assert result == (1.0, 3.0)
    assert result[0] <= result[1]


def test_find_closest_elements_single_element_returns_none():
    """Covers the False branch of 'if idx != idx2': with a single element the
    inner condition is never satisfied, so no pair is ever assigned and the
    function returns the initial None value."""
    assert find_closest_elements([7.0]) is None
