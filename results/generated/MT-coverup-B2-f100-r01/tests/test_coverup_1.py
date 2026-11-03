# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f100 import make_a_pile


def test_make_a_pile_basic():
    """make_a_pile(3) should build levels [3, 5, 7]."""
    result = make_a_pile(3)
    assert result == [3, 5, 7]
    assert len(result) == 3
    # each level is exactly 2 more than the previous one
    assert all(b - a == 2 for a, b in zip(result, result[1:]))


def test_make_a_pile_single():
    """make_a_pile(1) should return a single-element list."""
    assert make_a_pile(1) == [1]


def test_make_a_pile_zero():
    """make_a_pile(0) should return an empty list (range(0) is empty)."""
    assert make_a_pile(0) == []


def test_make_a_pile_matches_formula():
    """Every element must equal n + 2*i for its index i."""
    n = 5
    result = make_a_pile(n)
    assert result == [n + 2 * i for i in range(n)]
    assert result[0] == n
    assert result[-1] == n + 2 * (n - 1)
