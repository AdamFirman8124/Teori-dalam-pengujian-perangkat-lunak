# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


@pytest.mark.parametrize(
    "n, expected",
    [
        (8, True),    # even and >= 8 -> both operands True
        (10, True),   # even and >= 8
        (6, False),   # even but < 8 -> short-circuit on second operand
        (7, False),   # odd -> short-circuit on first operand
        (0, False),   # even but < 8
        (-2, False),  # even but < 8
    ],
)
def test_is_equal_to_sum_even(n, expected):
    assert is_equal_to_sum_even(n) is expected
