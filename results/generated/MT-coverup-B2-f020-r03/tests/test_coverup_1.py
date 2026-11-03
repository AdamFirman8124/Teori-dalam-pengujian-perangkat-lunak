# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

"""Tests for f020.find_closest_elements.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required; each test works only on
locally created data, avoiding any state pollution.
"""

from f020 import find_closest_elements


def test_find_closest_elements_finds_closest_pair():
    """Covers lines 6-21: initialization, both loops, the
    'distance is None' branch (lines 12-14), the 'new_distance < distance'
    update branch (lines 17-19), the no-update branch (line 17 False),
    and the self-comparison skip (line 11 False)."""
    result = find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2])
    assert result == (3.9, 4.0)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_find_closest_elements_two_elements():
    """Minimal input: only the first-pair branch (lines 12-14) and the
    return statement (line 21) are exercised; the update branch never
    triggers because the single pair is already the closest."""
    result = find_closest_elements([1.0, 2.0])
    assert result == (1.0, 2.0)


def test_find_closest_elements_sorts_unordered_pair():
    """The closest pair is first encountered in descending order
    (5.0 before 1.0, then 5.0 before 1.5), exercising the
    tuple(sorted(...)) calls in both the None branch and the
    update branch."""
    result = find_closest_elements([5.0, 1.0, 1.5])
    assert result == (1.0, 1.5)
    assert result[0] <= result[1]


def test_find_closest_elements_negative_values():
    """Works with negative floats; the closest pair (-3.0, -2.5) is
    found via the update branch (line 17 True) after an initial
    wider pair (-3.0, -1.0)."""
    result = find_closest_elements([-1.0, -3.0, -2.5])
    assert result == (-3.0, -2.5)


def test_find_closest_elements_does_not_mutate_input():
    """Verifies the function leaves its argument untouched.

    With [3.0, 1.0, 2.0] the first pair encountered is (3.0, 1.0)
    with distance 2.0; the pair (3.0, 2.0) has distance 1.0 and
    replaces it. All remaining pairs are at distance >= 1.0 (ties do
    not update, since the comparison is strict), so the result is
    (2.0, 3.0)."""
    numbers = [3.0, 1.0, 2.0]
    snapshot = list(numbers)
    result = find_closest_elements(numbers)
    assert numbers == snapshot
    assert result == (2.0, 3.0)
    assert result[0] <= result[1]
