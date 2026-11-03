# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import pytest

from f147 import get_max_triples


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),  # A is empty: outer loop body never runs (loop-skip branch)
        (1, 0),  # outer loop body runs, j-loop never runs (loop-skip branch)
        (2, 0),  # i- and j-loop bodies run, k-loop never runs (loop-skip branch)
        (3, 0),  # k-loop body runs, if-condition is False (1+3+7=11, 11%3=2)
        (4, 1),  # if-condition is True: (1, 7, 13) -> 21 is a multiple of 3
        (5, 1),  # canonical example: only (1, 7, 13) qualifies
        (6, 4),  # several qualifying triples: (1,7,13), (1,7,31), (1,13,31), (7,13,31)
    ],
)
def test_get_max_triples(n, expected):
    """Exercise every line and branch of get_max_triples.

    A = [i*i - i + 1 for i in 1..n]; the function counts index triples
    i < j < k whose values sum to a multiple of 3.
    """
    assert get_max_triples(n) == expected


def test_get_max_triples_matches_bruteforce():
    """Cross-check the implementation against an independent brute force."""
    for n in range(0, 9):
        A = [i * i - i + 1 for i in range(1, n + 1)]
        expected = sum(
            1
            for i in range(n)
            for j in range(i + 1, n)
            for k in range(j + 1, n)
            if (A[i] + A[j] + A[k]) % 3 == 0
        )
        assert get_max_triples(n) == expected
