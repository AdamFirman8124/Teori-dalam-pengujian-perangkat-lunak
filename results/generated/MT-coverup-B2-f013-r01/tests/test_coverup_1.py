# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_gcd_loop_body_executes_when_b_nonzero():
    # Covers line 3 (loop condition true) and line 4 (loop body).
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(18, 48) == 6
    assert greatest_common_divisor(17, 5) == 1


def test_gcd_returns_immediately_when_b_zero():
    # Covers line 3 (loop condition false branch) and line 5 (return).
    assert greatest_common_divisor(7, 0) == 7
    assert greatest_common_divisor(0, 0) == 0


def test_gcd_negative_first_argument():
    # Exercises the loop with a negative operand; Python's % keeps the
    # invariant so the result is still the (positive) gcd here.
    assert greatest_common_divisor(-48, 18) == 6
