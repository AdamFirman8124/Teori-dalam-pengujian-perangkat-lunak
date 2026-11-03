# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_basic_ascending():
    """Lines 6-8: min/max computed and list comprehension rescales to [0, 1]."""
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])


def test_rescale_unsorted_input():
    """Order of the input is preserved even when it is not sorted."""
    result = rescale_to_unit([5.0, 1.0, 3.0])
    assert result == pytest.approx([1.0, 0.0, 0.5])


def test_rescale_negative_numbers():
    """Negative values are handled correctly."""
    result = rescale_to_unit([-2.0, -1.0, 0.0, 1.0, 2.0])
    assert result == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])


def test_rescale_with_duplicates():
    """Duplicated min/max values still map to 0.0 and 1.0 respectively."""
    result = rescale_to_unit([3.0, 1.0, 3.0, 2.0, 1.0])
    assert result == pytest.approx([1.0, 0.0, 1.0, 0.5, 0.0])


def test_rescale_extremes_and_bounds():
    """Postconditions: first element of output is 0.0, last is 1.0,
    and every value lies within the unit interval."""
    numbers = [10.5, -3.2, 7.7, 0.0, 4.4]
    result = rescale_to_unit(numbers)
    assert result[0] == pytest.approx(1.0)          # max element -> 1.0
    assert result[1] == pytest.approx(0.0)          # min element -> 0.0
    assert all(0.0 <= v <= 1.0 for v in result)
    assert len(result) == len(numbers)
    # Input list must not be mutated (function is pure).
    assert numbers == [10.5, -3.2, 7.7, 0.0, 4.4]
