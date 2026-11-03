# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

"""Tests for f123.get_odd_collatz covering all previously unexecuted lines 3-16."""

from f123 import get_odd_collatz


def test_even_starting_value():
    """Even n takes the 'odd_collatz = []' branch (lines 3-4).

    Collatz sequence for 6: 6, 3, 10, 5, 16, 8, 4, 2, 1
    Odd members: {3, 5, 1} -> sorted [1, 3, 5].
    Exercises: even branch of line 3, line 4, loop entry (line 7),
    even branch of line 8 (line 9), odd branch of line 8 (line 11),
    both branches of line 13, append (line 14), return (line 16).
    """
    assert get_odd_collatz(6) == [1, 3, 5]


def test_odd_starting_value():
    """Odd n takes the 'odd_collatz = [n]' branch (line 6).

    Collatz sequence for 5: 5, 16, 8, 4, 2, 1
    Odd members: {5, 1} -> sorted [1, 5].
    """
    assert get_odd_collatz(5) == [1, 5]


def test_n_equals_one_loop_not_entered():
    """n=1: odd branch (line 6) taken, while loop (line 7) never entered."""
    assert get_odd_collatz(1) == [1]


def test_n_equals_two_single_iteration():
    """n=2: even branch (line 4), one loop iteration halving to 1 (line 9),
    then 1.0 % 2 == 1 triggers the append (lines 13-14)."""
    assert get_odd_collatz(2) == [1]


def test_result_is_sorted_list_of_ints():
    """Postcondition: result is a sorted list of ints regardless of input parity."""
    for n, expected in ((6, [1, 3, 5]), (5, [1, 5]), (1, [1]), (2, [1])):
        result = get_odd_collatz(n)
        assert isinstance(result, list)
        assert result == sorted(result)
        assert all(isinstance(x, int) for x in result)
        assert result == expected
