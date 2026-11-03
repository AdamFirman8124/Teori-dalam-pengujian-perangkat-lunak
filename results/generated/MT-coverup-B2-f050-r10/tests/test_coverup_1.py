# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f050.encode_shift.

These tests execute the (previously uncovered) return statement of
``encode_shift`` in f050/__init__.py, covering both the normal shift
path and the modulo wrap-around branch of the alphabet.
"""

from f050 import encode_shift


def test_encode_shift_basic():
    """Each lowercase letter is shifted forward by 5 positions."""
    assert encode_shift("abc") == "fgh"


def test_encode_shift_wraparound():
    """Letters near the end of the alphabet wrap around to the start."""
    assert encode_shift("xyz") == "cde"


def test_encode_shift_empty_string():
    """An empty input yields an empty output (comprehension runs zero times)."""
    assert encode_shift("") == ""


def test_encode_shift_full_alphabet():
    """Encoding the whole alphabet shifts every letter consistently."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    expected = "fghijklmnopqrstuvwxyzabcde"
    assert encode_shift(alphabet) == expected


def test_encode_shift_is_deterministic_and_preserves_length():
    """Encoding is deterministic and preserves the input length."""
    result1 = encode_shift("hello")
    result2 = encode_shift("hello")
    assert result1 == result2 == "mjqqt"
    assert len(result1) == len("hello")


def test_encode_shift_matches_reference_implementation():
    """Result matches an independent reference computation of the formula."""
    s = "attackatdawn"
    expected = "".join(
        chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s
    )
    assert encode_shift(s) == expected
