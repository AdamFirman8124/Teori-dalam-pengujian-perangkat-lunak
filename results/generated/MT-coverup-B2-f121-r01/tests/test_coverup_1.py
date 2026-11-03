# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f121 import solution


def test_empty_list_returns_zero():
    """Empty input: the comprehension loop body never executes."""
    assert solution([]) == 0


def test_even_index_odd_value_is_summed():
    """Branch: idx % 2 == 0 is True and x % 2 == 1 is True (element kept)."""
    # idx 0 -> 1 (odd, kept), idx 2 -> 3 (odd, kept)
    assert solution([1, 2, 3]) == 4


def test_even_index_even_value_is_skipped():
    """Branch: idx % 2 == 0 is True but x % 2 == 1 is False (element dropped)."""
    # Even indices hold even values (2 and 4), so nothing is summed.
    assert solution([2, 1, 4, 3]) == 0


def test_odd_index_is_skipped():
    """Branch: idx % 2 == 0 is False (short-circuits before evaluating x % 2 == 1)."""
    # Odd values appear only at odd indices, so they are all skipped.
    assert solution([0, 1, 0, 3]) == 0


def test_mixed_input_covers_all_branches():
    """All branches exercised together in a single call."""
    # idx 0, x=1 -> kept (1); idx 2, x=2 -> dropped; idx 4, x=5 -> kept (5);
    # odd indices 1, 3, 5 -> skipped regardless of value parity.
    assert solution([1, 1, 2, 3, 5, 5]) == 6
