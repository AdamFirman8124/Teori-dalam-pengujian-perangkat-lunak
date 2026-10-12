# file: script_85.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_85 import add


def test_add_even_at_odd_indices():
    """Test with even elements at odd indices."""
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 4, 3, 8]) == 12
    assert add([0, 10, 0, 20]) == 30


def test_add_odd_at_odd_indices():
    """Test with odd elements at odd indices - should return 0."""
    assert add([1, 3, 5, 7]) == 0
    assert add([2, 1, 4, 3]) == 0


def test_add_single_element():
    """Test with single element list - no odd indices."""
    assert add([5]) == 0
    assert add([10]) == 0


def test_add_two_elements_even_at_odd():
    """Test with two elements where second is even."""
    assert add([1, 4]) == 4
    assert add([3, 6]) == 6


def test_add_two_elements_odd_at_odd():
    """Test with two elements where second is odd."""
    assert add([1, 3]) == 0
    assert add([2, 5]) == 0


def test_add_mixed_values():
    """Test with mixed even and odd values at odd indices."""
    assert add([0, 1, 0, 2, 0, 3, 0, 4]) == 6
    # Indices: 0, 1, 2, 3, 4, 5, 6, 7
    # Odd indices: 1, 3, 5, 7
    # Values at odd indices: 2, 4, 6, 8 (all even)
    # Sum: 2 + 4 + 6 + 8 = 20
    assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 20


def test_add_empty_odd_indices():
    """Test where odd indices exist but contain only odd numbers."""
    assert add([2, 1, 4, 3, 6, 5]) == 0


def test_add_all_even_at_odd_indices():
    """Test where all odd indices contain even numbers."""
    assert add([1, 2, 3, 4, 5, 6]) == 12
    assert add([0, 8, 0, 10, 0, 12]) == 30
