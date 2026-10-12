# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest
from script_3 import below_zero


def test_below_zero_empty_list():
    """Test with empty list - should return False and execute lines 13, 20"""
    assert below_zero([]) == False


def test_below_zero_positive_operations():
    """Test with only positive operations - should return False"""
    assert below_zero([1, 2, 3]) == False


def test_below_zero_falls_below_zero():
    """Test when balance falls below zero - should return True and execute lines 15-18"""
    assert below_zero([1, 2, -4, 5]) == True


def test_below_zero_exactly_zero():
    """Test when balance reaches exactly zero but never below"""
    assert below_zero([5, -5, 3]) == False


def test_below_zero_single_negative():
    """Test with single negative operation"""
    assert below_zero([-1]) == True


def test_below_zero_single_positive():
    """Test with single positive operation"""
    assert below_zero([10]) == False


def test_below_zero_immediate_negative():
    """Test when first operation makes balance negative"""
    assert below_zero([-5, 10, 20]) == True


def test_below_zero_late_negative():
    """Test when balance goes negative later in the sequence"""
    assert below_zero([10, 20, -15, -16]) == True
