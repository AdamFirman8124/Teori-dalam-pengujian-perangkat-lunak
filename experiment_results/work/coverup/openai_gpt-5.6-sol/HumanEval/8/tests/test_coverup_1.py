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
        ([-2, 0, 5], (3, 0)),
    ],
)
def test_sum_product(numbers, expected):
    original_numbers = numbers.copy()

    assert sum_product(numbers) == expected
    assert numbers == original_numbers
