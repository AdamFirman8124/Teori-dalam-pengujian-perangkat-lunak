# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f062 import derivative


def test_derivative_empty():
    assert derivative([]) == []


def test_derivative_constant():
    assert derivative([5]) == []
    assert derivative([0]) == []


def test_derivative_linear():
    assert derivative([0, 1]) == [1]
    assert derivative([3, 2]) == [2]


def test_derivative_quadratic():
    assert derivative([1, 2, 3]) == [2, 6]


def test_derivative_cubic():
    assert derivative([0, 0, 0, 1]) == [0, 0, 3]
    assert derivative([1, 1, 1, 1]) == [1, 2, 3]


def test_derivative_does_not_mutate_input():
    xs = [1, 2, 3, 4]
    original = list(xs)
    result = derivative(xs)
    assert result == [2, 6, 12]
    assert xs == original
