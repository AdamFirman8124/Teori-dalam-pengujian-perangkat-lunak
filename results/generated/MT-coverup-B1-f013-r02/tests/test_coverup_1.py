# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_gcd_loop_executes_and_terminates():
    # b is nonzero, so the while loop body (lines 3-4) runs at least once
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(18, 48) == 6


def test_gcd_multiple_iterations():
    # Requires several loop iterations to reach the result
    assert greatest_common_divisor(270, 192) == 6
    assert greatest_common_divisor(1071, 462) == 21


def test_gcd_b_zero_skips_loop_body():
    # b == 0: line 3 evaluates the condition as false, line 5 returns a
    assert greatest_common_divisor(7, 0) == 7


def test_gcd_coprime():
    assert greatest_common_divisor(17, 13) == 1


def test_gcd_equal_values():
    assert greatest_common_divisor(9, 9) == 9
