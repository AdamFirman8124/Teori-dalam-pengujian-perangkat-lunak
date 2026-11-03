# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import itertools

import pytest

from f147 import get_max_triples


def _brute_force(n):
    """Independent reference implementation used to cross-check results."""
    A = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(
        1
        for triple in itertools.combinations(A, 3)
        if sum(triple) % 3 == 0
    )


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5, 6, 7, 10])
def test_get_max_triples_matches_brute_force(n):
    """Covers all lines: list comprehension, nested loops, the modulo
    branch (both taken and not taken), and the return statement."""
    assert get_max_triples(n) == _brute_force(n)


def test_get_max_triples_no_triples_for_small_n():
    """Exercises the loops and the False branch of the modulo condition
    (no qualifying triples exist for n <= 3)."""
    for n in (0, 1, 2, 3):
        assert get_max_triples(n) == 0


def test_get_max_triples_single_triple_for_n4():
    """A(4) = [1, 3, 7, 13]; only (1, 7, 13) sums to a multiple of 3.
    Exercises the True branch of the modulo condition."""
    assert get_max_triples(4) == 1


def test_get_max_triples_single_triple_for_n5():
    """A(5) = [1, 3, 7, 13, 21]; only (1, 7, 13) sums to a multiple of 3."""
    assert get_max_triples(5) == 1


def test_get_max_triples_multiple_triples_for_n6():
    """A(6) = [1, 3, 7, 13, 21, 31]; qualifying triples are
    (1,7,13), (1,7,31), (1,13,31), (7,13,31) -> 4 triples."""
    assert get_max_triples(6) == 4


def test_get_max_triples_is_pure():
    """The function must not mutate any shared state: calling it twice
    with the same argument yields the same result."""
    assert get_max_triples(6) == get_max_triples(6) == 4
