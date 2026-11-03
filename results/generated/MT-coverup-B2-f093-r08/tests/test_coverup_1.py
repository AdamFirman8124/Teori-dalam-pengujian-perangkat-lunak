# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

"""Tests for f093.encode (lines 3-6 of f093/__init__.py).

encode(message):
  1. builds a vowel -> (vowel + 2 ASCII chars) mapping for "aeiouAEIOU",
  2. swaps the case of the message,
  3. replaces every vowel of the swapped message with its mapping,
     leaving all other characters untouched.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching/cleanup is required; each test works on local string
data only, avoiding any state pollution.
"""

import pytest

from f093 import encode


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        # Lowercase input: swapcase -> uppercase, vowels shifted +2 (E->G, S kept).
        ("test", "TGST"),
        # Mixed case with spaces: exercises both branches of the conditional
        # (vowel replacement and pass-through) plus swapcase in both directions.
        ("This is a message", "tHKS KS C MGSSCGG"),
        # All lowercase vowels: swapcase makes them uppercase, then shifted.
        ("aeiou", "CGKQW"),
        # All uppercase vowels: swapcase makes them lowercase, then shifted.
        ("AEIOU", "cgkqw"),
        # Non-letter characters: never vowels, so the 'else' branch keeps them,
        # and swapcase leaves digits/punctuation unchanged.
        ("123!@#", "123!@#"),
        # Mixed letters, digits and punctuation. After swapcase the 'o' in
        # "pYtHoN" is a lowercase vowel, so it is replaced by 'q'.
        ("PyThOn 3.10!", "pYtHqN 3.10!"),
        # Empty string: loop body never runs, result is empty.
        ("", ""),
    ],
)
def test_encode(message, expected):
    original = message  # strings are immutable; snapshot for the postcondition
    result = encode(message)
    assert result == expected
    # Postcondition: the input argument is not modified.
    assert message == original


def test_encode_vowel_mapping_is_exactly_two_letters_ahead():
    # Every vowel, in both cases, must map to the letter two places ahead
    # in the alphabet (via the ASCII +2 construction on line 4).
    expected = {
        "a": "c", "e": "g", "i": "k", "o": "q", "u": "w",
        "A": "C", "E": "G", "I": "K", "O": "Q", "U": "W",
    }
    for vowel, shifted in expected.items():
        # Feeding a single vowel: swapcase flips its case, then it is replaced.
        assert encode(vowel) == shifted.swapcase()


def test_encode_returns_str_and_preserves_length():
    message = "Hello, World! 42"
    result = encode(message)
    assert isinstance(result, str)
    assert len(result) == len(message)
