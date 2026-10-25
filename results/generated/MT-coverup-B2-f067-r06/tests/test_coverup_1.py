# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f067 import fruit_distribution


def test_fruit_distribution_with_numbers_and_words():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("1 apple and 2 oranges", 10) == 7


def test_fruit_distribution_without_numbers():
    assert fruit_distribution("apples and oranges", 10) == 10
    assert fruit_distribution("apples", 7) == 7


def test_fruit_distribution_empty_string():
    assert fruit_distribution("", 5) == 5


def test_fruit_distribution_only_numbers():
    assert fruit_distribution("10 20", 100) == 70
    assert fruit_distribution("3", 3) == 0
