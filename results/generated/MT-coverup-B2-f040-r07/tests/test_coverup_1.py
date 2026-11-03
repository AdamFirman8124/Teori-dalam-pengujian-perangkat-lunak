# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f040 import triples_sum_to_zero


def test_finds_triple_summing_to_zero():
    """Covers lines 3-7: loops run, a triple sums to zero, True is returned."""
    # The first checked triple (1, 2, 3) does not sum to zero, forcing the
    # loops to continue; (1, 2, -3) does, exercising loop continuation
    # branches and the True return path.
    assert triples_sum_to_zero([1, 2, 3, -3]) is True


def test_triple_at_exact_positions():
    """Covers the triple check succeeding on the very first triple examined."""
    assert triples_sum_to_zero([-1, 2, -1]) is True


def test_no_triple_summing_to_zero():
    """Covers lines 3-6 and line 8: all triples checked, none sum to zero."""
    assert triples_sum_to_zero([1, 2, 3]) is False


def test_shorter_than_three_elements():
    """Covers line 3 and line 8 when inner loops have zero iterations."""
    assert triples_sum_to_zero([]) is False
    assert triples_sum_to_zero([1]) is False
    assert triples_sum_to_zero([1, 2]) is False


def test_negative_only_list():
    """Full traversal with negatives, taking the False path."""
    assert triples_sum_to_zero([-1, -2, -3, -4]) is False


def test_zero_in_list_without_triple():
    """A zero element alone is not enough for a triple to sum to zero."""
    assert triples_sum_to_zero([0, 5, 10]) is False
