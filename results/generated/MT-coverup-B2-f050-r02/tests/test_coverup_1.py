# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_basic_shift_executes_line_3():
    """A plain call must execute line 3 (the comprehension/return).

    Each lowercase letter is shifted forward by 5 positions:
    'a' -> 'f', 'b' -> 'g', 'c' -> 'h'.
    """
    assert encode_shift("abc") == "fgh"


def test_encode_shift_wraparound():
    """Letters near the end of the alphabet wrap around modulo 26.

    'x' -> 'c', 'y' -> 'd', 'z' -> 'e'.
    """
    assert encode_shift("xyz") == "cde"


def test_encode_shift_empty_string():
    """An empty input yields an empty output (comprehension runs zero times)."""
    assert encode_shift("") == ""


def test_encode_shift_mixed_string():
    """A longer string exercises the comprehension loop repeatedly."""
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"
