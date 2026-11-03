# file: project/f150/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 10], "branches": [[3, 4], [3, 5], [5, 6], [5, 10], [6, 5], [6, 7]]}

"""Tests for f150.x_or_y.

The function returns ``y`` when ``n`` is 1 or composite, and ``x`` when ``n``
is prime.  The previously uncovered lines are:

* lines 3-4: the ``n == 1`` early return,
* lines 5-7: the divisor loop and the ``return y`` for composite ``n``,
* line 10: the ``for``/``else`` branch taken when ``n`` is prime.

Note: line 8 (``break``) is unreachable dead code (it follows ``return y``),
so no test can execute it; it should be removed from the source instead.
"""

import pytest

from f150 import x_or_y


def test_n_equals_one_returns_y():
    """Covers lines 3-4: n == 1 short-circuits to ``return y``."""
    assert x_or_y(1, "x", "y") == "y"


def test_composite_returns_y():
    """Covers lines 5-7: composite n finds a divisor and returns ``y``."""
    assert x_or_y(4, "x", "y") == "y"   # divisor 2
    assert x_or_y(9, "x", "y") == "y"   # divisor 3
    assert x_or_y(15, "x", "y") == "y"  # divisor 3


def test_prime_returns_x():
    """Covers line 10: the for/else branch taken when n is prime."""
    assert x_or_y(2, "x", "y") == "x"   # empty loop range(2, 2) -> else branch
    assert x_or_y(7, "x", "y") == "x"   # loop runs, no divisor found
    assert x_or_y(13, "x", "y") == "x"


def test_values_are_returned_verbatim():
    """The function must return the exact objects passed in, not copies."""
    sentinel_x = object()
    sentinel_y = object()
    assert x_or_y(1, sentinel_x, sentinel_y) is sentinel_y
    assert x_or_y(6, sentinel_x, sentinel_y) is sentinel_y
    assert x_or_y(5, sentinel_x, sentinel_y) is sentinel_x


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "y"),
        (2, "x"),
        (3, "x"),
        (4, "y"),
        (5, "x"),
        (6, "y"),
        (7, "x"),
        (8, "y"),
        (9, "y"),
        (10, "y"),
        (11, "x"),
    ],
)
def test_primality_semantics(n, expected):
    """Parametrized sanity check of the prime/composite contract."""
    assert x_or_y(n, "x", "y") == expected
