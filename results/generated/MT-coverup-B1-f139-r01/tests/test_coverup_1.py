# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

from f139 import special_factorial


def test_special_factorial_positive_integer():
    assert special_factorial(4) == 288


def test_special_factorial_zero():
    assert special_factorial(0) == 1
