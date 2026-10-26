# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (8, True),
        (10, True),
        (6, False),
        (7, False),
    ],
)
def test_is_equal_to_sum_even(value, expected):
    assert is_equal_to_sum_even(value) is expected
