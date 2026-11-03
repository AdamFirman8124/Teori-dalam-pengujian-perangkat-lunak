# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

"""Tests for f146.specialFilter covering all lines and branches (lines 4-12)."""

from f146 import specialFilter


def test_specialFilter_empty_list():
    """Executes lines 4, 5 and 12: count initialized, loop body skipped, return 0."""
    assert specialFilter([]) == 0


def test_specialFilter_no_numbers_above_ten():
    """Executes line 6 with the False branch: loop runs but body never executes."""
    assert specialFilter([10, 9, -73, 0]) == 0


def test_specialFilter_above_ten_but_not_both_digits_odd():
    """Executes lines 6-9; the inner condition fails so line 10 is never reached.

    Covers both short-circuit paths of the 'and' on line 9:
    - 21/45: first digit even (second check skipped)
    - 12/100: first digit odd but last digit even
    """
    assert specialFilter([12, 21, 100, 45]) == 0


def test_specialFilter_counts_numbers_with_odd_first_and_last_digits():
    """Executes all lines including line 10 (count increment) and line 12."""
    assert specialFilter([15, 33, 97, 11]) == 4


def test_specialFilter_mixed_input():
    """Full behaviour check mixing all branches in a single call."""
    assert specialFilter([15, -73, 14, -15, 33, 10, 12, 109]) == 3
