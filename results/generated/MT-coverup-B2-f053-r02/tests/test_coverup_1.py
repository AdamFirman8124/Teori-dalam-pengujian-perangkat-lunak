# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f053 import add


def test_add_executes_return():
    assert add(2, 3) == 5


def test_add_negative_and_zero():
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
