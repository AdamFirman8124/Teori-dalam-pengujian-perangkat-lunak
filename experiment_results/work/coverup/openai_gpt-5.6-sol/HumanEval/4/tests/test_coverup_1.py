# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([1.0, 2.0, 3.0, 4.0], 1.0),
        ([5.0, 5.0, 5.0], 0.0),
        ([-2.0, 0.0, 2.0], 4.0 / 3.0),
    ],
)
def test_mean_absolute_deviation(numbers, expected):
    result = mean_absolute_deviation(numbers)

    assert result == pytest.approx(expected)
