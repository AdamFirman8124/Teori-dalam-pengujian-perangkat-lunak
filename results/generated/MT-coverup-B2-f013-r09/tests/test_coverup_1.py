# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_gcd_basic_two_iterations():
    """Covers the while loop (line 3), the loop body (line 4) and return (line 5)."""
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(12, 18) == 6


def test_gcd_one_iteration():
    """Covers a single pass through the loop body before b becomes falsy."""
    assert greatest_common_divisor(10, 5) == 5


def test_gcd_b_zero_no_iterations():
    """Covers the while-condition-false branch: loop body is skipped, return a."""
    assert greatest_common_divisor(7, 0) == 7


def test_gcd_a_zero():
    assert greatest_common_divisor(0, 9) == 9


def test_gcd_both_zero():
    assert greatest_common_divisor(0, 0) == 0


def test_gcd_commutative():
    assert greatest_common_divisor(18, 48) == greatest_common_divisor(48, 18) == 6


def test_gcd_coprime():
    assert greatest_common_divisor(17, 13) == 1


def test_gcd_negative_inputs():
    """Python's modulo keeps b non-negative here, but verify sane behavior."""
    assert greatest_common_divisor(-48, 18) == abs(6)
