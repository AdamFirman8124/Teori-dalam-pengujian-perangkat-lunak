# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

from f096 import count_up_to


def test_count_up_to_full_coverage_range():
    """Exercises every line: outer loop (4-5), inner loop (6), divisor
    check both branches (7), composite detection with break (8-9),
    append of primes (10-11) and the return (12)."""
    assert count_up_to(10) == [2, 3, 5, 7]


def test_count_up_to_outer_loop_never_runs():
    """Covers the branch of line 4 where range(2, n) is empty."""
    assert count_up_to(2) == []
    assert count_up_to(1) == []
    assert count_up_to(0) == []
    assert count_up_to(-3) == []


def test_count_up_to_inner_loop_never_runs():
    """Covers the branch of line 6 where range(2, i) is empty (i == 2)."""
    assert count_up_to(3) == [2]


def test_count_up_to_first_composite_triggers_break():
    """Covers lines 8-9 (is_prime = False; break) and the False branch
    of line 10 (composite not appended)."""
    assert count_up_to(4) == [2, 3]


def test_count_up_to_boundaries():
    """n is exclusive; verify boundary behaviour around primes."""
    assert count_up_to(7) == [2, 3, 5]
    assert count_up_to(8) == [2, 3, 5, 7]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(12) == [2, 3, 5, 7, 11]
