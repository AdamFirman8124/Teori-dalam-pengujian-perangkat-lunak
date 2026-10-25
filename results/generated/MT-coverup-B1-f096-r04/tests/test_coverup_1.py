# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

import pytest

from f096 import count_up_to


def test_count_up_to_empty_when_n_below_first_prime():
    # n <= 2: outer loop body never runs (lines 3 and 12 only)
    assert count_up_to(2) == []
    assert count_up_to(0) == []
    assert count_up_to(-5) == []


def test_count_up_to_returns_primes_below_n():
    result = count_up_to(10)
    assert result == [2, 3, 5, 7]
    assert isinstance(result, list)
    assert result == sorted(result)
    assert all(
        all(p % d != 0 for d in range(2, p)) for p in result
    )


def test_count_up_to_hits_composite_break_branch():
    # 4, 6, 8, 9 are composite -> is_prime = False and break (lines 8-9)
    result = count_up_to(12)
    assert result == [2, 3, 5, 7, 11]
    assert 4 not in result
    assert 9 not in result


def test_count_up_to_single_prime():
    assert count_up_to(3) == [2]


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, []),
        (3, [2]),
        (5, [2, 3]),
        (11, [2, 3, 5, 7]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    ],
)
def test_count_up_to_parametrized(n, expected):
    result = count_up_to(n)
    assert result == expected
    assert all(p < n for p in result)
