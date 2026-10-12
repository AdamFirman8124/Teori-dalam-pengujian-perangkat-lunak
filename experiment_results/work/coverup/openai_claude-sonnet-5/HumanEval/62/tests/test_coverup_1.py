# file: script_62.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest
from script_62 import derivative


def test_derivative_basic():
    """Test basic derivative calculation."""
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]


def test_derivative_simple():
    """Test simple polynomial derivative."""
    assert derivative([1, 2, 3]) == [2, 6]


def test_derivative_constant():
    """Test derivative of constant (single coefficient)."""
    assert derivative([5]) == []


def test_derivative_linear():
    """Test derivative of linear polynomial."""
    assert derivative([3, 2]) == [2]


def test_derivative_empty():
    """Test derivative of empty list."""
    assert derivative([]) == []


def test_derivative_zero_coefficients():
    """Test derivative with zero coefficients."""
    assert derivative([0, 0, 3, 0, 5]) == [0, 6, 0, 20]


def test_derivative_negative_coefficients():
    """Test derivative with negative coefficients."""
    assert derivative([5, -3, 2, -1]) == [-3, 4, -3]


def test_derivative_large_polynomial():
    """Test derivative of larger polynomial."""
    assert derivative([1, 2, 3, 4, 5, 6]) == [2, 6, 12, 20, 30]
