# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_greatest_common_divisor_iterates_until_remainder_is_zero():
    assert greatest_common_divisor(48, 18) == 6


def test_greatest_common_divisor_returns_first_argument_when_second_is_zero():
    assert greatest_common_divisor(21, 0) == 21


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (18, 48, 6),
        (1071, 462, 21),
    ],
)
def test_greatest_common_divisor_handles_multiple_inputs(a, b, expected):
    assert greatest_common_divisor(a, b) == expected
