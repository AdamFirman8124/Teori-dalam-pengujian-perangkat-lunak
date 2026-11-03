# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f104 import unique_digits


def test_unique_digits_all_odd_digits():
    """Covers lines 3-7: init, loop, True branch of the if, append, and return.

    Note: 1421 contains the even digit '2', so it is correctly excluded.
    """
    result = unique_digits([15, 33, 1421, 1, 15])
    assert result == [1, 15, 15, 33]
    # Every returned element must consist solely of odd digits
    for element in result:
        assert all(int(c) % 2 == 1 for c in str(element))


def test_unique_digits_multi_digit_odd_number():
    """Covers a multi-digit element where every digit is odd."""
    result = unique_digits([1357, 2468, 97531])
    assert result == [1357, 97531]
    assert 2468 not in result


def test_unique_digits_filters_out_even_digits():
    """Covers the False branch of the if on line 5 (elements are skipped)."""
    result = unique_digits([152, 3231, 14, 11, 111])
    assert result == [11, 111]
    assert 152 not in result
    assert 14 not in result


def test_unique_digits_empty_input():
    """Covers the loop-not-taken branch on line 4 (empty iterable)."""
    assert unique_digits([]) == []


def test_unique_digits_no_matching_elements():
    """Covers loop iterations where the if is always False, returning an empty list."""
    assert unique_digits([2, 4, 20, 100, 88]) == []


def test_unique_digits_single_element():
    """Covers a single loop iteration with a True branch."""
    assert unique_digits([7]) == [7]


def test_unique_digits_result_is_sorted():
    """Verifies the postcondition that the result is sorted (line 7)."""
    result = unique_digits([999, 1, 33, 5, 111])
    assert result == sorted(result)
    assert result == [1, 5, 33, 111, 999]
