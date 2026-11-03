# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_basic():
    """Each lowercase letter is shifted forward by 5 positions."""
    assert encode_shift("abc") == "fgh"
    assert encode_shift("hello") == "mjqqt"


def test_encode_shift_wraparound():
    """Letters near the end of the alphabet wrap around to the beginning."""
    assert encode_shift("xyz") == "cde"
    assert encode_shift("vwxyz") == "abcde"


def test_encode_shift_empty_string():
    """An empty input yields an empty output (still executes the comprehension)."""
    assert encode_shift("") == ""


def test_encode_shift_full_alphabet():
    """Shifting the whole alphabet by 5 is a rotation."""
    assert (
        encode_shift("abcdefghijklmnopqrstuvwxyz")
        == "fghijklmnopqrstuvwxyzabcde"
    )


def test_encode_shift_is_pure():
    """The function must not mutate its input."""
    original = "abcxyz"
    result = encode_shift(original)
    assert original == "abcxyz"
    assert result == "fghcde"
