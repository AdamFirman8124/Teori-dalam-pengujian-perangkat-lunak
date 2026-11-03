# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import itertools

import pytest

from f147 import get_max_triples


# Hand-computed expected values.
# A = [i*i - i + 1 for i in 1..n]; residues mod 3 alternate 1, 0, 1, 1, 0, ...
# A triple sums to a multiple of 3 iff all three residues are equal,
# so the count is C(#zeros, 3) + C(#ones, 3).
@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),  # line 3 runs on an empty range; loops on lines 5-7 never run a body
        (1, 0),  # body of the line-5 loop runs once; line-6 loop body never does
        (2, 0),  # body of the line-6 loop runs once; line-7 loop body never does
        (3, 0),  # line 8 evaluated with False branch; line 9 never runs
        (4, 1),  # (1, 7, 13) -> 21 % 3 == 0: True branch taken, line 9 executes
        (5, 1),
        (6, 4),
        (7, 10),
        (8, 11),
    ],
)
def test_get_max_triples_known_values(n, expected):
    assert get_max_triples(n) == expected


def test_get_max_triples_matches_independent_bruteforce():
    # Cross-check against an independent counting method (itertools.combinations)
    # to make sure every line/branch is exercised with correct behavior.
    for n in range(0, 15):
        a = [i * i - i + 1 for i in range(1, n + 1)]
        expected = sum(
            1 for triple in itertools.combinations(a, 3) if sum(triple) % 3 == 0
        )
        assert get_max_triples(n) == expected, f"mismatch for n={n}"


def test_get_max_triples_returns_int():
    result = get_max_triples(5)
    assert isinstance(result, int)
    assert result >= 0
