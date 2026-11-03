# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f060 import sum_to_n


def test_sum_to_n_basic():
    """Calling the function executes line 3 and returns the sum 0..n."""
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15  # 0+1+2+3+4+5


def test_sum_to_n_negative():
    """For negative n, range(n+1) is empty, so the result is 0."""
    assert sum_to_n(-1) == 0
    assert sum_to_n(-10) == 0


def test_sum_to_n_large():
    """Verify the closed-form formula n*(n+1)/2 for a larger input."""
    n = 100
    assert sum_to_n(n) == n * (n + 1) // 2
