# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

"""Tests for f142/__init__.py::sum_squares.

Covers all missing lines/branches:
- line 3:      result = [] (executed on every call)
- line 4:      loop body (including zero-iteration case via empty list)
- line 5-6:    i % 3 == 0 branch (indices 0, 3, 6)
- line 7-8:    i % 4 == 0 and i % 3 != 0 branch (indices 4, 8)
- line 10:     else branch (indices 1, 2, 5, 7)
- line 11:     return sum(result)

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching/teardown is required to avoid state pollution.
"""

from f142 import sum_squares


def test_sum_squares_all_branches():
    """Exercise every branch: square (i%3==0), cube (i%4==0 and i%3!=0), identity."""
    lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    # index: 0    1  2  3     4     5  6     7  8
    # branch: sq  id id sq    cube  id sq    id cube
    expected = (
        2 ** 2   # i=0: 0 % 3 == 0 -> square
        + 3      # i=1: else -> identity
        + 4      # i=2: else -> identity
        + 5 ** 2   # i=3: 3 % 3 == 0 -> square
        + 6 ** 3   # i=4: 4 % 4 == 0 and 4 % 3 != 0 -> cube
        + 7      # i=5: else -> identity
        + 8 ** 2   # i=6: 6 % 3 == 0 -> square
        + 9      # i=7: else -> identity
        + 10 ** 3  # i=8: 8 % 4 == 0 and 8 % 3 != 0 -> cube
    )
    assert expected == 1332
    assert sum_squares(lst) == expected


def test_sum_squares_empty_list():
    """Zero loop iterations: result stays [] and sum([]) == 0."""
    assert sum_squares([]) == 0


def test_sum_squares_single_element_square_branch():
    """Single element at index 0 hits the i % 3 == 0 branch only."""
    assert sum_squares([7]) == 49


def test_sum_squares_single_element_cube_branch():
    """A list long enough that only index 4 hits the cube branch."""
    # indices 0..4: sq, id, id, sq, cube
    assert sum_squares([1, 2, 3, 4, 5]) == 1 + 2 + 3 + 16 + 125
