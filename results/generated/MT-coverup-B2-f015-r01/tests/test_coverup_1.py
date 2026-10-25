# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f015 import string_sequence


def test_string_sequence_zero():
    assert string_sequence(0) == "0"


def test_string_sequence_one():
    assert string_sequence(1) == "0 1"


def test_string_sequence_positive():
    assert string_sequence(5) == "0 1 2 3 4 5"


def test_string_sequence_negative_empty():
    assert string_sequence(-1) == ""
    assert string_sequence(-5) == ""


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (2, "0 1 2"),
        (3, "0 1 2 3"),
        (10, "0 1 2 3 4 5 6 7 8 9 10"),
        (-1, ""),
    ],
)
def test_string_sequence_parametrized(n, expected):
    result = string_sequence(n)
    assert isinstance(result, str)
    assert result == expected
