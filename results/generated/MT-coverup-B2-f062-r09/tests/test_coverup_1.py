# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f062 import derivative


def test_derivative_returns_weighted_tail():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]


def test_derivative_handles_empty_input():
    assert derivative([]) == []
