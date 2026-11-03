# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import itertools

import pytest

from f147 import get_max_triples


def _reference_count(n):
    """Independent reference implementation (different style from the code
    under test): counts triples i < j < k such that
    (A[i] + A[j] + A[k]) % 3 == 0 where A = [i*i - i + 1 for i in 1..n]."""
    A = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(
        1
        for i, j, k in itertools.combinations(range(n), 3)
        if (A[i] + A[j] + A[k]) % 3 == 0
    )


def test_known_value_n5():
    # A = [1, 3, 7, 13, 21]; the only qualifying triple is (1, 7, 13) -> 21.
    assert get_max_triples(5) == 1


def test_known_values_larger_n():
    # Residues of A mod 3 are 1 except when i % 3 == 2 (residue 0), so a
    # triple sums to a multiple of 3 iff all three residues are equal.
    # n=6: ones at i=1,3,4,6 -> C(4,3)=4 ; zeros at i=2,5 -> C(2,3)=0
    assert get_max_triples(6) == 4
    # n=7: ones at i=1,3,4,6,7 -> C(5,3)=10 ; zeros at i=2,5 -> C(2,3)=0
    assert get_max_triples(7) == 10
    # n=8: ones at i=1,3,4,6,7 -> C(5,3)=10 ; zeros at i=2,5,8 -> C(3,3)=1
    assert get_max_triples(8) == 11


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_matches_independent_reference(n):
    assert get_max_triples(n) == _reference_count(n)


def test_edge_cases_return_zero():
    # n=0 exercises the empty-comprehension / skipped-loops branches;
    # n=1,2,3 exercise partially skipped nested loops and only the
    # false branch of the modulo test.
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0


def test_return_type_is_int():
    assert isinstance(get_max_triples(5), int)
    assert isinstance(get_max_triples(0), int)
