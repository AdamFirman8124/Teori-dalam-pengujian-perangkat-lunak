# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Empty / single-element input: lines 3 and 7 execute, loop body does not.
        ([], 0),
        ([1], 0),
        # Palindrome: loop runs, if-condition takes the False branch (line 5).
        ([1, 2, 3, 2, 1], 0),
        # [1, 4, 4, 2]: i=0 compares 1 vs 2 (mismatch), i=1 compares 4 vs 4 (match).
        ([1, 4, 4, 2], 1),
        # Mismatch found: if-condition takes the True branch and line 6 executes.
        ([1, 4, 2], 1),
        ([1, 2, 3, 5, 4, 7, 9, 6], 4),
        # Mixed: exercises both branches of the if within one call.
        ([1, 2, 3, 4, 3, 2, 2], 1),
    ],
)
def test_smallest_change(arr, expected):
    result = smallest_change(arr)
    assert result == expected
    # Postcondition: result is a non-negative int no larger than half the length.
    assert isinstance(result, int)
    assert 0 <= result <= len(arr) // 2
