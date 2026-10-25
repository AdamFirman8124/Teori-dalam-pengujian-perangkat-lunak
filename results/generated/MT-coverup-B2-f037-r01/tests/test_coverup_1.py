# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([4, 9, 2, 8], [2, 9, 4, 8]),
        ([5, 9, 1, 8, 3], [1, 9, 3, 8, 5]),
    ],
)
def test_sort_even_preserves_odd_positions_and_input(values, expected):
    original = values.copy()

    assert sort_even(values) == expected
    assert values == original
