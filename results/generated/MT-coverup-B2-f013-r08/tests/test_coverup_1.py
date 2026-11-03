# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_gcd_loop_executes_multiple_iterations():
    """Covers line 3 (loop condition true) and line 4 (loop body)."""
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(12, 8) == 4


def test_gcd_loop_body_skipped_when_b_is_zero():
    """Covers line 3 (loop condition false) and line 5 (return)."""
    assert greatest_common_divisor(7, 0) == 7


def test_gcd_both_zero():
    """Covers the degenerate case: loop skipped, returns 0."""
    assert greatest_common_divisor(0, 0) == 0


def test_gcd_coprime_numbers():
    """Loop runs until remainder is zero; result is 1 for coprime inputs."""
    assert greatest_common_divisor(17, 5) == 1


def test_gcd_negative_becomes_positive_via_modulo():
    """Python's % keeps the sign of b; verify behavior is consistent."""
    assert greatest_common_divisor(48, -18) == -6
    assert greatest_common_divisor(-48, 18) == 6
