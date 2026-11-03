# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

from f123 import get_odd_collatz


def test_even_starting_value():
    """Covers even-start branch (lines 3-4), even loop step (8-9),
    the append branch (13-14) and the skip branch."""
    # Collatz sequence from 6: 6, 3, 10, 5, 16, 8, 4, 2, 1
    # Odd values encountered: 3, 5, 1
    assert get_odd_collatz(6) == [1, 3, 5]


def test_odd_starting_value():
    """Covers odd-start branch (lines 5-6) and odd loop step (10-11)."""
    # Collatz sequence from 3: 3, 10, 5, 16, 8, 4, 2, 1
    # Odd values encountered: 3 (initial), 5, 1
    assert get_odd_collatz(3) == [1, 3, 5]


def test_n_equals_one():
    """Covers the branch where the while loop body never executes."""
    assert get_odd_collatz(1) == [1]


def test_n_equals_two():
    """Even start that reaches 1 in a single even step (append of 1)."""
    assert get_odd_collatz(2) == [1]
