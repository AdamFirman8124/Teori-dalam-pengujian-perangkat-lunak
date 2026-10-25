# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

from f150 import x_or_y


def test_n_equals_one_returns_y():
    assert x_or_y(1, "x", "y") == "y"
    assert x_or_y(1, 10, 20) == 20


def test_n_two_empty_range_returns_x():
    # range(2, 2) is empty, so for-else goes to else -> return x
    assert x_or_y(2, "x", "y") == "x"
    assert x_or_y(2, 10, 20) == 10


def test_prime_returns_x():
    # prime: loop completes without finding divisor -> else -> return x
    assert x_or_y(3, "x", "y") == "x"
    assert x_or_y(5, 10, 20) == 10
    assert x_or_y(13, "x", "y") == "x"


def test_composite_immediate_divisor_returns_y():
    # composite with divisor on first iteration: covers n % i == 0 True
    assert x_or_y(4, "x", "y") == "y"
    assert x_or_y(6, 10, 20) == 20


def test_composite_delayed_divisor_returns_y():
    # composite where first check is False then True: covers both outcomes of inner if
    # 9 % 2 != 0 (False), 9 % 3 == 0 (True)
    assert x_or_y(9, "x", "y") == "y"
    assert x_or_y(15, 10, 20) == 20
