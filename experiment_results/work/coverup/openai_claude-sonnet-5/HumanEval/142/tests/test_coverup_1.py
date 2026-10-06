# file: script_142.py:1-20
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19, 20], "branches": [[13, 14], [13, 20], [14, 15], [14, 16], [16, 17], [16, 19]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19, 20], "branches": [[13, 14], [13, 20], [14, 15], [14, 16], [16, 17], [16, 19]]}

import pytest
from script_142 import sum_squares


def test_sum_squares_empty_list():
    """Test with empty list"""
    assert sum_squares([]) == 0


def test_sum_squares_single_element():
    """Test with single element at index 0 (multiple of 3)"""
    assert sum_squares([5]) == 25  # 5^2 = 25


def test_sum_squares_example_1():
    """Test with [1,2,3] - should return 6"""
    # Index 0: multiple of 3 -> 1^2 = 1
    # Index 1: neither -> 2
    # Index 2: neither -> 3
    # Sum: 1 + 2 + 3 = 6
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_example_2():
    """Test with [-1,-5,2,-1,-5] - should return -126"""
    # Index 0: multiple of 3 -> (-1)^2 = 1
    # Index 1: neither -> -5
    # Index 2: neither -> 2
    # Index 3: multiple of 3 -> (-1)^2 = 1
    # Index 4: multiple of 4 and not 3 -> (-5)^3 = -125
    # Sum: 1 + (-5) + 2 + 1 + (-125) = -126
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_index_multiple_of_4_not_3():
    """Test with element at index 4 (multiple of 4 but not 3)"""
    # Need at least 5 elements to reach index 4
    # Index 0: multiple of 3 -> 1^2 = 1
    # Index 1: neither -> 0
    # Index 2: neither -> 0
    # Index 3: multiple of 3 -> 1^2 = 1
    # Index 4: multiple of 4 and not 3 -> 2^3 = 8
    # Sum: 1 + 0 + 0 + 1 + 8 = 10
    assert sum_squares([1, 0, 0, 1, 2]) == 10


def test_sum_squares_index_multiple_of_both_3_and_4():
    """Test with element at index 12 (multiple of both 3 and 4)"""
    # Index 12 is divisible by both 3 and 4, so condition i%3==0 takes precedence
    lst = [0] * 13
    lst[12] = 5
    # Index 12: multiple of 3 -> 5^2 = 25
    assert sum_squares(lst) == 25


def test_sum_squares_neither_multiple():
    """Test with indices that are neither multiples of 3 nor 4"""
    # Index 0: multiple of 3 -> 10^2 = 100
    # Index 1: neither -> 5
    # Index 2: neither -> 7
    # Sum: 100 + 5 + 7 = 112
    assert sum_squares([10, 5, 7]) == 112


def test_sum_squares_negative_numbers():
    """Test with negative numbers at various positions"""
    # Index 0: multiple of 3 -> (-3)^2 = 9
    # Index 1: neither -> 2
    # Index 2: neither -> -4
    # Index 3: multiple of 3 -> (-2)^2 = 4
    # Index 4: multiple of 4 and not 3 -> (-2)^3 = -8
    # Sum: 9 + 2 + (-4) + 4 + (-8) = 3
    assert sum_squares([-3, 2, -4, -2, -2]) == 3
