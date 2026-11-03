# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

"""Tests for f147.get_max_triples (f147/__init__.py).

The function under test is pure (no I/O, no globals, no mutable state outside
its own locals), so no monkeypatching or teardown is required; each test is
self-contained and leaves no state behind.

Coverage plan:
  - A call with n >= 4 executes every line 3-10, including the True branch of
    the `if` on line 8 and the append on line 9.
  - n = 0, 1, 2 exercise the zero-iteration (loop-skipped) branches of the
    loops on lines 5, 6 and 7 respectively.
  - n = 3 exercises the False branch of the `if` on line 8 (innermost loop
    body runs exactly once, condition fails).
"""

import pytest

from f147 import get_max_triples


def test_n_zero_all_loops_skipped():
    # Line 3 builds an empty list; the loop on line 5 never runs.
    assert get_max_triples(0) == 0


def test_n_one_middle_loop_skipped():
    # A = [1]; the loop on line 6 never runs (range(1, 1) is empty).
    assert get_max_triples(1) == 0


def test_n_two_inner_loop_skipped():
    # A = [1, 3]; the loop on line 7 never runs (range(2, 2) is empty).
    assert get_max_triples(2) == 0


def test_n_three_condition_false_branch():
    # A = [1, 3, 7]; the single triple sums to 11, not a multiple of 3,
    # so the False branch of the `if` on line 8 is taken.
    assert get_max_triples(3) == 0


def test_n_four_condition_true_branch():
    # A = [1, 3, 7, 13]; exactly one triple, (1, 7, 13), sums to 21,
    # so the True branch of the `if` on line 8 and line 9 execute.
    assert get_max_triples(4) == 1


def test_n_five_documented_example():
    # A = [1, 3, 7, 13, 21]; the only valid triple is (1, 7, 13).
    assert get_max_triples(5) == 1


def test_n_six_multiple_valid_triples():
    # A = [1, 3, 7, 13, 21, 31]; elements congruent to 1 mod 3 are
    # {1, 7, 13, 31} and any three of them sum to a multiple of 3,
    # giving C(4, 3) = 4 valid triples; no triple containing an element
    # congruent to 0 mod 3 can qualify (only two such elements exist).
    assert get_max_triples(6) == 4


def test_result_is_non_negative_int_for_various_n():
    # Postcondition sanity check across a range of inputs.
    for n in range(0, 10):
        result = get_max_triples(n)
        assert isinstance(result, int)
        assert result >= 0
