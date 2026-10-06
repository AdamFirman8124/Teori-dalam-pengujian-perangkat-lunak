# file: script_65.py:1-14
# asked: {"lines": [10, 11, 12, 14], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14], "branches": [[11, 12], [11, 14]]}

import pytest
from script_65 import circular_shift


def test_circular_shift_basic():
    """Test basic circular shift operation."""
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"


def test_circular_shift_exceeds_length():
    """Test when shift exceeds number of digits - should reverse."""
    assert circular_shift(12, 3) == "21"
    assert circular_shift(123, 5) == "321"
    assert circular_shift(5, 2) == "5"


def test_circular_shift_single_digit():
    """Test with single digit numbers."""
    assert circular_shift(5, 0) == "5"
    assert circular_shift(5, 1) == "5"


def test_circular_shift_zero_shift():
    """Test with zero shift."""
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift(99, 0) == "99"


def test_circular_shift_exact_length():
    """Test when shift equals number of digits."""
    assert circular_shift(123, 3) == "123"
    assert circular_shift(99, 2) == "99"


def test_circular_shift_multiple_digits():
    """Test with larger numbers."""
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(98765, 3) == "76598"
