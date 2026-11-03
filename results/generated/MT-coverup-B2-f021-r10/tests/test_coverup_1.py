# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic_scaling():
    """Lines 6-8: min/max computed and list comprehension returned."""
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rescale_to_unit(numbers)

    # Postcondition: values mapped linearly onto [0.0, 1.0]
    assert result == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])
    # Postcondition: extremes map exactly to bounds
    assert result[0] == 0.0
    assert result[-1] == 1.0
    # Postcondition: input list is not mutated
    assert numbers == [1.0, 2.0, 3.0, 4.0, 5.0]


def test_rescale_to_unit_with_negative_values():
    """Exercise min/max selection with negative endpoints."""
    numbers = [-2.0, -1.0, 0.0, 1.0, 2.0]
    result = rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])
    assert len(result) == len(numbers)


def test_rescale_to_unit_unordered_input():
    """min/max must be found regardless of ordering; order preserved in output."""
    numbers = [10.0, 30.0, 20.0]
    result = rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 1.0, 0.5])
    assert result[0] < result[2] < result[1]


def test_rescale_to_unit_two_elements():
    """Smallest non-trivial case: two distinct values."""
    result = rescale_to_unit([5.0, 10.0])

    assert result == pytest.approx([0.0, 1.0])


def test_rescale_to_unit_returns_new_list():
    """Postcondition: a brand-new list object is returned, not the input."""
    numbers = [1.0, 3.0]
    result = rescale_to_unit(numbers)

    assert result is not numbers
    assert isinstance(result, list)
    assert result == pytest.approx([0.0, 1.0])
