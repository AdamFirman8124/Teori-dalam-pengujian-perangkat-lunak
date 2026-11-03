# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f053


def test_add_executes_return_line():
    """Ensure add() executes its return statement (line 3) and returns the correct sum."""
    assert f053.add(2, 3) == 5
    assert f053.add(-1, 1) == 0
    assert f053.add(0, 0) == 0
