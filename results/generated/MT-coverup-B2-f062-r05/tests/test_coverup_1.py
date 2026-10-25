# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f062 import derivative


def test_derivative_standard_polynomial():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]


def test_derivative_linear():
    assert derivative([1, 2, 3]) == [2, 6]


def test_derivative_constant_only_returns_empty():
    assert derivative([5]) == []


def test_derivative_empty_list_returns_empty():
    assert derivative([]) == []


def test_derivative_does_not_mutate_input():
    xs = [3, 1, 2, 4, 5]
    original = list(xs)
    result = derivative(xs)
    assert xs == original
    assert result is not xs
