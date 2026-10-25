# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([-10, -3, -7, 2, 5, 9], (-3, 2)),
        ([-8, -1, -4], (-1, None)),
        ([3, 12, 7], (None, 3)),
        ([], (None, None)),
        ([0, -2, 0, 6], (-2, 6)),
    ],
)
def test_largest_smallest_integers(values, expected):
    assert largest_smallest_integers(values) == expected
