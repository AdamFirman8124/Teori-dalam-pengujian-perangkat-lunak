# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_executes_line_3():
    # Executes line 3 (the return statement) with a non-empty string.
    result = encode_shift("abc")
    assert result == "fgh"


def test_encode_shift_wraps_around_alphabet():
    # Exercises the modulo branch: 'v' + 5 wraps past 'z' back to 'a'.
    result = encode_shift("vwxyz")
    assert result == "abcde"


def test_encode_shift_empty_string():
    # Executes line 3 with an empty input; join over empty list.
    assert encode_shift("") == ""
