# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}

from f024 import largest_divisor


def test_largest_divisor_composite_numbers():
    """For composite n, the largest proper divisor is returned.

    n=10: candidates 9, 8, 7, 6 fail the condition (false branch),
    then i=5 satisfies it (true branch) and is returned.
    n=4: candidate 3 fails, candidate 2 satisfies -> 2.
    n=2: first candidate 1 immediately satisfies -> 1.
    """
    assert largest_divisor(10) == 5
    assert largest_divisor(4) == 2
    assert largest_divisor(2) == 1


def test_largest_divisor_prime_numbers():
    """For a prime n, every candidate fails until i=1, which is returned."""
    assert largest_divisor(7) == 1
    assert largest_divisor(3) == 1


def test_largest_divisor_non_positive_returns_none():
    """For n <= 0, range(n) is empty: the loop body never executes and the
    function falls off the end, implicitly returning None."""
    assert largest_divisor(0) is None
    assert largest_divisor(-6) is None
