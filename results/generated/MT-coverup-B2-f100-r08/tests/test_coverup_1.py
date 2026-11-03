# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f100 import make_a_pile


def test_make_a_pile_basic():
    """make_a_pile(3) should produce levels of 3, 5, 7 stones."""
    assert make_a_pile(3) == [3, 5, 7]


def test_make_a_pile_single_level():
    """A pile with one level contains exactly n stones."""
    assert make_a_pile(1) == [1]


def test_make_a_pile_zero_levels():
    """A pile with zero levels is empty."""
    assert make_a_pile(0) == []


def test_make_a_pile_structure():
    """Each level has n + 2*i stones; consecutive levels differ by 2."""
    n = 5
    result = make_a_pile(n)
    assert len(result) == n
    assert result[0] == n
    for i in range(n):
        assert result[i] == n + 2 * i
        if i > 0:
            assert result[i] == result[i - 1] + 2
