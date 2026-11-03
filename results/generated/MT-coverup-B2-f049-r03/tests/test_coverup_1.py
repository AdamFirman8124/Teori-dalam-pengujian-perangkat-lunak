# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

"""Tests for f049.modp, which computes 2**n % p.

Lines 3-6 (the function body) were previously never executed because the
function was never called.  These tests exercise every line and both
branches of the ``for`` loop (loop body taken for n > 0, and the empty
range case for n == 0).

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test is self-contained.
"""

from f049 import modp


def test_modp_zero_iterations_covers_empty_range_branch():
    # n == 0 -> range(0) is empty, so the loop body (line 5) never runs
    # and ret stays 1.  Covers the "loop not taken" branch.
    assert modp(0, 5) == 1
    assert modp(0, 1) == 1


def test_modp_single_iteration():
    # n == 1 -> loop body executes exactly once: ret = 2 % 7 = 2.
    assert modp(1, 7) == 2


def test_modp_multiple_iterations():
    # n == 3 -> loop body executes three times: 2, 4, 8 -> 8 % 5 == 3.
    assert modp(3, 5) == 3
    # Cross-check against Python's built-in modular exponentiation.
    assert modp(3, 5) == pow(2, 3, 5)


def test_modp_matches_builtin_pow_for_large_n():
    # Many iterations of the loop, with wrap-around modulo at every step.
    n, p = 100, 101
    assert modp(n, p) == pow(2, n, p)


def test_modp_modulus_one_wraps_to_zero():
    # With p == 1 every nonzero intermediate value wraps to 0.
    assert modp(5, 1) == 0


def test_modp_result_always_within_range():
    # Postcondition: 0 <= result < p for any n > 0.
    for n, p in [(10, 7), (13, 11), (50, 97)]:
        result = modp(n, p)
        assert 0 <= result < p
        assert result == pow(2, n, p)
