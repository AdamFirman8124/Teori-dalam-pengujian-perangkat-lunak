# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f060 import sum_to_n


def test_sum_to_n_zero():
    """sum_to_n(0) sums range(1) == [0], so the result must be 0."""
    assert sum_to_n(0) == 0


def test_sum_to_n_positive():
    """sum_to_n(5) sums 0+1+2+3+4+5 == 15."""
    assert sum_to_n(5) == 15


def test_sum_to_n_one():
    """sum_to_n(1) sums 0+1 == 1."""
    assert sum_to_n(1) == 1


def test_sum_to_n_negative():
    """For n < 0, range(n+1) is empty, so the sum must be 0."""
    assert sum_to_n(-1) == 0
    assert sum_to_n(-10) == 0
