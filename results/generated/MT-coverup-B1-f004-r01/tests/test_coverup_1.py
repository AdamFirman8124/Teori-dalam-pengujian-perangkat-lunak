# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f004 import mean_absolute_deviation


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([1.0, 2.0, 3.0], 2.0 / 3.0),
        ([5.0], 0.0),
        ([-2.0, 0.0, 2.0], 4.0 / 3.0),
    ],
)
def test_mean_absolute_deviation(numbers, expected):
    assert mean_absolute_deviation(numbers) == pytest.approx(expected)
