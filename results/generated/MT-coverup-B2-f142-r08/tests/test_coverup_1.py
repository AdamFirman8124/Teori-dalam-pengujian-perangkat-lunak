# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

"""Tests for f142.sum_squares covering all missing lines and branches.

sum_squares(lst):
    - i % 3 == 0            -> lst[i] ** 2   (squared)
    - i % 4 == 0, i % 3 != 0 -> lst[i] ** 3   (cubed)
    - otherwise              -> lst[i]        (unchanged)

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required; nothing can pollute state.
"""

from f142 import sum_squares


def test_empty_list():
    """Loop body never executes; result stays [] and sum([]) == 0."""
    assert sum_squares([]) == 0


def test_index_multiple_of_three_is_squared():
    """Covers branch i % 3 == 0 -> True (i=0 and i=3) and the squared append."""
    lst = [1, 2, 3, 4]
    # i=0: 1**2 = 1, i=1: 2 (else), i=2: 3 (else), i=3: 4**2 = 16
    assert sum_squares(lst) == 1 + 2 + 3 + 16 == 22


def test_index_multiple_of_four_but_not_three_is_cubed():
    """Covers the elif branch (i % 4 == 0 and i % 3 != 0 -> True) for i=4 and i=8."""
    lst = [0] * 4 + [5] + [0] * 3 + [9]  # values at indices 4 and 8
    # i=4: 5**3 = 125, i=8: 9**3 = 729; all zeros contribute nothing
    assert sum_squares(lst) == 125 + 729 == 854


def test_other_indices_added_unchanged():
    """Covers the else branch (both conditions False) for i=1, 2, 5, 7."""
    lst = [0, 1, 2, 0, 0, 5, 0, 7]
    # i=1 -> 1, i=2 -> 2, i=5 -> 5, i=7 -> 7; every other entry is 0
    assert sum_squares(lst) == 1 + 2 + 5 + 7 == 15


def test_index_multiple_of_twelve_takes_modulo_three_branch():
    """Index 12 satisfies both i % 3 == 0 and i % 4 == 0; the first branch wins."""
    lst = [0] * 12 + [2]
    assert sum_squares(lst) == 2 ** 2 == 4


def test_combined_coverage():
    """A single run over indices 0..9 exercises every line and branch."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = (
        1 ** 2    # i=0  (i % 3 == 0)
        + 2       # i=1  (else)
        + 3       # i=2  (else)
        + 4 ** 2  # i=3  (i % 3 == 0)
        + 5 ** 3  # i=4  (i % 4 == 0 and i % 3 != 0)
        + 6       # i=5  (else)
        + 7 ** 2  # i=6  (i % 3 == 0)
        + 8       # i=7  (else)
        + 9 ** 3  # i=8  (i % 4 == 0 and i % 3 != 0)
        + 10 ** 2  # i=9  (i % 3 == 0)
    )
    assert expected == 1039
    assert sum_squares(lst) == expected
