# file: project/f100/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f100.make_a_pile.

These tests exercise every line and branch of the list comprehension,
including the case where the comprehension loop body never runs (n <= 0),
runs exactly once (n == 1), and runs multiple times (n > 1).
"""

from f100 import make_a_pile


def test_make_a_pile_zero_skips_loop_body():
    """n = 0: range(0) is empty, so the comprehension loop body never runs."""
    result = make_a_pile(0)
    assert result == []
    assert isinstance(result, list)


def test_make_a_pile_one_runs_loop_once():
    """n = 1: the loop body runs exactly once and then exits the loop."""
    result = make_a_pile(1)
    assert result == [1]
    assert len(result) == 1


def test_make_a_pile_multiple_iterations():
    """n > 1: the loop takes its back edge (multiple iterations)."""
    result = make_a_pile(5)
    assert result == [5, 7, 9, 11, 13]
    assert len(result) == 5
    # Postcondition: consecutive levels differ by exactly 2 cubes.
    assert all(b - a == 2 for a, b in zip(result, result[1:]))
    # Postcondition: first element equals n, last equals n + 2*(n-1).
    assert result[0] == 5
    assert result[-1] == 5 + 2 * (5 - 1)


def test_make_a_pile_negative_n_yields_empty_list():
    """Negative n behaves like 0 because range(n) is empty."""
    assert make_a_pile(-3) == []
