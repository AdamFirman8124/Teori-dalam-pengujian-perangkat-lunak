# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

"""Tests for f082.prime_length.

prime_length is a pure function (no I/O, no globals, no mutable state),
so no monkeypatching or teardown is required -- calling it cannot pollute
state. Each test targets specific uncovered lines/branches (lines 3-9).
"""

from f082 import prime_length


def test_prime_length_empty_string_is_false():
    # Covers line 3, line 4 (l == 0 branch) and line 5.
    assert prime_length("") is False


def test_prime_length_single_char_is_false():
    # Covers line 3, line 4 (l == 1 branch, first condition False) and line 5.
    assert prime_length("x") is False


def test_prime_length_two_chars_is_true():
    # Covers line 3, line 4 (both conditions False), line 6 with an
    # empty loop body (range(2, 2)) and line 9.
    assert prime_length("ab") is True


def test_prime_length_prime_length_is_true():
    # Covers line 3, line 6 loop entry, line 7 (l % i != 0 branch)
    # and line 9. Length 3: single iteration i=2, 3 % 2 == 1.
    assert prime_length("abc") is True


def test_prime_length_even_composite_is_false():
    # Covers line 3, line 6, line 7 (l % i == 0 branch) and line 8.
    # Length 4: first iteration i=2 divides evenly.
    assert prime_length("abcd") is False


def test_prime_length_odd_composite_is_false():
    # Covers line 3, line 6 looping several times, line 7 taking the
    # non-divisor branch (i=2) before the divisor branch (i=3), line 8.
    # Length 9: 9 % 2 == 1, then 9 % 3 == 0.
    result = prime_length("123456789")
    assert result is False
    # Postcondition cross-checks against an independent computation.
    n = len("123456789")
    assert n == 9
    assert any(n % i == 0 for i in range(2, n))
