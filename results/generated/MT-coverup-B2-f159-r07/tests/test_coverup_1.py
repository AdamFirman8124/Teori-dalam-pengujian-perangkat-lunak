# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

"""Tests for f159.eat covering both branches (lines 3-6).

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test is self-contained.
"""

from f159 import eat


def test_eat_enough_remaining_covers_if_branch():
    """need <= remaining: rabbit eats `need` carrots, leftovers decrease.

    Covers line 3 (condition true) and line 4 (return in if-branch).
    """
    result = eat(5, 3, 10)
    assert result == [5 + 3, 10 - 3]
    assert result == [8, 7]


def test_eat_insufficient_remaining_covers_else_branch():
    """need > remaining: rabbit eats all remaining carrots, none left.

    Covers line 3 (condition false), line 5 (else) and line 6
    (return in else-branch).
    """
    result = eat(5, 12, 10)
    assert result == [5 + 10, 0]
    assert result == [15, 0]


def test_eat_exactly_equal_boundary():
    """Boundary case need == remaining takes the if-branch (<=).

    Reinforces line 3/4 coverage at the boundary and checks that
    leftovers hit exactly zero.
    """
    result = eat(5, 10, 10)
    assert result == [15, 0]


def test_eat_zero_need_takes_if_branch():
    """need == 0 is always <= remaining, so nothing is eaten."""
    result = eat(7, 0, 4)
    assert result == [7, 4]
