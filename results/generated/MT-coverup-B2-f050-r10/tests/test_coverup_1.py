# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_executes_line_3():
    # Non-empty input forces execution of the list-comprehension on line 3.
    result = encode_shift("abcxyz")
    # Each char is shifted forward by 5 with wraparound within 'a'..'z'.
    assert result == "fghcde"
    assert len(result) == len("abcxyz")
    assert all("a" <= ch <= "z" for ch in result)


def test_encode_shift_wraparound():
    # 'v' + 5 wraps around past 'z' back to 'a'.
    assert encode_shift("v") == "a"
    assert encode_shift("z") == "e"


def test_encode_shift_empty_string():
    # Empty input still executes line 3 (comprehension over empty iterable).
    assert encode_shift("") == ""
