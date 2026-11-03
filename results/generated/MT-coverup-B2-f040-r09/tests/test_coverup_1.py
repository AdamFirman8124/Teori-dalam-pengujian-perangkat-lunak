# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

"""Tests for f040.triples_sum_to_zero.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or teardown is required; each test only relies on its
own local inputs, avoiding any state pollution.
"""

from f040 import triples_sum_to_zero


def test_triple_found_immediately():
    """Covers lines 3-7: first examined triple sums to zero (True branch of line 6)."""
    assert triples_sum_to_zero([1, 2, -3]) is True


def test_triple_found_after_k_loop_continues():
    """Covers the k-loop continuing after a failed condition on line 6."""
    # 1 + 2 + 4 != 0, but 1 + 2 + (-3) == 0.
    assert triples_sum_to_zero([1, 2, 4, -3]) is True


def test_triple_found_after_j_loop_continues():
    """Covers the j-loop continuing after failed conditions."""
    # No triple starting with j=1 works; j=2 with k=3 gives 1 + 3 - 4 == 0.
    assert triples_sum_to_zero([1, 2, 3, -4]) is True


def test_triple_found_after_i_loop_continues():
    """Covers the i-loop continuing after failed conditions."""
    # No triple containing 10 sums to zero; i=1 gives 1 + 2 - 3 == 0.
    assert triples_sum_to_zero([10, 1, 2, -3]) is True


def test_triple_found_with_zeros():
    """Covers the equality branch with duplicate zero values."""
    assert triples_sum_to_zero([0, 0, 0]) is True


def test_no_triple_sums_to_zero():
    """Covers line 8 and the False branch of the condition on line 6."""
    assert triples_sum_to_zero([1, 2, 3, 4]) is False


def test_empty_list():
    """Covers the branch where the i-loop (line 3) never executes."""
    assert triples_sum_to_zero([]) is False


def test_single_element():
    """Covers the branch where the j-loop (line 4) never executes."""
    assert triples_sum_to_zero([1]) is False


def test_two_elements():
    """Covers the branch where the k-loop (line 5) never executes."""
    assert triples_sum_to_zero([1, -1]) is False
