# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f040 import triples_sum_to_zero


def test_triples_sum_to_zero_true_early():
    """A triple summing to zero exists; found early in the loops (lines 3-7)."""
    assert triples_sum_to_zero([1, 2, -3]) is True


def test_triples_sum_to_zero_true_with_zeros():
    """Triple of zeros sums to zero."""
    assert triples_sum_to_zero([0, 0, 0]) is True


def test_triples_sum_to_zero_true_late():
    """Triple found only at the very last (i, j, k) combination, exercising
    the deepest loop iterations before returning True."""
    assert triples_sum_to_zero([1, 2, 3, 4, -7]) is True


def test_triples_sum_to_zero_false():
    """No triple sums to zero; all loops run to completion and line 8 executes."""
    assert triples_sum_to_zero([1, 2, 3, 4]) is False


def test_triples_sum_to_zero_false_negatives_only():
    """All-negative list can never sum to zero."""
    assert triples_sum_to_zero([-1, -2, -3, -4]) is False


def test_triples_sum_to_zero_empty():
    """Empty list: outer loop body never runs, returns False."""
    assert triples_sum_to_zero([]) is False


def test_triples_sum_to_zero_single_element():
    """Fewer than three elements: inner loops never run, returns False."""
    assert triples_sum_to_zero([5]) is False


def test_triples_sum_to_zero_two_elements():
    """Exactly two elements: innermost loop never runs, returns False."""
    assert triples_sum_to_zero([1, -1]) is False


def test_triples_sum_to_zero_does_not_mutate_input():
    """The function must not modify its argument (postcondition check)."""
    original = [1, 2, -3]
    snapshot = list(original)
    result = triples_sum_to_zero(original)
    assert result is True
    assert original == snapshot
