# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_gcd_nonzero_values_executes_loop():
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(18, 48) == 6
    assert greatest_common_divisor(7, 5) == 1


def test_gcd_b_zero_skips_loop():
    assert greatest_common_divisor(5, 0) == 5


def test_gcd_a_zero():
    assert greatest_common_divisor(0, 5) == 5


def test_gcd_both_zero():
    assert greatest_common_divisor(0, 0) == 0
