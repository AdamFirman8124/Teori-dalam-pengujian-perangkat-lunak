# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

from f139 import special_factorial


def test_special_factorial_zero():
    assert special_factorial(0) == 1


def test_special_factorial_one():
    assert special_factorial(1) == 1


def test_special_factorial_two():
    assert special_factorial(2) == 2


def test_special_factorial_three():
    assert special_factorial(3) == 12


def test_special_factorial_four():
    assert special_factorial(4) == 288


def test_special_factorial_five():
    assert special_factorial(5) == 34560
