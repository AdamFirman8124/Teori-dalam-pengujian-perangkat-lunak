# file: project/f084/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f084 import solve


def test_solve_returns_binary_of_digit_sum():
    # Line 3 must execute: call the function and check the postcondition.
    result = solve(123)
    assert result == "110"  # digit sum 1+2+3 = 6 -> bin(6)[2:] == "110"
    assert isinstance(result, str)
    assert not result.startswith("0b")
    assert int(result, 2) == sum(int(d) for d in str(123))


def test_solve_single_digit():
    assert solve(0) == "0"
    assert solve(9) == "1001"
    assert int(solve(9), 2) == 9


def test_solve_all_nines():
    result = solve(999)
    assert result == "11011"  # 27 -> bin(27)[2:]
    assert int(result, 2) == 27


@pytest.mark.parametrize("n", [1, 7, 10, 42, 100, 2024, 99999])
def test_solve_matches_digit_sum_for_various_inputs(n):
    result = solve(n)
    assert result == bin(sum(int(d) for d in str(n)))[2:]
    assert int(result, 2) == sum(int(d) for d in str(n))
    assert set(result) <= {"0", "1"}
