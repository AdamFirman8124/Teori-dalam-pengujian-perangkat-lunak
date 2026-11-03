# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import math

import pytest

from f021 import rescale_to_unit


def test_rescale_basic_ascending():
    """Lines 6-8: min, max and the list comprehension all execute."""
    numbers = [1.0, 2.0, 3.0]
    result = rescale_to_unit(numbers)
    assert result == [0.0, 0.5, 1.0]
    # Postcondition: the (pure) function must not mutate its input.
    assert numbers == [1.0, 2.0, 3.0]


def test_rescale_unsorted_with_negatives():
    numbers = [5.0, 3.0, -5.0, 2.0]
    result = rescale_to_unit(numbers)
    assert result == [1.0, 0.8, 0.0, 0.7]
    assert len(result) == len(numbers)
    assert numbers == [5.0, 3.0, -5.0, 2.0]


def test_rescale_with_duplicates():
    """Duplicates equal to the minimum map to 0.0."""
    result = rescale_to_unit([2.0, 2.0, 4.0, 2.0])
    assert result == [0.0, 0.0, 1.0, 0.0]


def test_rescale_bounds_and_order_preserved():
    numbers = [10.0, -10.0, 0.0, 5.0]
    result = rescale_to_unit(numbers)
    # Postconditions: min -> 0.0, max -> 1.0, everything within [0, 1],
    # and element order is preserved.
    assert result[0] == 1.0
    assert result[1] == 0.0
    assert result == [1.0, 0.0, 0.5, 0.75]
    assert all(0.0 <= v <= 1.0 for v in result)
    assert all(math.isfinite(v) for v in result)


def test_rescale_single_element_divides_by_zero():
    """Edge branch: min == max makes the denominator zero."""
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([3.0])


def test_rescale_identity_when_range_is_one():
    result = rescale_to_unit([0.0, 1.0, 0.25])
    assert result == [0.0, 1.0, 0.25]
