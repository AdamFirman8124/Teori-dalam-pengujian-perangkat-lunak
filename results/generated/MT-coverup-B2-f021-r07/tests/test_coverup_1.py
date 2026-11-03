# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

"""Tests for f021.rescale_to_unit.

The function body (lines 6-8) was previously uncovered because the function
was never invoked by the existing tests. These tests call it directly and
verify its postconditions. The function is pure (no I/O, no globals), so no
cleanup beyond normal test isolation is required; the input list is checked
for non-mutation to guard against accidental state pollution.
"""

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic_ascending():
    """A simple ascending sequence maps linearly onto [0.0, 1.0]."""
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rescale_to_unit(numbers)
    # Postcondition: exact expected rescaling.
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]
    # Postcondition: every value lies within the unit interval.
    assert all(0.0 <= v <= 1.0 for v in result)


def test_rescale_to_unit_two_elements():
    """With two distinct values, the smaller becomes 0.0 and larger 1.0."""
    result = rescale_to_unit([2.0, 49.9])
    assert result[0] == 0.0
    assert result[1] == 1.0


def test_rescale_to_unit_unsorted_preserves_order():
    """Unsorted input keeps element order while rescaling values."""
    result = rescale_to_unit([5.0, 1.0, 3.0])
    assert result == [1.0, 0.0, 0.5]


def test_rescale_to_unit_negative_values():
    """Negative values are handled: min maps to 0.0, max to 1.0."""
    result = rescale_to_unit([-2.0, -1.0, 0.0])
    assert result == [0.0, 0.5, 1.0]


def test_rescale_to_unit_does_not_mutate_input():
    """Postcondition: the input list is left unchanged."""
    numbers = [3.0, 1.0, 2.0]
    snapshot = list(numbers)
    rescale_to_unit(numbers)
    assert numbers == snapshot


def test_rescale_to_unit_identical_values_raises_zero_division():
    """All-equal input makes the denominator zero on line 8."""
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([4.0, 4.0, 4.0])
