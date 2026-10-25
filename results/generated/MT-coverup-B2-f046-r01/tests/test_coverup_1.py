# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

import pytest

from f046 import fib4


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, 0), (1, 0), (2, 2), (3, 0)],
)
def test_fib4_initial_values(n, expected):
    assert fib4(n) == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [(4, 2), (5, 4), (6, 8)],
)
def test_fib4_iterative_values(n, expected):
    assert fib4(n) == expected
