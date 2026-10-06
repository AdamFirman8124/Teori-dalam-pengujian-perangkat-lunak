# file: script_76.py:1-18
# asked: {"lines": [13, 14, 15, 16, 17, 18], "branches": [[13, 14], [13, 15], [16, 17], [16, 18]]}
# gained: {"lines": [13, 14, 15, 16, 17, 18], "branches": [[13, 14], [13, 15], [16, 17], [16, 18]]}

import pytest
from script_76 import is_simple_power


def test_is_simple_power_n_equals_1_x_equals_1():
    """Test when n=1 and x=1, should return True"""
    assert is_simple_power(1, 1) == True


def test_is_simple_power_n_equals_1_x_not_equals_1():
    """Test when n=1 and x!=1, should return False"""
    assert is_simple_power(5, 1) == False


def test_is_simple_power_loop_executes():
    """Test that executes the while loop when power < x"""
    assert is_simple_power(8, 2) == True
    assert is_simple_power(16, 2) == True
    assert is_simple_power(27, 3) == True


def test_is_simple_power_loop_executes_false():
    """Test that executes the while loop and returns False"""
    assert is_simple_power(10, 2) == False
    assert is_simple_power(15, 3) == False


def test_is_simple_power_edge_cases():
    """Test edge cases"""
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
