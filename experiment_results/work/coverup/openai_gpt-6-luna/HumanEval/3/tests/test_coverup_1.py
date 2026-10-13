# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest

from script_3 import below_zero


@pytest.mark.parametrize(
    ("operations", "expected"),
    [
        ([], False),
        ([1, 2, 3], False),
        ([1, 2, -4, 5], True),
        ([-1, 10], True),
    ],
)
def test_below_zero_detects_balance_status(operations, expected):
    assert below_zero(operations) is expected
