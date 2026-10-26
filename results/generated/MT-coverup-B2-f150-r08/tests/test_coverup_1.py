# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

import pytest

from f150 import x_or_y


def test_x_or_y_n_equals_one_returns_y():
    assert x_or_y(1, 10, 20) == 20


def test_x_or_y_composite_returns_y():
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(9, 10, 20) == 20


def test_x_or_y_prime_returns_x():
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 10, 20) == 10
    assert x_or_y(7, 10, 20) == 10
