# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_basic_shift():
    """Calling encode_shift with a non-empty string executes line 3 (the comprehension)."""
    # Each lowercase letter shifts forward by 5 positions.
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("aaaaa") == "fffff"


def test_encode_shift_wraps_around_alphabet():
    """Verify the modulo-26 wraparound branch of the comprehension logic."""
    # 'v' is the first letter that wraps around: 'v' -> 'a', ..., 'z' -> 'e'.
    assert encode_shift("vwxyz") == "abcde"
    assert encode_shift("xyz") == "cde"


def test_encode_shift_empty_string():
    """Calling with an empty string still executes line 3 (comprehension yields empty join)."""
    assert encode_shift("") == ""
