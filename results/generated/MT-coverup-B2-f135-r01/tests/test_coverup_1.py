# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

"""Tests for f135.can_arrange.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test works on local data only.

Coverage targets:
- line 3 (ind = -1) and line 4 (i = 1): executed on every call.
- line 5 while-condition True branch: any list with len(arr) > 1.
- line 5 while-condition False branch: empty list / single-element list
  (loop body never runs, returns -1 immediately).
- line 6 if-condition True branch: an element smaller than its predecessor.
- line 6 if-condition False branch: an element >= its predecessor.
- line 7 (ind = i): executed when the if-branch is taken.
- line 8 (i += 1) and line 9 (return ind): executed on every non-empty
  loop run.
"""

import pytest

from f135 import can_arrange


def test_can_arrange_empty_list_returns_minus_one():
    # Covers the while-condition False branch on the very first check
    # (lines 3-4 run, loop body skipped, line 9 returns -1).
    assert can_arrange([]) == -1


def test_can_arrange_single_element_returns_minus_one():
    # Also covers the while-condition False branch (1 < 1 is False).
    assert can_arrange([7]) == -1


def test_can_arrange_no_descent_returns_minus_one():
    # Covers the if-condition False branch (arr[i] >= arr[i-1]) for every
    # iteration, plus both while branches (loop runs then exits).
    assert can_arrange([1, 2, 3]) == -1


def test_can_arrange_finds_largest_descent_index():
    # Covers the if-condition True branch (4 > 3 at i=3 sets ind=3) and
    # the if-condition False branch (i=1 and i=2 are ascents), plus both
    # while branches.
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_strictly_decreasing_returns_last_index():
    # Every iteration takes the if-True branch; the final assignment
    # (line 7) must be the last descent index, verifying ind is
    # overwritten rather than kept from the first descent.
    assert can_arrange([5, 4, 3, 2]) == 3


def test_can_arrange_descents_then_ascent_keeps_last_descent():
    # Descents at i=1 and i=2, then an ascent at i=3 (if-False branch
    # after if-True branches): ind must remain 2.
    assert can_arrange([9, 5, 1, 8]) == 2


def test_can_arrange_equal_neighbors_are_not_descents():
    # arr[i] == arr[i-1] must take the if-False branch (strict '<').
    assert can_arrange([1, 1, 1]) == -1


def test_can_arrange_two_elements_descent():
    # Minimal case exercising the loop body exactly once with the
    # if-True branch.
    assert can_arrange([2, 1]) == 1
