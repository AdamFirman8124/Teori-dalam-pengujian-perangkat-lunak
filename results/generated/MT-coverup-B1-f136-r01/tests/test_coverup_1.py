# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([-9, -2, -5, 0, 3, 8], (-2, 3)),
        ([-4, -1, 0], (-1, None)),
        ([0, 2, 7], (None, 2)),
        ([], (None, None)),
    ],
)
def test_largest_smallest_integers(values, expected):
    original_values = values.copy()

    result = largest_smallest_integers(values)

    assert result == expected
    assert values == original_values
