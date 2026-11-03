# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic():
    """Lines 6-8: min/max computed and list comprehension executed."""
    numbers = [1.0, 2.0, 3.0]
    result = rescale_to_unit(numbers)
    assert result == [0.0, 0.5, 1.0]
    # Postconditions: smallest maps to 0, largest maps to 1, length preserved.
    assert len(result) == len(numbers)
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_rescale_to_unit_negative_and_unsorted():
    """Covers lines 6-8 with negative values and unsorted input."""
    numbers = [3.0, -1.0, 1.0]
    result = rescale_to_unit(numbers)
    assert result == [1.0, 0.0, 0.5]
    # Order of the input must be preserved.
    assert result[0] == 1.0
    assert result[1] == 0.0
    assert result[2] == 0.5


def test_rescale_to_unit_two_elements():
    """Covers lines 6-8 with the minimal non-degenerate input."""
    result = rescale_to_unit([10.0, 20.0])
    assert result == [0.0, 1.0]


def test_rescale_to_unit_constant_list_raises():
    """Lines 6-8 execute, then division by zero occurs (max == min)."""
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0, 5.0, 5.0])
