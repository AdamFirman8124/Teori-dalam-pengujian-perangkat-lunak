# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_composite():
    # Exercises lines 3-5: loop over reversed(range(n)) and early return
    # on the first divisor found.
    assert largest_divisor(10) == 5
    assert largest_divisor(12) == 6
    assert largest_divisor(100) == 50


def test_largest_divisor_prime():
    # For a prime, the loop must run down to i == 1 before returning,
    # covering the loop-exhaustion branch of line 3 as well.
    assert largest_divisor(7) == 1
    assert largest_divisor(13) == 1


def test_largest_divisor_even():
    # Even numbers return n // 2 on the very first iteration (i = n - 1
    # fails, i = n - 2 succeeds for even n >= 4).
    assert largest_divisor(4) == 2
    assert largest_divisor(8) == 4
