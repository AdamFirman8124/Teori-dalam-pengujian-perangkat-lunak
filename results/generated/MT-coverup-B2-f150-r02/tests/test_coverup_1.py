# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

from f150 import x_or_y


def test_x_or_y_n_equals_one_returns_y():
    x = object()
    y = object()
    assert x_or_y(1, x, y) is y


def test_x_or_y_even_composite_returns_y():
    x = object()
    y = object()
    assert x_or_y(4, x, y) is y


def test_x_or_y_odd_composite_returns_y_after_non_divisor():
    x = object()
    y = object()
    assert x_or_y(9, x, y) is y


def test_x_or_y_prime_returns_x():
    x = object()
    y = object()
    assert x_or_y(5, x, y) is x


def test_x_or_y_two_returns_x_without_loop_iterations():
    x = object()
    y = object()
    assert x_or_y(2, x, y) is x
