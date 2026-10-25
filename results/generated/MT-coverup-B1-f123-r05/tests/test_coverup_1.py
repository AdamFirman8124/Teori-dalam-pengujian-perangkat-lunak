# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

from f123 import get_odd_collatz
import pytest


def test_even_start_n2_returns_one():
    result = get_odd_collatz(2)
    assert result == [1]


def test_one_returns_itself():
    assert get_odd_collatz(1) == [1]


def test_odd_start_includes_start_value():
    result = get_odd_collatz(3)
    assert result == [1, 3, 5]
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)


def test_even_start_excludes_start_value():
    result = get_odd_collatz(6)
    assert result == [1, 3, 5]
    assert 6 not in result
    assert all(x % 2 == 1 for x in result)


def test_large_even_value():
    result = get_odd_collatz(10)
    assert result == [1, 5]
    assert result == sorted(result)


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27])
def test_postconditions_hold(n):
    result = get_odd_collatz(n)
    assert isinstance(result, list)
    assert result == sorted(result)
    assert all(isinstance(x, int) and x % 2 == 1 for x in result)
    if n % 2 == 1:
        assert n in result
    else:
        assert n not in result
    if n > 1:
        assert 1 in result
