# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_composite():
    # Executes the loop (line 3), the branch (line 4), and the return (line 5).
    assert largest_divisor(10) == 5


def test_largest_divisor_prime():
    # For a prime, the loop runs down to i == 1, which always divides n.
    assert largest_divisor(7) == 1


def test_largest_divisor_even():
    # First iteration (i = n - 1) fails the branch; second (i = n // 2) hits it.
    assert largest_divisor(12) == 6
