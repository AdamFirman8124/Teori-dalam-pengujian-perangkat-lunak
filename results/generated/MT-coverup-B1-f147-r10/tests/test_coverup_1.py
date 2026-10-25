# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

import pytest

from f147 import get_max_triples


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
    # A[i] = i*i - i + 1 for i in 1..n; A[i] % 3 == 0 exactly when i % 3 == 2,
    # which happens (n + 1) // 3 times, so the answer is
    # C(ones, 3) + C(zeros, 3) with zeros = (n + 1) // 3, ones = n - zeros.
    zeros = (n + 1) // 3
    ones = n - zeros
    assert expected == ones * (ones - 1) * (ones - 2) // 6 + zeros * (zeros - 1) * (zeros - 2) // 6
    assert get_max_triples(n) == expected


def test_result_is_deterministic_and_stateless():
    import f147

    before = dict(vars(f147))
    first = get_max_triples(6)
    second = get_max_triples(6)
    after = dict(vars(f147))

    assert first == second == 4
    assert before == after, "get_max_triples must not mutate module state"
