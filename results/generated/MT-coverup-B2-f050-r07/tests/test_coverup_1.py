# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_basic_shift():
    """Each lowercase letter should be shifted forward by 5 positions."""
    assert encode_shift("a") == "f"
    assert encode_shift("b") == "g"
    assert encode_shift("hello") == "mjqqt"


def test_encode_shift_wraparound():
    """Letters near the end of the alphabet must wrap around to the beginning."""
    assert encode_shift("v") == "a"
    assert encode_shift("z") == "e"
    assert encode_shift("vwxyz") == "abcde"


def test_encode_shift_empty_string():
    """An empty input should produce an empty output (exercises the join on an empty list)."""
    assert encode_shift("") == ""


def test_encode_shift_is_pure():
    """The function must not mutate its input."""
    original = "abc"
    result = encode_shift(original)
    assert original == "abc"
    assert result == "fgh"
