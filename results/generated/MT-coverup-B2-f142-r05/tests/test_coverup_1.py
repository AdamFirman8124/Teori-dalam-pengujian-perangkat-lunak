# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

import pytest

from f142 import sum_squares


def test_sum_squares_all_branches():
    """Exercise every branch: i%3==0 (square), i%4==0 and i%3!=0 (cube), else (identity)."""
    # index:  0  1  2  3   4   5
    lst = [2, 3, 4, 5, 6, 7]
    # i=0: 0%3==0 -> 2**2 = 4
    # i=1: else -> 3
    # i=2: else -> 4
    # i=3: 3%3==0 -> 5**2 = 25
    # i=4: 4%4==0 and 4%3!=0 -> 6**3 = 216
    # i=5: else -> 7
    expected = 2**2 + 3 + 4 + 5**2 + 6**3 + 7
    assert sum_squares(lst) == expected == 259


def test_sum_squares_empty_list():
    """Covers line 3 (result = []) and line 11 (return sum([])) with no loop iterations."""
    assert sum_squares([]) == 0


def test_sum_squares_single_element_square_branch():
    """Single element hits the i%3==0 square branch."""
    assert sum_squares([10]) == 100


def test_sum_squares_index_multiple_of_both_3_and_4():
    """Index 12 is divisible by both 3 and 4; the i%3==0 branch must win (elif's i%3!=0 is False)."""
    lst = [0] * 12 + [2]  # only index 12 is nonzero
    assert sum_squares(lst) == 2**2 == 4


def test_sum_squares_cube_branch_at_index_8():
    """Index 8 hits the cube branch (8%4==0 and 8%3!=0); other indices hit else/square."""
    lst = [1] * 9
    # i=0: 1**2=1; i=3: 1**2=1; i=6: 1**2=1; i=8: 1**3=1; others: 1
    assert sum_squares(lst) == 9


def test_sum_squares_negative_values():
    """Verify correct arithmetic with negative values across all branches."""
    # i=0: (-2)**2 = 4; i=1: -3; i=2: -4; i=3: (-5)**2 = 25; i=4: (-6)**3 = -216; i=5: -7
    lst = [-2, -3, -4, -5, -6, -7]
    expected = (-2) ** 2 + (-3) + (-4) + (-5) ** 2 + (-6) ** 3 + (-7)
    assert sum_squares(lst) == expected == -201
