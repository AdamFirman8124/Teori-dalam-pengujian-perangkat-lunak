# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_zero_iterations():
    # n = 0: line 3 executes, loop body (lines 4-5) does not
    assert modp(0, 5) == 1


def test_modp_positive_n():
    # 2^10 % 13 = 1024 % 13 = 10
    assert modp(10, 13) == 10


def test_modp_matches_pow():
    for n in range(0, 20):
        for p in (3, 7, 13, 101):
            assert modp(n, p) == pow(2, n, p)


def test_modp_one_iteration():
    # single loop iteration: 2 % 5 = 2
    assert modp(1, 5) == 2
