# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f015 import string_sequence


def test_string_sequence_zero():
    result = string_sequence(0)
    assert result == "0"
    assert isinstance(result, str)


def test_string_sequence_positive():
    result = string_sequence(5)
    assert result == "0 1 2 3 4 5"
    assert result.split() == ["0", "1", "2", "3", "4", "5"]


def test_string_sequence_one():
    assert string_sequence(1) == "0 1"


def test_string_sequence_negative():
    result = string_sequence(-1)
    assert result == ""
    assert isinstance(result, str)
