# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_positive_n():
    # 2^10 % 13 == 1024 % 13 == 10
    assert modp(10, 13) == 10


def test_modp_zero_n():
    # Loop body never runs; returns initial ret == 1
    assert modp(0, 13) == 1


def test_modp_various():
    assert modp(3, 5) == 3      # 8 % 5
    assert modp(1, 2) == 0      # 2 % 2
    assert modp(5, 101) == 32   # 2^5 % 101
