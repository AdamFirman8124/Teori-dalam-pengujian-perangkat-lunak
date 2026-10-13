# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([1.0, 2.0, 3.0, 4.0], 1.0),
        ([-2.0, 0.0, 4.0], 20.0 / 9.0),
        ([7.5], 0.0),
    ],
)
def test_mean_absolute_deviation(numbers, expected):
    assert mean_absolute_deviation(numbers) == pytest.approx(expected)
