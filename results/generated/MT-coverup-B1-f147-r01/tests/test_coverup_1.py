# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import pytest

from f147 import get_max_triples


def _closed_form(n):
    # A[i] % 3 == 0 exactly when i % 3 == 2 (i.e. i in {2, 5, 8, ...}),
    # otherwise A[i] % 3 == 1, so a valid triple is either three "ones"
    # or three "zeros".
    zeros = (n + 1) // 3
    ones = n - zeros
    return (
        ones * (ones - 1) * (ones - 2) // 6
        + zeros * (zeros - 1) * (zeros - 2) // 6
    )


def _brute_force(n):
    A = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    count += 1
    return count


def test_n_zero_returns_zero():
    assert get_max_triples(0) == 0


def test_n_one_returns_zero():
    assert get_max_triples(1) == 0


def test_n_two_returns_zero():
    assert get_max_triples(2) == 0


def test_n_three_no_valid_triple():
    # A = [1, 3, 7]; 1 + 3 + 7 = 11, not divisible by 3
    assert get_max_triples(3) == 0


def test_n_four_one_valid_triple():
    # A = [1, 3, 7, 13]; only 1 + 7 + 13 = 21 is divisible by 3
    assert get_max_triples(4) == 1


def test_n_five_one_valid_triple():
    # A = [1, 3, 7, 13, 21]; only 1 + 7 + 13 = 21 is divisible by 3
    assert get_max_triples(5) == 1


def test_n_six_four_valid_triples():
    # A = [1, 3, 7, 13, 21, 31]; the four triples of {1, 7, 13, 31} all work
    assert get_max_triples(6) == 4


@pytest.mark.parametrize(
    "n, expected",
    [
        (7, 10),
        (8, 11),
        (9, 21),
        (10, 36),
        (11, 39),
    ],
)
def test_larger_n_matches_closed_form(n, expected):
    assert expected == _closed_form(n)
    assert expected == _brute_force(n)
    assert get_max_triples(n) == expected


@pytest.mark.parametrize("n", list(range(0, 13)))
def test_matches_brute_force_for_small_n(n):
    assert get_max_triples(n) == _brute_force(n) == _closed_form(n)


def test_result_is_deterministic_and_stateless():
    import f147

    before = dict(vars(f147))
    first = get_max_triples(6)
    second = get_max_triples(6)
    after = dict(vars(f147))

    assert first == second == 4
    assert before == after, "get_max_triples must not mutate module state"
