# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

from f076 import is_simple_power


def test_n_is_one_and_x_is_one():
    assert is_simple_power(1, 1) is True


def test_n_is_one_and_x_is_not_one():
    assert is_simple_power(2, 1) is False
    assert is_simple_power(5, 1) is False
    assert is_simple_power(0, 1) is False


def test_x_is_one_n_is_not_one():
    # power = 1, while condition False immediately, returns True
    assert is_simple_power(1, 2) is True
    assert is_simple_power(1, 3) is True


def test_simple_power_true():
    # covers loop iterating multiple times and power == x True branch
    assert is_simple_power(8, 2) is True
    assert is_simple_power(9, 3) is True
    assert is_simple_power(16, 2) is True
    assert is_simple_power(27, 3) is True


def test_simple_power_false_power_exceeds():
    # covers loop iterating multiple times and power == x False branch
    assert is_simple_power(6, 2) is False
    assert is_simple_power(10, 3) is False
    assert is_simple_power(12, 2) is False


def test_while_never_entered_not_power():
    # covers power = 1, while False on first check, return False
    assert is_simple_power(0, 2) is False
