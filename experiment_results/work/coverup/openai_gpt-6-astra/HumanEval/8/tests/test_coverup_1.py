# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

import pytest

from script_8 import sum_product


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([], (0, 1)),
        ([1, 2, 3, 4], (10, 24)),
        ([7], (7, 7)),
        ([0], (0, 0)),
        ([2, 0, 3], (5, 0)),
        ([-2, 3, 4], (5, -24)),
        ([-2, -3, 4], (-1, 24)),
    ],
)
def test_sum_product(numbers, expected):
    original = numbers.copy()

    result = sum_product(numbers)

    assert isinstance(result, tuple)
    assert result == expected
    assert numbers == original
