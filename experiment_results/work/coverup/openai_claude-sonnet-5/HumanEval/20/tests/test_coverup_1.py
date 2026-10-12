# file: script_20.py:4-27
# asked: {"lines": [12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27], "branches": [[15, 16], [15, 27], [16, 15], [16, 17], [17, 16], [17, 18], [18, 19], [18, 22], [23, 16], [23, 24]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27], "branches": [[15, 16], [15, 27], [16, 15], [16, 17], [17, 16], [17, 18], [18, 19], [18, 22], [23, 16], [23, 24]]}

import pytest
from script_20 import find_closest_elements


def test_find_closest_elements_basic():
    """Test with basic case from docstring - executes lines 12-27"""
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    assert result == (2.0, 2.2)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_find_closest_elements_duplicates():
    """Test with duplicate values - executes lines 12-27"""
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    assert result == (2.0, 2.0)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_find_closest_elements_two_elements():
    """Test with exactly two elements - executes lines 12-20, 27"""
    result = find_closest_elements([1.0, 3.0])
    assert result == (1.0, 3.0)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_find_closest_elements_negative_numbers():
    """Test with negative numbers - executes lines 12-27"""
    result = find_closest_elements([-5.0, -2.0, 0.0, 3.0])
    assert result == (-2.0, 0.0)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_find_closest_elements_all_negative():
    """Test with all negative numbers - executes lines 12-27"""
    result = find_closest_elements([-10.0, -8.0, -5.0, -7.9])
    assert result == (-8.0, -7.9)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_find_closest_elements_large_gap_then_small():
    """Test where first pair has large distance, later pair has small distance - executes lines 22-25"""
    result = find_closest_elements([100.0, 1.0, 1.5, 50.0])
    assert result == (1.0, 1.5)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_find_closest_elements_returns_sorted():
    """Test that result is always sorted (smaller, larger) - executes lines 12-27"""
    result = find_closest_elements([5.0, 1.0, 3.0])
    assert result[0] <= result[1]
    assert isinstance(result, tuple)
    assert len(result) == 2
