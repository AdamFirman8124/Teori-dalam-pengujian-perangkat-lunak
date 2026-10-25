# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_too_heavy_returns_false():
    # sum(q) > w -> line 3 branch True, line 4
    assert will_it_fly([3, 2, 3], 1) is False
    assert will_it_fly([5], 4) is False


def test_not_palindromic_returns_false():
    # sum <= w but q[i] != q[j] -> lines 6-9
    assert will_it_fly([1, 2], 5) is False
    assert will_it_fly([1, 2, 3, 4], 100) is False


def test_balanced_palindrome_returns_true():
    # loop runs, i+=1 / j-=1 execute (lines 10-11), then return True (line 12)
    assert will_it_fly([3, 2, 3], 9) is True
    assert will_it_fly([1, 2, 1], 5) is True


def test_even_length_palindrome_returns_true():
    # exercises the loop with even-length q
    assert will_it_fly([2, 2], 4) is True
    assert will_it_fly([1, 2, 2, 1], 6) is True


def test_single_element_returns_true():
    # while loop never runs (i == j), line 12 reached
    assert will_it_fly([1], 1) is True


def test_empty_list_returns_true():
    # len(q)-1 == -1, loop skipped, line 12 reached
    assert will_it_fly([], 0) is True
