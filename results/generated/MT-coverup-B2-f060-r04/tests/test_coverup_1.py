# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f060 import sum_to_n


def test_sum_to_n_positive():
    # Sum of integers from 0 to n inclusive
    assert sum_to_n(5) == 15  # 0+1+2+3+4+5
    assert sum_to_n(1) == 1
    assert sum_to_n(10) == 55


def test_sum_to_n_zero():
    # range(1) yields only 0, so the sum is 0
    assert sum_to_n(0) == 0


def test_sum_to_n_negative():
    # range(n+1) is empty for n < 0, so the sum is 0
    assert sum_to_n(-1) == 0
    assert sum_to_n(-10) == 0


def test_sum_to_n_matches_reference():
    # Cross-check against an independent computation
    for n in range(0, 20):
        assert sum_to_n(n) == sum(range(n + 1))
        assert sum_to_n(n) == n * (n + 1) // 2
