# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

import pytest

from f046 import fib4


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 0),
        (2, 2),
        (3, 0),
    ],
)
def test_fib4_base_cases(n, expected):
    """Covers lines 3-5: initial results list and the n < 4 early return."""
    assert fib4(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, 2),    # 0 + 0 + 2 + 0
        (5, 4),    # 0 + 2 + 0 + 2
        (6, 8),    # 2 + 0 + 2 + 4
        (7, 14),   # 0 + 2 + 4 + 8
        (8, 28),   # 2 + 4 + 8 + 14
        (10, 104),
    ],
)
def test_fib4_recursive_cases(n, expected):
    """Covers lines 7-11: the loop appending/popping and the final return."""
    assert fib4(n) == expected


def test_fib4_is_pure():
    """Calling fib4 repeatedly yields identical results (no state pollution)."""
    assert fib4(8) == 28
    assert fib4(8) == 28
    assert fib4(3) == 0
