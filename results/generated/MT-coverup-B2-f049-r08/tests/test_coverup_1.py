# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_basic_loop_executes():
    """modp(n, p) must compute (2 ** n) % p; exercises lines 3-6."""
    assert modp(10, 7) == 2 ** 10 % 7 == 2


def test_modp_single_iteration():
    """One loop iteration: line 5 runs exactly once."""
    assert modp(1, 5) == 2


def test_modp_zero_iterations():
    """n == 0: loop body never runs (false branch of line 4), result stays 1."""
    assert modp(0, 5) == 1


def test_modp_negative_n():
    """Negative n: range is empty, loop never runs, result is 1."""
    assert modp(-3, 5) == 1


def test_modp_modulus_one():
    """p == 1 makes every intermediate value 0 for n > 0."""
    assert modp(3, 1) == 0


def test_modp_matches_builtin_pow():
    """Cross-check against the standard library for a larger input."""
    assert modp(100, 13) == pow(2, 100, 13)


@pytest.mark.parametrize("n, p, expected", [
    (5, 11, 2 ** 5 % 11),
    (6, 3, 2 ** 6 % 3),
    (7, 17, 2 ** 7 % 17),
])
def test_modp_parametrized(n, p, expected):
    assert modp(n, p) == expected
