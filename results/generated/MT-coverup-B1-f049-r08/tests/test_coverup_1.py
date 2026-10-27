# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f049 import modp


def test_modp_n_zero_returns_one():
    assert modp(0, 5) == 1
    assert modp(0, 1) == 1


def test_modp_single_iteration():
    assert modp(1, 5) == 2
    assert modp(1, 7) == 2


def test_modp_multiple_iterations():
    assert modp(3, 5) == 3
    assert modp(4, 7) == pow(2, 4, 7)
    assert modp(10, 13) == pow(2, 10, 13)


def test_modp_matches_pow():
    for n, p in [(2, 5), (5, 7), (6, 11), (3, 1)]:
        assert modp(n, p) == pow(2, n, p) if n > 0 else modp(n, p) == 1
