# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

"""Tests for f123.get_odd_collatz covering all previously uncovered lines (3-16).

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching/teardown is required; each test leaves no state behind.
"""

from f123 import get_odd_collatz


def test_even_start_traverses_full_sequence():
    """n=6 (even) covers:
      - line 3 True / line 4 (even start -> empty list)
      - line 7 (loop entered), line 8 True / line 9 (halving: 6 -> 3)
      - line 8 False / line 11 (tripling: 3 -> 10)
      - line 13 True / line 14 (append odd values 3, 5, 1)
      - line 13 False (even values 10, 16, 8, 4, 2 skipped)
      - line 16 (sorted return)
    Collatz sequence: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    """
    result = get_odd_collatz(6)
    assert result == [1, 3, 5]
    assert result == sorted(result)  # postcondition: output is sorted


def test_odd_start_traverses_full_sequence():
    """n=3 (odd) covers:
      - line 3 False / line 6 (odd start -> [n])
      - line 7 (loop entered), line 11 (tripling: 3 -> 10)
      - line 9 (halving steps), line 13 both branches, line 14 (append)
      - line 16 (sorted return)
    Collatz sequence: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    Odd members: initial 3, then 5, then 1.
    """
    result = get_odd_collatz(3)
    assert result == [1, 3, 5]
    assert result == sorted(result)  # postcondition: output is sorted


def test_odd_start_loop_not_entered():
    """n=1 (odd) covers line 3 False / line 6 while the while-loop (line 7)
    never executes (1 is not > 1)."""
    assert get_odd_collatz(1) == [1]


def test_even_start_loop_not_entered():
    """n=0 (even) covers line 3 True / line 4 while the while-loop (line 7)
    never executes (0 is not > 1)."""
    assert get_odd_collatz(0) == []


def test_even_start_single_step():
    """n=2 (even) is the minimal loop run: covers line 9 (2 -> 1.0) and the
    final append of 1 (lines 13-14), returning [1]."""
    assert get_odd_collatz(2) == [1]
