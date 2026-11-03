# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f104 import unique_digits


def test_unique_digits_empty_input():
    """Covers line 3 (init), line 4 (loop over empty iterable) and line 7 (return)."""
    assert unique_digits([]) == []


def test_unique_digits_all_odd_digits():
    """Covers lines 3-7 including the True branch of the if on line 5 and append on line 6."""
    result = unique_digits([135, 1, 9, 111])
    assert result == [1, 9, 111, 135]


def test_unique_digits_mixed_digits():
    """Covers both branches of the if on line 5 (odd-only and even-containing numbers)."""
    result = unique_digits([15, 33, 1422, 1, 12, 135, 9])
    assert result == [1, 9, 15, 33, 135]


def test_unique_digits_no_odd_digit_numbers():
    """Covers the False branch of the if on line 5; line 6 (append) is skipped."""
    assert unique_digits([2, 20, 444, 68]) == []


def test_unique_digits_result_is_sorted():
    """Verifies the sorted() postcondition on line 7."""
    result = unique_digits([9, 1, 111, 3, 57])
    assert result == sorted(result)
    assert result == [1, 3, 9, 57, 111]


def test_unique_digits_does_not_mutate_input():
    """The function is pure: it must not modify its argument (avoids state pollution)."""
    data = [15, 33, 1422, 1]
    snapshot = list(data)
    result = unique_digits(data)
    assert data == snapshot
    assert result == [1, 15, 33]
