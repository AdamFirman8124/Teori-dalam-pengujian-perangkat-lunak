# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f040 import triples_sum_to_zero


def test_triples_sum_to_zero_true():
    # Covers lines 3-7: nested loops find a triple summing to zero
    assert triples_sum_to_zero([1, 3, 5, 0, -1]) is True


def test_triples_sum_to_zero_false():
    # Covers lines 3-6 and line 8: loops complete without finding a triple
    assert triples_sum_to_zero([1, 3, 5, 7]) is False


def test_triples_sum_to_zero_empty():
    # Covers line 8 immediately: loop body (lines 4-7) never runs
    assert triples_sum_to_zero([]) is False


def test_triples_sum_to_zero_too_short():
    # Fewer than 3 elements: inner loops never execute, returns False
    assert triples_sum_to_zero([1, -1]) is False


def test_triples_sum_to_zero_negative_only():
    # All-negative list: no triple sums to zero, full loop traversal
    assert triples_sum_to_zero([-1, -2, -3]) is False
