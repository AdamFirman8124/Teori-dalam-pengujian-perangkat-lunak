# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

from f150 import x_or_y


def test_n_equals_1_returns_y():
    assert x_or_y(1, "x", "y") == "y"
    assert x_or_y(1, 10, 20) == 20


def test_n_equals_2_returns_x_empty_range():
    # range(2, 2) is empty, so for-else returns x
    assert x_or_y(2, "x", "y") == "x"


def test_prime_returns_x():
    assert x_or_y(3, "x", "y") == "x"
    assert x_or_y(5, 10, 20) == 10
    assert x_or_y(13, "a", "b") == "a"


def test_composite_returns_y():
    assert x_or_y(4, "x", "y") == "y"
    assert x_or_y(9, 10, 20) == 20
    assert x_or_y(15, "a", "b") == "b"
