# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_zero_iterations():
    """n = 0: loop body never runs, ret stays 1 (covers lines 3, 4, 6)."""
    assert modp(0, 5) == 1
    assert modp(0, 1) == 1


def test_modp_positive_n():
    """n > 0: loop body executes (covers line 5); result equals 2**n % p."""
    assert modp(1, 5) == 2          # 2 % 5
    assert modp(3, 5) == 3          # 8 % 5
    assert modp(4, 7) == 2          # 16 % 7
    assert modp(10, 3) == 1         # 1024 % 3
    assert modp(10, 101) == 2 ** 10 % 101


def test_modp_p_one():
    """Modulo 1 always yields 0 once the loop body runs."""
    assert modp(5, 1) == 0
    assert modp(0, 1) == 1          # loop body skipped, so still 1


def test_modp_negative_n():
    """Negative n: range(n) is empty, so the loop body is skipped (branch)."""
    assert modp(-1, 5) == 1
    assert modp(-10, 7) == 1


@pytest.mark.parametrize(
    "n, p",
    [(0, 5), (1, 5), (2, 5), (3, 5), (10, 3), (20, 1000000007), (-3, 9)],
)
def test_modp_matches_power_mod(n, p):
    """Property check: modp(n, p) == 2**n % p for non-negative n."""
    if n >= 0:
        assert modp(n, p) == pow(2, n, p)
    else:
        assert modp(n, p) == 1
