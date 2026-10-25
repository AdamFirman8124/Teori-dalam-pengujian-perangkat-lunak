# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

import pytest

from f123 import get_odd_collatz


def test_get_odd_collatz_even_start():
    # even n -> odd_collatz starts empty (lines 3-4)
    assert get_odd_collatz(2) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(10) == [1, 5]


def test_get_odd_collatz_odd_start():
    # odd n -> odd_collatz starts with [n] (line 6)
    assert get_odd_collatz(5) == [1, 5]
    # 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert get_odd_collatz(3) == [1, 3, 5]


def test_get_odd_collatz_one_skips_loop():
    # while loop body never runs (line 7 false on entry)
    assert get_odd_collatz(1) == [1]


def test_get_odd_collatz_returns_sorted_list():
    result = get_odd_collatz(9)
    assert isinstance(result, list)
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    assert 1 in result
    assert 9 in result


def test_get_odd_collatz_does_not_mutate_input():
    n = 12
    get_odd_collatz(n)
    assert n == 12


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [1]),
        (2, [1]),
        (3, [1, 3, 5]),
        (4, [1]),
        (5, [1, 5]),
        (6, [1, 3, 5]),
        (7, [1, 5, 7, 11, 13, 17]),
        (8, [1]),
        (9, [1, 5, 7, 9, 11, 13, 17]),
        (12, [1, 3, 5]),
    ],
)
def test_get_odd_collatz_parametrized(n, expected):
    assert get_odd_collatz(n) == expected
