# file: script_100.py:1-15
# asked: {"lines": [15], "branches": []}
# gained: {"lines": [15], "branches": []}

import pytest
from script_100 import make_a_pile


def test_make_a_pile_odd():
    """Test make_a_pile with odd number."""
    result = make_a_pile(3)
    assert result == [3, 5, 7]
    assert len(result) == 3


def test_make_a_pile_even():
    """Test make_a_pile with even number."""
    result = make_a_pile(4)
    assert result == [4, 6, 8, 10]
    assert len(result) == 4


def test_make_a_pile_one():
    """Test make_a_pile with n=1."""
    result = make_a_pile(1)
    assert result == [1]
    assert len(result) == 1


def test_make_a_pile_larger_odd():
    """Test make_a_pile with larger odd number."""
    result = make_a_pile(5)
    assert result == [5, 7, 9, 11, 13]
    assert len(result) == 5


def test_make_a_pile_larger_even():
    """Test make_a_pile with larger even number."""
    result = make_a_pile(6)
    assert result == [6, 8, 10, 12, 14, 16]
    assert len(result) == 6
