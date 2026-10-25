# file: project/f050/__init__.py:6-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest

from f050 import decode_shift


def test_decode_shift_executes_line_8():
    # decode_shift shifts each char back by 5, wrapping modulo 26.
    # 'm' -> 'h', 'f' -> 'a', 'a' -> 'v' (wraps around)
    assert decode_shift("mfa") == "hav"
    # Wrap-around branch of the modulo operation
    assert decode_shift("a") == "v"
    assert decode_shift("e") == "z"
    # Empty string still executes the return line (empty join)
    assert decode_shift("") == ""
    # Round-trip property: encoding then decoding returns the original
    encoded = "".join(
        chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in "hello"
    )
    assert decode_shift(encoded) == "hello"
