# file: project/f050/__init__.py:6-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

"""Tests for f050.decode_shift — exercises line 8 (the join/comprehension return).

decode_shift is a pure function (no I/O, no globals, no side effects), so no
monkeypatching or teardown is required; there is no state to pollute.
"""

from f050 import decode_shift


def test_decode_shift_basic():
    # Letters f..j decode straight back to a..e (no wraparound).
    assert decode_shift("fghij") == "abcde"


def test_decode_shift_wraparound():
    # Letters a..e wrap around past 'z' via the negative-modulo branch.
    assert decode_shift("abcde") == "vwxyz"


def test_decode_shift_empty_string():
    # Empty input: comprehension runs zero times, join yields "".
    assert decode_shift("") == ""


def test_decode_shift_full_alphabet():
    # Every letter of the alphabet, covering all 26 modulo outcomes.
    plain = "abcdefghijklmnopqrstuvwxyz"
    # 'encoded' is the plain alphabet shifted FORWARD by 5 (a->f, ..., z->e);
    # decoding it must recover the original alphabet.
    encoded = "fghijklmnopqrstuvwxyzabcde"
    assert decode_shift(encoded) == plain
    # Conversely, decoding the plain alphabet shifts every letter back by 5.
    assert decode_shift(plain) == "vwxyzabcdefghijklmnopqrstu"


def test_decode_shift_roundtrip():
    # Decoding the forward-shift-by-5 encoding recovers the original message.
    message = "helloworld"
    encoded = "".join(
        chr((ord(ch) - ord("a") + 5) % 26 + ord("a")) for ch in message
    )
    assert decode_shift(encoded) == message
