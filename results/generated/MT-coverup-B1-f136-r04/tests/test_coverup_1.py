# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_largest_smallest_integers_with_negative_and_positive_values():
    values = [-7, -2, 0, 3, 9]

    result = largest_smallest_integers(values)

    assert result == (-2, 3)
    assert values == [-7, -2, 0, 3, 9]


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], (None, None)),
        ([0, 4, 8], (None, 4)),
        ([-9, -3, -1], (-1, None)),
    ],
)
def test_largest_smallest_integers_handles_missing_negative_or_positive_values(
    values, expected
):
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == expected
    assert values == original_values
