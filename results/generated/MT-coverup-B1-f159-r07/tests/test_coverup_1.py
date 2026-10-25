# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

from f159 import eat


def test_eat_when_enough_remaining():
    number, need, remaining = 3, 4, 10
    result = eat(number, need, remaining)

    assert result == [7, 6]
    assert isinstance(result, list) and len(result) == 2
    assert result[0] == number + need
    assert result[1] == remaining - need
    assert result[1] >= 0


def test_eat_when_not_enough_remaining():
    number, need, remaining = 3, 10, 4
    result = eat(number, need, remaining)

    assert result == [7, 0]
    assert isinstance(result, list) and len(result) == 2
    assert result[0] == number + remaining
    assert result[1] == 0


def test_eat_exact_remaining_boundary():
    number, need, remaining = 0, 5, 5
    result = eat(number, need, remaining)

    assert result == [5, 0]
    assert result[0] == number + need
    assert result[1] == remaining - need == 0


def test_eat_zero_need():
    result = eat(2, 0, 7)

    assert result == [2, 7]
    assert result[1] == 7
