# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f102 import choose_num


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (5, 3, -1),  # x > y
        (3, 4, 4),   # y is even
        (3, 3, -1),  # x == y and y is odd
        (2, 5, 4),   # x < y and y is odd
    ],
)
def test_choose_num_covers_all_branches(x, y, expected):
    assert choose_num(x, y) == expected
