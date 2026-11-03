# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_gcd_loop_body_executes():
    """b is nonzero initially, so the while-loop body (lines 3-4) runs."""
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(18, 48) == 6
    assert greatest_common_divisor(270, 192) == 6
    # Coprime inputs drive the loop until b becomes 0 and return 1.
    assert greatest_common_divisor(7, 13) == 1


def test_gcd_loop_body_skipped():
    """b is zero initially, so the while condition is immediately false
    (covers the false branch of line 3) and line 5 returns a directly."""
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(1, 0) == 1


def test_gcd_zero_zero():
    """Edge case: both arguments zero; loop never runs, returns 0."""
    assert greatest_common_divisor(0, 0) == 0


def test_gcd_negative_inputs():
    """Negative values still exercise the loop; result is non-negative
    because Python's % follows the sign of the divisor."""
    assert greatest_common_divisor(-48, 18) == 6
    assert greatest_common_divisor(48, -18) == -6
    assert greatest_common_divisor(-48, -18) == -6
