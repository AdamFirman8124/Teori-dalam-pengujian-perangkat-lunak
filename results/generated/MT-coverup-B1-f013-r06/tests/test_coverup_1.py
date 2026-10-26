# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f013 import greatest_common_divisor


def test_greatest_common_divisor_reduces_until_zero():
    assert greatest_common_divisor(48, 18) == 6


def test_greatest_common_divisor_returns_a_when_b_is_zero():
    assert greatest_common_divisor(7, 0) == 7
