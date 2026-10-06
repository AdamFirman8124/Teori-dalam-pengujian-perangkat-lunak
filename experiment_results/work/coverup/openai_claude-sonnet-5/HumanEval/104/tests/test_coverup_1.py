# file: script_104.py:1-17
# asked: {"lines": [13, 14, 15, 16, 17], "branches": [[14, 15], [14, 17], [15, 14], [15, 16]]}
# gained: {"lines": [13, 14, 15, 16, 17], "branches": [[14, 15], [14, 17], [15, 14], [15, 16]]}

import pytest
from script_104 import unique_digits


def test_unique_digits_mixed_numbers():
    """Test with a mix of numbers with odd and even digits."""
    result = unique_digits([15, 33, 1422, 1])
    assert result == [1, 15, 33]


def test_unique_digits_all_even_digits():
    """Test with numbers that all contain even digits."""
    result = unique_digits([152, 323, 1422, 10])
    assert result == []


def test_unique_digits_all_odd_digits():
    """Test with numbers that only have odd digits."""
    result = unique_digits([13, 57, 91, 3, 7])
    assert result == [3, 7, 13, 57, 91]


def test_unique_digits_single_digit_odd():
    """Test with single-digit odd numbers."""
    result = unique_digits([1, 3, 5, 7, 9])
    assert result == [1, 3, 5, 7, 9]


def test_unique_digits_single_digit_even():
    """Test with single-digit even numbers."""
    result = unique_digits([2, 4, 6, 8])
    assert result == []


def test_unique_digits_empty_list():
    """Test with an empty list."""
    result = unique_digits([])
    assert result == []


def test_unique_digits_unsorted_input():
    """Test that output is sorted even when input is not."""
    result = unique_digits([99, 11, 777, 33, 1])
    assert result == [1, 11, 33, 99, 777]


def test_unique_digits_large_numbers_with_odd_digits():
    """Test with larger numbers containing only odd digits."""
    result = unique_digits([13579, 97531, 11111])
    assert result == [11111, 13579, 97531]


def test_unique_digits_numbers_with_zero():
    """Test that numbers containing 0 (even) are excluded."""
    result = unique_digits([101, 303, 505, 13, 57])
    assert result == [13, 57]
