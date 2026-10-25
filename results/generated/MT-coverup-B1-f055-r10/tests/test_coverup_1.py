# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

import pytest

from f055 import fib


def test_fib_base_case_zero():
    assert fib(0) == 0


def test_fib_base_case_one():
    assert fib(1) == 1


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 1),
        (3, 2),
        (5, 5),
        (10, 55),
    ],
)
def test_fib_recursive(n, expected):
    assert fib(n) == expected
