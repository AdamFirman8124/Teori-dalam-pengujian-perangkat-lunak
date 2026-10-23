# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import pytest
from f003 import below_zero

def test_below_zero_empty_operations_returns_false():
 assert below_zero([]) is False

def test_below_zero_positive_operations_returns_false():
 assert below_zero([1, 2, 3, 10]) is False

def test_below_zero_balance_exactly_zero_returns_false():
 assert below_zero([5, -5, 5, -5]) is False

def test_below_zero_single_zero_returns_false():
 assert below_zero([0]) is False

def test_below_zero_drops_below_zero_returns_true():
 assert below_zero([1, -2, 3]) is True

def test_below_zero_first_operation_negative_returns_true():
 assert below_zero([-1, 5, 10]) is True

def test_below_zero_ends_below_zero_returns_true():
 assert below_zero([10, -20]) is True

def test_below_zero_recovers_then_drops_returns_true():
 assert below_zero([5, -3, 2, -10, 100]) is True

def test_below_zero_is_pure_no_state_pollution():
 ops = [1, -2, 1]
 first = below_zero(ops)
 second = below_zero(ops)
 assert first is True
 assert second is True
 assert ops == [1, -2, 1]