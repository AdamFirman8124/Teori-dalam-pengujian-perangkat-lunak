# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f084 import solve


def _digit_sum(n):
    return sum(int(d) for d in str(n))


def test_solve_returns_binary_of_digit_sum():
    assert solve(123) == "110"  # 1+2+3 = 6 -> 0b110


def test_solve_single_digit():
    assert solve(7) == "111"


def test_solve_zero():
    assert solve(0) == "0"


def test_solve_large_number():
    assert solve(999) == "11011"  # 27 -> 0b11011


@pytest.mark.parametrize("n", [0, 1, 5, 10, 99, 123, 4567, 999999])
def test_solve_postconditions(n):
    result = solve(n)
    assert isinstance(result, str)
    assert result and set(result) <= {"0", "1"}
    assert not result.startswith("0b")
    assert result == result.lstrip("0") or result == "0"
    assert int(result, 2) == _digit_sum(n)
