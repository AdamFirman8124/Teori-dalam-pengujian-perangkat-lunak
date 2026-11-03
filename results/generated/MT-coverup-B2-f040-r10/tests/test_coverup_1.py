# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f040 import triples_sum_to_zero


def test_triple_exists_returns_true():
    # A triple of distinct indices sums to zero -> True (covers lines 3-7)
    assert triples_sum_to_zero([1, 3, -4, 5]) is True
    assert triples_sum_to_zero([1, 3, -2, 1]) is True


def test_triple_found_late_in_loops():
    # The zero-sum triple is only found with i > 0 and k near the end,
    # so all three loops must keep iterating before returning True.
    assert triples_sum_to_zero([10, 1, 2, 3, -5]) is True


def test_no_triple_returns_false():
    # No combination of three distinct indices sums to zero -> False
    # (covers lines 3-6 falling through to line 8)
    assert triples_sum_to_zero([1, 2, 3]) is False
    assert triples_sum_to_zero([1, 2, 3, 4, 5]) is False


def test_pair_sums_to_zero_but_no_triple():
    # A pair cancels out, but every triple is nonzero -> False
    assert triples_sum_to_zero([1, -1, 2]) is False


def test_empty_list_returns_false():
    # Outer loop body never runs; falls straight to line 8
    assert triples_sum_to_zero([]) is False


def test_fewer_than_three_elements_returns_false():
    # Inner loops never execute; must still return False via line 8
    assert triples_sum_to_zero([1]) is False
    assert triples_sum_to_zero([1, -1]) is False


def test_all_zeroes_returns_true():
    assert triples_sum_to_zero([0, 0, 0]) is True


def test_negative_only_triple():
    assert triples_sum_to_zero([-1, -2, 3]) is True


def test_result_is_bool():
    result = triples_sum_to_zero([2, 7, 4])
    assert result is False
    result = triples_sum_to_zero([2, 7, -9])
    assert result is True
