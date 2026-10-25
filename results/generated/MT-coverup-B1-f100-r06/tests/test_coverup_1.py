# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f100 import make_a_pile


def test_make_a_pile_returns_n_elements_starting_at_n():
    result = make_a_pile(5)
    assert result == [5, 7, 9, 11, 13]
    assert len(result) == 5
    assert result[0] == 5
    assert all(b - a == 2 for a, b in zip(result, result[1:]))


def test_make_a_pile_preserves_parity_of_n():
    for n in (1, 2, 3, 4, 10):
        result = make_a_pile(n)
        assert len(result) == n
        assert all(value % 2 == n % 2 for value in result)


def test_make_a_pile_single_element():
    assert make_a_pile(1) == [1]


def test_make_a_pile_zero_returns_empty_list():
    assert make_a_pile(0) == []


def test_make_a_pile_does_not_mutate_input_and_is_repeatable():
    n = 4
    first = make_a_pile(n)
    second = make_a_pile(n)
    assert first == second == [4, 6, 8, 10]
    assert n == 4
    assert first is not second
