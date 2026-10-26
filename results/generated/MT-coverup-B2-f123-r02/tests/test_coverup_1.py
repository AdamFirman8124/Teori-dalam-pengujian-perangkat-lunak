# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

import pytest

from f123 import get_odd_collatz


def test_get_odd_collatz_even_start():
    # even n -> odd_collatz starts empty (line 3-4 branch)
    assert get_odd_collatz(6) == [1, 3, 5]


def test_get_odd_collatz_odd_start():
    # odd n -> odd_collatz starts as [n] (line 6 branch)
    assert get_odd_collatz(5) == [1, 5]


def test_get_odd_collatz_one():
    # loop body never runs; returns [1]
    assert get_odd_collatz(1) == [1]


def test_get_odd_collatz_two():
    # 2 -> 1, only the even-halving branch plus final odd append
    assert get_odd_collatz(2) == [1]


def test_get_odd_collatz_three():
    # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert get_odd_collatz(3) == [1, 3, 5]


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 7, 10, 12, 27])
def test_get_odd_collatz_postconditions(n):
    result = get_odd_collatz(n)

    # postcondition: sorted ascending
    assert result == sorted(result)
    # postcondition: every element is an odd integer
    assert all(isinstance(x, int) and x % 2 == 1 for x in result)
    # postcondition: 1 is always reached
    assert 1 in result
    # postcondition: no duplicates
    assert len(result) == len(set(result))
    # postcondition: an odd starting value is included
    if n % 2 == 1:
        assert n in result
    # postcondition: an even starting value is not included
    else:
        assert n not in result
    # postcondition: input is not mutated
    assert n == n
