# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f015 import string_sequence


def test_string_sequence_zero():
    """n = 0 yields a single element '0'."""
    result = string_sequence(0)
    assert result == '0'


def test_string_sequence_positive():
    """n > 0 yields all numbers from 0 to n inclusive, space-separated."""
    result = string_sequence(5)
    assert result == '0 1 2 3 4 5'
    assert result.split(' ') == [str(x) for x in range(6)]


def test_string_sequence_negative():
    """n < 0 yields an empty string since range(n + 1) is empty."""
    result = string_sequence(-1)
    assert result == ''
    assert result.split(' ') == ['']
