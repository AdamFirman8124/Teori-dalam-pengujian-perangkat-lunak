# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_zero_iterations():
    # n = 0: lines 3 and 6 execute, loop body (lines 4-5) does not
    assert modp(0, 13) == 1


def test_modp_loop_executes():
    # n > 0: lines 3-6 all execute, including the loop body
    # 2^10 mod 13 = 1024 mod 13 = 10
    assert modp(10, 13) == 10
    # 2^3 mod 5 = 8 mod 5 = 3
    assert modp(3, 5) == 3
    # 2^1 mod 2 = 0
    assert modp(1, 2) == 0
