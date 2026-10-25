# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_executes_return_line():
    # Executes line 3 (the return with the list comprehension).
    # Each lowercase letter shifts forward by 5 with wrap-around.
    assert encode_shift("abc") == "fgh"
    # Wrap-around branch: 'v' + 5 -> 'a', 'z' + 5 -> 'e'
    assert encode_shift("vwxyz") == "abcde"
    # Empty string: comprehension body still runs (zero iterations),
    # but the return line itself is executed.
    assert encode_shift("") == ""


def test_encode_shift_full_alphabet_wraparound():
    # Ensures every character path through the comprehension,
    # including the modulo wrap-around for all letters.
    original = "abcdefghijklmnopqrstuvwxyz"
    expected = "fghijklmnopqrstuvwxyzabcde"
    assert encode_shift(original) == expected
    # Postcondition: shifting twice by 5 then back by 10 (i.e. -5 mod 26)
    # restores the original string.
    shifted = encode_shift(original)
    restored = "".join(
        chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in shifted
    )
    assert restored == original
