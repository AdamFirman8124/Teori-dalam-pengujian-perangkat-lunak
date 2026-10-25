# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3, 1, 2], 2),
        ([4, 1, 3, 2], 2.5),
    ],
)
def test_median_covers_odd_and_even_inputs(values, expected):
    original = values.copy()

    assert median(values) == expected
    assert values == original
