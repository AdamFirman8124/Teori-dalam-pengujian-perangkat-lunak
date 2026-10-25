# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


@pytest.mark.parametrize(
    ("number", "need", "remaining", "expected"),
    [
        (10, 3, 5, [13, 2]),
        (10, 5, 5, [15, 0]),
        (10, 7, 5, [15, 0]),
    ],
)
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected
