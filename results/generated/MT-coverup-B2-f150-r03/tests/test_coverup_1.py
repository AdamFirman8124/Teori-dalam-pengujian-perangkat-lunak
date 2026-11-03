# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

import pytest

from f150 import x_or_y


def test_x_or_y_returns_y_when_n_is_one():
    # Covers lines 3-4: the `if n == 1` branch.
    assert x_or_y(1, "x", "y") == "y"
    assert x_or_y(1, 10, 20) == 20


def test_x_or_y_returns_y_when_n_is_composite():
    # Covers lines 5-7: loop entered and a divisor found, returning y.
    assert x_or_y(4, "x", "y") == "y"   # divisible by 2
    assert x_or_y(9, "x", "y") == "y"   # divisible by 3
    assert x_or_y(15, 100, -1) == -1    # divisible by 3 and 5


def test_x_or_y_returns_x_when_n_is_prime():
    # Covers lines 9-10: the for-else branch (loop exhausts without break).
    # n=2 makes range(2, 2) empty, exercising the else via loop exhaustion.
    assert x_or_y(2, "x", "y") == "x"
    # n=3 runs the loop body once with no divisor found.
    assert x_or_y(3, "x", "y") == "x"
    assert x_or_y(7, 1, 2) == 1
    assert x_or_y(13, True, False) is True
