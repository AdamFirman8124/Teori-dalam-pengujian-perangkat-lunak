# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f104 import unique_digits


def test_unique_digits_mixed_matches_and_sorting():
    """Covers init (line 3), loop (line 4), both branches of the all() check
    (line 5), append (line 6), and sorted return (line 7)."""
    result = unique_digits([15, 33, 1422, 1])
    # 15 -> digits 1,5 (odd); 33 -> 3,3 (odd); 1422 -> contains 4 and 2 (even); 1 -> odd
    assert result == [1, 15, 33]
    # Verify the returned list is sorted regardless of input order
    assert result == sorted(result)


def test_unique_digits_no_matches_returns_empty_sorted_list():
    """Covers the if-false branch (line 5) and returning an empty sorted list
    (lines 4 and 7)."""
    result = unique_digits([152, 323, 1422, 10])
    assert result == []
    assert isinstance(result, list)


def test_unique_digits_empty_input():
    """Covers the loop executing zero times (line 4) and the return (line 7)."""
    assert unique_digits([]) == []


def test_unique_digits_all_match_out_of_order_input():
    """Covers append being called repeatedly (line 6) and sorting of the
    accumulated elements (line 7)."""
    result = unique_digits([135, 9, 57, 3])
    assert result == [3, 9, 57, 135]


def test_unique_digits_single_digit_even_and_odd():
    """Exercises int(c) % 2 == 1 on single-character strings for both parities."""
    result = unique_digits([2, 3, 4, 5])
    assert result == [3, 5]
