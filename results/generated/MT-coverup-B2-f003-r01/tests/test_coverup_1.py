# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import pytest
from f003 import below_zero

def test_below_zero_empty_operations_returns_false():
 # Covers line 6 (balance = 0), skips the loop body, and hits line 13.
 assert below_zero([]) is False

def test_below_zero_strictly_positive_operations_returns_false():
 # Covers lines 6, 8, 9, 10 (branch not taken), and 13.
 assert below_zero([1, 2, 3, 4]) is False

def test_below_zero_balance_touches_zero_but_never_negative():
 # Exercises the loop with negative ops while balance stays >= 0.
 assert below_zero([10, -10, 5, -5, 1]) is False

def test_below_zero_drops_below_zero_midway():
 # Covers lines 6, 8, 9, 10 (branch taken), and 11 (return True).
 assert below_zero([1, -2, 3]) is True

def test_below_zero_first_operation_negative():
 # Immediate negative balance on the first iteration.
 assert below_zero([-1, 5, 5]) is True

def test_below_zero_late_drop_below_zero():
 # Balance stays positive for several iterations, then dips below zero.
 assert below_zero([5, 5, 5, -20, 1]) is True