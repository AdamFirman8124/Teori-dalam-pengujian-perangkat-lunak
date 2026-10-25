# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (9, False),  # Odd: short-circuits the second operand.
        (6, False),  # Even but less than 8.
        (8, True),   # Even and at least 8.
    ],
)
def test_is_equal_to_sum_even(value, expected):
    assert is_equal_to_sum_even(value) is expected
