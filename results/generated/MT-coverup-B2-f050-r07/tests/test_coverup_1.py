# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f050 import encode_shift


def test_encode_shift_executes_line_3():
    # Wrap-around: 'x' + 5 -> 'c' (exercises the % 26 branch)
    assert encode_shift("xyz") == "cde"
    # Plain shift within range
    assert encode_shift("abc") == "fgh"
    # Empty string still executes the return line
    assert encode_shift("") == ""
    # Full alphabet shifts by 5 with wrap-around at the end
    assert encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"
    # No state is created or modified; nothing to clean up.
