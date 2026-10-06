# file: script_130.py:1-26
# asked: {"lines": [18, 19, 20, 21, 22, 23, 25, 26], "branches": [[18, 19], [18, 20], [21, 22], [21, 26], [22, 23], [22, 25]]}
# gained: {"lines": [18, 19, 20, 21, 22, 23, 25, 26], "branches": [[18, 19], [18, 20], [21, 22], [21, 26], [22, 23], [22, 25]]}

import pytest
from script_130 import tri


def test_tri_zero():
    """Test tri(0) returns [1]"""
    result = tri(0)
    assert result == [1]
    assert len(result) == 1


def test_tri_even_numbers():
    """Test tri with even n values"""
    result = tri(2)
    assert result == [1, 3, 2.0]
    assert len(result) == 3
    
    result = tri(4)
    assert result == [1, 3, 2.0, 8.0, 3.0]
    assert len(result) == 5


def test_tri_odd_numbers():
    """Test tri with odd n values"""
    result = tri(3)
    assert result == [1, 3, 2.0, 8.0]
    assert len(result) == 4
    
    result = tri(5)
    assert result == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert len(result) == 6


def test_tri_single():
    """Test tri(1) returns [1, 3]"""
    result = tri(1)
    assert result == [1, 3]
    assert len(result) == 2


def test_tri_larger_value():
    """Test tri with larger n to ensure iteration works correctly"""
    result = tri(6)
    assert len(result) == 7
    assert result[0] == 1
    assert result[1] == 3
    assert result[2] == 2.0  # even: 2/2 + 1
    assert result[3] == 8.0  # odd: 2.0 + 3 + (3+3)/2
    assert result[4] == 3.0  # even: 4/2 + 1
    assert result[5] == 15.0  # odd: 3.0 + 8.0 + (5+3)/2
    assert result[6] == 4.0  # even: 6/2 + 1
