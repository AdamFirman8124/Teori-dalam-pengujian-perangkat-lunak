# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic():
    """Covers lines 6-8 with a simple, already-sorted positive list."""
    numbers = [1.0, 2.0, 3.0]
    result = rescale_to_unit(numbers)
    # Postconditions: correct rescaled values, same length, input untouched.
    assert result == [0.0, 0.5, 1.0]
    assert len(result) == len(numbers)
    assert numbers == [1.0, 2.0, 3.0]


def test_rescale_to_unit_negative_and_unsorted():
    """Covers lines 6-8 with negative values and an unsorted input list."""
    numbers = [4.0, -2.0, 0.0, 10.0]
    result = rescale_to_unit(numbers)
    # min = -2, max = 10, range = 12
    assert result == pytest.approx([0.5, 0.0, 1.0 / 6.0, 1.0])
    # Postconditions: smallest input maps to 0.0, largest maps to 1.0.
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)
    assert len(result) == 4
    # Input list must not be mutated.
    assert numbers == [4.0, -2.0, 0.0, 10.0]


def test_rescale_to_unit_empty_list_raises():
    """Line 6 (min on empty sequence) raises ValueError."""
    with pytest.raises(ValueError):
        rescale_to_unit([])


def test_rescale_to_unit_degenerate_range_raises():
    """Line 8 executes and raises ZeroDivisionError when max == min."""
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0, 5.0, 5.0])
