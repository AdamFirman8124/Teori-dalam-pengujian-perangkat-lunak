# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest
from script_3 import below_zero


def test_below_zero_empty_list():
    """Test with empty list - balance never goes below zero"""
    assert below_zero([]) == False


def test_below_zero_positive_operations():
    """Test with only positive operations - balance never goes below zero"""
    assert below_zero([1, 2, 3]) == False


def test_below_zero_goes_negative():
    """Test when balance falls below zero"""
    assert below_zero([1, 2, -4, 5]) == True


def test_below_zero_single_negative():
    """Test with single negative operation that makes balance negative"""
    assert below_zero([-1]) == True


def test_below_zero_zero_operations():
    """Test with operations that sum to zero but never go negative"""
    assert below_zero([5, -5]) == False


def test_below_zero_negative_at_end():
    """Test when balance goes negative at the end"""
    assert below_zero([10, 5, -20]) == True


def test_below_zero_stays_at_zero():
    """Test with only zero operations"""
    assert below_zero([0, 0, 0]) == False
