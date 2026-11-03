# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

"""Tests for f147.get_max_triples.

The function under test is pure (no I/O, no globals, no mutable state), so no
monkeypatching/teardown is required; each test leaves no state behind.
"""

from itertools import combinations

import pytest

from f147 import get_max_triples


def _expected_count(n):
    """Independent brute-force reference implementation.

    Counts 3-element combinations of [i*i - i + 1 for i in 1..n] whose sum is
    divisible by 3, using itertools.combinations rather than the nested-loop
    structure of the code under test.
    """
    A = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(1 for triple in combinations(A, 3) if sum(triple) % 3 == 0)


def test_no_triples_when_fewer_than_three_elements():
    # n = 0 and n = 1: A has fewer than 3 elements, so no triple can exist.
    # Exercises the list comprehension (line 3), ans init (line 4) and
    # the return (line 10) with immediately-exhausted loops.
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0


def test_candidate_triple_fails_modulo_check():
    # n = 3: A = [1, 3, 7]; the only candidate triple sums to 11, and
    # 11 % 3 != 0, so the False branch of the modulo test is taken.
    assert get_max_triples(3) == 0


def test_single_qualifying_triple_appends_to_ans():
    # n = 5: A = [1, 3, 7, 13, 21]; exactly one triple (1, 7, 13) has a sum
    # (21) divisible by 3, so the True branch (line 9: ans += [...]) runs.
    assert get_max_triples(5) == 1


def test_both_branches_of_modulo_check_exercised():
    # n = 8: A = [1, 3, 7, 13, 21, 31, 43, 57].
    # Values mod 3 are [1, 0, 1, 1, 0, 1, 1, 0]; a triple sums to 0 mod 3
    # iff all three values are 1 mod 3 (C(5,3) = 10 triples) or all three
    # are 0 mod 3 (the single triple (3, 21, 57)). Total = 11, and both
    # branches of the if are taken during the run.
    assert get_max_triples(8) == 11


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_matches_independent_bruteforce_reference(n):
    # Cross-check the nested-loop implementation against an independent
    # combinations-based reference for a range of sizes, covering every
    # loop-entry/exit and if branch combination.
    assert get_max_triples(n) == _expected_count(n)
