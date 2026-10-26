# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

from f159 import eat


def test_eat_need_less_than_remaining():
    result = eat(5, 2, 7)
    assert result == [7, 5]


def test_eat_need_equal_to_remaining():
    result = eat(5, 3, 3)
    assert result == [8, 0]


def test_eat_need_greater_than_remaining():
    result = eat(2, 5, 3)
    assert result == [5, 0]
