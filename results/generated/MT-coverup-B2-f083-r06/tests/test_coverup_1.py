# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

"""Tests for f083.starts_one_ends.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; there is no
state to pollute. Each test below targets a specific uncovered line/branch:

- test_starts_one_ends_single_digit  -> covers line 3 (if) and line 4 (return 1)
- test_starts_one_ends_multi_digit   -> covers line 5 (return 18 * 10 ** (n - 2))
"""

from f083 import starts_one_ends


def test_starts_one_ends_single_digit():
    """n == 1 must take the true branch of the if and return 1."""
    assert starts_one_ends(1) == 1


def test_starts_one_ends_two_digits():
    """n == 2 must skip the if and hit the final return (line 5)."""
    assert starts_one_ends(2) == 18


def test_starts_one_ends_multi_digit():
    """Larger n values exercise line 5 with different exponents."""
    assert starts_one_ends(3) == 180
    assert starts_one_ends(4) == 1800
    assert starts_one_ends(10) == 18 * 10 ** 8


def test_starts_one_ends_matches_formula():
    """Property check: every n >= 2 agrees with the closed-form formula."""
    for n in range(2, 8):
        assert starts_one_ends(n) == 18 * 10 ** (n - 2)
