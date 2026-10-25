# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_largest_smallest_integers_with_negative_and_positive_values():
    values = [-10, -3, -7, 2, 8, 5]
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == (-3, 2)
    assert values == original_values


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([-5, -2, -9], (-2, None)),
        ([7, 3, 11], (None, 3)),
        ([], (None, None)),
        ([0], (None, None)),
    ],
)
def test_largest_smallest_integers_handles_missing_signs(values, expected):
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == expected
    assert values == original_values
