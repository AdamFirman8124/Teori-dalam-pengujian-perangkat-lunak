# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f040 import triples_sum_to_zero


def test_triples_sum_to_zero_true():
    # A triple (2, -3, 1) sums to zero -> returns True
    assert triples_sum_to_zero([2, -3, 1, 4]) is True


def test_triples_sum_to_zero_false():
    # No triple sums to zero -> loop completes and returns False
    assert triples_sum_to_zero([1, 2, 3, 4]) is False


def test_triples_sum_to_zero_too_short():
    # Fewer than 3 elements: inner loops never find a triple -> False
    assert triples_sum_to_zero([1, -1]) is False


def test_triples_sum_to_zero_empty():
    assert triples_sum_to_zero([]) is False


def test_triples_sum_to_zero_negative_only():
    # All negatives, no zero-sum triple -> False
    assert triples_sum_to_zero([-1, -2, -3]) is False


def test_triples_sum_to_zero_triple_at_end():
    # Only the final triple (7, 11, -18) sums to zero, forcing full iteration
    assert triples_sum_to_zero([5, 7, 11, -18]) is True
