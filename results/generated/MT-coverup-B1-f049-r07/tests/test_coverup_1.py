# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f049 import modp


def test_modp_n_zero_no_loop():
    # n=0: executes ret=1, for header, skips body, returns
    assert modp(0, 5) == 1
    assert modp(0, 1) == 1


def test_modp_single_iteration():
    # n=1: executes loop body exactly once
    assert modp(1, 5) == 2
    assert modp(1, 7) == 2


def test_modp_multiple_iterations():
    # n>1: executes loop body multiple times
    assert modp(3, 5) == pow(2, 3, 5) == 3
    assert modp(4, 7) == pow(2, 4, 7) == 2
    assert modp(10, 1000) == pow(2, 10, 1000) == 24
    assert modp(5, 13) == pow(2, 5, 13) == 6
