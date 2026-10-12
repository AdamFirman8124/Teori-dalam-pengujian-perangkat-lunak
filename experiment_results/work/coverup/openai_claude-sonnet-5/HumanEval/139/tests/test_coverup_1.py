# file: script_139.py:1-18
# asked: {"lines": [13, 14, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [13, 14, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

import pytest
from script_139 import special_factorial


def test_special_factorial_1():
    """Test special_factorial with n=1"""
    assert special_factorial(1) == 1


def test_special_factorial_2():
    """Test special_factorial with n=2"""
    assert special_factorial(2) == 2


def test_special_factorial_3():
    """Test special_factorial with n=3"""
    assert special_factorial(3) == 12


def test_special_factorial_4():
    """Test special_factorial with n=4"""
    assert special_factorial(4) == 288


def test_special_factorial_5():
    """Test special_factorial with n=5"""
    assert special_factorial(5) == 34560
