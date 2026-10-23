# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import pytest

from f003 import below_zero

def test_below_zero_empty_operations_returns_false():
 # Empty input: the for-loop body never executes, balance stays 0, returns False.
 assert below_zero([]) is False

def test_below_zero_all_positive_operations_returns_false():
 # Loop runs, balance never drops below zero, returns False.
 assert below_zero([1, 2, 3, 4]) is False

def test_below_zero_balance_hits_exact_zero_returns_false():
 # balance reaches exactly 0, which is not < 0, so the early return is skipped.
 assert below_zero([5, -5, 10, -10]) is False

def test_below_zero_zero_valued_operations_returns_false():
 # Operations of 0 keep the balance at 0; never below zero.
 assert below_zero([0, 0, 0]) is False

def test_below_zero_single_negative_operation_returns_true():
 # First operation drives the balance below zero immediately.
 assert below_zero([-1]) is True

def test_below_zero_drops_below_zero_midway_returns_true():
 # Balance goes negative partway through the sequence, triggering the early return.
 assert below_zero([10, -25, 100]) is True