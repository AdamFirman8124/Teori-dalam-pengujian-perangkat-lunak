# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


@pytest.mark.parametrize(
    "n, expected",
    [
        (8, True),    # even and >= 8 -> True branch
        (10, True),   # even and >= 8 -> True branch
        (6, False),   # even but < 8 -> False branch
        (7, False),   # odd and >= 8 -> False branch
        (9, False),   # odd and < 8 -> False branch
        (0, False),   # even but < 8 -> False branch
        (-2, False),  # even but < 8 -> False branch
    ],
)
def test_is_equal_to_sum_even(n, expected):
    assert is_equal_to_sum_even(n) is expected
