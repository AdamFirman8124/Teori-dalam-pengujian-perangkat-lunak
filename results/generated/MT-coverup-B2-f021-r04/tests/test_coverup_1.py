# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic_ascending():
    """Lines 6-8: min/max computed and list comprehension executed."""
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rescale_to_unit(numbers)
    # min=1.0, max=5.0, range=4.0
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]
    # Postcondition: all values lie in the unit interval
    assert all(0.0 <= x <= 1.0 for x in result)


def test_rescale_to_unit_with_negatives_and_duplicates():
    """Covers lines 6-8 with negative values, duplicates and unsorted input."""
    numbers = [5.0, 3.0, -5.0, 2.0, -3.0, 3.0, 0.0, -0.5, 4.0]
    result = rescale_to_unit(numbers)
    # min=-5.0, max=5.0, range=10.0
    assert result == [1.0, 0.8, 0.0, 0.7, 0.2, 0.8, 0.5, 0.45, 0.9]
    # Postcondition: smallest input maps to 0.0, largest maps to 1.0
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_rescale_to_unit_does_not_mutate_input():
    """Lines 6-8 must not modify the caller's list."""
    numbers = [2.0, 4.0, 6.0]
    snapshot = list(numbers)
    result = rescale_to_unit(numbers)
    assert numbers == snapshot
    assert result == [0.0, 0.5, 1.0]
    assert result is not numbers


def test_rescale_to_unit_returns_new_list_of_floats():
    """The comprehension on line 8 builds a fresh list of floats."""
    numbers = [10.0, 20.0, 30.0]
    result = rescale_to_unit(numbers)
    assert isinstance(result, list)
    assert all(isinstance(x, float) for x in result)
    assert result == [0.0, 0.5, 1.0]
