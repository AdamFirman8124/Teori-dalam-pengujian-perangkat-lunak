# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


@pytest.mark.parametrize(
    ("num", "expected"),
    [
        (0, (1, 0)),
        (2468, (4, 0)),
        (13579, (0, 5)),
        (1234567890, (5, 5)),
        (-10203, (3, 2)),
    ],
)
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected
