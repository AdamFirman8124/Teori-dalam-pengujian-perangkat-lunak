# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f053 import add


def test_add_returns_sum():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, 6) == 2
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 7) == 7
