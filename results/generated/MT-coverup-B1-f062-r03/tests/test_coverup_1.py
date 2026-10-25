# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f062 import derivative


def test_derivative_multiplies_each_coefficient_by_its_index():
    assert derivative([5, 4, 3, 2]) == [4, 6, 6]
