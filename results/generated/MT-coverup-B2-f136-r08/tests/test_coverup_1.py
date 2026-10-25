# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([-5, -2, 0, 3, 7], (-2, 3)),
        ([-5, -1, 0], (-1, None)),
        ([0, 2, 8], (None, 2)),
        ([0], (None, None)),
    ],
)
def test_largest_smallest_integers(values, expected):
    assert largest_smallest_integers(values) == expected
