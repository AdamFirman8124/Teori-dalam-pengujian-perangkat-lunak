# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic_sorted():
    """Covers lines 6-8: min, max, and the list comprehension."""
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rescale_to_unit(numbers)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]
    # Postconditions: smallest value maps to 0, largest maps to 1
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_rescale_to_unit_unsorted_input():
    """Ensures min/max are computed independently of input order."""
    numbers = [5.0, 3.0, 1.0, 4.0, 2.0]
    result = rescale_to_unit(numbers)
    assert result == [1.0, 0.5, 0.0, 0.75, 0.25]
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_rescale_to_unit_negative_numbers():
    """Covers the arithmetic with negative min/max values."""
    numbers = [-2.0, -1.0, 0.0, 1.0, 2.0]
    result = rescale_to_unit(numbers)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_rescale_to_unit_does_not_mutate_input():
    """The function must be pure: input list is left unchanged."""
    numbers = [1.0, 2.0, 3.0]
    snapshot = list(numbers)
    result = rescale_to_unit(numbers)
    assert numbers == snapshot
    assert result == [0.0, 0.5, 1.0]
    assert result is not numbers
