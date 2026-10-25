# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

from f150 import x_or_y


def test_x_or_y_returns_y_when_n_is_one():
    assert x_or_y(1, "x", "y") == "y"


def test_x_or_y_returns_y_for_composite_number():
    assert x_or_y(4, "x", "y") == "y"


def test_x_or_y_returns_x_for_prime_number():
    assert x_or_y(5, "x", "y") == "x"
