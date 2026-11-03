# file: project/f106/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

import pytest

from f106 import f


def test_f_mixed_even_and_odd():
    """
    Covers both branches of the if/else for multiple iterations:
      - even i  -> factorial of i (lines 6-8)
      - odd i   -> sum 1..i (lines 10-12)
    and the final return (line 13).
    Expected for n=5:
      i=1 (odd):  sum 1..1   = 1
      i=2 (even): 2!         = 2
      i=3 (odd):  sum 1..3   = 6
      i=4 (even): 4!         = 24
      i=5 (odd):  sum 1..5   = 15
    """
    assert f(5) == [1, 2, 6, 24, 15]


def test_f_single_odd():
    """Covers the odd branch with a single iteration (loop entered once)."""
    assert f(1) == [1]


def test_f_single_even():
    """Covers the even branch with a single iteration (loop entered once)."""
    assert f(2) == [1, 2]


def test_f_zero_iterations():
    """Covers the zero-iteration branch of the for loop (n < 1)."""
    assert f(0) == []
