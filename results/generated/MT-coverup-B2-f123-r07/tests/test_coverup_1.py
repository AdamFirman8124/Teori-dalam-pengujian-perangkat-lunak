# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

from f123 import get_odd_collatz


def test_odd_start_loop_not_entered():
    """n=1 is odd: initial list is [1] and the while loop never runs."""
    result = get_odd_collatz(1)
    assert result == [1]


def test_odd_start_full_sequence():
    """n=5 is odd: covers the else branch of the first if, the loop body,
    both branches of the inner parity if, and the append."""
    # Collatz sequence for 5: 5, 16, 8, 4, 2, 1 -> odd values {5, 1}
    result = get_odd_collatz(5)
    assert result == [1, 5]
    assert result == sorted(result)


def test_even_start_full_sequence():
    """n=6 is even: covers the if branch of the first if (empty start list),
    the loop body, both branches of the inner parity if, and the append."""
    # Collatz sequence for 6: 6, 3, 10, 5, 16, 8, 4, 2, 1 -> odd values {3, 5, 1}
    result = get_odd_collatz(6)
    assert result == [1, 3, 5]
    assert result == sorted(result)


def test_even_start_single_step():
    """n=2 is even: one loop iteration halves n to 1, which gets appended."""
    result = get_odd_collatz(2)
    assert result == [1]
