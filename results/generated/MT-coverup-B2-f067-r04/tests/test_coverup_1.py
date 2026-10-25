# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f067 import fruit_distribution


def test_fruit_distribution_mixed_digits_and_words():
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_no_digits():
    assert fruit_distribution("apples and oranges", 10) == 10


def test_fruit_distribution_all_digits():
    assert fruit_distribution("1 2 3", 10) == 4


def test_fruit_distribution_empty_string():
    assert fruit_distribution("", 5) == 5
