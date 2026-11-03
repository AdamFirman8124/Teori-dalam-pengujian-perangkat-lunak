# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f062 import derivative


def test_derivative_multiplies_by_index_and_skips_first():
    # [0*1, 1*2, 2*3] == [0, 2, 6]; dropping the first element yields [2, 6]
    assert derivative([1, 2, 3]) == [2, 6]


def test_derivative_empty_list():
    # Empty input: comprehension produces [], slicing yields []
    assert derivative([]) == []


def test_derivative_single_element():
    # Single element: [0*7] == [0]; slicing off the first element yields []
    assert derivative([7]) == []
