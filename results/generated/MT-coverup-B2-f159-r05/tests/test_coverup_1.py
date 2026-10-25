# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_when_need_is_less_than_remaining():
    result = eat(3, 2, 5)
    assert result == [5, 3]
    assert result[0] + result[1] == 3 + 5


def test_eat_when_need_equals_remaining():
    result = eat(0, 4, 4)
    assert result == [4, 0]


def test_eat_when_need_exceeds_remaining():
    result = eat(2, 10, 3)
    assert result == [5, 0]
    assert result[1] == 0


def test_eat_when_remaining_is_zero():
    result = eat(7, 1, 0)
    assert result == [7, 0]


@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (0, 0, 0, [0, 0]),
        (1, 1, 1, [2, 0]),
        (5, 3, 10, [8, 7]),
        (5, 10, 3, [8, 0]),
    ],
)
def test_eat_parametrized(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected
