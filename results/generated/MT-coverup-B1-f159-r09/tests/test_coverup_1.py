# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

from f159 import eat


def test_eat_need_less_than_remaining():
    result = eat(10, 3, 5)
    assert result == [13, 2]


def test_eat_need_equal_to_remaining():
    result = eat(10, 5, 5)
    assert result == [15, 0]


def test_eat_need_greater_than_remaining():
    result = eat(10, 7, 5)
    assert result == [15, 0]
