# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f013 import greatest_common_divisor


def test_greatest_common_divisor_iterates_until_remainder_is_zero():
    result = greatest_common_divisor(48, 18)

    assert result == 6
    assert 48 % result == 0
    assert 18 % result == 0


def test_greatest_common_divisor_returns_a_when_b_is_zero():
    result = greatest_common_divisor(7, 0)

    assert result == 7
    assert 7 % result == 0
