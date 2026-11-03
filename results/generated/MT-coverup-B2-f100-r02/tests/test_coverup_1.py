# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f100 import make_a_pile


def test_make_a_pile_basic():
    """Execute line 3 (the list comprehension return) with a typical n."""
    result = make_a_pile(3)
    assert result == [3, 5, 7]
    assert len(result) == 3


def test_make_a_pile_zero():
    """Execute line 3 with n=0, covering the empty-range branch."""
    assert make_a_pile(0) == []


def test_make_a_pile_one():
    """Execute line 3 with n=1, covering the single-iteration branch."""
    assert make_a_pile(1) == [1]


def test_make_a_pile_values_are_odd_and_increasing():
    """Verify postconditions: each element is n + 2*i, strictly increasing."""
    n = 5
    result = make_a_pile(n)
    assert result == [n + 2 * i for i in range(n)]
    assert all(result[i] < result[i + 1] for i in range(len(result) - 1))
    assert all(x % 2 == n % 2 for x in result)
