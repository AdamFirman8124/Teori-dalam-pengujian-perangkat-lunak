# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f053 import add


def test_add_executes_return_line():
    # Exercise line 3 (the `return x + y` statement) with several inputs
    # and verify the postcondition: the result equals the sum of the args.
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-4, -6) == -10
    assert add(1000, 234) == 1234
