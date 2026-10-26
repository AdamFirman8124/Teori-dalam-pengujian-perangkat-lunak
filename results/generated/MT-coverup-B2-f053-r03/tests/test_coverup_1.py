# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f053


def test_add_returns_sum():
    result = f053.add(2, 3)
    assert result == 5
    assert f053.add(-1, 1) == 0
    assert f053.add(0, 0) == 0
