# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic():
    numbers = [1.0, 2.0, 3.0]
    result = rescale_to_unit(numbers)
    # Executes lines 6-8: min, max, and the list comprehension
    assert result == [0.0, 0.5, 1.0]
    # Postcondition: input list is not mutated
    assert numbers == [1.0, 2.0, 3.0]


def test_rescale_to_unit_negative_and_unsorted():
    numbers = [5.0, -5.0, 0.0]
    result = rescale_to_unit(numbers)
    # min = -5.0, max = 5.0, range = 10.0
    assert result == [1.0, 0.0, 0.5]
    assert all(0.0 <= x <= 1.0 for x in result)


def test_rescale_to_unit_single_element():
    # Degenerate branch: max_number - min_number == 0 -> ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([7.0])
