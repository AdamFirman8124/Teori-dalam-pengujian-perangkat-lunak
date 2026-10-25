# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

from f076 import is_simple_power


def test_is_simple_power_when_exponent_is_one():
    assert is_simple_power(1, 1) is True
    assert is_simple_power(2, 1) is False


def test_is_simple_power_for_exact_power():
    assert is_simple_power(8, 2) is True


def test_is_simple_power_for_non_power():
    assert is_simple_power(7, 2) is False


def test_is_simple_power_without_entering_loop():
    assert is_simple_power(1, 2) is True
