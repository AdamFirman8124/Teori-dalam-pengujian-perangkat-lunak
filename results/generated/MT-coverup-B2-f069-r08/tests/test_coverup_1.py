# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest

from f069 import search


def test_search_returns_greatest_value_with_sufficient_frequency():
    # Covers line 12 (frq allocation), lines 13-14 (counting loop),
    # line 16 (ans = -1), lines 17-19 (both branches of the if:
    # frq[i] >= i is True for i=1,2 and False for i=3,4), and line 21.
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_multiple_candidates_returns_largest():
    # Ensures the loop keeps updating ans (line 19) for the greatest
    # qualifying value, exercising the True branch multiple times.
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_valid_value_returns_minus_one():
    # Covers the False branch of the if on every iteration, so ans
    # stays -1 (lines 16 and 21 with the loop never taking the True branch).
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element_list():
    # Minimal input: frq has length 2, loop runs once with the True branch.
    assert search([1]) == 1


def test_search_single_element_no_match():
    # Minimal input where the only loop iteration takes the False branch.
    assert search([2]) == -1
