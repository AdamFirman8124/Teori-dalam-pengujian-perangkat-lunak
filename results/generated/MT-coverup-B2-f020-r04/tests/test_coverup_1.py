# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

from f020 import find_closest_elements


def test_initial_pair_and_no_improvement_branch():
    """Covers lines 6-14 (initialization, both loop levels, the idx != idx2
    guard, the distance-is-None branch) plus the false branch of the
    new_distance < distance comparison (lines 16-17) and the return (line 21).
    """
    result = find_closest_elements([1.0, 2.0, 3.0])
    assert result == (1.0, 2.0)


def test_closer_pair_update_branch():
    """Covers the true branch of new_distance < distance (lines 18-19):
    the pair (5.0, 5.5) is closer than the initially recorded (1.0, 5.0).
    """
    result = find_closest_elements([1.0, 5.0, 5.5])
    assert result == (5.0, 5.5)


def test_result_is_sorted_pair():
    """The returned pair must be sorted regardless of input order."""
    result = find_closest_elements([3.0, 1.0])
    assert result == (1.0, 3.0)


def test_zero_distance_does_not_reenter_none_branch():
    """distance == 0.0 is falsy but not None, so line 12's `is None` check
    must route to the else branch and keep (2.0, 2.0) as the closest pair.
    """
    result = find_closest_elements([2.0, 2.0, 3.0])
    assert result == (2.0, 2.0)


def test_negative_values():
    """Works with negative numbers; closest pair is (-1.5, -1.0)."""
    result = find_closest_elements([-1.0, -5.0, -1.5])
    assert result == (-1.5, -1.0)


def test_fewer_than_two_elements_returns_none():
    """With fewer than two elements no pair is ever compared, so the
    function returns the initial None value of closest_pair.
    """
    assert find_closest_elements([]) is None
    assert find_closest_elements([7.0]) is None
