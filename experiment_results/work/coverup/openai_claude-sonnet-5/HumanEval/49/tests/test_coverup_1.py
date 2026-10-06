# file: script_49.py:1-17
# asked: {"lines": [14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}
# gained: {"lines": [14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}

import pytest
from script_49 import modp


def test_modp_basic():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1


def test_modp_zero():
    """Test with n=0, which should return 1 without entering the loop."""
    assert modp(0, 101) == 1
    assert modp(0, 5) == 1
    assert modp(0, 2) == 1


def test_modp_positive_n():
    """Test with positive n values to execute lines 14-17."""
    assert modp(1, 5) == 2
    assert modp(2, 5) == 4
    assert modp(3, 5) == 3
    assert modp(4, 7) == 2
    assert modp(5, 13) == 6


def test_modp_large_n():
    """Test with larger n values to ensure loop executes multiple times."""
    assert modp(10, 17) == 4
    assert modp(50, 53) == 40
    assert modp(100, 101) == 1
