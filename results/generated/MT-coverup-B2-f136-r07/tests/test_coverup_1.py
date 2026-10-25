# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([-5, -2, 0, 3, 7], (-2, 3)),
        ([0, 0], (None, None)),
        ([-4, -1], (-1, None)),
        ([2, 6], (None, 2)),
    ],
)
def test_largest_smallest_integers(values, expected):
    original = values.copy()

    assert largest_smallest_integers(values) == expected
    assert values == original
