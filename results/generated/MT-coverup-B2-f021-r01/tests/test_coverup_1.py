# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic():
    """Typical case: min maps to 0, max maps to 1, others scale linearly."""
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rescale_to_unit(numbers)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]
    # The function must not mutate its input (no state pollution).
    assert numbers == [1.0, 2.0, 3.0, 4.0, 5.0]


def test_rescale_to_unit_unsorted_with_negatives():
    """Unsorted input containing negative values is handled correctly."""
    numbers = [10.0, -10.0, 0.0]
    result = rescale_to_unit(numbers)
    assert result == [1.0, 0.0, 0.5]
    assert numbers == [10.0, -10.0, 0.0]


def test_rescale_to_unit_two_values():
    """Minimal non-degenerate input: exactly two distinct values."""
    result = rescale_to_unit([3.0, 7.0])
    assert result == [0.0, 1.0]


def test_rescale_to_unit_all_equal_raises():
    """Degenerate input (all equal) divides by zero; document that behavior."""
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([2.0, 2.0, 2.0])
