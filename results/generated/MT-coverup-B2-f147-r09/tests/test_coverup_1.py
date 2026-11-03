# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import pytest

from f147 import get_max_triples


def test_n_zero_returns_zero():
    # Covers line 3 (empty list comprehension), line 4, line 5 (loop body
    # never entered) and line 10 (return).
    assert get_max_triples(0) == 0


def test_n_one_returns_zero():
    # Covers line 5 executing once with inner loops (lines 6-7) never entered.
    assert get_max_triples(1) == 0


def test_n_two_returns_zero():
    # Covers line 6 executing once with innermost loop (line 7) never entered.
    assert get_max_triples(2) == 0


def test_n_three_no_triple_satisfies_condition():
    # Covers lines 5-8 with the `if` condition (line 8) always False:
    # the only candidate triple is (1, 3, 7) whose sum 11 % 3 == 2.
    assert get_max_triples(3) == 0


def test_n_four_finds_exactly_one_triple():
    # Covers line 9 (True branch of the `if`): (1, 7, 13) sums to 21 % 3 == 0.
    assert get_max_triples(4) == 1


def test_n_five_finds_exactly_one_triple():
    # A = [1, 3, 7, 13, 21]; only (1, 7, 13) works (3 and 21 are the only
    # elements divisible by 3, not enough for a triple).
    assert get_max_triples(5) == 1


def test_n_six_finds_four_triples():
    # A = [1, 3, 7, 13, 21, 31]; the four triples among {1, 7, 13, 31}
    # all sum to a multiple of 3: 21, 39, 45, 51.
    assert get_max_triples(6) == 4


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 1),
        (5, 1),
        (6, 4),
        # For n=7: A = [1, 3, 7, 13, 21, 31, 43]; residues mod 3 are
        # [1, 0, 1, 1, 0, 1, 1]. Only all-≡1 triples qualify (no three
        # elements are ≡ 0), and there are C(5, 3) = 10 of them.
        (7, 10),
    ],
)
def test_get_max_triples_parametrized(n, expected):
    assert get_max_triples(n) == expected


def test_result_matches_brute_force_for_range_of_n():
    # Independent brute-force reimplementation used as an oracle to
    # cross-check the function for every n in 0..12.
    def oracle(n):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (A[i] + A[j] + A[k]) % 3 == 0:
                        count += 1
        return count

    for n in range(13):
        assert get_max_triples(n) == oracle(n), f"mismatch for n={n}"
