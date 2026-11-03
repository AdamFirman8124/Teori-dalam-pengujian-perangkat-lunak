# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_composite():
    # Exercises the loop (line 3), the modulo check (line 4) with both
    # False branches (14..6) and the True branch returning early (line 5).
    assert largest_divisor(15) == 5


def test_largest_divisor_even_composite():
    assert largest_divisor(10) == 5
    assert largest_divisor(4) == 2


def test_largest_divisor_prime():
    # Loop runs through every candidate down to 1 before returning,
    # covering the final-iteration True branch.
    assert largest_divisor(7) == 1
    assert largest_divisor(3) == 1


def test_largest_divisor_smallest_valid():
    assert largest_divisor(2) == 1


def test_largest_divisor_zero_loop_never_runs():
    # range(0) is empty, so the loop body never executes and the
    # function falls through to an implicit `return None`.
    assert largest_divisor(0) is None


def test_largest_divisor_one_raises_zero_division():
    # For n == 1 the only candidate is 0, and 1 % 0 raises.
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)
