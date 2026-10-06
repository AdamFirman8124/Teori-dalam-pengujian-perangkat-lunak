# file: script_49.py:1-17
# asked: {"lines": [14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}
# gained: {"lines": [14, 15, 16, 17], "branches": [[15, 16], [15, 17]]}

import pytest
from script_49 import modp


def test_modp_basic():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1


def test_modp_zero():
    assert modp(0, 101) == 1
    assert modp(0, 5) == 1
    assert modp(0, 2) == 1


def test_modp_one():
    assert modp(1, 5) == 2
    assert modp(1, 101) == 2
    assert modp(1, 11) == 2


def test_modp_positive_n():
    assert modp(5, 7) == 4
    assert modp(10, 13) == 10
    assert modp(2, 3) == 1
