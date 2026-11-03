# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

"""Tests for f150.x_or_y.

x_or_y(n, x, y) returns y when n == 1 or n is composite (a divisor is
found in the loop), and x when n is prime (the for-loop completes
without breaking, so the for-else branch runs).

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or teardown is required to avoid state pollution.
"""

from f150 import x_or_y


def test_n_equals_one_returns_y():
    """Covers lines 3-4: the `n == 1` branch taken."""
    assert x_or_y(1, "prime", "not-prime") == "not-prime"


def test_composite_n_returns_y():
    """Covers lines 5-7: loop body runs and the divisor branch is taken."""
    # 4 % 2 == 0 -> returns y on the first iteration.
    assert x_or_y(4, "prime", "not-prime") == "not-prime"
    # 9 needs a couple of iterations before 9 % 3 == 0.
    assert x_or_y(9, "prime", "not-prime") == "not-prime"
    # Larger composite exercises more loop iterations.
    assert x_or_y(15, "prime", "not-prime") == "not-prime"


def test_prime_n_returns_x():
    """Covers lines 5-6 (false branch) plus lines 8-10: the for-else."""
    # n == 2: range(2, 2) is empty, loop falls through to the else.
    assert x_or_y(2, "prime", "not-prime") == "prime"
    # n == 3: loop body executes once with a false condition, then else.
    assert x_or_y(3, "prime", "not-prime") == "prime"
    # Larger primes exercise several loop iterations with false conditions.
    assert x_or_y(7, "prime", "not-prime") == "prime"
    assert x_or_y(13, "prime", "not-prime") == "prime"


def test_result_depends_only_on_primality():
    """Postcondition: x and y are returned verbatim, unmodified."""
    sentinel_x = object()
    sentinel_y = object()
    assert x_or_y(2, sentinel_x, sentinel_y) is sentinel_x
    assert x_or_y(1, sentinel_x, sentinel_y) is sentinel_y
    assert x_or_y(6, sentinel_x, sentinel_y) is sentinel_y
