# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

"""Tests for f043.pairs_sum_to_zero.

Covers all previously unexecuted lines (3-7):
- line 3: outer loop over enumerate(l) (any call, including empty list)
- line 4: inner loop over range(i + 1, len(l)) (list with >= 1 element)
- line 5: the comparison l1 + l[j] == 0 (list with >= 2 elements)
- line 6: return True (a pair summing to zero exists)
- line 7: return False (no pair sums to zero)

The function under test is pure (no I/O, no globals mutated), so no
monkeypatching or cleanup is required.
"""

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_true_covers_return_true():
    # Lines 3-6: outer loop, inner loop, comparison, and early return True.
    assert pairs_sum_to_zero([1, -1]) is True
    # Pair found later in the list, exercising several inner-loop iterations.
    assert pairs_sum_to_zero([2, 3, 4, -3]) is True
    # Zero paired with itself at distinct indices.
    assert pairs_sum_to_zero([0, 0]) is True


def test_pairs_sum_to_zero_false_covers_return_false():
    # Lines 3-5 and 7: loops run fully, comparison never true, fall through.
    assert pairs_sum_to_zero([1, 2, 3]) is False
    assert pairs_sum_to_zero([1, 2, 3, 4]) is False


def test_pairs_sum_to_zero_edge_cases():
    # Empty list: line 3 executes, inner loop never entered, line 7 returns False.
    assert pairs_sum_to_zero([]) is False
    # Single element: line 4 executes with an empty range, then line 7.
    assert pairs_sum_to_zero([5]) is False
    # No element is the negation of another, including duplicates of same sign.
    assert pairs_sum_to_zero([1, 1, 2]) is False
