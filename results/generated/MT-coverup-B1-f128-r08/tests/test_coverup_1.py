# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

import pytest

from f128 import prod_signs


def test_prod_signs_empty_array_returns_none():
    assert prod_signs([]) is None


@pytest.mark.parametrize(
    ("arr", "expected"),
    [
        ([1, 2, 3], 6),
        ([-1, 2, 3], -6),
        ([-1, -2, 3], 6),
        ([0, -2, 3], 0),
    ],
)
def test_prod_signs_nonempty_arrays(arr, expected):
    original = arr.copy()

    assert prod_signs(arr) == expected
    assert arr == original
