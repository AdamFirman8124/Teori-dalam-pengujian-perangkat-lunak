# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


@pytest.mark.parametrize(
    ("arr", "expected"),
    [
        ([], -1),
        ([1, 2, 3], -1),
        ([1, 3, 2, 5, 4], 4),
    ],
)
def test_can_arrange_returns_last_decreasing_index(arr, expected):
    assert can_arrange(arr) == expected
