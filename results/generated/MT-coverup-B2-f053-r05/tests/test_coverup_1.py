# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f053 import add


def test_add_executes_return_line():
    """Call add() so that line 3 (the return statement) is executed."""
    result = add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    """Also exercise the return line with negative integers."""
    assert add(-4, 9) == 5
