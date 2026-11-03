# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f104 import unique_digits


def test_unique_digits_empty_list():
    """Covers lines 3 and 7 with an empty input (loop body never runs)."""
    assert unique_digits([]) == []


def test_unique_digits_all_odd_digits():
    """Every element has only odd digits, so all are kept (line 6 executes)."""
    result = unique_digits([135, 1, 9, 111])
    assert result == [1, 9, 111, 135]


def test_unique_digits_mixed_digits_both_branches():
    """Covers both branches of the 'if' on line 5, the append on line 6,
    and the sorted return on line 7."""
    result = unique_digits([15, 33, 1422, 1, 12, 135, 9])
    # 15, 33, 1, 135, 9 have only odd digits; 1422 and 12 do not.
    assert result == [1, 9, 15, 33, 135]


def test_unique_digits_no_odd_digit_numbers():
    """No element qualifies, so the result is empty (False branch of line 5)."""
    assert unique_digits([2, 20, 444, 88]) == []


def test_unique_digits_sorts_unsorted_input():
    """The returned list must be sorted regardless of input order (line 7)."""
    result = unique_digits([9, 1, 111, 3, 757])
    assert result == [1, 3, 9, 111, 757]


def test_unique_digits_single_element_odd():
    """A single qualifying element is returned as a one-item sorted list."""
    assert unique_digits([7]) == [7]


def test_unique_digits_does_not_mutate_input():
    """The function must not modify its argument (no state pollution)."""
    data = [15, 22, 3]
    snapshot = list(data)
    result = unique_digits(data)
    assert data == snapshot
    assert result == [3, 15]
