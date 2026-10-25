# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f053 import add


def test_add_returns_sum():
    assert add(2, 3) == 5
