# file: project/f009/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

from f009 import rolling_max


def test_rolling_max_empty():
    numbers = []
    result = rolling_max(numbers)
    assert result == []
    assert numbers == []


def test_rolling_max_single_element():
    numbers = [5]
    snapshot = list(numbers)
    result = rolling_max(numbers)
    assert result == [5]
    assert numbers == snapshot


def test_rolling_max_increasing():
    numbers = [1, 2, 3, 4]
    snapshot = list(numbers)
    result = rolling_max(numbers)
    assert result == [1, 2, 3, 4]
    assert numbers == snapshot


def test_rolling_max_decreasing():
    numbers = [4, 3, 2, 1]
    snapshot = list(numbers)
    result = rolling_max(numbers)
    assert result == [4, 4, 4, 4]
    assert numbers == snapshot


def test_rolling_max_mixed():
    numbers = [1, 3, 2, 4, 3]
    snapshot = list(numbers)
    result = rolling_max(numbers)
    assert result == [1, 3, 3, 4, 4]
    assert numbers == snapshot
