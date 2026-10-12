# file: script_65.py:1-14
# asked: {"lines": [10, 11, 12, 14], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14], "branches": [[11, 12], [11, 14]]}

import pytest
from script_65 import circular_shift


def test_circular_shift_basic():
    """Test basic circular shift functionality."""
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"


def test_circular_shift_exceeds_length():
    """Test when shift exceeds number of digits - should reverse."""
    assert circular_shift(12, 3) == "21"
    assert circular_shift(123, 5) == "321"
    assert circular_shift(5, 2) == "5"


def test_circular_shift_edge_cases():
    """Test edge cases including zero shift and single digit."""
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift(0, 1) == "0"
    assert circular_shift(9, 1) == "9"


def test_circular_shift_larger_numbers():
    """Test with larger numbers."""
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(987654, 3) == "654987"
