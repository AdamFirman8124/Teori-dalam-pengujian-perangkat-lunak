# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_returns_largest_proper_divisor():
    # n=4: i=3 fails the modulo check, i=2 succeeds -> exercises both branches
    assert largest_divisor(4) == 2
    assert largest_divisor(9) == 3
    assert largest_divisor(2) == 1
    assert largest_divisor(7) == 1


def test_result_is_a_proper_divisor():
    for n in (2, 3, 4, 6, 12, 25, 97):
        result = largest_divisor(n)
        assert result is not None
        assert 0 < result < n
        assert n % result == 0


def test_no_divisor_found_returns_none():
    # range(0) is empty -> loop body never runs, function falls through
    assert largest_divisor(0) is None


def test_one_raises_zero_division_error():
    # range(1) -> [0], and n % 0 raises
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)
