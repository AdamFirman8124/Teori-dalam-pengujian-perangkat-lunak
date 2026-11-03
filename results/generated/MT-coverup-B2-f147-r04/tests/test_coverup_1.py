# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

"""Tests for f147.get_max_triples.

get_max_triples builds A = [i*i - i + 1 for i in 1..n] and counts the
triples (A[i], A[j], A[k]) with i < j < k whose sum is divisible by 3.

The function under test is pure (no I/O, no module-level state, no
randomness), so no monkeypatching or teardown is required; each test
leaves no state behind and cannot pollute other tests.
"""

import math

import pytest

from f147 import get_max_triples


def _reference_count(n):
    """Independent brute-force oracle: enumerate all triples directly."""
    A = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        for k in range(j + 1, n)
        if (A[i] + A[j] + A[k]) % 3 == 0
    )


def _closed_form(n):
    """Independent combinatorial oracle.

    i*i - i + 1 is 0 mod 3 exactly when i % 3 == 2, otherwise 1 mod 3.
    A triple sums to 0 mod 3 only if all three residues are equal
    (0+0+0 or 1+1+1), so the answer is C(z, 3) + C(o, 3) where z is the
    number of elements congruent to 0 and o the number congruent to 1.
    """
    zeros = sum(1 for i in range(1, n + 1) if i % 3 == 2)
    ones = n - zeros
    return math.comb(zeros, 3) + math.comb(ones, 3)


def test_n_zero_no_loops_execute():
    # Covers: comprehension over empty range, ans = [], all three loops
    # skipped entirely, and the return statement.
    assert get_max_triples(0) == 0


def test_n_one_outer_loop_only():
    # Covers: i-loop body entered once, j-loop immediately exhausted.
    assert get_max_triples(1) == 0


def test_n_two_middle_loop_only():
    # Covers: j-loop body entered once, k-loop immediately exhausted.
    assert get_max_triples(2) == 0


def test_n_three_if_branch_false():
    # Covers: k-loop body plus the False branch of the modulo test:
    # the only candidate triple is (1, 3, 7) and 1 + 3 + 7 = 11 % 3 != 0.
    assert get_max_triples(3) == 0


def test_n_five_if_branch_true_appends():
    # Covers: the True branch of the modulo test and the `ans += [...]`
    # statement. For n = 5, A = [1, 3, 7, 13, 21] and the only valid
    # triple is (1, 7, 13) because 1 + 7 + 13 = 21 is divisible by 3.
    assert get_max_triples(5) == 1


def test_n_six_known_value():
    # A = [1, 3, 7, 13, 21, 31]; residues mod 3 are [1, 0, 1, 1, 0, 1].
    # Valid triples are exactly the C(4, 3) = 4 all-ones combinations:
    # (1,7,13), (1,7,31), (1,13,31), (7,13,31) -> sums 21, 39, 45, 51.
    assert get_max_triples(6) == 4


@pytest.mark.parametrize("n", [4, 5, 6, 7, 8, 12, 25])
def test_matches_brute_force_reference(n):
    assert get_max_triples(n) == _reference_count(n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 1),    # z = 2, o = 3 -> C(2,3) + C(3,3) = 0 + 1
        (10, 36),  # z = 3, o = 7 -> C(3,3) + C(7,3) = 1 + 35
        (11, 39),  # z = 4, o = 7 -> C(4,3) + C(7,3) = 4 + 35
    ],
)
def test_matches_closed_form(n, expected):
    assert _closed_form(n) == expected
    assert get_max_triples(n) == expected
