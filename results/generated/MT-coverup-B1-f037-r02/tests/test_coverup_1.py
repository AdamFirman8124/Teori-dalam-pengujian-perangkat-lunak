# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([5, 9, 1], [1, 9, 5]),
        ([5, 9, 1, 8], [1, 9, 5, 8]),
    ],
)
def test_sort_even_sorts_even_positions_and_preserves_input(values, expected):
    original = values.copy()

    assert sort_even(values) == expected
    assert values == original
