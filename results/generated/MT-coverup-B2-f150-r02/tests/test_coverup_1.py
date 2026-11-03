# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

import pytest

from f150 import x_or_y


def test_n_equals_one_returns_y():
    """Covers lines 3-4: the `if n == 1` branch."""
    assert x_or_y(1, "x", "y") == "y"


def test_composite_returns_y():
    """Covers lines 5-7: loop body where n % i == 0, returning y."""
    assert x_or_y(4, "x", "y") == "y"
    assert x_or_y(9, "x", "y") == "y"
    assert x_or_y(15, "x", "y") == "y"


def test_prime_with_loop_iterations_returns_x():
    """Covers lines 5-6 (loop runs, condition false) and line 10 (for-else)."""
    assert x_or_y(7, "x", "y") == "x"
    assert x_or_y(11, "x", "y") == "x"


def test_prime_with_empty_loop_returns_x():
    """Covers line 5 (range(2, n) empty) and line 10 via the for-else."""
    assert x_or_y(2, "x", "y") == "x"
    assert x_or_y(3, "x", "y") == "x"


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "not-prime"),
        (2, "prime"),
        (3, "prime"),
        (4, "not-prime"),
        (5, "prime"),
        (6, "not-prime"),
        (7, "prime"),
        (8, "not-prime"),
        (9, "not-prime"),
        (10, "not-prime"),
        (13, "prime"),
        (25, "not-prime"),
    ],
)
def test_x_or_y_truth_table(n, expected):
    """Full truth-table check: y ('not-prime') for 1 and composites,
    x ('prime') for primes."""
    assert x_or_y(n, "prime", "not-prime") == expected
