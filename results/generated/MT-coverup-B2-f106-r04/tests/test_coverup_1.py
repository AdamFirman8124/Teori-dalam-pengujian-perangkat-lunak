# file: project/f106/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

import pytest

from f106 import f


def test_f_mixed_parity():
    """Covers both branches: even i (factorial) and odd i (triangular sum)."""
    # i=1 (odd): 1
    # i=2 (even): 2! = 2
    # i=3 (odd): 1+2+3 = 6
    # i=4 (even): 4! = 24
    # i=5 (odd): 1+2+3+4+5 = 15
    assert f(5) == [1, 2, 6, 24, 15]


def test_f_even_only():
    """Covers the even branch repeatedly."""
    assert f(2) == [1, 2]
    assert f(4) == [1, 2, 6, 24]


def test_f_odd_only():
    """Covers the odd branch repeatedly."""
    assert f(1) == [1]
    assert f(3) == [1, 2, 6]


def test_f_zero():
    """Covers the case where the loop body never executes."""
    assert f(0) == []


def test_f_negative():
    """Covers the case where range(1, n+1) is empty for negative n."""
    assert f(-5) == []
