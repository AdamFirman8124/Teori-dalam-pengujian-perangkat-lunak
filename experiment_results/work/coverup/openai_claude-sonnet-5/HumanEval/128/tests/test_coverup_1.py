# file: script_128.py:1-15
# asked: {"lines": [13, 14, 15], "branches": [[13, 13], [13, 14]]}
# gained: {"lines": [13, 14, 15], "branches": [[13, 13], [13, 14]]}

import pytest
from script_128 import prod_signs


def test_prod_signs_empty_array():
    """Test that empty array returns None."""
    assert prod_signs([]) is None


def test_prod_signs_with_zero():
    """Test that array containing zero returns 0."""
    result = prod_signs([0, 1])
    assert result == 0


def test_prod_signs_with_zero_and_negatives():
    """Test that array with zero and negatives returns 0."""
    result = prod_signs([0, -1, -2, 3])
    assert result == 0


def test_prod_signs_all_positive():
    """Test array with all positive numbers."""
    result = prod_signs([1, 2, 3])
    assert result == 6


def test_prod_signs_even_negatives():
    """Test array with even number of negative numbers."""
    result = prod_signs([-1, -2, 3])
    assert result == 6


def test_prod_signs_odd_negatives():
    """Test array with odd number of negative numbers."""
    result = prod_signs([1, 2, 2, -4])
    assert result == -9


def test_prod_signs_single_negative():
    """Test array with single negative number."""
    result = prod_signs([-5])
    assert result == -5


def test_prod_signs_single_positive():
    """Test array with single positive number."""
    result = prod_signs([7])
    assert result == 7
