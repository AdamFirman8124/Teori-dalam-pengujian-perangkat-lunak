# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

"""Tests for f031.is_prime covering all lines and branches (lines 3-8)."""

from f031 import is_prime


def test_is_prime_returns_false_for_n_below_two():
    # Covers line 3 (True branch) and line 4.
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False


def test_is_prime_returns_true_for_two_and_three_without_looping():
    # Covers line 3 (False branch) and line 8; the loop body never runs
    # because range(2, n - 1) is empty for n = 2 and n = 3.
    assert is_prime(2) is True
    assert is_prime(3) is True


def test_is_prime_returns_false_for_composite_with_loop_executed():
    # Covers lines 5, 6 (True branch) and 7: the loop runs and finds a divisor.
    assert is_prime(4) is False   # range(2, 3) -> k = 2, 4 % 2 == 0
    assert is_prime(9) is False   # range(2, 8) -> k = 3, 9 % 3 == 0
    assert is_prime(15) is False  # range(2, 14) -> k = 3, 15 % 3 == 0


def test_is_prime_returns_true_for_prime_with_loop_executed():
    # Covers lines 5, 6 (False branch) and 8: the loop runs, finds no divisor,
    # and the final return True is reached.
    assert is_prime(5) is True    # range(2, 4) -> k in (2, 3), no divisor
    assert is_prime(7) is True    # range(2, 6) -> k in (2, 3, 4, 5), no divisor
    assert is_prime(13) is True   # range(2, 12) -> no divisor found
