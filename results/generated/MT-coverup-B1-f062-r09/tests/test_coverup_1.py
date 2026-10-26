# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f062 import derivative


def test_derivative_executes_line_3():
    xs = [1, 2, 3, 4]
    result = derivative(xs)
    # enumerate pairs: (0,1),(1,2),(2,3),(3,4) -> [0,2,6,12]; slice [1:] drops first
    assert result == [2, 6, 12]
    # original list is not mutated
    assert xs == [1, 2, 3, 4]


def test_derivative_empty_list():
    assert derivative([]) == []


def test_derivative_single_element():
    # only element is dropped by [1:] slice
    assert derivative([5]) == []
