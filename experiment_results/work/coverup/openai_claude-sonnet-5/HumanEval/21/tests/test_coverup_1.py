# file: script_21.py:4-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from typing import List
from script_21 import rescale_to_unit


def test_rescale_to_unit_basic():
    """Test basic rescaling with a simple list"""
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_rescale_to_unit_two_elements():
    """Test with exactly two elements"""
    result = rescale_to_unit([0.0, 10.0])
    assert result == [0.0, 1.0]


def test_rescale_to_unit_negative_numbers():
    """Test with negative numbers"""
    result = rescale_to_unit([-5.0, 0.0, 5.0])
    assert result == [0.0, 0.5, 1.0]


def test_rescale_to_unit_all_negative():
    """Test with all negative numbers"""
    result = rescale_to_unit([-10.0, -5.0, -1.0])
    assert result == [0.0, 0.5555555555555556, 1.0]


def test_rescale_to_unit_identical_min_max():
    """Test with identical values (edge case for division by zero)"""
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0, 5.0, 5.0])


def test_rescale_to_unit_float_precision():
    """Test with floats requiring precision"""
    result = rescale_to_unit([0.5, 1.5, 2.5, 3.5])
    assert abs(result[0] - 0.0) < 1e-9
    assert abs(result[1] - 0.3333333333333333) < 1e-9
    assert abs(result[2] - 0.6666666666666666) < 1e-9
    assert abs(result[3] - 1.0) < 1e-9
