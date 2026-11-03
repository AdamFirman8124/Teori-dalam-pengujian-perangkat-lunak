# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

"""Tests for f123.get_odd_collatz covering all previously unexecuted lines (3-16).

The function under test is pure (no I/O, no module state, no randomness), so no
monkeypatching/teardown is required; each test is self-contained and leaves no
state behind.
"""

from f123 import get_odd_collatz


def test_even_start_covers_empty_list_branch_and_full_loop():
    """n even -> line 4 (odd_collatz = []), loop with even division (line 9),
    odd multiplication (line 11), both branches of the append check (line 13),
    the append itself (line 14) and the sorted return (line 16)."""
    # Collatz sequence for 14: 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
    result = get_odd_collatz(14)
    assert result == [1, 5, 7, 11, 13, 17]
    assert all(x % 2 == 1 for x in result)
    assert result == sorted(result)


def test_odd_start_covers_seeded_list_branch_and_odd_step():
    """n odd -> line 6 (odd_collatz = [n]) and the n*3+1 branch (line 11);
    also exercises the False branch of the append check (line 13) when the
    updated value is even (5 -> 16)."""
    # Collatz sequence for 5: 5, 16, 8, 4, 2, 1
    result = get_odd_collatz(5)
    assert result == [1, 5]
    assert 5 in result  # the starting odd value is seeded into the list


def test_n_equals_one_skips_loop_body():
    """n == 1 (odd) -> line 6 taken, but the while condition (line 7) is False
    on the first evaluation, so the loop body never runs."""
    assert get_odd_collatz(1) == [1]


def test_even_n_single_iteration():
    """n == 2 (even) -> line 4 taken, loop entered exactly once, even division
    branch (line 9) taken, odd result appended, then loop exits (line 7 False)."""
    assert get_odd_collatz(2) == [1]


def test_odd_n_single_odd_step():
    """n == 3 (odd) -> line 6 taken, n*3+1 branch (line 11) taken on the first
    iteration, then even divisions until termination."""
    # Collatz sequence for 3: 3, 10, 5, 16, 8, 4, 2, 1
    result = get_odd_collatz(3)
    assert result == [1, 3, 5]
    assert all(x % 2 == 1 for x in result)
